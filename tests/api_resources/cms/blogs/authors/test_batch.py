# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.authors.batch.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.authors.batch.with_raw_response.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.batch.with_streaming_response.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.authors.batch.update(
            inputs=[{}],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.authors.batch.update(
            inputs=[{}],
            archived=True,
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.authors.batch.with_raw_response.update(
            inputs=[{}],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.batch.with_streaming_response.update(
            inputs=[{}],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        batch = client.cms.blogs.authors.batch.delete(
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.blogs.authors.batch.with_raw_response.delete(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.blogs.authors.batch.with_streaming_response.delete(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.authors.batch.get(
            inputs=["string"],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.authors.batch.get(
            inputs=["string"],
            archived=True,
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.authors.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.batch.with_streaming_response.get(
            inputs=["string"],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.authors.batch.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.authors.batch.with_raw_response.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.batch.with_streaming_response.create(
            inputs=[
                {
                    "id": "id",
                    "avatar": "avatar",
                    "bio": "bio",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "display_name": "displayName",
                    "email": "email",
                    "facebook": "facebook",
                    "full_name": "fullName",
                    "language": "aa",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.authors.batch.update(
            inputs=[{}],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.authors.batch.update(
            inputs=[{}],
            archived=True,
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.authors.batch.with_raw_response.update(
            inputs=[{}],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.batch.with_streaming_response.update(
            inputs=[{}],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.cms.blogs.authors.batch.delete(
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.authors.batch.with_raw_response.delete(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.authors.batch.with_streaming_response.delete(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.authors.batch.get(
            inputs=["string"],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.authors.batch.get(
            inputs=["string"],
            archived=True,
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.authors.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.batch.with_streaming_response.get(
            inputs=["string"],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True
