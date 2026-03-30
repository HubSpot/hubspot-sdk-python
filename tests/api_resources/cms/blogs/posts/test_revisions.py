# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = client.cms.blogs.posts.revisions.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert revision.is_closed
        assert revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert revision.json() == {"foo": "bar"}
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.revisions.with_streaming_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, StreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_previous_version(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = client.cms.blogs.posts.revisions.get_previous_versions(
            object_id="objectId",
        )
        assert revision.is_closed
        assert revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_versions_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = client.cms.blogs.posts.revisions.get_previous_versions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert revision.is_closed
        assert revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = client.cms.blogs.posts.revisions.with_raw_response.get_previous_versions(
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert revision.json() == {"foo": "bar"}
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.revisions.with_streaming_response.get_previous_versions(
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, StreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_previous_versions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.get_previous_versions(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = client.cms.blogs.posts.revisions.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert revision.is_closed
        assert revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert revision.json() == {"foo": "bar"}
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.revisions.with_streaming_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, StreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_restore_previous_version(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_restore_previous_version_to_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = client.cms.blogs.posts.revisions.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert revision.is_closed
        assert revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_restore_previous_version_to_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert revision.json() == {"foo": "bar"}
        assert isinstance(revision, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_restore_previous_version_to_draft(
        self, client: Hubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.revisions.with_streaming_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, StreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_restore_previous_version_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version_to_draft(
                revision_id=0,
                object_id="",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = await async_client.cms.blogs.posts.revisions.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert revision.is_closed
        assert await revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = await async_client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await revision.json() == {"foo": "bar"}
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.revisions.with_streaming_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_previous_version(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.get_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_versions(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = await async_client.cms.blogs.posts.revisions.get_previous_versions(
            object_id="objectId",
        )
        assert revision.is_closed
        assert await revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_versions_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = await async_client.cms.blogs.posts.revisions.get_previous_versions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert revision.is_closed
        assert await revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_previous_versions(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = await async_client.cms.blogs.posts.revisions.with_raw_response.get_previous_versions(
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await revision.json() == {"foo": "bar"}
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_previous_versions(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.revisions.with_streaming_response.get_previous_versions(
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_previous_versions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.get_previous_versions(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_restore_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = await async_client.cms.blogs.posts.revisions.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert revision.is_closed
        assert await revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_restore_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = await async_client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await revision.json() == {"foo": "bar"}
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_restore_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.revisions.with_streaming_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_restore_previous_version(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        revision = await async_client.cms.blogs.posts.revisions.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert revision.is_closed
        assert await revision.json() == {"foo": "bar"}
        assert cast(Any, revision.is_closed) is True
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        revision = await async_client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert revision.is_closed is True
        assert revision.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await revision.json() == {"foo": "bar"}
        assert isinstance(revision, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.revisions.with_streaming_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as revision:
            assert not revision.is_closed
            assert revision.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await revision.json() == {"foo": "bar"}
            assert cast(Any, revision.is_closed) is True
            assert isinstance(revision, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, revision.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_restore_previous_version_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.revisions.with_raw_response.restore_previous_version_to_draft(
                revision_id=0,
                object_id="",
            )
