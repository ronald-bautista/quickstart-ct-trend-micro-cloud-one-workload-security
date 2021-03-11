# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 12.5.841
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class ComputerGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_computer_group(self, computer_group, api_version, **kwargs):  # noqa: E501
        """Create a Computer Group  # noqa: E501

        Create a new computer group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_computer_group(computer_group, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ComputerGroup computer_group: The settings of the new computer group. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_computer_group_with_http_info(computer_group, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_computer_group_with_http_info(computer_group, api_version, **kwargs)  # noqa: E501
            return data

    def create_computer_group_with_http_info(self, computer_group, api_version, **kwargs):  # noqa: E501
        """Create a Computer Group  # noqa: E501

        Create a new computer group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_computer_group_with_http_info(computer_group, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ComputerGroup computer_group: The settings of the new computer group. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_group', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_computer_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_group' is set
        if ('computer_group' not in params or
                params['computer_group'] is None):
            raise ValueError("Missing the required parameter `computer_group` when calling `create_computer_group`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_computer_group`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'computer_group' in params:
            body_params = params['computer_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputerGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_computer_group(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Delete a Computer Group  # noqa: E501

        Delete a computer group by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_computer_group(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_computer_group_with_http_info(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Delete a Computer Group  # noqa: E501

        Delete a computer group by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_computer_group_with_http_info(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_group_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_computer_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_group_id' is set
        if ('computer_group_id' not in params or
                params['computer_group_id'] is None):
            raise ValueError("Missing the required parameter `computer_group_id` when calling `delete_computer_group`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_computer_group`")  # noqa: E501

        if 'computer_group_id' in params and not re.search('\\d+', str(params['computer_group_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_group_id` when calling `delete_computer_group`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_group_id' in params:
            path_params['computerGroupID'] = params['computer_group_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups/{computerGroupID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_computer_group(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Describe a Computer Group  # noqa: E501

        Describe a computer group by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_computer_group(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_computer_group_with_http_info(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Describe a Computer Group  # noqa: E501

        Describe a computer group by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_computer_group_with_http_info(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_group_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_computer_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_group_id' is set
        if ('computer_group_id' not in params or
                params['computer_group_id'] is None):
            raise ValueError("Missing the required parameter `computer_group_id` when calling `describe_computer_group`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_computer_group`")  # noqa: E501

        if 'computer_group_id' in params and not re.search('\\d+', str(params['computer_group_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_group_id` when calling `describe_computer_group`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_group_id' in params:
            path_params['computerGroupID'] = params['computer_group_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups/{computerGroupID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputerGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_computer_groups(self, api_version, **kwargs):  # noqa: E501
        """List Computer Groups  # noqa: E501

        Lists all computer groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_computer_groups(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_computer_groups_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_computer_groups_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_computer_groups_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Computer Groups  # noqa: E501

        Lists all computer groups.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_computer_groups_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: ComputerGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_computer_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_computer_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputerGroups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_computer_group(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Modify a Computer Group  # noqa: E501

        Modify a computer group by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_computer_group(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param ComputerGroup computer_group: The settings of the computer group to modify.
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_computer_group_with_http_info(computer_group_id, api_version, **kwargs)  # noqa: E501
            return data

    def modify_computer_group_with_http_info(self, computer_group_id, api_version, **kwargs):  # noqa: E501
        """Modify a Computer Group  # noqa: E501

        Modify a computer group by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_computer_group_with_http_info(computer_group_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_group_id: The ID number of the computer group to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param ComputerGroup computer_group: The settings of the computer group to modify.
        :return: ComputerGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_group_id', 'api_version', 'computer_group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_computer_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_group_id' is set
        if ('computer_group_id' not in params or
                params['computer_group_id'] is None):
            raise ValueError("Missing the required parameter `computer_group_id` when calling `modify_computer_group`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_computer_group`")  # noqa: E501

        if 'computer_group_id' in params and not re.search('\\d+', str(params['computer_group_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_group_id` when calling `modify_computer_group`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_group_id' in params:
            path_params['computerGroupID'] = params['computer_group_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'computer_group' in params:
            body_params = params['computer_group']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups/{computerGroupID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputerGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_computer_groups(self, api_version, **kwargs):  # noqa: E501
        """Search Computer Groups  # noqa: E501

        Search for computer groups using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_computer_groups(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: ComputerGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_computer_groups_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_computer_groups_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_computer_groups_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Computer Groups  # noqa: E501

        Search for computer groups using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_computer_groups_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: ComputerGroups
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_computer_groups" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_computer_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computergroups/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComputerGroups',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
