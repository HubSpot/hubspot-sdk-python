# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.account import (
    PublicLoginAudit,
    HydratedCriticalAction,
    PublicAPIUserActionEvent,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_audit_logs(self, client: Hubspot) -> None:
        activity = client.account.activity.list_audit_logs()
        assert_matches_type(SyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_audit_logs_with_all_params(self, client: Hubspot) -> None:
        activity = client.account.activity.list_audit_logs(
            acting_user_id=[0],
            after="after",
            fill_final_timestamp=True,
            limit=0,
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
        )
        assert_matches_type(SyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_audit_logs(self, client: Hubspot) -> None:
        response = client.account.activity.with_raw_response.list_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(SyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_audit_logs(self, client: Hubspot) -> None:
        with client.account.activity.with_streaming_response.list_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(SyncPage[PublicAPIUserActionEvent], activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_login_activities(self, client: Hubspot) -> None:
        activity = client.account.activity.list_login_activities()
        assert_matches_type(SyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_login_activities_with_all_params(self, client: Hubspot) -> None:
        activity = client.account.activity.list_login_activities(
            after="after",
            limit=0,
            user_id=0,
        )
        assert_matches_type(SyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_login_activities(self, client: Hubspot) -> None:
        response = client.account.activity.with_raw_response.list_login_activities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(SyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_login_activities(self, client: Hubspot) -> None:
        with client.account.activity.with_streaming_response.list_login_activities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(SyncPage[PublicLoginAudit], activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_security_activities(self, client: Hubspot) -> None:
        activity = client.account.activity.list_security_activities()
        assert_matches_type(SyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_security_activities_with_all_params(self, client: Hubspot) -> None:
        activity = client.account.activity.list_security_activities(
            after="after",
            from_timestamp=0,
            limit=0,
            to_timestamp=0,
            user_id=0,
        )
        assert_matches_type(SyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_security_activities(self, client: Hubspot) -> None:
        response = client.account.activity.with_raw_response.list_security_activities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = response.parse()
        assert_matches_type(SyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_security_activities(self, client: Hubspot) -> None:
        with client.account.activity.with_streaming_response.list_security_activities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = response.parse()
            assert_matches_type(SyncPage[HydratedCriticalAction], activity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncActivity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_audit_logs(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_audit_logs()
        assert_matches_type(AsyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_audit_logs_with_all_params(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_audit_logs(
            acting_user_id=[0],
            after="after",
            fill_final_timestamp=True,
            limit=0,
            occurred_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            occurred_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
        )
        assert_matches_type(AsyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_audit_logs(self, async_client: AsyncHubspot) -> None:
        response = await async_client.account.activity.with_raw_response.list_audit_logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(AsyncPage[PublicAPIUserActionEvent], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_audit_logs(self, async_client: AsyncHubspot) -> None:
        async with async_client.account.activity.with_streaming_response.list_audit_logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(AsyncPage[PublicAPIUserActionEvent], activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_login_activities(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_login_activities()
        assert_matches_type(AsyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_login_activities_with_all_params(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_login_activities(
            after="after",
            limit=0,
            user_id=0,
        )
        assert_matches_type(AsyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_login_activities(self, async_client: AsyncHubspot) -> None:
        response = await async_client.account.activity.with_raw_response.list_login_activities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(AsyncPage[PublicLoginAudit], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_login_activities(self, async_client: AsyncHubspot) -> None:
        async with async_client.account.activity.with_streaming_response.list_login_activities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(AsyncPage[PublicLoginAudit], activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_security_activities(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_security_activities()
        assert_matches_type(AsyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_security_activities_with_all_params(self, async_client: AsyncHubspot) -> None:
        activity = await async_client.account.activity.list_security_activities(
            after="after",
            from_timestamp=0,
            limit=0,
            to_timestamp=0,
            user_id=0,
        )
        assert_matches_type(AsyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_security_activities(self, async_client: AsyncHubspot) -> None:
        response = await async_client.account.activity.with_raw_response.list_security_activities()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        activity = await response.parse()
        assert_matches_type(AsyncPage[HydratedCriticalAction], activity, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_security_activities(self, async_client: AsyncHubspot) -> None:
        async with async_client.account.activity.with_streaming_response.list_security_activities() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            activity = await response.parse()
            assert_matches_type(AsyncPage[HydratedCriticalAction], activity, path=["response"])

        assert cast(Any, response.is_closed) is True
