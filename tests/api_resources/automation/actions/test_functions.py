# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.automation import (
    PublicActionFunction,
    PublicActionFunctionIdentifier,
    CollectionResponsePublicActionFunctionIdentifierNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.delete(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.automation.actions.functions.with_raw_response.delete(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_replace(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_or_replace(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_or_replace(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_or_replace(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.create_or_replace(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.automation.actions.functions.with_raw_response.create_or_replace(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_or_replace_by_function_type(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_or_replace_by_function_type(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_or_replace_by_function_type(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_or_replace_by_function_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.create_or_replace_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_by_function_type(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_by_function_type(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_function_type(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_by_function_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.delete_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(PublicActionFunction, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.get(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            client.automation.actions.functions.with_raw_response.get(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_function_type(self, client: HubSpot) -> None:
        function = client.automation.actions.functions.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_function_type(self, client: HubSpot) -> None:
        response = client.automation.actions.functions.with_raw_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_function_type(self, client: HubSpot) -> None:
        with client.automation.actions.functions.with_streaming_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(PublicActionFunction, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_function_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            client.automation.actions.functions.with_raw_response.get_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.list(
            definition_id="definitionId",
            app_id=0,
        )
        assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.list(
            definition_id="definitionId",
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.list(
            definition_id="definitionId",
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(CollectionResponsePublicActionFunctionIdentifierNoPaging, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.list(
                definition_id="",
                app_id=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.delete(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.delete(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.delete(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_replace(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_or_replace(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_or_replace(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.create_or_replace(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_or_replace(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.create_or_replace(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.create_or_replace(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_or_replace_by_function_type(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_or_replace_by_function_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_or_replace_by_function_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.create_or_replace_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
            body="body",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(PublicActionFunctionIdentifier, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_or_replace_by_function_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.create_or_replace_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
                body="body",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_by_function_type(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_function_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_function_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.delete_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_by_function_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.delete_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.get(
            function_id="functionId",
            app_id=0,
            definition_id="definitionId",
            function_type="POST_ACTION_EXECUTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(PublicActionFunction, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.get(
                function_id="functionId",
                app_id=0,
                definition_id="",
                function_type="POST_ACTION_EXECUTION",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.get(
                function_id="",
                app_id=0,
                definition_id="definitionId",
                function_type="POST_ACTION_EXECUTION",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_function_type(self, async_client: AsyncHubSpot) -> None:
        function = await async_client.automation.actions.functions.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_function_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.automation.actions.functions.with_raw_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(PublicActionFunction, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_function_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.automation.actions.functions.with_streaming_response.get_by_function_type(
            function_type="POST_ACTION_EXECUTION",
            app_id=0,
            definition_id="definitionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(PublicActionFunction, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_function_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `definition_id` but received ''"):
            await async_client.automation.actions.functions.with_raw_response.get_by_function_type(
                function_type="POST_ACTION_EXECUTION",
                app_id=0,
                definition_id="",
            )
