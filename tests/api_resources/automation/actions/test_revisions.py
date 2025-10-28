# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.automation import PublicActionRevision

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        revision = client.automation.actions.revisions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(SyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        revision = client.automation.actions.revisions.list(
            definition_id="definitionId",
            app_id=0,
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.automation.actions.revisions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(SyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.automation.actions.revisions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(SyncPage[PublicActionRevision], revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.revisions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        revision = client.automation.actions.revisions.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionRevision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.automation.actions.revisions.with_raw_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(PublicActionRevision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.automation.actions.revisions.with_streaming_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(PublicActionRevision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.revisions.with_raw_response.get(
                revision_id="revisionId",
                app_id=0,
                definition_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.automation.actions.revisions.with_raw_response.get(
                revision_id="",
                app_id=0,
                definition_id="definitionId",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.automation.actions.revisions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(AsyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.automation.actions.revisions.list(
            definition_id="definitionId",
            app_id=0,
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.revisions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(AsyncPage[PublicActionRevision], revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.revisions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(AsyncPage[PublicActionRevision], revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.revisions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        revision = await async_client.automation.actions.revisions.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionRevision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.revisions.with_raw_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(PublicActionRevision, revision, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.revisions.with_streaming_response.get(
            revision_id="revisionId",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(PublicActionRevision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.revisions.with_raw_response.get(
                revision_id="revisionId",
                app_id=0,
                definition_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.automation.actions.revisions.with_raw_response.get(
                revision_id="",
                app_id=0,
                definition_id="definitionId",
            )
