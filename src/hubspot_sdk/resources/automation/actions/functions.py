# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.automation.actions import (
    function_create_or_replace_params,
    function_create_or_replace_by_function_type_params,
)
from ....types.automation.public_action_function import PublicActionFunction
from ....types.automation.public_action_function_identifier import PublicActionFunctionIdentifier
from ....types.automation.collection_response_public_action_function_identifier_no_paging import (
    CollectionResponsePublicActionFunctionIdentifierNoPaging,
)

__all__ = ["FunctionsResource", "AsyncFunctionsResource"]


class FunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FunctionsResourceWithStreamingResponse(self)

    def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicActionFunctionIdentifierNoPaging:
        """
        Retrieve all functions included in a definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicActionFunctionIdentifierNoPaging,
        )

    def delete(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a function for a definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_or_replace(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Update a function for a given definition by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._put(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            body=maybe_transform(body, function_create_or_replace_params.FunctionCreateOrReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    def create_or_replace_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Add a function for a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return self._put(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            body=maybe_transform(
                body, function_create_or_replace_by_function_type_params.FunctionCreateOrReplaceByFunctionTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    def delete_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a function within a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Retrieve a specific function from a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )

    def get_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Retrieve functions by a type for a given definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )


class AsyncFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFunctionsResourceWithStreamingResponse(self)

    async def list(
        self,
        definition_id: str,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicActionFunctionIdentifierNoPaging:
        """
        Retrieve all functions included in a definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        return await self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicActionFunctionIdentifierNoPaging,
        )

    async def delete(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a function for a definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_or_replace(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Update a function for a given definition by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._put(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            body=await async_maybe_transform(body, function_create_or_replace_params.FunctionCreateOrReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    async def create_or_replace_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunctionIdentifier:
        """
        Add a function for a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return await self._put(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            body=await async_maybe_transform(
                body, function_create_or_replace_by_function_type_params.FunctionCreateOrReplaceByFunctionTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunctionIdentifier,
        )

    async def delete_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a function within a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        function_id: str,
        *,
        app_id: int,
        definition_id: str,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Retrieve a specific function from a given definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        if not function_id:
            raise ValueError(f"Expected a non-empty value for `function_id` but received {function_id!r}")
        return await self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}/{function_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )

    async def get_by_function_type(
        self,
        function_type: Literal[
            "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
        ],
        *,
        app_id: int,
        definition_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicActionFunction:
        """
        Retrieve functions by a type for a given definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not definition_id:
            raise ValueError(f"Expected a non-empty value for `definition_id` but received {definition_id!r}")
        if not function_type:
            raise ValueError(f"Expected a non-empty value for `function_type` but received {function_type!r}")
        return await self._get(
            f"/automation/v4/actions/{app_id}/{definition_id}/functions/{function_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicActionFunction,
        )


class FunctionsResourceWithRawResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.list = to_raw_response_wrapper(
            functions.list,
        )
        self.delete = to_raw_response_wrapper(
            functions.delete,
        )
        self.create_or_replace = to_raw_response_wrapper(
            functions.create_or_replace,
        )
        self.create_or_replace_by_function_type = to_raw_response_wrapper(
            functions.create_or_replace_by_function_type,
        )
        self.delete_by_function_type = to_raw_response_wrapper(
            functions.delete_by_function_type,
        )
        self.get = to_raw_response_wrapper(
            functions.get,
        )
        self.get_by_function_type = to_raw_response_wrapper(
            functions.get_by_function_type,
        )


class AsyncFunctionsResourceWithRawResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.list = async_to_raw_response_wrapper(
            functions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            functions.delete,
        )
        self.create_or_replace = async_to_raw_response_wrapper(
            functions.create_or_replace,
        )
        self.create_or_replace_by_function_type = async_to_raw_response_wrapper(
            functions.create_or_replace_by_function_type,
        )
        self.delete_by_function_type = async_to_raw_response_wrapper(
            functions.delete_by_function_type,
        )
        self.get = async_to_raw_response_wrapper(
            functions.get,
        )
        self.get_by_function_type = async_to_raw_response_wrapper(
            functions.get_by_function_type,
        )


class FunctionsResourceWithStreamingResponse:
    def __init__(self, functions: FunctionsResource) -> None:
        self._functions = functions

        self.list = to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = to_streamed_response_wrapper(
            functions.delete,
        )
        self.create_or_replace = to_streamed_response_wrapper(
            functions.create_or_replace,
        )
        self.create_or_replace_by_function_type = to_streamed_response_wrapper(
            functions.create_or_replace_by_function_type,
        )
        self.delete_by_function_type = to_streamed_response_wrapper(
            functions.delete_by_function_type,
        )
        self.get = to_streamed_response_wrapper(
            functions.get,
        )
        self.get_by_function_type = to_streamed_response_wrapper(
            functions.get_by_function_type,
        )


class AsyncFunctionsResourceWithStreamingResponse:
    def __init__(self, functions: AsyncFunctionsResource) -> None:
        self._functions = functions

        self.list = async_to_streamed_response_wrapper(
            functions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            functions.delete,
        )
        self.create_or_replace = async_to_streamed_response_wrapper(
            functions.create_or_replace,
        )
        self.create_or_replace_by_function_type = async_to_streamed_response_wrapper(
            functions.create_or_replace_by_function_type,
        )
        self.delete_by_function_type = async_to_streamed_response_wrapper(
            functions.delete_by_function_type,
        )
        self.get = async_to_streamed_response_wrapper(
            functions.get,
        )
        self.get_by_function_type = async_to_streamed_response_wrapper(
            functions.get_by_function_type,
        )
