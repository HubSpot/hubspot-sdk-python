# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.cms import (
    URLMapping,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLRedirects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            client.cms.url_redirects.with_raw_response.update(
                url_redirect_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                destination="destination",
                is_match_full_url=True,
                is_match_query_string=True,
                is_only_after_not_found=True,
                is_pattern=True,
                is_protocol_agnostic=True,
                is_trailing_slash_optional=True,
                precedence=0,
                redirect_style=0,
                route_prefix="routePrefix",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.list()
        assert_matches_type(SyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert_matches_type(SyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert_matches_type(SyncPage[URLMapping], url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.delete(
            "urlRedirectId",
        )
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.delete(
            "urlRedirectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.delete(
            "urlRedirectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert url_redirect is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            client.cms.url_redirects.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = client.cms.url_redirects.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert url_redirect.is_closed
        assert url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = client.cms.url_redirects.with_raw_response.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.url_redirects.with_streaming_response.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, StreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_url_mapping(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.delete_url_mapping(
            0,
        )
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_url_mapping(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.delete_url_mapping(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_url_mapping(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.delete_url_mapping(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert url_redirect is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        url_redirect = client.cms.url_redirects.get(
            "urlRedirectId",
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.cms.url_redirects.with_raw_response.get(
            "urlRedirectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.cms.url_redirects.with_streaming_response.get(
            "urlRedirectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            client.cms.url_redirects.with_raw_response.get(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = client.cms.url_redirects.get_url_mapping(
            0,
        )
        assert url_redirect.is_closed
        assert url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = client.cms.url_redirects.with_raw_response.get_url_mapping(
            0,
        )

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_url_mapping(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.url_redirects.with_streaming_response.get_url_mapping(
            0,
        ) as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, StreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_url_mappings(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = client.cms.url_redirects.list_url_mappings()
        assert url_redirect.is_closed
        assert url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list_url_mappings(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = client.cms.url_redirects.with_raw_response.list_url_mappings()

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list_url_mappings(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.url_redirects.with_streaming_response.list_url_mappings() as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, StreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True


class TestAsyncURLRedirects:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.create(
            destination="destination",
            redirect_style=0,
            route_prefix="routePrefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.update(
            url_redirect_id="urlRedirectId",
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            await async_client.cms.url_redirects.with_raw_response.update(
                url_redirect_id="",
                id="id",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                destination="destination",
                is_match_full_url=True,
                is_match_query_string=True,
                is_only_after_not_found=True,
                is_pattern=True,
                is_protocol_agnostic=True,
                is_trailing_slash_optional=True,
                precedence=0,
                redirect_style=0,
                route_prefix="routePrefix",
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.list()
        assert_matches_type(AsyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert_matches_type(AsyncPage[URLMapping], url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert_matches_type(AsyncPage[URLMapping], url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.delete(
            "urlRedirectId",
        )
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.delete(
            "urlRedirectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.delete(
            "urlRedirectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert url_redirect is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            await async_client.cms.url_redirects.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_url_mapping(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = await async_client.cms.url_redirects.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert url_redirect.is_closed
        assert await url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_url_mapping(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = await async_client.cms.url_redirects.with_raw_response.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_url_mapping(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.url_redirects.with_streaming_response.create_url_mapping(
            id="id",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            destination="destination",
            is_match_full_url=True,
            is_match_query_string=True,
            is_only_after_not_found=True,
            is_pattern=True,
            is_protocol_agnostic=True,
            is_trailing_slash_optional=True,
            precedence=0,
            redirect_style=0,
            route_prefix="routePrefix",
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_url_mapping(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.delete_url_mapping(
            0,
        )
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_url_mapping(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.delete_url_mapping(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert url_redirect is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_url_mapping(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.delete_url_mapping(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert url_redirect is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        url_redirect = await async_client.cms.url_redirects.get(
            "urlRedirectId",
        )
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.url_redirects.with_raw_response.get(
            "urlRedirectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_redirect = await response.parse()
        assert_matches_type(URLMapping, url_redirect, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.url_redirects.with_streaming_response.get(
            "urlRedirectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_redirect = await response.parse()
            assert_matches_type(URLMapping, url_redirect, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url_redirect_id` but received ''"):
            await async_client.cms.url_redirects.with_raw_response.get(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_url_mapping(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = await async_client.cms.url_redirects.get_url_mapping(
            0,
        )
        assert url_redirect.is_closed
        assert await url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_url_mapping(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = await async_client.cms.url_redirects.with_raw_response.get_url_mapping(
            0,
        )

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_url_mapping(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings/0").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.url_redirects.with_streaming_response.get_url_mapping(
            0,
        ) as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_url_mappings(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        url_redirect = await async_client.cms.url_redirects.list_url_mappings()
        assert url_redirect.is_closed
        assert await url_redirect.json() == {"foo": "bar"}
        assert cast(Any, url_redirect.is_closed) is True
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list_url_mappings(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        url_redirect = await async_client.cms.url_redirects.with_raw_response.list_url_mappings()

        assert url_redirect.is_closed is True
        assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await url_redirect.json() == {"foo": "bar"}
        assert isinstance(url_redirect, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list_url_mappings(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/url-redirects/2026-03/url-mappings").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.url_redirects.with_streaming_response.list_url_mappings() as url_redirect:
            assert not url_redirect.is_closed
            assert url_redirect.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await url_redirect.json() == {"foo": "bar"}
            assert cast(Any, url_redirect.is_closed) is True
            assert isinstance(url_redirect, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, url_redirect.is_closed) is True
