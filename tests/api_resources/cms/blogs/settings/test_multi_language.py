# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.cms.blogs import Blog

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultiLanguage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.settings.multi_language.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.settings.multi_language.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.settings.multi_language.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.settings.multi_language.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, StreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_language_variation(self, client: Hubspot) -> None:
        multi_language = client.cms.blogs.settings.multi_language.create_language_variation(
            id="id",
        )
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_language_variation_with_all_params(self, client: Hubspot) -> None:
        multi_language = client.cms.blogs.settings.multi_language.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
            slug="slug",
        )
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_language_variation(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.multi_language.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = response.parse()
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_language_variation(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.multi_language.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = response.parse()
            assert_matches_type(Blog, multi_language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.settings.multi_language.detach_from_lang_group(
            id="id",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.settings.multi_language.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.settings.multi_language.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, StreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: Hubspot) -> None:
        multi_language = client.cms.blogs.settings.multi_language.set_new_lang_primary(
            id="id",
        )
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.blogs.settings.multi_language.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = response.parse()
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: Hubspot) -> None:
        with client.cms.blogs.settings.multi_language.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = response.parse()
            assert multi_language is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_languages(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.settings.multi_language.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_languages(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.settings.multi_language.with_raw_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_languages(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.settings.multi_language.with_streaming_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, StreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True


class TestAsyncMultiLanguage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.settings.multi_language.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.settings.multi_language.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.settings.multi_language.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_attach_to_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.settings.multi_language.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_language_variation(self, async_client: AsyncHubspot) -> None:
        multi_language = await async_client.cms.blogs.settings.multi_language.create_language_variation(
            id="id",
        )
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_language_variation_with_all_params(self, async_client: AsyncHubspot) -> None:
        multi_language = await async_client.cms.blogs.settings.multi_language.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
            slug="slug",
        )
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.multi_language.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = await response.parse()
        assert_matches_type(Blog, multi_language, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.multi_language.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = await response.parse()
            assert_matches_type(Blog, multi_language, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.settings.multi_language.detach_from_lang_group(
            id="id",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.settings.multi_language.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.settings.multi_language.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        multi_language = await async_client.cms.blogs.settings.multi_language.set_new_lang_primary(
            id="id",
        )
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.settings.multi_language.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = await response.parse()
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.settings.multi_language.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = await response.parse()
            assert multi_language is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_languages(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.settings.multi_language.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_languages(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.settings.multi_language.with_raw_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_languages(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blog-settings/2026-03/settings/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.settings.multi_language.with_streaming_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True
