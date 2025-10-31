# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Hubspot) -> None:
        send = client.events.send.send(
            event_name="pe123456_account_login",
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Hubspot) -> None:
        send = client.events.send.send(
            event_name="pe123456_account_login",
            email="mark.s@lumon.industries",
            object_id="089274502",
            occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            properties={
                "0": "{",
                "1": '"',
                "2": "h",
                "3": "s",
                "4": "_",
                "5": "p",
                "6": "a",
                "7": "g",
                "8": "e",
                "9": "_",
                "10": "i",
                "11": "d",
                "12": '"',
                "13": ":",
                "14": '"',
                "15": "1",
                "16": "2",
                "17": "3",
                "18": "4",
                "19": "5",
                "20": "6",
                "21": "7",
                "22": "8",
                "23": "9",
                "24": "0",
                "25": '"',
                "26": ",",
                "27": '"',
                "28": "h",
                "29": "s",
                "30": "_",
                "31": "e",
                "32": "l",
                "33": "e",
                "34": "m",
                "35": "e",
                "36": "n",
                "37": "t",
                "38": "_",
                "39": "i",
                "40": "d",
                "41": '"',
                "42": ":",
                "43": '"',
                "44": "l",
                "45": "o",
                "46": "g",
                "47": "i",
                "48": "n",
                "49": "-",
                "50": "b",
                "51": "u",
                "52": "t",
                "53": "t",
                "54": "o",
                "55": "n",
                "56": '"',
                "57": ",",
                "58": '"',
                "59": "h",
                "60": "s",
                "61": "_",
                "62": "p",
                "63": "a",
                "64": "g",
                "65": "e",
                "66": "_",
                "67": "t",
                "68": "i",
                "69": "t",
                "70": "l",
                "71": "e",
                "72": '"',
                "73": ":",
                "74": '"',
                "75": "h",
                "76": "o",
                "77": "m",
                "78": "e",
                "79": "p",
                "80": "a",
                "81": "g",
                "82": "e",
                "83": '"',
                "84": "}",
            },
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.send(
            event_name="pe123456_account_login",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.send(
            event_name="pe123456_account_login",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_batch(self, client: Hubspot) -> None:
        send = client.events.send.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_batch(self, client: Hubspot) -> None:
        response = client.events.send.with_raw_response.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_batch(self, client: Hubspot) -> None:
        with client.events.send.with_streaming_response.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send(
            event_name="pe123456_account_login",
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send(
            event_name="pe123456_account_login",
            email="mark.s@lumon.industries",
            object_id="089274502",
            occurred_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            properties={
                "0": "{",
                "1": '"',
                "2": "h",
                "3": "s",
                "4": "_",
                "5": "p",
                "6": "a",
                "7": "g",
                "8": "e",
                "9": "_",
                "10": "i",
                "11": "d",
                "12": '"',
                "13": ":",
                "14": '"',
                "15": "1",
                "16": "2",
                "17": "3",
                "18": "4",
                "19": "5",
                "20": "6",
                "21": "7",
                "22": "8",
                "23": "9",
                "24": "0",
                "25": '"',
                "26": ",",
                "27": '"',
                "28": "h",
                "29": "s",
                "30": "_",
                "31": "e",
                "32": "l",
                "33": "e",
                "34": "m",
                "35": "e",
                "36": "n",
                "37": "t",
                "38": "_",
                "39": "i",
                "40": "d",
                "41": '"',
                "42": ":",
                "43": '"',
                "44": "l",
                "45": "o",
                "46": "g",
                "47": "i",
                "48": "n",
                "49": "-",
                "50": "b",
                "51": "u",
                "52": "t",
                "53": "t",
                "54": "o",
                "55": "n",
                "56": '"',
                "57": ",",
                "58": '"',
                "59": "h",
                "60": "s",
                "61": "_",
                "62": "p",
                "63": "a",
                "64": "g",
                "65": "e",
                "66": "_",
                "67": "t",
                "68": "i",
                "69": "t",
                "70": "l",
                "71": "e",
                "72": '"',
                "73": ":",
                "74": '"',
                "75": "h",
                "76": "o",
                "77": "m",
                "78": "e",
                "79": "p",
                "80": "a",
                "81": "g",
                "82": "e",
                "83": '"',
                "84": "}",
            },
            utk="utk",
            uuid="uuid",
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.send(
            event_name="pe123456_account_login",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.send(
            event_name="pe123456_account_login",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_batch(self, async_client: AsyncHubspot) -> None:
        send = await async_client.events.send.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        )
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.events.send.with_raw_response.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert send is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.events.send.with_streaming_response.send_batch(
            inputs=[{"event_name": "pe123456_account_login"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert send is None

        assert cast(Any, response.is_closed) is True
