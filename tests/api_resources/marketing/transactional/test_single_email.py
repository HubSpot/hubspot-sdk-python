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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: HubSpot) -> None:
        single_email = client.marketing.transactional.single_email.send(
            email_id=0,
            message={"to": "to"},
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: HubSpot) -> None:
        single_email = client.marketing.transactional.single_email.send(
            email_id=0,
            message={
                "to": "to",
                "bcc": ["string"],
                "cc": ["string"],
                "from": "from",
                "reply_to": ["string"],
                "send_id": "sendId",
            },
            contact_properties={
                "0": "{",
                "1": '"',
                "2": "l",
                "3": "a",
                "4": "s",
                "5": "t",
                "6": "n",
                "7": "a",
                "8": "m",
                "9": "e",
                "10": '"',
                "11": ":",
                "12": '"',
                "13": "d",
                "14": "o",
                "15": "e",
                "16": '"',
                "17": ",",
                "18": '"',
                "19": "f",
                "20": "i",
                "21": "r",
                "22": "s",
                "23": "t",
                "24": "n",
                "25": "a",
                "26": "m",
                "27": "e",
                "28": '"',
                "29": ":",
                "30": '"',
                "31": "j",
                "32": "o",
                "33": "h",
                "34": "n",
                "35": '"',
                "36": "}",
            },
            custom_properties={
                "0": {},
                "1": {},
                "2": {},
                "3": {},
                "4": {},
                "5": {},
                "6": {},
                "7": {},
                "8": {},
                "9": {},
                "10": {},
                "11": {},
                "12": {},
                "13": {},
                "14": {},
                "15": {},
                "16": {},
                "17": {},
                "18": {},
                "19": {},
                "20": {},
                "21": {},
                "22": {},
                "23": {},
                "24": {},
                "25": {},
                "26": {},
                "27": {},
                "28": {},
                "29": {},
                "30": {},
                "31": {},
                "32": {},
                "33": {},
                "34": {},
                "35": {},
                "36": {},
                "37": {},
                "38": {},
                "39": {},
                "40": {},
                "41": {},
                "42": {},
                "43": {},
                "44": {},
                "45": {},
                "46": {},
                "47": {},
                "48": {},
                "49": {},
                "50": {},
                "51": {},
                "52": {},
                "53": {},
                "54": {},
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: HubSpot) -> None:
        response = client.marketing.transactional.single_email.with_raw_response.send(
            email_id=0,
            message={"to": "to"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        single_email = response.parse()
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: HubSpot) -> None:
        with client.marketing.transactional.single_email.with_streaming_response.send(
            email_id=0,
            message={"to": "to"},
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncHubSpot) -> None:
        single_email = await async_client.marketing.transactional.single_email.send(
            email_id=0,
            message={"to": "to"},
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncHubSpot) -> None:
        single_email = await async_client.marketing.transactional.single_email.send(
            email_id=0,
            message={
                "to": "to",
                "bcc": ["string"],
                "cc": ["string"],
                "from": "from",
                "reply_to": ["string"],
                "send_id": "sendId",
            },
            contact_properties={
                "0": "{",
                "1": '"',
                "2": "l",
                "3": "a",
                "4": "s",
                "5": "t",
                "6": "n",
                "7": "a",
                "8": "m",
                "9": "e",
                "10": '"',
                "11": ":",
                "12": '"',
                "13": "d",
                "14": "o",
                "15": "e",
                "16": '"',
                "17": ",",
                "18": '"',
                "19": "f",
                "20": "i",
                "21": "r",
                "22": "s",
                "23": "t",
                "24": "n",
                "25": "a",
                "26": "m",
                "27": "e",
                "28": '"',
                "29": ":",
                "30": '"',
                "31": "j",
                "32": "o",
                "33": "h",
                "34": "n",
                "35": '"',
                "36": "}",
            },
            custom_properties={
                "0": {},
                "1": {},
                "2": {},
                "3": {},
                "4": {},
                "5": {},
                "6": {},
                "7": {},
                "8": {},
                "9": {},
                "10": {},
                "11": {},
                "12": {},
                "13": {},
                "14": {},
                "15": {},
                "16": {},
                "17": {},
                "18": {},
                "19": {},
                "20": {},
                "21": {},
                "22": {},
                "23": {},
                "24": {},
                "25": {},
                "26": {},
                "27": {},
                "28": {},
                "29": {},
                "30": {},
                "31": {},
                "32": {},
                "33": {},
                "34": {},
                "35": {},
                "36": {},
                "37": {},
                "38": {},
                "39": {},
                "40": {},
                "41": {},
                "42": {},
                "43": {},
                "44": {},
                "45": {},
                "46": {},
                "47": {},
                "48": {},
                "49": {},
                "50": {},
                "51": {},
                "52": {},
                "53": {},
                "54": {},
            },
        )
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.transactional.single_email.with_raw_response.send(
            email_id=0,
            message={"to": "to"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        single_email = await response.parse()
        assert_matches_type(EmailSendStatusView, single_email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.transactional.single_email.with_streaming_response.send(
            email_id=0,
            message={"to": "to"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            single_email = await response.parse()
            assert_matches_type(EmailSendStatusView, single_email, path=["response"])

        assert cast(Any, response.is_closed) is True
