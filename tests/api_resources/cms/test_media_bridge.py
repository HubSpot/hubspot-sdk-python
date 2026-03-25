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
    MediaBridgeObject,
    EventVisibilityChange,
    EventVisibilityResponse,
    ObjectDefinitionResponse,
    IntegratorOEmbedDomainModel,
    OEmbedDomainsCollectionResponse,
    BulkIntegratorObjectCreationResponse,
    MediaBridgeProviderRegistrationResponse,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.events import AssociationDefinition
from hubspot_sdk.types.shared import (
    Property,
    ObjectSchema,
    PropertyGroup,
    ObjectTypeDefinition,
    CollectionResponsePropertyNoPaging,
    CollectionResponseObjectSchemaNoPaging,
    CollectionResponsePropertyGroupNoPaging,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMediaBridge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list(
            media_type="AUDIO",
        )
        assert_matches_type(SyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list(
            media_type="AUDIO",
            after="after",
            limit=0,
        )
        assert_matches_type(SyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list(
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(SyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list(
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(SyncPage[MediaBridgeObject], media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete(
            object_id=0,
            media_type="AUDIO",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.delete(
            object_id=0,
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.delete(
            object_id=0,
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_association(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_association_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_association(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_association(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_association(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_association(
                object_type="objectType",
                app_id="",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.create_association(
                object_type="",
                app_id="appId",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_attention_span_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_attention_span_event_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            derived_values={
                "total_percent_played": 0,
                "total_seconds_played": 0,
            },
            external_id="externalId",
            external_play_context="EMAIL",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
            raw_data_string="rawDataString",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_attention_span_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = client.cms.media_bridge.with_raw_response.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_attention_span_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.media_bridge.with_streaming_response.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, StreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_media_played_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_media_played_event_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            external_play_context="EMAIL",
            iframe_url="iframeUrl",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_media_played_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = client.cms.media_bridge.with_raw_response.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_media_played_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.media_bridge.with_streaming_response.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, StreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_media_played_percent_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_media_played_percent_event_with_all_params(
        self, client: Hubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = client.cms.media_bridge.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            external_play_context="EMAIL",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert media_bridge.is_closed
        assert media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_media_played_percent_event(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = client.cms.media_bridge.with_raw_response.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_media_played_percent_event(
        self, client: Hubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.media_bridge.with_streaming_response.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, StreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_object_type(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        )
        assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_object_type(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_object_type(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_object_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_object_type(
                app_id="",
                media_types=["VIDEO"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_oembed_domain(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_oembed_domain_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_oembed_domain(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_oembed_domain(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_oembed_domain(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_oembed_domain(
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="highly_sensitive",
            description="description",
            display_order=0,
            external_options=True,
            form_field=True,
            has_unique_value=True,
            hidden=True,
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            referenced_object_type="referencedObjectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_property(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_property(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_property(
                object_type="objectType",
                app_id="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.create_property(
                object_type="",
                app_id="appId",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property_group(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_property_group_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
            display_order=0,
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_property_group(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_property_group(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_property_group(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_property_group(
                object_type="objectType",
                app_id="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.create_property_group(
                object_type="",
                app_id="appId",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_video_association_definition(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.create_video_association_definition(
            "appId",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_video_association_definition(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.create_video_association_definition(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_video_association_definition(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.create_video_association_definition(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_video_association_definition(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.create_video_association_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_association(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_association(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_association(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_association(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_association(
                association_id="associationId",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_association(
                association_id="associationId",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_id` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_association(
                association_id="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_oembed_domain(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete_oembed_domain(
            app_id="appId",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_oembed_domain_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete_oembed_domain(
            app_id="appId",
            id=0,
            domain_portal_id=0,
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_oembed_domain(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.delete_oembed_domain(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_oembed_domain(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.delete_oembed_domain(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_oembed_domain(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_oembed_domain(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_property(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_property(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_property(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_property_group(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_property_group(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_property_group(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_property_group(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get(
            object_id=0,
            media_type="AUDIO",
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get(
            object_id=0,
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get(
            object_id=0,
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_event_visibility_settings(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_event_visibility_settings(
            "appId",
        )
        assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_event_visibility_settings(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get_event_visibility_settings(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_event_visibility_settings(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get_event_visibility_settings(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_event_visibility_settings(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_event_visibility_settings(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_oembed_domain(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_oembed_domain(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_oembed_domain(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_oembed_domain(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_property(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_property_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            archived=True,
            properties="properties",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_property(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_property(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_property_group(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_property_group(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_property_group(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_property_group(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_schema(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.get_schema(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(ObjectSchema, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_schema(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.get_schema(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(ObjectSchema, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_schema(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.get_schema(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(ObjectSchema, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_schema(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.get_schema(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.get_schema(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_object_types_by_media_type(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        )
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_object_types_by_media_type_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
            include_full_definition=True,
        )
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_object_types_by_media_type(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_object_types_by_media_type(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_object_types_by_media_type(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.list_object_types_by_media_type(
                media_type="AUDIO",
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_oembed_domains(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_oembed_domains(
            app_id="appId",
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_oembed_domains_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_oembed_domains(
            app_id="appId",
            domain_portal_id=0,
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_oembed_domains(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list_oembed_domains(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_oembed_domains(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list_oembed_domains(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_oembed_domains(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.list_oembed_domains(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_properties(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_properties(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_properties_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_properties(
            object_type="objectType",
            app_id="appId",
            archived=True,
            properties="properties",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_properties(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list_properties(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_properties(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list_properties(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_properties(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.list_properties(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.list_properties(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_property_groups(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_property_groups(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_property_groups(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list_property_groups(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_property_groups(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list_property_groups(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_property_groups(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.list_property_groups(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.list_property_groups(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_schemas(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_schemas(
            app_id="appId",
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_schemas_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.list_schemas(
            app_id="appId",
            archived=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_schemas(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.list_schemas(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_schemas(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.list_schemas(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_schemas(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.list_schemas(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_app_name(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            media_bridge = client.cms.media_bridge.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_register_app_name_with_all_params(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            media_bridge = client.cms.media_bridge.register_app_name(
                app_id="appId",
                updated_at=0,
                allow_import_on_disconnect=True,
                module_name="moduleName",
                name="name",
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_register_app_name(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.cms.media_bridge.with_raw_response.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_register_app_name(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.cms.media_bridge.with_streaming_response.register_app_name(
                app_id="appId",
                updated_at=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                media_bridge = response.parse()
                assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_register_app_name(self, client: Hubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
                client.cms.media_bridge.with_raw_response.register_app_name(
                    app_id="",
                    updated_at=0,
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_visibility_settings(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_event_visibility_settings_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
            show_in_reporting=True,
            show_in_timeline=True,
            show_in_workflows=True,
        )
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_event_visibility_settings(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_event_visibility_settings(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_event_visibility_settings(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_event_visibility_settings(
                app_id="",
                event_type="ALL",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_oembed_domain(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_oembed_domain_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_oembed_domain(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_oembed_domain(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_oembed_domain(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            has_unique_value=True,
            hidden=True,
            label="label",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            type="bool",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_property(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_property(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_property(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property_group(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_property_group_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
            display_order=0,
            label="label",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_property_group(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_property_group(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_property_group(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_schema(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        )
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_schema_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
            allows_sensitive_properties=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="primaryDisplayProperty",
            required_properties=["string"],
            restorable=True,
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_schema(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_schema(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_schema(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_schema(
                object_type="objectType",
                app_id="",
                clear_description=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.cms.media_bridge.with_raw_response.update_schema(
                object_type="",
                app_id="appId",
                clear_description=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_settings(
            app_id="appId",
            updated_at=0,
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_settings_with_all_params(self, client: Hubspot) -> None:
        media_bridge = client.cms.media_bridge.update_settings(
            app_id="appId",
            updated_at=0,
            allow_import_on_disconnect=True,
            module_name="moduleName",
            name="name",
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_settings(self, client: Hubspot) -> None:
        response = client.cms.media_bridge.with_raw_response.update_settings(
            app_id="appId",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_settings(self, client: Hubspot) -> None:
        with client.cms.media_bridge.with_streaming_response.update_settings(
            app_id="appId",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = response.parse()
            assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_settings(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.with_raw_response.update_settings(
                app_id="",
                updated_at=0,
            )


class TestAsyncMediaBridge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update(
            0,
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list(
            media_type="AUDIO",
        )
        assert_matches_type(AsyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list(
            media_type="AUDIO",
            after="after",
            limit=0,
        )
        assert_matches_type(AsyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list(
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(AsyncPage[MediaBridgeObject], media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list(
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(AsyncPage[MediaBridgeObject], media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete(
            object_id=0,
            media_type="AUDIO",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.delete(
            object_id=0,
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.delete(
            object_id=0,
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_association(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_association_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
            name="name",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_association(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_association(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_association(
            object_type="objectType",
            app_id="appId",
            from_object_type_id="fromObjectTypeId",
            to_object_type_id="toObjectTypeId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_association(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_association(
                object_type="objectType",
                app_id="",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_association(
                object_type="",
                app_id="appId",
                from_object_type_id="fromObjectTypeId",
                to_object_type_id="toObjectTypeId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_attention_span_event(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_attention_span_event_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            derived_values={
                "total_percent_played": 0,
                "total_seconds_played": 0,
            },
            external_id="externalId",
            external_play_context="EMAIL",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
            raw_data_string="rawDataString",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_attention_span_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = await async_client.cms.media_bridge.with_raw_response.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_attention_span_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/attention-span").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.media_bridge.with_streaming_response.create_attention_span_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            raw_data_map={"foo": 0},
            session_id="sessionId",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_media_played_event(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_media_played_event_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            external_play_context="EMAIL",
            iframe_url="iframeUrl",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_media_played_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = await async_client.cms.media_bridge.with_raw_response.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_media_played_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.media_bridge.with_streaming_response.create_media_played_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            session_id="sessionId",
            state="STARTED",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_media_played_percent_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_media_played_percent_event_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        media_bridge = await async_client.cms.media_bridge.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
            _hsenc="_hsenc",
            contact_id=0,
            contact_utk="contactUtk",
            external_id="externalId",
            external_play_context="EMAIL",
            media_bridge_id=0,
            media_name="mediaName",
            media_url="mediaUrl",
            page_id=0,
            page_name="pageName",
            page_url="pageUrl",
        )
        assert media_bridge.is_closed
        assert await media_bridge.json() == {"foo": "bar"}
        assert cast(Any, media_bridge.is_closed) is True
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_media_played_percent_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        media_bridge = await async_client.cms.media_bridge.with_raw_response.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        )

        assert media_bridge.is_closed is True
        assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await media_bridge.json() == {"foo": "bar"}
        assert isinstance(media_bridge, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_media_played_percent_event(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/media-bridge/2026-03/events/media-played-percent").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.media_bridge.with_streaming_response.create_media_played_percent_event(
            media_type="AUDIO",
            occurred_timestamp=0,
            played_percent=0,
            session_id="sessionId",
        ) as media_bridge:
            assert not media_bridge.is_closed
            assert media_bridge.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await media_bridge.json() == {"foo": "bar"}
            assert cast(Any, media_bridge.is_closed) is True
            assert isinstance(media_bridge, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, media_bridge.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_object_type(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        )
        assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_object_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_object_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_object_type(
            app_id="appId",
            media_types=["VIDEO"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(BulkIntegratorObjectCreationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_object_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_object_type(
                app_id="",
                media_types=["VIDEO"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_oembed_domain(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_oembed_domain_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_oembed_domain(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_oembed_domain(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_oembed_domain(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_oembed_domain(
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
            calculation_formula="calculationFormula",
            data_sensitivity="highly_sensitive",
            description="description",
            display_order=0,
            external_options=True,
            form_field=True,
            has_unique_value=True,
            hidden=True,
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            referenced_object_type="referencedObjectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_property(
            object_type="objectType",
            app_id="appId",
            field_type="booleancheckbox",
            group_name="groupName",
            label="label",
            name="name",
            type="bool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_property(
                object_type="objectType",
                app_id="",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_property(
                object_type="",
                app_id="appId",
                field_type="booleancheckbox",
                group_name="groupName",
                label="label",
                name="name",
                type="bool",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property_group(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_property_group_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
            display_order=0,
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_property_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_property_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_property_group(
            object_type="objectType",
            app_id="appId",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_property_group(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_property_group(
                object_type="objectType",
                app_id="",
                label="label",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_property_group(
                object_type="",
                app_id="appId",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_video_association_definition(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.create_video_association_definition(
            "appId",
        )
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_video_association_definition(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.create_video_association_definition(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_video_association_definition(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.create_video_association_definition(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(AssociationDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_video_association_definition(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.create_video_association_definition(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_association(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_association(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_association(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.delete_association(
            association_id="associationId",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_association(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_association(
                association_id="associationId",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_association(
                association_id="associationId",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `association_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_association(
                association_id="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_oembed_domain(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete_oembed_domain(
            app_id="appId",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_oembed_domain_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete_oembed_domain(
            app_id="appId",
            id=0,
            domain_portal_id=0,
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_oembed_domain(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.delete_oembed_domain(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_oembed_domain(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.delete_oembed_domain(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_oembed_domain(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_oembed_domain(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_property(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.delete_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_property_group(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_property_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert media_bridge is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_property_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.delete_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert media_bridge is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_property_group(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.delete_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get(
            object_id=0,
            media_type="AUDIO",
        )
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get(
            object_id=0,
            media_type="AUDIO",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get(
            object_id=0,
            media_type="AUDIO",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeObject, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_event_visibility_settings(
            "appId",
        )
        assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get_event_visibility_settings(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get_event_visibility_settings(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(EventVisibilityResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_event_visibility_settings(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_oembed_domain(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_oembed_domain(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_oembed_domain(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_oembed_domain(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_property(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_property_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            archived=True,
            properties="properties",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_property_group(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_property_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_property_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_property_group(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_schema(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.get_schema(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(ObjectSchema, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_schema(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.get_schema(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(ObjectSchema, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_schema(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.get_schema(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(ObjectSchema, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_schema(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_schema(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.get_schema(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_object_types_by_media_type(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        )
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_object_types_by_media_type_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
            include_full_definition=True,
        )
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_object_types_by_media_type(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_object_types_by_media_type(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list_object_types_by_media_type(
            media_type="AUDIO",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(ObjectDefinitionResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_object_types_by_media_type(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_object_types_by_media_type(
                media_type="AUDIO",
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_oembed_domains(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_oembed_domains(
            app_id="appId",
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_oembed_domains_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_oembed_domains(
            app_id="appId",
            domain_portal_id=0,
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_oembed_domains(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list_oembed_domains(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_oembed_domains(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list_oembed_domains(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(OEmbedDomainsCollectionResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_oembed_domains(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_oembed_domains(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_properties(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_properties(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_properties_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_properties(
            object_type="objectType",
            app_id="appId",
            archived=True,
            properties="properties",
        )
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_properties(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list_properties(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_properties(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list_properties(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(CollectionResponsePropertyNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_properties(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_properties(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_properties(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_property_groups(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_property_groups(
            object_type="objectType",
            app_id="appId",
        )
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_property_groups(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list_property_groups(
            object_type="objectType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_property_groups(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list_property_groups(
            object_type="objectType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(CollectionResponsePropertyGroupNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_property_groups(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_property_groups(
                object_type="objectType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_property_groups(
                object_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_schemas(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_schemas(
            app_id="appId",
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_schemas_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.list_schemas(
            app_id="appId",
            archived=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_schemas(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.list_schemas(
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_schemas(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.list_schemas(
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_schemas(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.list_schemas(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_app_name(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            media_bridge = await async_client.cms.media_bridge.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_register_app_name_with_all_params(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            media_bridge = await async_client.cms.media_bridge.register_app_name(
                app_id="appId",
                updated_at=0,
                allow_import_on_disconnect=True,
                module_name="moduleName",
                name="name",
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_register_app_name(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.cms.media_bridge.with_raw_response.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_register_app_name(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.cms.media_bridge.with_streaming_response.register_app_name(
                app_id="appId",
                updated_at=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                media_bridge = await response.parse()
                assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_register_app_name(self, async_client: AsyncHubspot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
                await async_client.cms.media_bridge.with_raw_response.register_app_name(
                    app_id="",
                    updated_at=0,
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_event_visibility_settings_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
            show_in_reporting=True,
            show_in_timeline=True,
            show_in_workflows=True,
        )
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(EventVisibilityChange, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_event_visibility_settings(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_event_visibility_settings(
                app_id="",
                event_type="ALL",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_oembed_domain(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_oembed_domain_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_oembed_domain(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_oembed_domain(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_oembed_domain(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=0,
            field_type="booleancheckbox",
            form_field=True,
            group_name="groupName",
            has_unique_value=True,
            hidden=True,
            label="label",
            options=[
                {
                    "display_order": 0,
                    "hidden": True,
                    "label": "label",
                    "value": "value",
                    "description": "description",
                }
            ],
            type="bool",
        )
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_property(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(Property, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_property(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_property(
            property_name="propertyName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(Property, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_property(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property(
                property_name="propertyName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property(
                property_name="propertyName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property(
                property_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property_group(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_property_group_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
            display_order=0,
            label="label",
        )
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_property_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(PropertyGroup, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_property_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_property_group(
            group_name="groupName",
            app_id="appId",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(PropertyGroup, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_property_group(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="groupName",
                app_id="",
                object_type="objectType",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="groupName",
                app_id="appId",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_name` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_property_group(
                group_name="",
                app_id="appId",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_schema(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        )
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_schema_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
            allows_sensitive_properties=True,
            description="description",
            labels={
                "plural": "plural",
                "singular": "singular",
            },
            primary_display_property="primaryDisplayProperty",
            required_properties=["string"],
            restorable=True,
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_schema(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_schema(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_schema(
            object_type="objectType",
            app_id="appId",
            clear_description=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(ObjectTypeDefinition, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_schema(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_schema(
                object_type="objectType",
                app_id="",
                clear_description=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_schema(
                object_type="",
                app_id="appId",
                clear_description=True,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_settings(
            app_id="appId",
            updated_at=0,
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncHubspot) -> None:
        media_bridge = await async_client.cms.media_bridge.update_settings(
            app_id="appId",
            updated_at=0,
            allow_import_on_disconnect=True,
            module_name="moduleName",
            name="name",
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.media_bridge.with_raw_response.update_settings(
            app_id="appId",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media_bridge = await response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.media_bridge.with_streaming_response.update_settings(
            app_id="appId",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media_bridge = await response.parse()
            assert_matches_type(MediaBridgeProviderRegistrationResponse, media_bridge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.with_raw_response.update_settings(
                app_id="",
                updated_at=0,
            )
