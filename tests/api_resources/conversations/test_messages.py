# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.conversations import (
    PublicMessage,
    PublicMessageContent,
)
from hubspot_sdk.types.conversations.collection_response_public_message_forward_paging import Result

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Hubspot) -> None:
        message = client.conversations.messages.create(
            0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Hubspot) -> None:
        response = client.conversations.messages.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Hubspot) -> None:
        with client.conversations.messages.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Hubspot) -> None:
        message = client.conversations.messages.create(
            0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Hubspot) -> None:
        response = client.conversations.messages.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Hubspot) -> None:
        with client.conversations.messages.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        message = client.conversations.messages.list(
            thread_id=0,
        )
        assert_matches_type(SyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        message = client.conversations.messages.list(
            thread_id=0,
            after="after",
            archived=True,
            limit=0,
            property="property",
            sort=["string"],
        )
        assert_matches_type(SyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.conversations.messages.with_raw_response.list(
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(SyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.conversations.messages.with_streaming_response.list(
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(SyncPage[Result], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        message = client.conversations.messages.get(
            message_id="messageId",
            thread_id=0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        message = client.conversations.messages.get(
            message_id="messageId",
            thread_id=0,
            property="property",
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.conversations.messages.with_raw_response.get(
            message_id="messageId",
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.conversations.messages.with_streaming_response.get(
            message_id="messageId",
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.conversations.messages.with_raw_response.get(
                message_id="",
                thread_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_original_content(self, client: Hubspot) -> None:
        message = client.conversations.messages.get_original_content(
            message_id="messageId",
            thread_id=0,
        )
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_original_content_with_all_params(self, client: Hubspot) -> None:
        message = client.conversations.messages.get_original_content(
            message_id="messageId",
            thread_id=0,
            property="property",
        )
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_original_content(self, client: Hubspot) -> None:
        response = client.conversations.messages.with_raw_response.get_original_content(
            message_id="messageId",
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_original_content(self, client: Hubspot) -> None:
        with client.conversations.messages.with_streaming_response.get_original_content(
            message_id="messageId",
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicMessageContent, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_original_content(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.conversations.messages.with_raw_response.get_original_content(
                message_id="",
                thread_id=0,
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.create(
            0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.messages.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.messages.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.create(
            0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.messages.with_raw_response.create(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.messages.with_streaming_response.create(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.list(
            thread_id=0,
        )
        assert_matches_type(AsyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.list(
            thread_id=0,
            after="after",
            archived=True,
            limit=0,
            property="property",
            sort=["string"],
        )
        assert_matches_type(AsyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.messages.with_raw_response.list(
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(AsyncPage[Result], message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.messages.with_streaming_response.list(
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(AsyncPage[Result], message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.get(
            message_id="messageId",
            thread_id=0,
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.get(
            message_id="messageId",
            thread_id=0,
            property="property",
        )
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.messages.with_raw_response.get(
            message_id="messageId",
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.messages.with_streaming_response.get(
            message_id="messageId",
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.conversations.messages.with_raw_response.get(
                message_id="",
                thread_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_original_content(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.get_original_content(
            message_id="messageId",
            thread_id=0,
        )
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_original_content_with_all_params(self, async_client: AsyncHubspot) -> None:
        message = await async_client.conversations.messages.get_original_content(
            message_id="messageId",
            thread_id=0,
            property="property",
        )
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_original_content(self, async_client: AsyncHubspot) -> None:
        response = await async_client.conversations.messages.with_raw_response.get_original_content(
            message_id="messageId",
            thread_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicMessageContent, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_original_content(self, async_client: AsyncHubspot) -> None:
        async with async_client.conversations.messages.with_streaming_response.get_original_content(
            message_id="messageId",
            thread_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicMessageContent, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_original_content(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.conversations.messages.with_raw_response.get_original_content(
                message_id="",
                thread_id=0,
            )
