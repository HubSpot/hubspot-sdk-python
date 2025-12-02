# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.cms import (
    AssetFileMetadata,
)
from hubspot_sdk.types.shared import TaskLocator, ActionResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSourceCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            source_code = client.cms.source_code.create(
                file_path="file_path",
                environment="environment",
            )

        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            source_code = client.cms.source_code.create(
                file_path="file_path",
                environment="environment",
                file=b"raw file contents",
            )

        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.cms.source_code.with_raw_response.create(
                file_path="file_path",
                environment="environment",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.cms.source_code.with_streaming_response.create(
                file_path="file_path",
                environment="environment",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source_code = response.parse()
                assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
                client.cms.source_code.with_raw_response.create(
                    file_path="file_path",
                    environment="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
                client.cms.source_code.with_raw_response.create(
                    file_path="",
                    environment="environment",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.delete(
            file_path="file_path",
            environment="environment",
        )
        assert source_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.source_code.with_raw_response.delete(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert source_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.source_code.with_streaming_response.delete(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert source_code is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            client.cms.source_code.with_raw_response.delete(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.cms.source_code.with_raw_response.delete(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_extract_async(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.extract_async(
            path="path",
        )
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_extract_async(self, client: Hubspot) -> None:
        response = client.cms.source_code.with_raw_response.extract_async(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_extract_async(self, client: Hubspot) -> None:
        with client.cms.source_code.with_streaming_response.extract_async(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(TaskLocator, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = client.cms.source_code.get(
            file_path="file_path",
            environment="environment",
        )
        assert source_code.is_closed
        assert source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source_code = client.cms.source_code.with_raw_response.get(
            file_path="file_path",
            environment="environment",
        )

        assert source_code.is_closed is True
        assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"
        assert source_code.json() == {"foo": "bar"}
        assert isinstance(source_code, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.source_code.with_streaming_response.get(
            file_path="file_path",
            environment="environment",
        ) as source_code:
            assert not source_code.is_closed
            assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"

            assert source_code.json() == {"foo": "bar"}
            assert cast(Any, source_code.is_closed) is True
            assert isinstance(source_code, StreamedBinaryAPIResponse)

        assert cast(Any, source_code.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            client.cms.source_code.with_raw_response.get(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.cms.source_code.with_raw_response.get(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_extraction_status(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.get_extraction_status(
            0,
        )
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_extraction_status(self, client: Hubspot) -> None:
        response = client.cms.source_code.with_raw_response.get_extraction_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_extraction_status(self, client: Hubspot) -> None:
        with client.cms.source_code.with_streaming_response.get_extraction_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(ActionResponse, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.get_metadata(
            file_path="file_path",
            environment="environment",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata_with_all_params(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.get_metadata(
            file_path="file_path",
            environment="environment",
            properties="properties",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_metadata(self, client: Hubspot) -> None:
        response = client.cms.source_code.with_raw_response.get_metadata(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_metadata(self, client: Hubspot) -> None:
        with client.cms.source_code.with_streaming_response.get_metadata(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_metadata(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            client.cms.source_code.with_raw_response.get_metadata(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.cms.source_code.with_raw_response.get_metadata(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.upsert(
            file_path="file_path",
            environment="environment",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Hubspot) -> None:
        source_code = client.cms.source_code.upsert(
            file_path="file_path",
            environment="environment",
            file=b"raw file contents",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: Hubspot) -> None:
        response = client.cms.source_code.with_raw_response.upsert(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: Hubspot) -> None:
        with client.cms.source_code.with_streaming_response.upsert(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = response.parse()
            assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upsert(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            client.cms.source_code.with_raw_response.upsert(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.cms.source_code.with_raw_response.upsert(
                file_path="",
                environment="environment",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_validate(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = client.cms.source_code.validate(
            file_path="file_path",
            environment="environment",
        )
        assert source_code.is_closed
        assert source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_validate_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = client.cms.source_code.validate(
            file_path="file_path",
            environment="environment",
            file=b"raw file contents",
        )
        assert source_code.is_closed
        assert source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_validate(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source_code = client.cms.source_code.with_raw_response.validate(
            file_path="file_path",
            environment="environment",
        )

        assert source_code.is_closed is True
        assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"
        assert source_code.json() == {"foo": "bar"}
        assert isinstance(source_code, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_validate(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.source_code.with_streaming_response.validate(
            file_path="file_path",
            environment="environment",
        ) as source_code:
            assert not source_code.is_closed
            assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"

            assert source_code.json() == {"foo": "bar"}
            assert cast(Any, source_code.is_closed) is True
            assert isinstance(source_code, StreamedBinaryAPIResponse)

        assert cast(Any, source_code.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_validate(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            client.cms.source_code.with_raw_response.validate(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            client.cms.source_code.with_raw_response.validate(
                file_path="",
                environment="environment",
            )


class TestAsyncSourceCode:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            source_code = await async_client.cms.source_code.create(
                file_path="file_path",
                environment="environment",
            )

        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            source_code = await async_client.cms.source_code.create(
                file_path="file_path",
                environment="environment",
                file=b"raw file contents",
            )

        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.cms.source_code.with_raw_response.create(
                file_path="file_path",
                environment="environment",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.cms.source_code.with_streaming_response.create(
                file_path="file_path",
                environment="environment",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                source_code = await response.parse()
                assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
                await async_client.cms.source_code.with_raw_response.create(
                    file_path="file_path",
                    environment="",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
                await async_client.cms.source_code.with_raw_response.create(
                    file_path="",
                    environment="environment",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.delete(
            file_path="file_path",
            environment="environment",
        )
        assert source_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.source_code.with_raw_response.delete(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert source_code is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.source_code.with_streaming_response.delete(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert source_code is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            await async_client.cms.source_code.with_raw_response.delete(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.cms.source_code.with_raw_response.delete(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_extract_async(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.extract_async(
            path="path",
        )
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_extract_async(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.source_code.with_raw_response.extract_async(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(TaskLocator, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_extract_async(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.source_code.with_streaming_response.extract_async(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(TaskLocator, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = await async_client.cms.source_code.get(
            file_path="file_path",
            environment="environment",
        )
        assert source_code.is_closed
        assert await source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source_code = await async_client.cms.source_code.with_raw_response.get(
            file_path="file_path",
            environment="environment",
        )

        assert source_code.is_closed is True
        assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await source_code.json() == {"foo": "bar"}
        assert isinstance(source_code, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/source-code/environment/content/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.source_code.with_streaming_response.get(
            file_path="file_path",
            environment="environment",
        ) as source_code:
            assert not source_code.is_closed
            assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await source_code.json() == {"foo": "bar"}
            assert cast(Any, source_code.is_closed) is True
            assert isinstance(source_code, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, source_code.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            await async_client.cms.source_code.with_raw_response.get(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.cms.source_code.with_raw_response.get(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_extraction_status(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.get_extraction_status(
            0,
        )
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_extraction_status(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.source_code.with_raw_response.get_extraction_status(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(ActionResponse, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_extraction_status(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.source_code.with_streaming_response.get_extraction_status(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(ActionResponse, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.get_metadata(
            file_path="file_path",
            environment="environment",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata_with_all_params(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.get_metadata(
            file_path="file_path",
            environment="environment",
            properties="properties",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.source_code.with_raw_response.get_metadata(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.source_code.with_streaming_response.get_metadata(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_metadata(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            await async_client.cms.source_code.with_raw_response.get_metadata(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.cms.source_code.with_raw_response.get_metadata(
                file_path="",
                environment="environment",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.upsert(
            file_path="file_path",
            environment="environment",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncHubspot) -> None:
        source_code = await async_client.cms.source_code.upsert(
            file_path="file_path",
            environment="environment",
            file=b"raw file contents",
        )
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.source_code.with_raw_response.upsert(
            file_path="file_path",
            environment="environment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source_code = await response.parse()
        assert_matches_type(AssetFileMetadata, source_code, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.source_code.with_streaming_response.upsert(
            file_path="file_path",
            environment="environment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source_code = await response.parse()
            assert_matches_type(AssetFileMetadata, source_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            await async_client.cms.source_code.with_raw_response.upsert(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.cms.source_code.with_raw_response.upsert(
                file_path="",
                environment="environment",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_validate(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = await async_client.cms.source_code.validate(
            file_path="file_path",
            environment="environment",
        )
        assert source_code.is_closed
        assert await source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_validate_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        source_code = await async_client.cms.source_code.validate(
            file_path="file_path",
            environment="environment",
            file=b"raw file contents",
        )
        assert source_code.is_closed
        assert await source_code.json() == {"foo": "bar"}
        assert cast(Any, source_code.is_closed) is True
        assert isinstance(source_code, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_validate(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        source_code = await async_client.cms.source_code.with_raw_response.validate(
            file_path="file_path",
            environment="environment",
        )

        assert source_code.is_closed is True
        assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await source_code.json() == {"foo": "bar"}
        assert isinstance(source_code, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_validate(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/v3/source-code/environment/validate/file_path").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.source_code.with_streaming_response.validate(
            file_path="file_path",
            environment="environment",
        ) as source_code:
            assert not source_code.is_closed
            assert source_code.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await source_code.json() == {"foo": "bar"}
            assert cast(Any, source_code.is_closed) is True
            assert isinstance(source_code, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, source_code.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_validate(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment` but received ''"):
            await async_client.cms.source_code.with_raw_response.validate(
                file_path="file_path",
                environment="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_path` but received ''"):
            await async_client.cms.source_code.with_raw_response.validate(
                file_path="",
                environment="environment",
            )
