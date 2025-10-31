# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing import CollectionResponseWithTotalPublicListNoPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.list(
            "marketingEventId",
        )
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.list(
            "marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.list(
            "marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.delete(
                list_id="listId",
                marketing_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.marketing.events.associations.with_raw_response.delete(
                list_id="",
                marketing_event_id="marketingEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_associate(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_associate(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_associate(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_associate(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.associate(
                list_id="listId",
                marketing_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.marketing.events.associations.with_raw_response.associate(
                list_id="",
                marketing_event_id="marketingEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_associate_by_external_account(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_associate_by_external_account(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_associate_by_external_account(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_associate_by_external_account(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="listId",
                external_account_id="",
                external_event_id="externalEventId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="listId",
                external_account_id="externalAccountId",
                external_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="",
                external_account_id="externalAccountId",
                external_event_id="externalEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_external_account(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_external_account(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_external_account(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_by_external_account(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="listId",
                external_account_id="",
                external_event_id="externalEventId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="listId",
                external_account_id="externalAccountId",
                external_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="",
                external_account_id="externalAccountId",
                external_event_id="externalEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_by_external_account(self, client: Hubspot) -> None:
        association = client.marketing.events.associations.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_by_external_account(self, client: Hubspot) -> None:
        response = client.marketing.events.associations.with_raw_response.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_by_external_account(self, client: Hubspot) -> None:
        with client.marketing.events.associations.with_streaming_response.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_by_external_account(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            client.marketing.events.associations.with_raw_response.list_by_external_account(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            client.marketing.events.associations.with_raw_response.list_by_external_account(
                external_event_id="",
                external_account_id="externalAccountId",
            )


class TestAsyncAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.list(
            "marketingEventId",
        )
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.list(
            "marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.list(
            "marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.delete(
            list_id="listId",
            marketing_event_id="marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.delete(
                list_id="listId",
                marketing_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.delete(
                list_id="",
                marketing_event_id="marketingEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_associate(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_associate(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_associate(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.associate(
            list_id="listId",
            marketing_event_id="marketingEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_associate(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `marketing_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.associate(
                list_id="listId",
                marketing_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.associate(
                list_id="",
                marketing_event_id="marketingEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_associate_by_external_account(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_associate_by_external_account(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_associate_by_external_account(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.associate_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_associate_by_external_account(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="listId",
                external_account_id="",
                external_event_id="externalEventId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="listId",
                external_account_id="externalAccountId",
                external_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.associate_by_external_account(
                list_id="",
                external_account_id="externalAccountId",
                external_event_id="externalEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_external_account(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_external_account(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_external_account(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.delete_by_external_account(
            list_id="listId",
            external_account_id="externalAccountId",
            external_event_id="externalEventId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_by_external_account(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="listId",
                external_account_id="",
                external_event_id="externalEventId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="listId",
                external_account_id="externalAccountId",
                external_event_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.delete_by_external_account(
                list_id="",
                external_account_id="externalAccountId",
                external_event_id="externalEventId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_by_external_account(self, async_client: AsyncHubspot) -> None:
        association = await async_client.marketing.events.associations.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_by_external_account(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.events.associations.with_raw_response.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_external_account(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.events.associations.with_streaming_response.list_by_external_account(
            external_event_id="externalEventId",
            external_account_id="externalAccountId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(CollectionResponseWithTotalPublicListNoPaging, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_by_external_account(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_account_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.list_by_external_account(
                external_event_id="externalEventId",
                external_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_event_id` but received ''"):
            await async_client.marketing.events.associations.with_raw_response.list_by_external_account(
                external_event_id="",
                external_account_id="externalAccountId",
            )
