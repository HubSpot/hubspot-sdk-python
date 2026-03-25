# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import SimplePublicObjectWithAssociations, CollectionResponseWithTotalSimplePublicObject
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedbackSubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.list()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.objects.feedback_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.objects.feedback_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.get(
            feedback_submission_id="feedbackSubmissionId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.get(
            feedback_submission_id="feedbackSubmissionId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.objects.feedback_submissions.with_raw_response.get(
            feedback_submission_id="feedbackSubmissionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.objects.feedback_submissions.with_streaming_response.get(
            feedback_submission_id="feedbackSubmissionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `feedback_submission_id` but received ''"
        ):
            client.crm.objects.feedback_submissions.with_raw_response.get(
                feedback_submission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Hubspot) -> None:
        feedback_submission = client.crm.objects.feedback_submissions.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
            query="query",
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Hubspot) -> None:
        response = client.crm.objects.feedback_submissions.with_raw_response.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Hubspot) -> None:
        with client.crm.objects.feedback_submissions.with_streaming_response.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedbackSubmissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.list()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.feedback_submissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.feedback_submissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.get(
            feedback_submission_id="feedbackSubmissionId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.get(
            feedback_submission_id="feedbackSubmissionId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.feedback_submissions.with_raw_response.get(
            feedback_submission_id="feedbackSubmissionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.feedback_submissions.with_streaming_response.get(
            feedback_submission_id="feedbackSubmissionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `feedback_submission_id` but received ''"
        ):
            await async_client.crm.objects.feedback_submissions.with_raw_response.get(
                feedback_submission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubspot) -> None:
        feedback_submission = await async_client.crm.objects.feedback_submissions.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
            query="query",
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.objects.feedback_submissions.with_raw_response.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback_submission = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.objects.feedback_submissions.with_streaming_response.search(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "BETWEEN",
                            "property_name": "propertyName",
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            sorts=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback_submission = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, feedback_submission, path=["response"])

        assert cast(Any, response.is_closed) is True
