import time
import boto3
import json
import c1wsconnectorapi
import ctlifecycleevent
import logging
import c1wsresources
import cfnhelper

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_org_id():
    client = boto3.client("organizations")
    # TODO This assumes there is only one root... should we extend to support more?
    return client.list_roots()["Roots"][0]["ARN"].split(":")[4]


def create_cross_account_role(aws_account_id):
    sts_session = assume_role(aws_account_id, c1wsresources.ControlTowerRoleName)

    sts_client = sts_session.client("sts")
    sts_identity = sts_client.get_caller_identity()
    partition = sts_identity["Arn"].split(":")[1]

    client = sts_session.client("iam")
    logger.info(
        f"Creating role {c1wsresources.IamRoleName} and policy {c1wsresources.IamPolicyName} in account {aws_account_id}"
    )
    path = "/"
    try:
        logger.info("Creating role...")
        client.create_role(
            Path=path,
            RoleName=c1wsresources.IamRoleName,
            AssumeRolePolicyDocument=c1wsresources.get_assume_role_policy_document(),
            Description="Cloud One Workload Security Connector Role created by Control Tower",
        )
    except Exception as e:
        logger.error(f"Failed to create role: {e}")
        raise e
    try:
        logger.info("Creating policy...")
        client.create_policy(
            PolicyName=c1wsresources.IamPolicyName,
            PolicyDocument=json.dumps(c1wsresources.policy_document),
        )
    except Exception as e:
        logger.error(f"Failed to create policy: {e}")
        raise e
    try:
        logger.info("Attaching policy...")
        # TODO this won't work if the partition is not aws.
        client.attach_role_policy(
            PolicyArn=f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}",
            RoleName=c1wsresources.IamRoleName,
        )
    except Exception as e:
        logger.error(f"Failed to attach policy: {e}")
        raise e
    else:
        return True


def delete_cross_account_role(aws_account_id):
    sts_session = assume_role(aws_account_id, c1wsresources.ControlTowerRoleName)

    sts_client = sts_session.client("sts")
    sts_identity = sts_client.get_caller_identity()
    partition = sts_identity["Arn"].split(":")[1]

    client = sts_session.client("iam")
    logger.info(f'Account is {boto3.client("sts").get_caller_identity()["Account"]}')
    try:
        # TODO this won't work if the partition is not aws.
        client.detach_role_policy(
            PolicyArn=f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}",
            RoleName=c1wsresources.IamRoleName,
        )
        logger.info("Detached policy")
    except Exception as e:
        logger.error(
            f"Failed to detach policy {c1wsresources.IamPolicyName} from role {c1wsresources.IamRoleName} \
                in account {aws_account_id}: {e}"
        )
    try:
        client.delete_role(RoleName=c1wsresources.IamRoleName)
        logger.info("Deleted role")
    except Exception as e:
        logger.error(
            f"Failed to delete role {c1wsresources.IamRoleName} in account {aws_account_id}: {e}"
        )
    try:
        # TODO this won't work if the partition is not aws.
        client.delete_policy(
            PolicyArn=f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}"
        )
        logger.info("Deleted policy")
    except Exception as e:
        logger.error(
            f"Failed to delete policy: arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}: {e}"
        )
    return


def assume_role(aws_account_number, role_name) -> boto3.Session:
    try:
        sts_client = boto3.client("sts")
        logger.info(f"Retrieving session for operation")
        logger.info(
            f"currently executing in "
            f'{sts_client.get_caller_identity()["Account"]};'
            f" called account is {aws_account_number}"
        )
        if sts_client.get_caller_identity()["Account"] == aws_account_number:
            logger.info(
                f"Target account is Control Tower Management; returning local credentials session"
            )
            return boto3.session.Session()
        partition = sts_client.get_caller_identity()["Arn"].split(":")[1]

        assume_role_response = sts_client.assume_role(
            RoleArn="arn:{}:iam::{}:role/{}".format(
                partition, aws_account_number, role_name
            ),
            RoleSessionName=str(aws_account_number + "-" + role_name),
        )
        sts_session = boto3.Session(
            aws_access_key_id=assume_role_response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=assume_role_response["Credentials"][
                "SecretAccessKey"
            ],
            aws_session_token=assume_role_response["Credentials"]["SessionToken"],
        )
        logger.info(f"Assumed session for {aws_account_number} - {role_name}.")
        return sts_session
    except Exception as e:
        logger.error(f"Could not assume role : {e}")
        raise e


