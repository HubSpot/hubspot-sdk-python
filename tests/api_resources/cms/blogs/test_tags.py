# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.cms.blogs import (
    Tag,
    BatchResponseTag,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.update(
                object_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                language="af",
                name="name",
                translated_from_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.list()
        assert_matches_type(SyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
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
        assert_matches_type(SyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(SyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(SyncPage[Tag], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.delete(
            object_id="objectId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.delete(
            object_id="objectId",
            archived=True,
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_batch(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.archive_batch(
            inputs=["string"],
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_batch(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.archive_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_batch(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.archive_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach_to_lang_group(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach_to_lang_group(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_lang_variation(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_lang_variation_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_lang_variation(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.create_lang_variation(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_lang_variation(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.create_lang_variation(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach_from_lang_group(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.detach_from_lang_group(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach_from_lang_group(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach_from_lang_group(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.read(
            object_id="objectId",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.read(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.read(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.read(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.tags.with_raw_response.read(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_batch(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.read_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_batch_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.read_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read_batch(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.read_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read_batch(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.read_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_lang_primary(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.set_lang_primary(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_lang_primary(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_lang_primary(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch_with_all_params(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_langs(self, client: HubSpot) -> None:
        tag = client.cms.blogs.tags.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_langs(self, client: HubSpot) -> None:
        response = client.cms.blogs.tags.with_raw_response.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_langs(self, client: HubSpot) -> None:
        with client.cms.blogs.tags.with_streaming_response.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.create(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.update(
            object_id="objectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            language="af",
            name="name",
            translated_from_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.update(
                object_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                language="af",
                name="name",
                translated_from_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.list()
        assert_matches_type(AsyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
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
        assert_matches_type(AsyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(AsyncPage[Tag], tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(AsyncPage[Tag], tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.delete(
            object_id="objectId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.delete(
            object_id="objectId",
            archived=True,
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_batch(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.archive_batch(
            inputs=["string"],
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.archive_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.archive_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "language": "af",
                    "name": "name",
                    "translated_from_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_lang_variation(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_lang_variation_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.create_lang_variation(
            id="id",
            name="name",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_lang_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.create_lang_variation(
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_lang_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.create_lang_variation(
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.detach_from_lang_group(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.read(
            object_id="objectId",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.read(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.read(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(Tag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.read(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(Tag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.tags.with_raw_response.read(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_batch(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.read_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.read_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.read_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.read_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.set_lang_primary(
            id="id",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_lang_primary(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(BatchResponseTag, tag, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(BatchResponseTag, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_langs(self, async_client: AsyncHubSpot) -> None:
        tag = await async_client.cms.blogs.tags.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_langs(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.tags.with_raw_response.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert tag is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_langs(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.tags.with_streaming_response.update_langs(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert tag is None

        assert cast(Any, response.is_closed) is True
