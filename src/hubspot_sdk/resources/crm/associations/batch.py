# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.associations import (
    batch_get_params,
    batch_create_params,
    batch_delete_params,
    batch_delete_labels_params,
    batch_create_default_params,
)
from ....types.crm.public_association_multi_post_param import PublicAssociationMultiPostParam
from ....types.crm.public_association_multi_archive_param import PublicAssociationMultiArchiveParam
from ....types.crm.batch_response_labels_between_object_pair import BatchResponseLabelsBetweenObjectPair
from ....types.crm.batch_response_public_default_association import BatchResponsePublicDefaultAssociation
from ....types.crm.public_default_association_multi_post_param import PublicDefaultAssociationMultiPostParam
from ....types.crm.public_fetch_associations_batch_request_param import PublicFetchAssociationsBatchRequestParam
from ....types.crm.batch_response_public_association_multi_with_label import (
    BatchResponsePublicAssociationMultiWithLabel,
)

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseLabelsBetweenObjectPair:
        """
        Batch create associations for objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/create",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseLabelsBetweenObjectPair,
        )

    def delete(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiArchiveParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Batch delete associations for objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/archive",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_default(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicDefaultAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicDefaultAssociation:
        """
        Create the default (most generic) association type between two object types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/associate/default",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, batch_create_default_params.BatchCreateDefaultParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicDefaultAssociation,
        )

    def delete_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Batch delete specific association labels for objects.

        Deleting an unlabeled
        association will also delete all labeled associations between those two objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/labels/archive",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, batch_delete_labels_params.BatchDeleteLabelsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicFetchAssociationsBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationMultiWithLabel:
        """Batch read associations for objects to specific object type.

        The 'after' field
        in a returned paging object can be added alongside the 'id' to retrieve the next
        page of associations from that objectId. The 'link' field is deprecated and
        should be ignored. Note: The 'paging' field will only be present if there are
        more pages and absent otherwise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/read",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationMultiWithLabel,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseLabelsBetweenObjectPair:
        """
        Batch create associations for objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/create",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseLabelsBetweenObjectPair,
        )

    async def delete(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiArchiveParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Batch delete associations for objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/archive",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_params.BatchDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_default(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicDefaultAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicDefaultAssociation:
        """
        Create the default (most generic) association type between two object types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/associate/default",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, batch_create_default_params.BatchCreateDefaultParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicDefaultAssociation,
        )

    async def delete_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Batch delete specific association labels for objects.

        Deleting an unlabeled
        association will also delete all labeled associations between those two objects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/labels/archive",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, batch_delete_labels_params.BatchDeleteLabelsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicFetchAssociationsBatchRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationMultiWithLabel:
        """Batch read associations for objects to specific object type.

        The 'after' field
        in a returned paging object can be added alongside the 'id' to retrieve the next
        page of associations from that objectId. The 'link' field is deprecated and
        should be ignored. Note: The 'paging' field will only be present if there are
        more pages and absent otherwise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/batch/read",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, batch_get_params.BatchGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationMultiWithLabel,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_raw_response_wrapper(
            batch.create,
        )
        self.delete = to_raw_response_wrapper(
            batch.delete,
        )
        self.create_default = to_raw_response_wrapper(
            batch.create_default,
        )
        self.delete_labels = to_raw_response_wrapper(
            batch.delete_labels,
        )
        self.get = to_raw_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_raw_response_wrapper(
            batch.create,
        )
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
        )
        self.create_default = async_to_raw_response_wrapper(
            batch.create_default,
        )
        self.delete_labels = async_to_raw_response_wrapper(
            batch.delete_labels,
        )
        self.get = async_to_raw_response_wrapper(
            batch.get,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.create = to_streamed_response_wrapper(
            batch.create,
        )
        self.delete = to_streamed_response_wrapper(
            batch.delete,
        )
        self.create_default = to_streamed_response_wrapper(
            batch.create_default,
        )
        self.delete_labels = to_streamed_response_wrapper(
            batch.delete_labels,
        )
        self.get = to_streamed_response_wrapper(
            batch.get,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.create = async_to_streamed_response_wrapper(
            batch.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
        )
        self.create_default = async_to_streamed_response_wrapper(
            batch.create_default,
        )
        self.delete_labels = async_to_streamed_response_wrapper(
            batch.delete_labels,
        )
        self.get = async_to_streamed_response_wrapper(
            batch.get,
        )
