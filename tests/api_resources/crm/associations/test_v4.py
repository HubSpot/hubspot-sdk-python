# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import SimplePublicObject

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV4:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge(self, client: Hubspot) -> None:
        v4 = client.crm.associations.v4.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: Hubspot) -> None:
        response = client.crm.associations.v4.with_raw_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = response.parse()
        assert_matches_type(SimplePublicObject, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: Hubspot) -> None:
        with client.crm.associations.v4.with_streaming_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = response.parse()
            assert_matches_type(SimplePublicObject, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_merge(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.associations.v4.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )


class TestAsyncV4:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHubspot) -> None:
        v4 = await async_client.crm.associations.v4.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.associations.v4.with_raw_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v4 = await response.parse()
        assert_matches_type(SimplePublicObject, v4, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.associations.v4.with_streaming_response.merge(
            object_type="objectType",
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v4 = await response.parse()
            assert_matches_type(SimplePublicObject, v4, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_merge(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.associations.v4.with_raw_response.merge(
                object_type="",
                object_id_to_merge="objectIdToMerge",
                primary_object_id="primaryObjectId",
            )
