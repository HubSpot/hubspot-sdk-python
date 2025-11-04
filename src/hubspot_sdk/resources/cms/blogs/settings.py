# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cms.blogs import (
    setting_list_params,
    setting_list_revisions_params,
    setting_update_languages_params,
    setting_attach_to_lang_group_params,
    setting_set_new_lang_primary_params,
    setting_detach_from_lang_group_params,
    setting_create_language_variation_params,
)
from ....types.cms.blogs.blog import Blog
from ....types.cms.blogs.version_blog import VersionBlog

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Blog]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/blog-settings/settings",
            page=SyncPage[Blog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    setting_list_params.SettingListParams,
                ),
            ),
            model=Blog,
        )

    def attach_to_lang_group(
        self,
        *,
        id: str,
        language: str,
        primary_id: str,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of the object to add to a multi-language group.

          language: Designated language of the object to add to a multi-language group.

          primary_id: ID of primary language object in multi-language group.

          primary_language: Primary language of the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/blog-settings/settings/multi-language/attach-to-lang-group",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                setting_attach_to_lang_group_params.SettingAttachToLangGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_language_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        primary_language: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Args:
          id: ID of blog to clone.

          language: Target language of new variant.

          primary_language: Language of primary blog to clone.

          slug: Path to this blog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/blog-settings/settings/multi-language/create-language-variation",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_language": primary_language,
                    "slug": slug,
                },
                setting_create_language_variation_params.SettingCreateLanguageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    def detach_from_lang_group(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/blog-settings/settings/multi-language/detach-from-lang-group",
            body=maybe_transform({"id": id}, setting_detach_from_lang_group_params.SettingDetachFromLangGroupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        blog_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get(
            f"/cms/v3/blog-settings/settings/{blog_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    def get_revision(
        self,
        revision_id: str,
        *,
        blog_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionBlog:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/cms/v3/blog-settings/settings/{blog_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionBlog,
        )

    def list_revisions(
        self,
        blog_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[VersionBlog]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get_api_list(
            f"/cms/v3/blog-settings/settings/{blog_id}/revisions",
            page=SyncPage[VersionBlog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    setting_list_revisions_params.SettingListRevisionsParams,
                ),
            ),
            model=VersionBlog,
        )

    def set_new_lang_primary(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/cms/v3/blog-settings/settings/multi-language/set-new-lang-primary",
            body=maybe_transform({"id": id}, setting_set_new_lang_primary_params.SettingSetNewLangPrimaryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_languages(
        self,
        *,
        languages: Dict[str, str],
        primary_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          languages: Map of object IDs to associated languages of object in the multi-language group.

          primary_id: ID of the primary object in the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/blog-settings/settings/multi-language/update-languages",
            body=maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                setting_update_languages_params.SettingUpdateLanguagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Blog, AsyncPage[Blog]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/blog-settings/settings",
            page=AsyncPage[Blog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    setting_list_params.SettingListParams,
                ),
            ),
            model=Blog,
        )

    async def attach_to_lang_group(
        self,
        *,
        id: str,
        language: str,
        primary_id: str,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of the object to add to a multi-language group.

          language: Designated language of the object to add to a multi-language group.

          primary_id: ID of primary language object in multi-language group.

          primary_language: Primary language of the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/blog-settings/settings/multi-language/attach-to-lang-group",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                setting_attach_to_lang_group_params.SettingAttachToLangGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_language_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        primary_language: str | Omit = omit,
        slug: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Args:
          id: ID of blog to clone.

          language: Target language of new variant.

          primary_language: Language of primary blog to clone.

          slug: Path to this blog.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/blog-settings/settings/multi-language/create-language-variation",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_language": primary_language,
                    "slug": slug,
                },
                setting_create_language_variation_params.SettingCreateLanguageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    async def detach_from_lang_group(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/blog-settings/settings/multi-language/detach-from-lang-group",
            body=await async_maybe_transform(
                {"id": id}, setting_detach_from_lang_group_params.SettingDetachFromLangGroupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        blog_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Blog:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return await self._get(
            f"/cms/v3/blog-settings/settings/{blog_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Blog,
        )

    async def get_revision(
        self,
        revision_id: str,
        *,
        blog_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionBlog:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/cms/v3/blog-settings/settings/{blog_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionBlog,
        )

    def list_revisions(
        self,
        blog_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VersionBlog, AsyncPage[VersionBlog]]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not blog_id:
            raise ValueError(f"Expected a non-empty value for `blog_id` but received {blog_id!r}")
        return self._get_api_list(
            f"/cms/v3/blog-settings/settings/{blog_id}/revisions",
            page=AsyncPage[VersionBlog],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    setting_list_revisions_params.SettingListRevisionsParams,
                ),
            ),
            model=VersionBlog,
        )

    async def set_new_lang_primary(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/cms/v3/blog-settings/settings/multi-language/set-new-lang-primary",
            body=await async_maybe_transform(
                {"id": id}, setting_set_new_lang_primary_params.SettingSetNewLangPrimaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_languages(
        self,
        *,
        languages: Dict[str, str],
        primary_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          languages: Map of object IDs to associated languages of object in the multi-language group.

          primary_id: ID of the primary object in the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/blog-settings/settings/multi-language/update-languages",
            body=await async_maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                setting_update_languages_params.SettingUpdateLanguagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_raw_response_wrapper(
            settings.list,
        )
        self.attach_to_lang_group = to_raw_response_wrapper(
            settings.attach_to_lang_group,
        )
        self.create_language_variation = to_raw_response_wrapper(
            settings.create_language_variation,
        )
        self.detach_from_lang_group = to_raw_response_wrapper(
            settings.detach_from_lang_group,
        )
        self.get = to_raw_response_wrapper(
            settings.get,
        )
        self.get_revision = to_raw_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = to_raw_response_wrapper(
            settings.list_revisions,
        )
        self.set_new_lang_primary = to_raw_response_wrapper(
            settings.set_new_lang_primary,
        )
        self.update_languages = to_raw_response_wrapper(
            settings.update_languages,
        )


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_raw_response_wrapper(
            settings.list,
        )
        self.attach_to_lang_group = async_to_raw_response_wrapper(
            settings.attach_to_lang_group,
        )
        self.create_language_variation = async_to_raw_response_wrapper(
            settings.create_language_variation,
        )
        self.detach_from_lang_group = async_to_raw_response_wrapper(
            settings.detach_from_lang_group,
        )
        self.get = async_to_raw_response_wrapper(
            settings.get,
        )
        self.get_revision = async_to_raw_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            settings.list_revisions,
        )
        self.set_new_lang_primary = async_to_raw_response_wrapper(
            settings.set_new_lang_primary,
        )
        self.update_languages = async_to_raw_response_wrapper(
            settings.update_languages,
        )


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.list = to_streamed_response_wrapper(
            settings.list,
        )
        self.attach_to_lang_group = to_streamed_response_wrapper(
            settings.attach_to_lang_group,
        )
        self.create_language_variation = to_streamed_response_wrapper(
            settings.create_language_variation,
        )
        self.detach_from_lang_group = to_streamed_response_wrapper(
            settings.detach_from_lang_group,
        )
        self.get = to_streamed_response_wrapper(
            settings.get,
        )
        self.get_revision = to_streamed_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = to_streamed_response_wrapper(
            settings.list_revisions,
        )
        self.set_new_lang_primary = to_streamed_response_wrapper(
            settings.set_new_lang_primary,
        )
        self.update_languages = to_streamed_response_wrapper(
            settings.update_languages,
        )


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.list = async_to_streamed_response_wrapper(
            settings.list,
        )
        self.attach_to_lang_group = async_to_streamed_response_wrapper(
            settings.attach_to_lang_group,
        )
        self.create_language_variation = async_to_streamed_response_wrapper(
            settings.create_language_variation,
        )
        self.detach_from_lang_group = async_to_streamed_response_wrapper(
            settings.detach_from_lang_group,
        )
        self.get = async_to_streamed_response_wrapper(
            settings.get,
        )
        self.get_revision = async_to_streamed_response_wrapper(
            settings.get_revision,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            settings.list_revisions,
        )
        self.set_new_lang_primary = async_to_streamed_response_wrapper(
            settings.set_new_lang_primary,
        )
        self.update_languages = async_to_streamed_response_wrapper(
            settings.update_languages,
        )
