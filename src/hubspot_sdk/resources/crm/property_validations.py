# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import (
    property_validation_crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type_params,
)
from ..._base_client import make_request_options
from ...types.crm.collection_response_public_property_validation_rule_no_paging import (
    CollectionResponsePublicPropertyValidationRuleNoPaging,
)
from ...types.crm.collection_response_public_property_validation_rule_map_no_paging import (
    CollectionResponsePublicPropertyValidationRuleMapNoPaging,
)

__all__ = ["PropertyValidationsResource", "AsyncPropertyValidationsResource"]


class PropertyValidationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PropertyValidationsResourceWithStreamingResponse(self)

    def list(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleMapNoPaging:
        """
        Read all properties with validation rules for a given object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return self._get(
            f"/crm/v3/property-validations/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    def crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type(
        self,
        rule_type: Literal[
            "FORMAT",
            "ALPHANUMERIC",
            "MAX_LENGTH",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "MAX_NUMBER",
            "START_DATE",
            "END_DATE",
            "SPECIAL_CHARACTERS",
            "WHITESPACE",
            "DECIMAL",
            "BEFORE_DURATION",
            "AFTER_DURATION",
            "DAYS_OF_WEEK",
            "REGEX",
            "START_DATETIME",
            "END_DATETIME",
            "BEFORE_DATETIME_DURATION",
            "AFTER_DATETIME_DURATION",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "DOMAIN",
        ],
        *,
        object_type_id: str,
        property_name: str,
        rule_arguments: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a specific validation rule for a property identified by its name and rule
        type.

        Args:
          rule_arguments: A list of arguments that define the constraints for the validation rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        if not rule_type:
            raise ValueError(f"Expected a non-empty value for `rule_type` but received {rule_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}/rule-type/{rule_type}",
            body=maybe_transform(
                {"rule_arguments": rule_arguments},
                property_validation_crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type_params.PropertyValidationCrmV3PropertyValidationsObjectTypeIDPropertyNameRuleTypeRuleTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        property_name: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleNoPaging:
        """
        Read a property's validation rules identified by {propertyName}.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._get(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )


class AsyncPropertyValidationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertyValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertyValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertyValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertyValidationsResourceWithStreamingResponse(self)

    async def list(
        self,
        object_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleMapNoPaging:
        """
        Read all properties with validation rules for a given object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return await self._get(
            f"/crm/v3/property-validations/{object_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    async def crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type(
        self,
        rule_type: Literal[
            "FORMAT",
            "ALPHANUMERIC",
            "MAX_LENGTH",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "MAX_NUMBER",
            "START_DATE",
            "END_DATE",
            "SPECIAL_CHARACTERS",
            "WHITESPACE",
            "DECIMAL",
            "BEFORE_DURATION",
            "AFTER_DURATION",
            "DAYS_OF_WEEK",
            "REGEX",
            "START_DATETIME",
            "END_DATETIME",
            "BEFORE_DATETIME_DURATION",
            "AFTER_DATETIME_DURATION",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "DOMAIN",
        ],
        *,
        object_type_id: str,
        property_name: str,
        rule_arguments: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update a specific validation rule for a property identified by its name and rule
        type.

        Args:
          rule_arguments: A list of arguments that define the constraints for the validation rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        if not rule_type:
            raise ValueError(f"Expected a non-empty value for `rule_type` but received {rule_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}/rule-type/{rule_type}",
            body=await async_maybe_transform(
                {"rule_arguments": rule_arguments},
                property_validation_crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type_params.PropertyValidationCrmV3PropertyValidationsObjectTypeIDPropertyNameRuleTypeRuleTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        property_name: str,
        *,
        object_type_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicPropertyValidationRuleNoPaging:
        """
        Read a property's validation rules identified by {propertyName}.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._get(
            f"/crm/v3/property-validations/{object_type_id}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )


class PropertyValidationsResourceWithRawResponse:
    def __init__(self, property_validations: PropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = to_raw_response_wrapper(
            property_validations.list,
        )
        self.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type = to_raw_response_wrapper(
            property_validations.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type,
        )
        self.get = to_raw_response_wrapper(
            property_validations.get,
        )


class AsyncPropertyValidationsResourceWithRawResponse:
    def __init__(self, property_validations: AsyncPropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = async_to_raw_response_wrapper(
            property_validations.list,
        )
        self.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type = (
            async_to_raw_response_wrapper(
                property_validations.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type,
            )
        )
        self.get = async_to_raw_response_wrapper(
            property_validations.get,
        )


class PropertyValidationsResourceWithStreamingResponse:
    def __init__(self, property_validations: PropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = to_streamed_response_wrapper(
            property_validations.list,
        )
        self.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type = (
            to_streamed_response_wrapper(
                property_validations.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type,
            )
        )
        self.get = to_streamed_response_wrapper(
            property_validations.get,
        )


class AsyncPropertyValidationsResourceWithStreamingResponse:
    def __init__(self, property_validations: AsyncPropertyValidationsResource) -> None:
        self._property_validations = property_validations

        self.list = async_to_streamed_response_wrapper(
            property_validations.list,
        )
        self.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type = (
            async_to_streamed_response_wrapper(
                property_validations.crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type,
            )
        )
        self.get = async_to_streamed_response_wrapper(
            property_validations.get,
        )
