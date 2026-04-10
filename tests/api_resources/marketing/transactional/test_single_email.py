# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import EmailSendStatusView

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSingleEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: HubSpot) -> None:
        single_email = client.marketing.transactional.single_email.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: HubSpot) -> None:
        single_email = client.marketing.transactional.single_email.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
                "from": "from",
                "send_id": "sendId",
                "to": "to",
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: HubSpot) -> None:
        response = client.marketing.transactional.single_email.with_raw_response.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        single_email = response.parse()
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: HubSpot) -> None:
        with client.marketing.transactional.single_email.with_streaming_response.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            single_email = response.parse()
            assert_matches_type(EmailSendStatusView, single_email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSingleEmail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncHubSpot) -> None:
        single_email = await async_client.marketing.transactional.single_email.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncHubSpot) -> None:
        single_email = await async_client.marketing.transactional.single_email.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
                "from": "from",
                "send_id": "sendId",
                "to": "to",
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.single_email.with_raw_response.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        single_email = await response.parse()
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.single_email.with_streaming_response.send(
            contact_properties={"foo": "string"},
            custom_properties={"foo": {}},
            email_id=0,
            message={
                "bcc": ["string"],
                "cc": ["string"],
                "reply_to": ["string"],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            single_email = await response.parse()
            assert_matches_type(EmailSendStatusView, single_email, path=["response"])

        assert cast(Any, response.is_closed) is True
