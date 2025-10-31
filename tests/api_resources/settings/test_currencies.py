# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.settings import (
    ExchangeRate,
    CompanyCurrency,
    BatchResponseExchangeRate,
    CollectionResponseExchangeRateNoPaging,
    CollectionResponseCurrencyCodeInfoNoPaging,
    CollectionResponseExchangeRateForwardPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_create(self, client: Hubspot) -> None:
        currency = client.settings.currencies.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_create(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_create(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_get(self, client: Hubspot) -> None:
        currency = client.settings.currencies.batch_get(
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_get(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.batch_get(
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_get(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.batch_get(
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_batch_update(self, client: Hubspot) -> None:
        currency = client.settings.currencies.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_batch_update(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_batch_update(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_exchange_rate(self, client: Hubspot) -> None:
        currency = client.settings.currencies.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_exchange_rate_with_all_params(self, client: Hubspot) -> None:
        currency = client.settings.currencies.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_exchange_rate(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_exchange_rate(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_company_currency(self, client: Hubspot) -> None:
        currency = client.settings.currencies.get_company_currency()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_company_currency(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.get_company_currency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_company_currency(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.get_company_currency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_exchange_rate_by_id(self, client: Hubspot) -> None:
        currency = client.settings.currencies.get_exchange_rate_by_id(
            "exchangeRateId",
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_exchange_rate_by_id(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.get_exchange_rate_by_id(
            "exchangeRateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_exchange_rate_by_id(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.get_exchange_rate_by_id(
            "exchangeRateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_exchange_rate_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            client.settings.currencies.with_raw_response.get_exchange_rate_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_codes(self, client: Hubspot) -> None:
        currency = client.settings.currencies.list_codes()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_codes(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.list_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_codes(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.list_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_current_exchange_rates(self, client: Hubspot) -> None:
        currency = client.settings.currencies.list_current_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_current_exchange_rates(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.list_current_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_current_exchange_rates(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.list_current_exchange_rates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_exchange_rates(self, client: Hubspot) -> None:
        currency = client.settings.currencies.list_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_exchange_rates(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.list_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_exchange_rates(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.list_exchange_rates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_company_currency(self, client: Hubspot) -> None:
        currency = client.settings.currencies.update_company_currency(
            currency_code="AED",
        )
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_company_currency(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.update_company_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_company_currency(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.update_company_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_exchange_rate(self, client: Hubspot) -> None:
        currency = client.settings.currencies.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_exchange_rate_with_all_params(self, client: Hubspot) -> None:
        currency = client.settings.currencies.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_exchange_rate(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_exchange_rate(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_exchange_rate(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            client.settings.currencies.with_raw_response.update_exchange_rate(
                exchange_rate_id="",
                conversion_rate=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_visibility(self, client: Hubspot) -> None:
        currency = client.settings.currencies.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )
        assert currency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_visibility(self, client: Hubspot) -> None:
        response = client.settings.currencies.with_raw_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert currency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_visibility(self, client: Hubspot) -> None:
        with client.settings.currencies.with_streaming_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert currency is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_create(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.batch_create(
            inputs=[
                {
                    "conversion_rate": 0,
                    "from_currency_code": "AED",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_get(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.batch_get(
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.batch_get(
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.batch_get(
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_batch_update(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_batch_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_batch_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.batch_update(
            inputs=[
                {
                    "id": "id",
                    "conversion_rate": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(BatchResponseExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_exchange_rate(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_exchange_rate_with_all_params(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_exchange_rate(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_exchange_rate(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.create_exchange_rate(
            conversion_rate=0,
            from_currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_company_currency(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.get_company_currency()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_company_currency(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.get_company_currency()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_company_currency(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.get_company_currency() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_exchange_rate_by_id(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.get_exchange_rate_by_id(
            "exchangeRateId",
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_exchange_rate_by_id(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.get_exchange_rate_by_id(
            "exchangeRateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_exchange_rate_by_id(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.get_exchange_rate_by_id(
            "exchangeRateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_exchange_rate_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            await async_client.settings.currencies.with_raw_response.get_exchange_rate_by_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_codes(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.list_codes()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_codes(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.list_codes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_codes(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.list_codes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CollectionResponseCurrencyCodeInfoNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_current_exchange_rates(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.list_current_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_current_exchange_rates(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.list_current_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_current_exchange_rates(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.list_current_exchange_rates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CollectionResponseExchangeRateNoPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_exchange_rates(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.list_exchange_rates()
        assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_exchange_rates(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.list_exchange_rates()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_exchange_rates(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.list_exchange_rates() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CollectionResponseExchangeRateForwardPaging, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_company_currency(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.update_company_currency(
            currency_code="AED",
        )
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_company_currency(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.update_company_currency(
            currency_code="AED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CompanyCurrency, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_company_currency(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.update_company_currency(
            currency_code="AED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CompanyCurrency, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_exchange_rate(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_exchange_rate_with_all_params(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
            effective_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_exchange_rate(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(ExchangeRate, currency, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_exchange_rate(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.update_exchange_rate(
            exchange_rate_id="exchangeRateId",
            conversion_rate=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(ExchangeRate, currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_exchange_rate(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `exchange_rate_id` but received ''"):
            await async_client.settings.currencies.with_raw_response.update_exchange_rate(
                exchange_rate_id="",
                conversion_rate=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_visibility(self, async_client: AsyncHubspot) -> None:
        currency = await async_client.settings.currencies.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )
        assert currency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_visibility(self, async_client: AsyncHubspot) -> None:
        response = await async_client.settings.currencies.with_raw_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert currency is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_visibility(self, async_client: AsyncHubspot) -> None:
        async with async_client.settings.currencies.with_streaming_response.update_visibility(
            from_currency_code="AED",
            to_currency_code="AED",
            visible_in_ui=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert currency is None

        assert cast(Any, response.is_closed) is True
