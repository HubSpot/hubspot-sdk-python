# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import ObjectTypeEnablementPublicResponse, PortalObjectTypeEnablementPublicResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnablement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        enablement = client.crm.object_library.enablement.list()
        assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.crm.object_library.enablement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enablement = response.parse()
        assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.crm.object_library.enablement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enablement = response.parse()
            assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        enablement = client.crm.object_library.enablement.get(
            "objectTypeId",
        )
        assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.crm.object_library.enablement.with_raw_response.get(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enablement = response.parse()
        assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.crm.object_library.enablement.with_streaming_response.get(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enablement = response.parse()
            assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            client.crm.object_library.enablement.with_raw_response.get(
                "",
            )


class TestAsyncEnablement:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        enablement = await async_client.crm.object_library.enablement.list()
        assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.object_library.enablement.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enablement = await response.parse()
        assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.object_library.enablement.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enablement = await response.parse()
            assert_matches_type(PortalObjectTypeEnablementPublicResponse, enablement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        enablement = await async_client.crm.object_library.enablement.get(
            "objectTypeId",
        )
        assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.crm.object_library.enablement.with_raw_response.get(
            "objectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enablement = await response.parse()
        assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.crm.object_library.enablement.with_streaming_response.get(
            "objectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enablement = await response.parse()
            assert_matches_type(ObjectTypeEnablementPublicResponse, enablement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type_id` but received ''"):
            await async_client.crm.object_library.enablement.with_raw_response.get(
                "",
            )
