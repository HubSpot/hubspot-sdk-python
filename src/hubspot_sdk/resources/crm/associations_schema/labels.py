# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ....types.crm.associations_schema import (
    label_batch_create_params,
    label_create_label_params,
    label_update_label_params,
)
from ....types.crm.collection_response_association_spec_with_label_no_paging import (
    CollectionResponseAssociationSpecWithLabelNoPaging,
)
from ....types.crm.batch_response_public_association_definition_user_configuration import (
    BatchResponsePublicAssociationDefinitionUserConfiguration,
)
from ....types.crm.public_association_definition_configuration_create_request_param import (
    PublicAssociationDefinitionConfigurationCreateRequestParam,
)

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def batch_create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionUserConfiguration:
        """
        Create multiple association definitions between two specified CRM object types
        in a single request.

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
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/create",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform({"inputs": inputs}, label_batch_create_params.LabelBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionUserConfiguration,
        )

    def create_label(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        label: str,
        name: str,
        inverse_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationSpecWithLabelNoPaging:
        """
        Create a new label that describes the relationship between two specified CRM
        object types. This can help in categorizing and managing associations more
        effectively.

        Args:
          label: A descriptor that provides context about the relationship between two associated
              CRM objects.

          name: The unique identifier for the association definition.

          inverse_label: An optional descriptor that clarifies the reverse relationship in the
              association.

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
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "inverse_label": inverse_label,
                },
                label_create_label_params.LabelCreateLabelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseAssociationSpecWithLabelNoPaging,
        )

    def delete_label(
        self,
        association_type_id: int,
        *,
        from_object_type: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a specific label from the association between two CRM object types.

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
        return self._delete(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels/{association_type_id}",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
                association_type_id=association_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationSpecWithLabelNoPaging:
        """
        Retrieve all labels that describe the relationships between two specified CRM
        object types. These labels provide context about the nature of the associations.

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
        return self._get(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseAssociationSpecWithLabelNoPaging,
        )

    def update_label(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        association_type_id: int,
        label: str,
        inverse_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update an existing label that describes the relationship between two specified
        CRM object types. This allows for modifications to existing association labels
        to better reflect the nature of the relationship.

        Args:
          association_type_id: The unique identifier for the association type.

          label: A descriptor that provides context about the relationship between associated
              records.

          inverse_label: An optional descriptor for the inverse relationship between associated records.

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
        return self._put(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=maybe_transform(
                {
                    "association_type_id": association_type_id,
                    "label": label,
                    "inverse_label": inverse_label,
                },
                label_update_label_params.LabelUpdateLabelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def batch_create(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[PublicAssociationDefinitionConfigurationCreateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicAssociationDefinitionUserConfiguration:
        """
        Create multiple association definitions between two specified CRM object types
        in a single request.

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
                "/crm/associations/2026-03/definitions/configurations/{from_object_type}/{to_object_type}/batch/create",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform({"inputs": inputs}, label_batch_create_params.LabelBatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicAssociationDefinitionUserConfiguration,
        )

    async def create_label(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        label: str,
        name: str,
        inverse_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationSpecWithLabelNoPaging:
        """
        Create a new label that describes the relationship between two specified CRM
        object types. This can help in categorizing and managing associations more
        effectively.

        Args:
          label: A descriptor that provides context about the relationship between two associated
              CRM objects.

          name: The unique identifier for the association definition.

          inverse_label: An optional descriptor that clarifies the reverse relationship in the
              association.

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
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "inverse_label": inverse_label,
                },
                label_create_label_params.LabelCreateLabelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseAssociationSpecWithLabelNoPaging,
        )

    async def delete_label(
        self,
        association_type_id: int,
        *,
        from_object_type: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a specific label from the association between two CRM object types.

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
        return await self._delete(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels/{association_type_id}",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
                association_type_id=association_type_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseAssociationSpecWithLabelNoPaging:
        """
        Retrieve all labels that describe the relationships between two specified CRM
        object types. These labels provide context about the nature of the associations.

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
        return await self._get(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseAssociationSpecWithLabelNoPaging,
        )

    async def update_label(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        association_type_id: int,
        label: str,
        inverse_label: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update an existing label that describes the relationship between two specified
        CRM object types. This allows for modifications to existing association labels
        to better reflect the nature of the relationship.

        Args:
          association_type_id: The unique identifier for the association type.

          label: A descriptor that provides context about the relationship between associated
              records.

          inverse_label: An optional descriptor for the inverse relationship between associated records.

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
        return await self._put(
            path_template(
                "/crm/associations/2026-03/{from_object_type}/{to_object_type}/labels",
                from_object_type=from_object_type,
                to_object_type=to_object_type,
            ),
            body=await async_maybe_transform(
                {
                    "association_type_id": association_type_id,
                    "label": label,
                    "inverse_label": inverse_label,
                },
                label_update_label_params.LabelUpdateLabelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.batch_create = to_raw_response_wrapper(
            labels.batch_create,
        )
        self.create_label = to_raw_response_wrapper(
            labels.create_label,
        )
        self.delete_label = to_raw_response_wrapper(
            labels.delete_label,
        )
        self.list_labels = to_raw_response_wrapper(
            labels.list_labels,
        )
        self.update_label = to_raw_response_wrapper(
            labels.update_label,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.batch_create = async_to_raw_response_wrapper(
            labels.batch_create,
        )
        self.create_label = async_to_raw_response_wrapper(
            labels.create_label,
        )
        self.delete_label = async_to_raw_response_wrapper(
            labels.delete_label,
        )
        self.list_labels = async_to_raw_response_wrapper(
            labels.list_labels,
        )
        self.update_label = async_to_raw_response_wrapper(
            labels.update_label,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.batch_create = to_streamed_response_wrapper(
            labels.batch_create,
        )
        self.create_label = to_streamed_response_wrapper(
            labels.create_label,
        )
        self.delete_label = to_streamed_response_wrapper(
            labels.delete_label,
        )
        self.list_labels = to_streamed_response_wrapper(
            labels.list_labels,
        )
        self.update_label = to_streamed_response_wrapper(
            labels.update_label,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.batch_create = async_to_streamed_response_wrapper(
            labels.batch_create,
        )
        self.create_label = async_to_streamed_response_wrapper(
            labels.create_label,
        )
        self.delete_label = async_to_streamed_response_wrapper(
            labels.delete_label,
        )
        self.list_labels = async_to_streamed_response_wrapper(
            labels.list_labels,
        )
        self.update_label = async_to_streamed_response_wrapper(
            labels.update_label,
        )
