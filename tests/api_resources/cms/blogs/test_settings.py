# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.cms.blogs import (
    Blog,
    VersionBlog,
    CollectionResponseWithTotalVersionBlog,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.list()
        assert_matches_type(SyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SyncPage[Blog], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach_to_lang_group(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.create_language_variation(
            id="id",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation_with_all_params(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
            slug="slug",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_language_variation(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_language_variation(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Blog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach_from_lang_group(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.detach_from_lang_group(
            id="id",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach_from_lang_group(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.get(
            "blogId",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.get(
            "blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.get(
            "blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(Blog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            client.cms.blogs.settings.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        )
        assert_matches_type(VersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(VersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(VersionBlog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            client.cms.blogs.settings.with_raw_response.get_revision(
                revision_id="revisionId",
                blog_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.blogs.settings.with_raw_response.get_revision(
                revision_id="",
                blog_id="blogId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.list_revisions(
            blog_id="blogId",
        )
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.list_revisions(
            blog_id="blogId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.list_revisions(
            blog_id="blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.list_revisions(
            blog_id="blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            client.cms.blogs.settings.with_raw_response.list_revisions(
                blog_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.set_new_lang_primary(
            id="id",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_languages(self, client: Hubspot) -> None:
        setting = client.cms.blogs.settings.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_languages(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_languages(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.list()
        assert_matches_type(AsyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(AsyncPage[Blog], setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(AsyncPage[Blog], setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group_with_all_params(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.create_language_variation(
            id="id",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation_with_all_params(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
            slug="slug",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Blog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.detach_from_lang_group(
            id="id",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.get(
            "blogId",
        )
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.get(
            "blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(Blog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.get(
            "blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(Blog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            await async_client.cms.blogs.settings.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        )
        assert_matches_type(VersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(VersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.get_revision(
            revision_id="revisionId",
            blog_id="blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(VersionBlog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            await async_client.cms.blogs.settings.with_raw_response.get_revision(
                revision_id="revisionId",
                blog_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.blogs.settings.with_raw_response.get_revision(
                revision_id="",
                blog_id="blogId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.list_revisions(
            blog_id="blogId",
        )
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.list_revisions(
            blog_id="blogId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.list_revisions(
            blog_id="blogId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.list_revisions(
            blog_id="blogId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(CollectionResponseWithTotalVersionBlog, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `blog_id` but received ''"):
            await async_client.cms.blogs.settings.with_raw_response.list_revisions(
                blog_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.set_new_lang_primary(
            id="id",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_languages(self, async_client: AsyncHubspot) -> None:
        setting = await async_client.cms.blogs.settings.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_languages(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_languages(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert setting is None

        assert cast(Any, response.is_closed) is True
