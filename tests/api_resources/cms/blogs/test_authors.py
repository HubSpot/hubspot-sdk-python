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


class TestAuthors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = client.cms.blogs.authors.with_raw_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.authors.with_streaming_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
            archived=True,
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.authors.with_raw_response.update(
                object_id="",
                id="id",
                avatar="avatar",
                bio="bio",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                display_name="displayName",
                email="email",
                facebook="facebook",
                full_name="fullName",
                language="aa",
                linkedin="linkedin",
                name="name",
                slug="slug",
                translated_from_id=0,
                twitter="twitter",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                website="website",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.list()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.list(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = client.cms.blogs.authors.with_raw_response.list()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.authors.with_streaming_response.list() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        author = client.cms.blogs.authors.delete(
            object_id="objectId",
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        author = client.cms.blogs.authors.delete(
            object_id="objectId",
            archived=True,
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.blogs.authors.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.blogs.authors.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.authors.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_attach_to_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_language_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.create_language_variation(
            id="id",
            blog_author={
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
            },
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_language_variation_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.create_language_variation(
            id="id",
            blog_author={
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
            },
            language="language",
            primary_language="primaryLanguage",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_language_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.create_language_variation(
            id="id",
            blog_author={
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
            },
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_language_variation(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.create_language_variation(
            id="id",
            blog_author={
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
            },
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.detach_from_lang_group(
            id="id",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_detach_from_lang_group(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get(
            object_id="objectId",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.get(
            object_id="objectId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.get(
            object_id="objectId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.authors.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_cursor()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_cursor_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_cursor(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = client.cms.blogs.authors.with_raw_response.get_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.authors.with_streaming_response.get_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_cursor_by_query()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_cursor_by_query_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_cursor_by_query(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.get_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.get_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_posts_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_posts_cursor()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_posts_cursor_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_posts_cursor(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_posts_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = client.cms.blogs.authors.with_raw_response.get_posts_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_posts_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.authors.with_streaming_response.get_posts_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_posts_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_posts_cursor_by_query()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_posts_cursor_by_query_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_posts_cursor_by_query(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_posts_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.get_posts_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_posts_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.get_posts_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_tags_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_tags_cursor()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_tags_cursor_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = client.cms.blogs.authors.get_tags_cursor(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_tags_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = client.cms.blogs.authors.with_raw_response.get_tags_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_tags_cursor(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.authors.with_streaming_response.get_tags_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_tags_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_tags_cursor_by_query()
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_tags_cursor_by_query_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.get_tags_cursor_by_query(
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
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_tags_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.get_tags_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_tags_cursor_by_query(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.get_tags_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: HubSpot) -> None:
        author = client.cms.blogs.authors.set_new_lang_primary(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: HubSpot) -> None:
        response = client.cms.blogs.authors.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: HubSpot) -> None:
        with client.cms.blogs.authors.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_languages(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = client.cms.blogs.authors.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert author.is_closed
        assert author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_languages(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = client.cms.blogs.authors.with_raw_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert author.json() == {"foo": "bar"}
        assert isinstance(author, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_languages(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.authors.with_streaming_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, StreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True


class TestAsyncAuthors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = await async_client.cms.blogs.authors.with_raw_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.authors.with_streaming_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
            archived=True,
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.update(
            object_id="objectId",
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="aa",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.authors.with_raw_response.update(
                object_id="",
                id="id",
                avatar="avatar",
                bio="bio",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                display_name="displayName",
                email="email",
                facebook="facebook",
                full_name="fullName",
                language="aa",
                linkedin="linkedin",
                name="name",
                slug="slug",
                translated_from_id=0,
                twitter="twitter",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                website="website",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.list()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.list(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = await async_client.cms.blogs.authors.with_raw_response.list()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.authors.with_streaming_response.list() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        author = await async_client.cms.blogs.authors.delete(
            object_id="objectId",
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        author = await async_client.cms.blogs.authors.delete(
            object_id="objectId",
            archived=True,
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.authors.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_attach_to_lang_group(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_language_variation(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.create_language_variation(
            id="id",
            blog_author={
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
            },
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_language_variation_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.create_language_variation(
            id="id",
            blog_author={
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
            },
            language="language",
            primary_language="primaryLanguage",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_language_variation(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.create_language_variation(
            id="id",
            blog_author={
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
            },
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_language_variation(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.create_language_variation(
            id="id",
            blog_author={
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
            },
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.detach_from_lang_group(
            id="id",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_detach_from_lang_group(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_detach_from_lang_group(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get(
            object_id="objectId",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.get(
            object_id="objectId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.get(
            object_id="objectId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.authors.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_cursor()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_cursor_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_cursor(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = await async_client.cms.blogs.authors.with_raw_response.get_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.authors.with_streaming_response.get_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_cursor_by_query(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_cursor_by_query()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_cursor_by_query_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_cursor_by_query(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_cursor_by_query(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.get_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_cursor_by_query(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/authors/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.get_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_posts_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_posts_cursor()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_posts_cursor_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_posts_cursor(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_posts_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = await async_client.cms.blogs.authors.with_raw_response.get_posts_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_posts_cursor(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.authors.with_streaming_response.get_posts_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_posts_cursor_by_query(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_posts_cursor_by_query()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_posts_cursor_by_query_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_posts_cursor_by_query(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_posts_cursor_by_query(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.get_posts_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_posts_cursor_by_query(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.get_posts_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_tags_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_tags_cursor()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_tags_cursor_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        author = await async_client.cms.blogs.authors.get_tags_cursor(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_tags_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        author = await async_client.cms.blogs.authors.with_raw_response.get_tags_cursor()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_tags_cursor(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.authors.with_streaming_response.get_tags_cursor() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_tags_cursor_by_query(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_tags_cursor_by_query()
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_tags_cursor_by_query_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.get_tags_cursor_by_query(
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
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_tags_cursor_by_query(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.get_tags_cursor_by_query()

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_tags_cursor_by_query(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/tags/cursor/query").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.get_tags_cursor_by_query() as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        author = await async_client.cms.blogs.authors.set_new_lang_primary(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_languages(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        author = await async_client.cms.blogs.authors.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert author.is_closed
        assert await author.json() == {"foo": "bar"}
        assert cast(Any, author.is_closed) is True
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_languages(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        author = await async_client.cms.blogs.authors.with_raw_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert author.is_closed is True
        assert author.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await author.json() == {"foo": "bar"}
        assert isinstance(author, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_languages(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/authors/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.authors.with_streaming_response.update_languages(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as author:
            assert not author.is_closed
            assert author.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await author.json() == {"foo": "bar"}
            assert cast(Any, author.is_closed) is True
            assert isinstance(author, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, author.is_closed) is True
