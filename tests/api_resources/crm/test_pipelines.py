# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    Pipeline,
    PipelineStage,
    CollectionResponsePipelineNoPaging,
    CollectionResponsePipelineStageNoPaging,
    CollectionResponsePublicAuditInfoNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPipelines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                    "stage_id": "stageId",
                }
            ],
            pipeline_id="pipelineId",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.create(
                object_type="",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update(
            pipeline_id="pipelineId",
            object_type="objectType",
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
            archived=True,
            display_order=0,
            label="label",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.update(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.update(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.list(
            "objectType",
        )
        assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.list(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.list(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.delete(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.delete(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stage(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_stage_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
            stage_id="stageId",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_stage(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_stage(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_stage(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.create_stage(
                pipeline_id="pipelineId",
                object_type="",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.create_stage(
                pipeline_id="",
                object_type="objectType",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_stage(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_stage(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_stage(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_stage(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.get(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.get(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_stage(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_stage(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_stage(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_stage(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.get_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.get_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            client.crm.pipelines.with_raw_response.get_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_audit(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_audit(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_audit(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_audit(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.list_audit(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.list_audit(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_stage_audit(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_stage_audit(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_stage_audit(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_stage_audit(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_stages(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_stages(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_stages(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_stages(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.list_stages(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.list_stages(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_all_properties(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_all_properties_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                    "stage_id": "stageId",
                }
            ],
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_all_properties(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_all_properties(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_all_properties(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.update_all_properties(
                pipeline_id="pipelineId",
                object_type="",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.update_all_properties(
                pipeline_id="",
                object_type="objectType",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_stage(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_stage_with_all_params(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
            archived=True,
            display_order=0,
            label="label",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_stage(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_stage(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_stage(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
                metadata={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_stage_all_properties(self, client: HubSpot) -> None:
        pipeline = client.crm.pipelines.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_stage_all_properties(self, client: HubSpot) -> None:
        response = client.crm.pipelines.with_raw_response.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_stage_all_properties(self, client: HubSpot) -> None:
        with client.crm.pipelines.with_streaming_response.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_stage_all_properties(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )


class TestAsyncPipelines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                    "stage_id": "stageId",
                }
            ],
            pipeline_id="pipelineId",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.create(
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.create(
                object_type="",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update(
            pipeline_id="pipelineId",
            object_type="objectType",
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
            archived=True,
            display_order=0,
            label="label",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.update(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.list(
            "objectType",
        )
        assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.list(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.list(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(CollectionResponsePipelineNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.delete(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.delete(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.delete(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stage(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_stage_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
            stage_id="stageId",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_stage(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_stage(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.create_stage(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_stage(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.create_stage(
                pipeline_id="pipelineId",
                object_type="",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.create_stage(
                pipeline_id="",
                object_type="objectType",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_stage(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_stage(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_stage(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.delete_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_stage(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.delete_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.get(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.get(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.get(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_stage(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_stage(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_stage(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.get_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_stage(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.get_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.get_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.get_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_audit(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_audit(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_audit(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.list_audit(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_audit(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_audit(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_audit(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_stage_audit(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_stage_audit(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_stage_audit(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.list_stage_audit(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(CollectionResponsePublicAuditInfoNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_stage_audit(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_stage_audit(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_stages(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        )
        assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_stages(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_stages(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.list_stages(
            pipeline_id="pipelineId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(CollectionResponsePipelineStageNoPaging, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_stages(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_stages(
                pipeline_id="pipelineId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.list_stages(
                pipeline_id="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_all_properties(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_all_properties_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                    "stage_id": "stageId",
                }
            ],
            validate_deal_stage_usages_before_delete=True,
            validate_references_before_delete=True,
        )
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_all_properties(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_all_properties(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.update_all_properties(
            pipeline_id="pipelineId",
            object_type="objectType",
            display_order=0,
            label="label",
            stages=[
                {
                    "display_order": 0,
                    "label": "label",
                    "metadata": {"foo": "string"},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_all_properties(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_all_properties(
                pipeline_id="pipelineId",
                object_type="",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_all_properties(
                pipeline_id="",
                object_type="objectType",
                display_order=0,
                label="label",
                stages=[
                    {
                        "display_order": 0,
                        "label": "label",
                        "metadata": {"foo": "string"},
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_stage(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_stage_with_all_params(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
            archived=True,
            display_order=0,
            label="label",
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_stage(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_stage(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.update_stage(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_stage(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
                metadata={"foo": "string"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_stage_all_properties(self, async_client: AsyncHubSpot) -> None:
        pipeline = await async_client.crm.pipelines.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_stage_all_properties(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.pipelines.with_raw_response.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineStage, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_stage_all_properties(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.pipelines.with_streaming_response.update_stage_all_properties(
            stage_id="stageId",
            object_type="objectType",
            pipeline_id="pipelineId",
            display_order=0,
            label="label",
            metadata={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineStage, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_stage_all_properties(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="stageId",
                object_type="",
                pipeline_id="pipelineId",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="stageId",
                object_type="objectType",
                pipeline_id="",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stage_id` but received ''"):
            await async_client.crm.pipelines.with_raw_response.update_stage_all_properties(
                stage_id="",
                object_type="objectType",
                pipeline_id="pipelineId",
                display_order=0,
                label="label",
                metadata={"foo": "string"},
            )
