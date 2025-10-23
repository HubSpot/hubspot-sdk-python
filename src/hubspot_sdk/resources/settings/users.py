# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.settings import (
    user_get_params,
    user_list_params,
    user_create_params,
    user_delete_params,
    user_update_params,
)
from ...types.settings.public_user import PublicUser
from ...types.settings.collection_response_public_team_no_paging import CollectionResponsePublicTeamNoPaging
from ...types.settings.collection_response_public_permission_set_no_paging import (
    CollectionResponsePublicPermissionSetNoPaging,
)

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        primary_team_id: str | Omit = omit,
        role_id: str | Omit = omit,
        secondary_team_ids: SequenceNotStr[str] | Omit = omit,
        send_welcome_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """New users will only have minimal permissions, which is contacts-base.

        A welcome
        email will prompt them to set a password and log in to HubSpot.

        Args:
          email: The created user's email

          primary_team_id: The user's primary team

          role_id: The user's role

          secondary_team_ids: The user's additional teams

          send_welcome_email: Whether to send a welcome email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/settings/v3/users/",
            body=maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "primary_team_id": primary_team_id,
                    "role_id": role_id,
                    "secondary_team_ids": secondary_team_ids,
                    "send_welcome_email": send_welcome_email,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicUser,
        )

    def update(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        primary_team_id: str | Omit = omit,
        role_id: str | Omit = omit,
        secondary_team_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """Modifies a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          primary_team_id: The user's primary team

          role_id: The user's role

          secondary_team_ids: The user's additional teams

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            f"/settings/v3/users/{user_id}",
            body=maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "primary_team_id": primary_team_id,
                    "role_id": role_id,
                    "secondary_team_ids": secondary_team_ids,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_property": id_property}, user_update_params.UserUpdateParams),
            ),
            cast_to=PublicUser,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicUser]:
        """
        Retrieves a list of users from an account

        Args:
          after: Results will display maximum 100 users per page. Additional results will be on
              the next page.

          limit: The number of users to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/settings/v3/users/",
            page=SyncPage[PublicUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=PublicUser,
        )

    def delete(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/settings/v3/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_property": id_property}, user_delete_params.UserDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """Retrieves a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            f"/settings/v3/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id_property": id_property}, user_get_params.UserGetParams),
            ),
            cast_to=PublicUser,
        )

    def list_roles(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPermissionSetNoPaging:
        """Retrieves the roles on an account"""
        return self._get(
            "/settings/v3/users/roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPermissionSetNoPaging,
        )

    def list_teams(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicTeamNoPaging:
        """View teams for this account"""
        return self._get(
            "/settings/v3/users/teams",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicTeamNoPaging,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        primary_team_id: str | Omit = omit,
        role_id: str | Omit = omit,
        secondary_team_ids: SequenceNotStr[str] | Omit = omit,
        send_welcome_email: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """New users will only have minimal permissions, which is contacts-base.

        A welcome
        email will prompt them to set a password and log in to HubSpot.

        Args:
          email: The created user's email

          primary_team_id: The user's primary team

          role_id: The user's role

          secondary_team_ids: The user's additional teams

          send_welcome_email: Whether to send a welcome email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/settings/v3/users/",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "primary_team_id": primary_team_id,
                    "role_id": role_id,
                    "secondary_team_ids": secondary_team_ids,
                    "send_welcome_email": send_welcome_email,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicUser,
        )

    async def update(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        primary_team_id: str | Omit = omit,
        role_id: str | Omit = omit,
        secondary_team_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """Modifies a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          primary_team_id: The user's primary team

          role_id: The user's role

          secondary_team_ids: The user's additional teams

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            f"/settings/v3/users/{user_id}",
            body=await async_maybe_transform(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "primary_team_id": primary_team_id,
                    "role_id": role_id,
                    "secondary_team_ids": secondary_team_ids,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id_property": id_property}, user_update_params.UserUpdateParams),
            ),
            cast_to=PublicUser,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicUser, AsyncPage[PublicUser]]:
        """
        Retrieves a list of users from an account

        Args:
          after: Results will display maximum 100 users per page. Additional results will be on
              the next page.

          limit: The number of users to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/settings/v3/users/",
            page=AsyncPage[PublicUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=PublicUser,
        )

    async def delete(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/settings/v3/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id_property": id_property}, user_delete_params.UserDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        user_id: str,
        *,
        id_property: Literal["USER_ID", "EMAIL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicUser:
        """Retrieves a user identified by `userId`.

        `userId` refers to the user's ID by
        default, or optionally email as specified by the `IdProperty` query param.

        Args:
          id_property: The name of a property with unique user values. Valid values are
              `USER_ID`(default) or `EMAIL`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            f"/settings/v3/users/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id_property": id_property}, user_get_params.UserGetParams),
            ),
            cast_to=PublicUser,
        )

    async def list_roles(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPermissionSetNoPaging:
        """Retrieves the roles on an account"""
        return await self._get(
            "/settings/v3/users/roles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPermissionSetNoPaging,
        )

    async def list_teams(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicTeamNoPaging:
        """View teams for this account"""
        return await self._get(
            "/settings/v3/users/teams",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicTeamNoPaging,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.list_roles = to_raw_response_wrapper(
            users.list_roles,
        )
        self.list_teams = to_raw_response_wrapper(
            users.list_teams,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.list_roles = async_to_raw_response_wrapper(
            users.list_roles,
        )
        self.list_teams = async_to_raw_response_wrapper(
            users.list_teams,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.list_roles = to_streamed_response_wrapper(
            users.list_roles,
        )
        self.list_teams = to_streamed_response_wrapper(
            users.list_teams,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.list_roles = async_to_streamed_response_wrapper(
            users.list_roles,
        )
        self.list_teams = async_to_streamed_response_wrapper(
            users.list_teams,
        )