def configure_account(aws_account_id):
    c1w_connector = c1wsconnectorapi.CloudOneConnector(c1wsresources.get_api_key())

    sts_client = boto3.client("sts")
    sts_identity = sts_client.get_caller_identity()
    partition = sts_identity["Arn"].split(":")[1]

    iam_client = boto3.client("iam")
    try:
        logger.info("Create Connector Object")

        logger.info("Create role in target account")
        create_cross_account_role(aws_account_id)
    except iam_client.exceptions.EntityAlreadyExistsException as e:
        update_policy(aws_account_id)
    except Exception as e:
        logger.error(
            f"Failed to configure account {aws_account_id} with exception: {e}"
        )

    # Wait for eventual consistency to become consistent
    time.sleep(20)

    try:
        logger.info("Add account to Cloud One Workload Security")
        # TODO this won't work if the partition is not aws.
        return c1w_connector.add_connector(
            f"arn:{partition}:iam::{aws_account_id}:role/{c1wsresources.IamRoleName}",
            aws_account_id,
        )
    except Exception as e:
        logger.error(f"Failed to add workload connector with exception {e}")


def remove_account_config(aws_account_id):
    try:
        c1ws_connector = c1wsconnectorapi.CloudOneConnector(c1wsresources.get_api_key())
        logger.info(f"Removing account from Cloud One Workload Security")
        c1ws_connector.delete_connector(aws_account_id)
        logger.info("Removing role from target account")
        delete_cross_account_role(aws_account_id)
    except Exception as e:
        logger.error(
            f"Failed to remove account {aws_account_id} config with exception: {e}"
        )


def update_policy(aws_account_id):
    logger.info(f"Updating account {aws_account_id}")
    sts_session = assume_role(aws_account_id, c1wsresources.ControlTowerRoleName)

    sts_client = sts_session.client("sts")
    sts_identity = sts_client.get_caller_identity()
    partition = sts_identity["Arn"].split(":")[1]

    client = sts_session.client("iam")
    policy_resource = sts_session.resource("iam")
    logger.info(f"Updating policy in account {aws_account_id}")
    try:
        client.get_role(RoleName=c1wsresources.IamRoleName)
    except client.exceptions.NoSuchEntityException:
        logger.info(f"Policy not found; configuring account")
        configure_account(aws_account_id)
        return
    logger.info(f"Updating AssumeRolePolicyDocument in account {aws_account_id}")
    try:
        client.update_assume_role_policy(
            RoleName=c1wsresources.IamRoleName,
            PolicyDocument=c1wsresources.get_assume_role_policy_document(),
        )
    except Exception as e:
        logger.error(f"Failed to update AssumeRolePolicyDocument: {e}")
        raise
    try:
        # TODO this won't work if the partition is not aws.
        policy = policy_resource.Policy(
            f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}"
        )
        version = policy.default_version
        client.create_policy_version(
            PolicyArn=f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}",
            PolicyDocument=json.dumps(c1wsresources.policy_document),
            SetAsDefault=True,
        )
        client.delete_policy_version(
            PolicyArn=f"arn:{partition}:iam::{aws_account_id}:policy/{c1wsresources.IamPolicyName}",
            VersionId=version.version_id,
        )
    except Exception as e:
        logger.error(f"Failed to update policy: {e}")
        raise


def get_accounts():
    account_ids = []
    client = boto3.client("organizations")
    paginator = client.get_paginator("list_accounts")
    page_iterator = paginator.paginate()
    for page in page_iterator:
        for account in page.get("Accounts"):
            account_ids.append(account.get("Id"))
    return account_ids


def fresh_deploy(function_name):
    client = boto3.client("lambda")
    logger.info(f"Received function name {function_name} from context")
    count = 0
    for account_id in get_accounts():
        logger.info(f"Launched configure_account for {account_id}")
        client.invoke(
            FunctionName=function_name,
            InvocationType="Event",
            Payload=json.dumps(
                {"InvokeAction": "configure_account", "account_id": account_id}
            ),
        )
        count += 1
    logger.info(f"Launched configure_account for {count} accounts")
    return None


