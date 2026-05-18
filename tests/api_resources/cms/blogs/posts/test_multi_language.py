# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMultiLanguage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.attach_to_lang_group(
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
    def test_method_attach_to_lang_group_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.attach_to_lang_group(
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
    def test_raw_response_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.posts.multi_language.with_raw_response.attach_to_lang_group(
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
    def test_streaming_response_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.multi_language.with_streaming_response.attach_to_lang_group(
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.create_lang_variation(
            id="id",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.create_lang_variation(
            id="id",
            language="language",
            use_published=True,
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_lang_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.posts.multi_language.with_raw_response.create_lang_variation(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_lang_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.multi_language.with_streaming_response.create_lang_variation(
            id="id",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, StreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.detach_from_lang_group(
            id="id",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.posts.multi_language.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.multi_language.with_streaming_response.detach_from_lang_group(
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
    def test_method_set_lang_primary(self, client: HubSpot) -> None:
        multi_language = client.cms.blogs.posts.multi_language.set_lang_primary(
            id="id",
        )
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_lang_primary(self, client: HubSpot) -> None:
        response = client.cms.blogs.posts.multi_language.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = response.parse()
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_lang_primary(self, client: HubSpot) -> None:
        with client.cms.blogs.posts.multi_language.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = response.parse()
            assert multi_language is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_langs(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = client.cms.blogs.posts.multi_language.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_langs(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = client.cms.blogs.posts.multi_language.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_langs(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.multi_language.with_streaming_response.update_langs(
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
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.attach_to_lang_group(
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
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.attach_to_lang_group(
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
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.posts.multi_language.with_raw_response.attach_to_lang_group(
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
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.multi_language.with_streaming_response.attach_to_lang_group(
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.create_lang_variation(
            id="id",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.create_lang_variation(
            id="id",
            language="language",
            use_published=True,
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_lang_variation(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.posts.multi_language.with_raw_response.create_lang_variation(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_lang_variation(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.multi_language.with_streaming_response.create_lang_variation(
            id="id",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.detach_from_lang_group(
            id="id",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_detach_from_lang_group(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.posts.multi_language.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_detach_from_lang_group(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.multi_language.with_streaming_response.detach_from_lang_group(
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
    async def test_method_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        multi_language = await async_client.cms.blogs.posts.multi_language.set_lang_primary(
            id="id",
        )
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.posts.multi_language.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        multi_language = await response.parse()
        assert multi_language is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.posts.multi_language.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            multi_language = await response.parse()
            assert multi_language is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_langs(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        multi_language = await async_client.cms.blogs.posts.multi_language.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert multi_language.is_closed
        assert await multi_language.json() == {"foo": "bar"}
        assert cast(Any, multi_language.is_closed) is True
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_langs(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        multi_language = await async_client.cms.blogs.posts.multi_language.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert multi_language.is_closed is True
        assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await multi_language.json() == {"foo": "bar"}
        assert isinstance(multi_language, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_langs(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.multi_language.with_streaming_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as multi_language:
            assert not multi_language.is_closed
            assert multi_language.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await multi_language.json() == {"foo": "bar"}
            assert cast(Any, multi_language.is_closed) is True
            assert isinstance(multi_language, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, multi_language.is_closed) is True
