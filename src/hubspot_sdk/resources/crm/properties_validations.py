# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import properties_validation_update_by_object_type_id_property_name_and_rule_type_params
from ..._base_client import make_request_options
from ...types.crm.public_property_validation_rule import PublicPropertyValidationRule
from ...types.crm.collection_response_public_property_validation_rule_no_paging import (
    CollectionResponsePublicPropertyValidationRuleNoPaging,
)
from ...types.crm.collection_response_public_property_validation_rule_map_no_paging import (
    CollectionResponsePublicPropertyValidationRuleMapNoPaging,
)

__all__ = ["PropertiesValidationsResource", "AsyncPropertiesValidationsResource"]


class PropertiesValidationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertiesValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PropertiesValidationsResourceWithStreamingResponse(self)

    def get_by_object_type_id(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return self._get(
            path_template("/crm/property-validations/2026-03/{object_type_id}", object_type_id=object_type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    def get_by_object_type_id_and_property_name(
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
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}",
                object_type_id=object_type_id,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )

    def get_by_object_type_id_property_name_and_rule_type(
        self,
        rule_type: Literal[
            "AFTER_DATETIME_DURATION",
            "AFTER_DURATION",
            "ALPHANUMERIC",
            "BEFORE_DATETIME_DURATION",
            "BEFORE_DURATION",
            "DAYS_OF_WEEK",
            "DECIMAL",
            "DOMAIN",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "END_DATE",
            "END_DATETIME",
            "FORMAT",
            "MAX_LENGTH",
            "MAX_NUMBER",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "REGEX",
            "SPECIAL_CHARACTERS",
            "START_DATE",
            "START_DATETIME",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "WHITESPACE",
        ],
        *,
        object_type_id: str,
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPropertyValidationRule:
        """
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
        if not rule_type:
            raise ValueError(f"Expected a non-empty value for `rule_type` but received {rule_type!r}")
        return self._get(
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}/rule-type/{rule_type}",
                object_type_id=object_type_id,
                property_name=property_name,
                rule_type=rule_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPropertyValidationRule,
        )

    def update_by_object_type_id_property_name_and_rule_type(
        self,
        rule_type: Literal[
            "AFTER_DATETIME_DURATION",
            "AFTER_DURATION",
            "ALPHANUMERIC",
            "BEFORE_DATETIME_DURATION",
            "BEFORE_DURATION",
            "DAYS_OF_WEEK",
            "DECIMAL",
            "DOMAIN",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "END_DATE",
            "END_DATETIME",
            "FORMAT",
            "MAX_LENGTH",
            "MAX_NUMBER",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "REGEX",
            "SPECIAL_CHARACTERS",
            "START_DATE",
            "START_DATETIME",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "WHITESPACE",
        ],
        *,
        object_type_id: str,
        property_name: str,
        rule_arguments: SequenceNotStr[str],
        should_apply_normalization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
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
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}/rule-type/{rule_type}",
                object_type_id=object_type_id,
                property_name=property_name,
                rule_type=rule_type,
            ),
            body=maybe_transform(
                {
                    "rule_arguments": rule_arguments,
                    "should_apply_normalization": should_apply_normalization,
                },
                properties_validation_update_by_object_type_id_property_name_and_rule_type_params.PropertiesValidationUpdateByObjectTypeIDPropertyNameAndRuleTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPropertiesValidationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertiesValidationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesValidationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesValidationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertiesValidationsResourceWithStreamingResponse(self)

    async def get_by_object_type_id(
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
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type_id:
            raise ValueError(f"Expected a non-empty value for `object_type_id` but received {object_type_id!r}")
        return await self._get(
            path_template("/crm/property-validations/2026-03/{object_type_id}", object_type_id=object_type_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleMapNoPaging,
        )

    async def get_by_object_type_id_and_property_name(
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
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}",
                object_type_id=object_type_id,
                property_name=property_name,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicPropertyValidationRuleNoPaging,
        )

    async def get_by_object_type_id_property_name_and_rule_type(
        self,
        rule_type: Literal[
            "AFTER_DATETIME_DURATION",
            "AFTER_DURATION",
            "ALPHANUMERIC",
            "BEFORE_DATETIME_DURATION",
            "BEFORE_DURATION",
            "DAYS_OF_WEEK",
            "DECIMAL",
            "DOMAIN",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "END_DATE",
            "END_DATETIME",
            "FORMAT",
            "MAX_LENGTH",
            "MAX_NUMBER",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "REGEX",
            "SPECIAL_CHARACTERS",
            "START_DATE",
            "START_DATETIME",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "WHITESPACE",
        ],
        *,
        object_type_id: str,
        property_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicPropertyValidationRule:
        """
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
        if not rule_type:
            raise ValueError(f"Expected a non-empty value for `rule_type` but received {rule_type!r}")
        return await self._get(
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}/rule-type/{rule_type}",
                object_type_id=object_type_id,
                property_name=property_name,
                rule_type=rule_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicPropertyValidationRule,
        )

    async def update_by_object_type_id_property_name_and_rule_type(
        self,
        rule_type: Literal[
            "AFTER_DATETIME_DURATION",
            "AFTER_DURATION",
            "ALPHANUMERIC",
            "BEFORE_DATETIME_DURATION",
            "BEFORE_DURATION",
            "DAYS_OF_WEEK",
            "DECIMAL",
            "DOMAIN",
            "EMAIL",
            "EMAIL_ALLOWED_DOMAINS",
            "EMAIL_BLOCKED_DOMAINS",
            "END_DATE",
            "END_DATETIME",
            "FORMAT",
            "MAX_LENGTH",
            "MAX_NUMBER",
            "MIN_LENGTH",
            "MIN_NUMBER",
            "PHONE_NUMBER_WITH_EXPLICIT_COUNTRY_CODE",
            "REGEX",
            "SPECIAL_CHARACTERS",
            "START_DATE",
            "START_DATETIME",
            "URL",
            "URL_ALLOWED_DOMAINS",
            "URL_BLOCKED_DOMAINS",
            "WHITESPACE",
        ],
        *,
        object_type_id: str,
        property_name: str,
        rule_arguments: SequenceNotStr[str],
        should_apply_normalization: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
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
            path_template(
                "/crm/property-validations/2026-03/{object_type_id}/{property_name}/rule-type/{rule_type}",
                object_type_id=object_type_id,
                property_name=property_name,
                rule_type=rule_type,
            ),
            body=await async_maybe_transform(
                {
                    "rule_arguments": rule_arguments,
                    "should_apply_normalization": should_apply_normalization,
                },
                properties_validation_update_by_object_type_id_property_name_and_rule_type_params.PropertiesValidationUpdateByObjectTypeIDPropertyNameAndRuleTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PropertiesValidationsResourceWithRawResponse:
    def __init__(self, properties_validations: PropertiesValidationsResource) -> None:
        self._properties_validations = properties_validations

        self.get_by_object_type_id = to_raw_response_wrapper(
            properties_validations.get_by_object_type_id,
        )
        self.get_by_object_type_id_and_property_name = to_raw_response_wrapper(
            properties_validations.get_by_object_type_id_and_property_name,
        )
        self.get_by_object_type_id_property_name_and_rule_type = to_raw_response_wrapper(
            properties_validations.get_by_object_type_id_property_name_and_rule_type,
        )
        self.update_by_object_type_id_property_name_and_rule_type = to_raw_response_wrapper(
            properties_validations.update_by_object_type_id_property_name_and_rule_type,
        )


class AsyncPropertiesValidationsResourceWithRawResponse:
    def __init__(self, properties_validations: AsyncPropertiesValidationsResource) -> None:
        self._properties_validations = properties_validations

        self.get_by_object_type_id = async_to_raw_response_wrapper(
            properties_validations.get_by_object_type_id,
        )
        self.get_by_object_type_id_and_property_name = async_to_raw_response_wrapper(
            properties_validations.get_by_object_type_id_and_property_name,
        )
        self.get_by_object_type_id_property_name_and_rule_type = async_to_raw_response_wrapper(
            properties_validations.get_by_object_type_id_property_name_and_rule_type,
        )
        self.update_by_object_type_id_property_name_and_rule_type = async_to_raw_response_wrapper(
            properties_validations.update_by_object_type_id_property_name_and_rule_type,
        )


class PropertiesValidationsResourceWithStreamingResponse:
    def __init__(self, properties_validations: PropertiesValidationsResource) -> None:
        self._properties_validations = properties_validations

        self.get_by_object_type_id = to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id,
        )
        self.get_by_object_type_id_and_property_name = to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id_and_property_name,
        )
        self.get_by_object_type_id_property_name_and_rule_type = to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id_property_name_and_rule_type,
        )
        self.update_by_object_type_id_property_name_and_rule_type = to_streamed_response_wrapper(
            properties_validations.update_by_object_type_id_property_name_and_rule_type,
        )


class AsyncPropertiesValidationsResourceWithStreamingResponse:
    def __init__(self, properties_validations: AsyncPropertiesValidationsResource) -> None:
        self._properties_validations = properties_validations

        self.get_by_object_type_id = async_to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id,
        )
        self.get_by_object_type_id_and_property_name = async_to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id_and_property_name,
        )
        self.get_by_object_type_id_property_name_and_rule_type = async_to_streamed_response_wrapper(
            properties_validations.get_by_object_type_id_property_name_and_rule_type,
        )
        self.update_by_object_type_id_property_name_and_rule_type = async_to_streamed_response_wrapper(
            properties_validations.update_by_object_type_id_property_name_and_rule_type,
        )
