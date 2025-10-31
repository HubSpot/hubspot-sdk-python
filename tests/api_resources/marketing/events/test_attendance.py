# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import BatchResponseSubscriberVidResponse, BatchResponseSubscriberEmailResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttendance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_event_id_and_contact_id(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_by_event_id_and_contact_id(self, client: Hubspot) -> None:
        response = client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_by_event_id_and_contact_id(self, client: Hubspot) -> None:
        with client.marketing.events.attendance.with_streaming_response.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_by_event_id_and_contact_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
                subscriber_state="subscriberState",
                object_id="",
                inputs=[{"interaction_date_time": 0}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
                subscriber_state="",
                object_id="objectId",
                inputs=[{"interaction_date_time": 0}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_event_id_and_email(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_by_event_id_and_email(self, client: Hubspot) -> None:
        response = client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_by_event_id_and_email(self, client: Hubspot) -> None:
        with client.marketing.events.attendance.with_streaming_response.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_by_event_id_and_email(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
                subscriber_state="subscriberState",
                object_id="",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
                subscriber_state="",
                object_id="objectId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_external_event_id_and_contact_id(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[{"interaction_date_time": 0}],
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_external_event_id_and_contact_id_with_all_params(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
            external_account_id="externalAccountId",
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_by_external_event_id_and_contact_id(self, client: Hubspot) -> None:
        response = client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[{"interaction_date_time": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_by_external_event_id_and_contact_id(self, client: Hubspot) -> None:
        with client.marketing.events.attendance.with_streaming_response.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[{"interaction_date_time": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_by_external_event_id_and_contact_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
                subscriber_state="subscriberState",
                external_event_id="",
                inputs=[{"interaction_date_time": 0}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
                subscriber_state="",
                external_event_id="externalEventId",
                inputs=[{"interaction_date_time": 0}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_external_event_id_and_email(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_external_event_id_and_email_with_all_params(self, client: Hubspot) -> None:
        attendance = client.marketing.events.attendance.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                    "contact_properties": {"foo": "string"},
                    "properties": {"foo": "string"},
                }
            ],
            external_account_id="externalAccountId",
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_by_external_event_id_and_email(self, client: Hubspot) -> None:
        response = client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_by_external_event_id_and_email(self, client: Hubspot) -> None:
        with client.marketing.events.attendance.with_streaming_response.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_by_external_event_id_and_email(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
                subscriber_state="subscriberState",
                external_event_id="",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
                subscriber_state="",
                external_event_id="externalEventId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )


class TestAsyncAttendance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_by_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.attendance.with_streaming_response.create_by_event_id_and_contact_id(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[{"interaction_date_time": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_by_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
                subscriber_state="subscriberState",
                object_id="",
                inputs=[{"interaction_date_time": 0}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_contact_id(
                subscriber_state="",
                object_id="objectId",
                inputs=[{"interaction_date_time": 0}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_by_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.attendance.with_streaming_response.create_by_event_id_and_email(
            subscriber_state="subscriberState",
            object_id="objectId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_by_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
                subscriber_state="subscriberState",
                object_id="",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_event_id_and_email(
                subscriber_state="",
                object_id="objectId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_external_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[{"interaction_date_time": 0}],
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_external_event_id_and_contact_id_with_all_params(
        self, async_client: AsyncHubspot
    ) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_external_event_id_and_contact_id(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "interaction_date_time": 0,
                    "properties": {"foo": "string"},
                    "vid": 0,
                }
            ],
            external_account_id="externalAccountId",
        )
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_by_external_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        response = (
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                inputs=[{"interaction_date_time": 0}],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_external_event_id_and_contact_id(
        self, async_client: AsyncHubspot
    ) -> None:
        async with (
            async_client.marketing.events.attendance.with_streaming_response.create_by_external_event_id_and_contact_id(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                inputs=[{"interaction_date_time": 0}],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(BatchResponseSubscriberVidResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_by_external_event_id_and_contact_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
                subscriber_state="subscriberState",
                external_event_id="",
                inputs=[{"interaction_date_time": 0}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_contact_id(
                subscriber_state="",
                external_event_id="externalEventId",
                inputs=[{"interaction_date_time": 0}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_external_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_external_event_id_and_email_with_all_params(
        self, async_client: AsyncHubspot
    ) -> None:
        attendance = await async_client.marketing.events.attendance.create_by_external_event_id_and_email(
            subscriber_state="subscriberState",
            external_event_id="externalEventId",
            inputs=[
                {
                    "email": "email",
                    "interaction_date_time": 0,
                    "contact_properties": {"foo": "string"},
                    "properties": {"foo": "string"},
                }
            ],
            external_account_id="externalAccountId",
        )
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_by_external_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        response = (
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_external_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        async with (
            async_client.marketing.events.attendance.with_streaming_response.create_by_external_event_id_and_email(
                subscriber_state="subscriberState",
                external_event_id="externalEventId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(BatchResponseSubscriberEmailResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_by_external_event_id_and_email(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
                subscriber_state="subscriberState",
                external_event_id="",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_state` but received ''"):
            await async_client.marketing.events.attendance.with_raw_response.create_by_external_event_id_and_email(
                subscriber_state="",
                external_event_id="externalEventId",
                inputs=[
                    {
                        "email": "email",
                        "interaction_date_time": 0,
                    }
                ],
            )
