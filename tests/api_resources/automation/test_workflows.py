# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.automation import (
    APIFlow,
    APIFlowListing,
    BatchResponseAPIFlow,
    CollectionResponseAPIFlowEmailCampaign,
    BatchResponseFlowIDWorkflowIDMappingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.create()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.create()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.update(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.update(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.update(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.automation.workflows.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.update(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.update(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.update(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.automation.workflows.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.list()
        assert_matches_type(SyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.list(
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(SyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(SyncPage[APIFlowListing], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.delete(
            0,
        )
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        )
        assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_get(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_get(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get_id_mappings(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        )
        assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_get_id_mappings(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_get_id_mappings(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.get(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.get(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.get(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            client.automation.workflows.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_email_campaigns(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.list_email_campaigns()
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_email_campaigns_with_all_params(self, client: Hubspot) -> None:
        workflow = client.automation.workflows.list_email_campaigns(
            after="after",
            before="before",
            flow_id=["string"],
            limit=0,
        )
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_email_campaigns(self, client: Hubspot) -> None:
        response = client.automation.workflows.with_raw_response.list_email_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_email_campaigns(self, client: Hubspot) -> None:
        with client.automation.workflows.with_streaming_response.list_email_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.create()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.create()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.update(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.update(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.update(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.automation.workflows.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.update(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.update(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.update(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.automation.workflows.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.list()
        assert_matches_type(AsyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.list(
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(AsyncPage[APIFlowListing], workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(AsyncPage[APIFlowListing], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.delete(
            0,
        )
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        )
        assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.batch_get(
            inputs=[
                {
                    "flow_id": "flowId",
                    "type": "FLOW_ID",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(BatchResponseAPIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get_id_mappings(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        )
        assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_get_id_mappings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get_id_mappings(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.batch_get_id_mappings(
            inputs=[
                {
                    "flow_migration_statuses": "12345",
                    "type": "FLOW_ID",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(BatchResponseFlowIDWorkflowIDMappingResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.get(
            "flowId",
        )
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.get(
            "flowId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(APIFlow, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.get(
            "flowId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(APIFlow, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `flow_id` but received ''"):
            await async_client.automation.workflows.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_email_campaigns(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.list_email_campaigns()
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_email_campaigns_with_all_params(self, async_client: AsyncHubspot) -> None:
        workflow = await async_client.automation.workflows.list_email_campaigns(
            after="after",
            before="before",
            flow_id=["string"],
            limit=0,
        )
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_email_campaigns(self, async_client: AsyncHubspot) -> None:
        response = await async_client.automation.workflows.with_raw_response.list_email_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_email_campaigns(self, async_client: AsyncHubspot) -> None:
        async with async_client.automation.workflows.with_streaming_response.list_email_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(CollectionResponseAPIFlowEmailCampaign, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True
