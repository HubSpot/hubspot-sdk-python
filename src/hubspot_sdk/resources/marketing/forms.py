# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.marketing import (
    form_list_params,
    form_read_params,
    form_update_params,
)
from ...types.marketing.field_group_param import FieldGroupParam
from ...types.marketing.form_definition_base import FormDefinitionBase
from ...types.marketing.hub_spot_form_definition import HubSpotFormDefinition
from ...types.marketing.form_display_options_param import FormDisplayOptionsParam
from ...types.marketing.hub_spot_form_configuration_param import HubSpotFormConfigurationParam

__all__ = ["FormsResource", "AsyncFormsResource"]


class FormsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FormsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """Add a new `hubspot` form"""
        return self._post(
            "/marketing/v3/forms/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )

    def update(
        self,
        form_id: str,
        *,
        archived: bool | Omit = omit,
        configuration: HubSpotFormConfigurationParam | Omit = omit,
        display_options: FormDisplayOptionsParam | Omit = omit,
        field_groups: Iterable[FieldGroupParam] | Omit = omit,
        legal_consent_options: form_update_params.LegalConsentOptions | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Update some of the form definition components

        Args:
          archived: Whether this form is archived.

          display_options: Options for styling the form.

          field_groups: The fields in the form, grouped in rows.

          name: The name of the form. Expected to be unique for a hub.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._patch(
            f"/marketing/v3/forms/{form_id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "configuration": configuration,
                    "display_options": display_options,
                    "field_groups": field_groups,
                    "legal_consent_options": legal_consent_options,
                    "name": name,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        form_types: List[Literal["hubspot", "captured", "flow", "blog_comment", "all"]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[HubSpotFormDefinition]:
        """Returns a list of forms based on the search filters.

        By default, it returns the
        first 20 `hubspot` forms

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          form_types: The form types to be included in the results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/v3/forms/",
            page=SyncPage[HubSpotFormDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "form_types": form_types,
                        "limit": limit,
                    },
                    form_list_params.FormListParams,
                ),
            ),
            model=HubSpotFormDefinition,
        )

    def delete(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a form definition.

        New submissions will not be accepted and the form
        definition will be permanently deleted after 3 months.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
        self,
        form_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Returns a form based on the form ID provided.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._get(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, form_read_params.FormReadParams),
            ),
            cast_to=FormDefinitionBase,
        )

    def replace(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Update all fields of a hubspot form definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return self._put(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )


class AsyncFormsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFormsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """Add a new `hubspot` form"""
        return await self._post(
            "/marketing/v3/forms/",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )

    async def update(
        self,
        form_id: str,
        *,
        archived: bool | Omit = omit,
        configuration: HubSpotFormConfigurationParam | Omit = omit,
        display_options: FormDisplayOptionsParam | Omit = omit,
        field_groups: Iterable[FieldGroupParam] | Omit = omit,
        legal_consent_options: form_update_params.LegalConsentOptions | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Update some of the form definition components

        Args:
          archived: Whether this form is archived.

          display_options: Options for styling the form.

          field_groups: The fields in the form, grouped in rows.

          name: The name of the form. Expected to be unique for a hub.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._patch(
            f"/marketing/v3/forms/{form_id}",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "configuration": configuration,
                    "display_options": display_options,
                    "field_groups": field_groups,
                    "legal_consent_options": legal_consent_options,
                    "name": name,
                },
                form_update_params.FormUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        form_types: List[Literal["hubspot", "captured", "flow", "blog_comment", "all"]] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[HubSpotFormDefinition, AsyncPage[HubSpotFormDefinition]]:
        """Returns a list of forms based on the search filters.

        By default, it returns the
        first 20 `hubspot` forms

        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          form_types: The form types to be included in the results.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/v3/forms/",
            page=AsyncPage[HubSpotFormDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "form_types": form_types,
                        "limit": limit,
                    },
                    form_list_params.FormListParams,
                ),
            ),
            model=HubSpotFormDefinition,
        )

    async def delete(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a form definition.

        New submissions will not be accepted and the form
        definition will be permanently deleted after 3 months.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
        self,
        form_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Returns a form based on the form ID provided.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._get(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, form_read_params.FormReadParams),
            ),
            cast_to=FormDefinitionBase,
        )

    async def replace(
        self,
        form_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormDefinitionBase:
        """
        Update all fields of a hubspot form definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not form_id:
            raise ValueError(f"Expected a non-empty value for `form_id` but received {form_id!r}")
        return await self._put(
            f"/marketing/v3/forms/{form_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormDefinitionBase,
        )


class FormsResourceWithRawResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.create = to_raw_response_wrapper(
            forms.create,
        )
        self.update = to_raw_response_wrapper(
            forms.update,
        )
        self.list = to_raw_response_wrapper(
            forms.list,
        )
        self.delete = to_raw_response_wrapper(
            forms.delete,
        )
        self.read = to_raw_response_wrapper(
            forms.read,
        )
        self.replace = to_raw_response_wrapper(
            forms.replace,
        )


class AsyncFormsResourceWithRawResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.create = async_to_raw_response_wrapper(
            forms.create,
        )
        self.update = async_to_raw_response_wrapper(
            forms.update,
        )
        self.list = async_to_raw_response_wrapper(
            forms.list,
        )
        self.delete = async_to_raw_response_wrapper(
            forms.delete,
        )
        self.read = async_to_raw_response_wrapper(
            forms.read,
        )
        self.replace = async_to_raw_response_wrapper(
            forms.replace,
        )


class FormsResourceWithStreamingResponse:
    def __init__(self, forms: FormsResource) -> None:
        self._forms = forms

        self.create = to_streamed_response_wrapper(
            forms.create,
        )
        self.update = to_streamed_response_wrapper(
            forms.update,
        )
        self.list = to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = to_streamed_response_wrapper(
            forms.delete,
        )
        self.read = to_streamed_response_wrapper(
            forms.read,
        )
        self.replace = to_streamed_response_wrapper(
            forms.replace,
        )


class AsyncFormsResourceWithStreamingResponse:
    def __init__(self, forms: AsyncFormsResource) -> None:
        self._forms = forms

        self.create = async_to_streamed_response_wrapper(
            forms.create,
        )
        self.update = async_to_streamed_response_wrapper(
            forms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            forms.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            forms.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            forms.read,
        )
        self.replace = async_to_streamed_response_wrapper(
            forms.replace,
        )
