# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.update(
                object_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                language="aa",
                name="name",
                slug="slug",
                translated_from_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.list()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.list() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        tag = client.cms.blogs.tags.delete(
            object_id="objectId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        tag = client.cms.blogs.tags.delete(
            object_id="objectId",
            archived=True,
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.blogs.tags.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.blogs.tags.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
            language="language",
            primary_language="primaryLanguage",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.create_lang_variation(
            id="id",
            name="name",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.create_lang_variation(
            id="id",
            name="name",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.detach_from_lang_group(
            id="id",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.get(
            object_id="objectId",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.get(
            object_id="objectId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.get(
            object_id="objectId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_authors_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_authors_cursor()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_authors_cursor_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_authors_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_authors_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.list_authors_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_authors_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.list_authors_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_authors_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_authors_cursor_by_query()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_authors_cursor_by_query_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_authors_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_authors_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.list_authors_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_authors_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.list_authors_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_cursor()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_cursor_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.list_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.list_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_cursor_by_query()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_cursor_by_query_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.list_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.list_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_posts_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_posts_cursor()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_posts_cursor_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = client.cms.blogs.tags.list_posts_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_posts_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = client.cms.blogs.tags.with_raw_response.list_posts_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_posts_cursor(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.tags.with_streaming_response.list_posts_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_posts_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_posts_cursor_by_query()
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_posts_cursor_by_query_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.list_posts_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_posts_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.list_posts_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_posts_cursor_by_query(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.list_posts_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_lang_primary(self, client: Hubspot) -> None:
        tag = client.cms.blogs.tags.set_lang_primary(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.blogs.tags.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_lang_primary(self, client: Hubspot) -> None:
        with client.cms.blogs.tags.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = client.cms.blogs.tags.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert tag.is_closed
        assert tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = client.cms.blogs.tags.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert tag.json() == {"foo": "bar"}
        assert isinstance(tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.tags.with_streaming_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, StreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="aa",
            name="name",
            slug="slug",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.update(
                object_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                language="aa",
                name="name",
                slug="slug",
                translated_from_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.list()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.list() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        tag = await async_client.cms.blogs.tags.delete(
            object_id="objectId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        tag = await async_client.cms.blogs.tags.delete(
            object_id="objectId",
            archived=True,
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_attach_to_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
            language="language",
            primary_language="primaryLanguage",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_lang_variation(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.create_lang_variation(
            id="id",
            name="name",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_lang_variation(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.create_lang_variation(
            id="id",
            name="name",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.detach_from_lang_group(
            id="id",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.get(
            object_id="objectId",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.get(
            object_id="objectId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.get(
            object_id="objectId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_authors_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_authors_cursor()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_authors_cursor_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_authors_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_authors_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.list_authors_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_authors_cursor(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.list_authors_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_authors_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_authors_cursor_by_query()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_authors_cursor_by_query_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_authors_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_authors_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.list_authors_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_authors_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.list_authors_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_cursor()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_cursor_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.list_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.list_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_cursor_by_query(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_cursor_by_query()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_cursor_by_query_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_cursor_by_query(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.list_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.list_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_posts_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_posts_cursor()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_posts_cursor_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        tag = await async_client.cms.blogs.tags.list_posts_cursor(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_posts_cursor(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        tag = await async_client.cms.blogs.tags.with_raw_response.list_posts_cursor()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_posts_cursor(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.tags.with_streaming_response.list_posts_cursor() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_posts_cursor_by_query(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_posts_cursor_by_query()
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_posts_cursor_by_query_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.list_posts_cursor_by_query(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_posts_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.list_posts_cursor_by_query()

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_posts_cursor_by_query(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.list_posts_cursor_by_query() as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        tag = await async_client.cms.blogs.tags.set_lang_primary(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        tag = await async_client.cms.blogs.tags.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert tag.is_closed
        assert await tag.json() == {"foo": "bar"}
        assert cast(Any, tag.is_closed) is True
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        tag = await async_client.cms.blogs.tags.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert tag.is_closed is True
        assert tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await tag.json() == {"foo": "bar"}
        assert isinstance(tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/tags/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.tags.with_streaming_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as tag:
            assert not tag.is_closed
            assert tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await tag.json() == {"foo": "bar"}
            assert cast(Any, tag.is_closed) is True
            assert isinstance(tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, tag.is_closed) is True
