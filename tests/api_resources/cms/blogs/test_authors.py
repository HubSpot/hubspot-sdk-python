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
    BlogAuthor,
    BatchResponseBlogAuthor,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
            archived=True,
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.update(
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
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
                language="af",
                linkedin="linkedin",
                name="name",
                slug="slug",
                translated_from_id=0,
                twitter="twitter",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                website="website",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.list()
        assert_matches_type(SyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
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
        assert_matches_type(SyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(SyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(SyncPage[BlogAuthor], author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.delete(
            object_id="objectId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.delete(
            object_id="objectId",
            archived=True,
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.authors.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach_to_lang_group(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.create_batch(
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
                    "language": "af",
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
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.create_batch(
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
                    "language": "af",
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.create_batch(
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
                    "language": "af",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation(self, client: Hubspot) -> None:
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation_with_all_params(self, client: Hubspot) -> None:
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
                "language": "af",
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
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_language_variation(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.create_language_variation(
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_language_variation(self, client: Hubspot) -> None:
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.delete_batch(
            inputs=["string"],
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_batch(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_batch(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach_from_lang_group(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.detach_from_lang_group(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach_from_lang_group(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.get(
            object_id="objectId",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.authors.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_with_all_params(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.set_new_lang_primary(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch_with_all_params(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_languages(self, client: Hubspot) -> None:
        author = client.cms.blogs.authors.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_languages(self, client: Hubspot) -> None:
        response = client.cms.blogs.authors.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_languages(self, client: Hubspot) -> None:
        with client.cms.blogs.authors.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.create(
            id="id",
            avatar="avatar",
            bio="bio",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_name="displayName",
            email="email",
            facebook="facebook",
            full_name="fullName",
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
            archived=True,
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.update(
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
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
            language="af",
            linkedin="linkedin",
            name="name",
            slug="slug",
            translated_from_id=0,
            twitter="twitter",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            website="website",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
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
                language="af",
                linkedin="linkedin",
                name="name",
                slug="slug",
                translated_from_id=0,
                twitter="twitter",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                website="website",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.list()
        assert_matches_type(AsyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
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
        assert_matches_type(AsyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(AsyncPage[BlogAuthor], author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(AsyncPage[BlogAuthor], author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.delete(
            object_id="objectId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.delete(
            object_id="objectId",
            archived=True,
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.authors.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group_with_all_params(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.create_batch(
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
                    "language": "af",
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
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.create_batch(
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
                    "language": "af",
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.create_batch(
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
                    "language": "af",
                    "linkedin": "linkedin",
                    "name": "name",
                    "slug": "slug",
                    "translated_from_id": 0,
                    "twitter": "twitter",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "website": "website",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation(self, async_client: AsyncHubspot) -> None:
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation_with_all_params(self, async_client: AsyncHubspot) -> None:
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
                "language": "af",
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
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.create_language_variation(
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
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
                "language": "af",
                "linkedin": "linkedin",
                "name": "name",
                "slug": "slug",
                "translated_from_id": 0,
                "twitter": "twitter",
                "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                "website": "website",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.delete_batch(
            inputs=["string"],
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.detach_from_lang_group(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.get(
            object_id="objectId",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.authors.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.set_new_lang_primary(
            id="id",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert_matches_type(BatchResponseBlogAuthor, author, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_languages(self, async_client: AsyncHubspot) -> None:
        author = await async_client.cms.blogs.authors.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_languages(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.authors.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        author = await response.parse()
        assert author is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_languages(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.authors.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            author = await response.parse()
            assert author is None

        assert cast(Any, response.is_closed) is True