def update_accounts(function_name):
    client = boto3.client("lambda")
    logger.info(f"Received function name {function_name} from context")
    count = 0
    for account_id in get_accounts():
        logger.info(f"Launched update_accounts for {account_id}")
        client.invoke(
            FunctionName=function_name,
            InvocationType="Event",
            Payload=json.dumps(
                {"InvokeAction": "update_account", "account_id": account_id}
            ),
        )
        count += 1
    logger.info(f"Launched update_accounts for {count} accounts")
    return None


def remove_all(function_name):
    client = boto3.client("lambda")
    logger.info(f"Received function name {function_name} from context")
    count = 0
    for account_id in get_accounts():
        logger.info(f"Launched remove_account_config for {account_id}")
        client.invoke(
            FunctionName=function_name,
            InvocationType="Event",
            Payload=json.dumps(
                {"InvokeAction": "remove_account_config", "account_id": account_id}
            ),
        )
        count += 1
    logger.info(f"Launched remove_account_config for {count} accounts")
    return None


def lambda_handler(event, context):
    logger.info(f"Event received by handler: {event}")
    logger.info(
        f"function name: {context.function_name} "
        f"invoked arn: {context.invoked_function_arn}"
    )
    if "RequestType" in event:
        logger.info(f"Handling CloudFormation request")
        if event["RequestType"] == "Create":
            logger.info(f"Received CloudFormation create")
            response = cfnhelper.cfnResponse(event, context)
            try:
                fresh_deploy(context.function_name)
            except Exception as e:
                logger.error(f"Failed to handle create event with exception: {e}")
                response.send(cfnhelper.responseCode.FAILED)
                return
            response.send(cfnhelper.responseCode.SUCCESS)
        elif event["RequestType"] == "Update":
            logger.info(f"Received CloudFormation update")
            response = cfnhelper.cfnResponse(event, context)
            try:
                update_accounts(context.function_name)
            except Exception as e:
                logger.error(f"Failed to handle update event with exception: {e}")
                response.send(cfnhelper.responseCode.FAILED)
                return
            response.send(cfnhelper.responseCode.SUCCESS)
        else:
            logger.info(
                f"Ignoring unhandled CloudFormation request type: {event['RequestType']}"
            )
            response = cfnhelper.cfnResponse(event, context)
            response.send(cfnhelper.responseCode.SUCCESS)
    elif "InvokeAction" in event:
        try:
            if event["InvokeAction"] == "configure_account":
                configure_account(event["account_id"])
            elif event["InvokeAction"] == "update_account":
                update_policy(event["account_id"])
            elif event["InvokeAction"] == "remove_account_config":
                remove_account_config(event["account_id"])
            elif event["InvokeAction"] == "remove_all":
                remove_all(context.function_name)
            else:
                logger.warn(
                    f'Unrecognized InvokeAction {event["InvokeAction"]} -- try one of configure_account, update_account, remove_account_config, remove_all'
                )
        except Exception as e:
            logger.error(f"Failed to handle invoke action: {e}")
        return False
    else:
        try:
            life_cycle_event = ctlifecycleevent.LifeCycleEvent(event)
        except Exception as e:
            logger.warn(f"Did not find a supported event: {e}")
            return
        if life_cycle_event.create_account:
            try:
                configure_account(life_cycle_event.child_account_id)
            except Exception as e:
                logger.error(
                    f"Failed to handle create/update event from Control Tower: {e}"
                )
        elif life_cycle_event.remove_account:
            try:
                remove_account_config(life_cycle_event.child_account_id)
            except Exception as e:
                logger.error(f"Failed to handle remove event from Control Tower: {e}")
        else:
            # TODO understand if this case is actually workable -- it would only work if
            # there's no `RequestType` in the event but there is enough information to
            # construct the CloudFormation response.
            logger.info(
                f"This is not an event handled by the integration. SKIPPING: {event}"
            )
            response = cfnhelper.cfnResponse(event, context)
            response.send(cfnhelper.responseCode.FAILED)
        return False
