import c1wsconnectorapi
import boto3
from botocore.exceptions import ClientError
import base64
import logging
import json
import os

logger = logging.getLogger()


SECRET_ID = "TrendMicro/CloudOne/WorkloadSecurityApiKey"
ControlTowerRoleName = "AWSControlTowerExecution"
IamRoleName = "CloudOneWorkloadConnectorRole"
IamPolicyName = "CloudOneWorkloadConnectorPolicy"
CloudOneWorkloadAccountId = os.environ["AccountIdForRole"]


def get_api_key():
    client = boto3.client("secretsmanager")
    try:
        get_secret_value_response = client.get_secret_value(SecretId=SECRET_ID)
    except ClientError as e:
        logger.error(f"Failed to retrieve secret {SECRET_ID}: {e}")
        if e.response["Error"]["Code"] == "DecryptionFailureException":
            raise e
        elif e.response["Error"]["Code"] == "InternalServiceErrorException":
            raise e
        elif e.response["Error"]["Code"] == "InvalidParameterException":
            raise e
        elif e.response["Error"]["Code"] == "InvalidRequestException":
            raise e
        elif e.response["Error"]["Code"] == "ResourceNotFoundException":
            raise e
        elif e.response["Error"]["Code"] == "AccessDeniedException":
            raise e
    else:
        if "SecretString" in get_secret_value_response:
            secret = json.loads(get_secret_value_response["SecretString"])["ApiKey"]
            return secret
        else:
            decoded_binary_secret = base64.b64decode(
                get_secret_value_response["SecretBinary"]
            )
            password = decoded_binary_secret.password
            return password


def get_assume_role_policy_document():
    connector_api = c1wsconnectorapi.CloudOneConnector(get_api_key())
    assume_role_policy_document = {
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {"AWS": CloudOneWorkloadAccountId},
                "Condition": {
                    "StringEquals": {"sts:ExternalId": connector_api.get_externalid()}
                },
                "Sid": "",
            }
        ],
        "Version": "2012-10-17",
    }
    return json.dumps(assume_role_policy_document)


policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeLicenses",
                "ec2:DescribeInstances",
                "ec2:DescribeTags",
                "ec2:DescribeImages",
                "ec2:DescribeRegions",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "iam:ListAccountAliases",
                "iam:GetRolePolicy",
                "iam:GetRole",
                "workspaces:DescribeWorkspaces",
                "workspaces:DescribeWorkspaceBundles",
                "workspaces:DescribeWorkspaceDirectories",
                "workspaces:DescribeTags",
            ],
            "Resource": "*",
        }
    ],
}
