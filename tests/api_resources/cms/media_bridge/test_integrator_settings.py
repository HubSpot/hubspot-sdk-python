# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import (
    EventVisibilityChange,
    EventVisibilityResponse,
    ObjectDefinitionResponse,
    IntegratorOEmbedDomainModel,
    OEmbedDomainsCollectionResponse,
    BulkIntegratorObjectCreationResponse,
    MediaBridgeProviderRegistrationResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegratorSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_object_definition(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        )
        assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_object_definition(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_object_definition(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_object_definition(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.create_object_definition(
                app_id="",
                media_types=["VIDEO"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_oembed_domain(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_oembed_domain_with_all_params(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_oembed_domain(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_oembed_domain(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_oembed_domain(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.create_oembed_domain(
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_oembed_domain(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.delete_oembed_domain(
            "appId",
        )
        assert integrator_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_oembed_domain(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.delete_oembed_domain(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert integrator_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_oembed_domain(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.delete_oembed_domain(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert integrator_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_oembed_domain(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.delete_oembed_domain(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_event_visibility_settings(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.get_event_visibility_settings(
            "appId",
        )
        assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_event_visibility_settings(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.get_event_visibility_settings(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_event_visibility_settings(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.get_event_visibility_settings(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_event_visibility_settings(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.get_event_visibility_settings(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_object_definitions_by_media_type(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.get_object_definitions_by_media_type(
            media_type="mediaType",
            app_id="appId",
        )
        assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_object_definitions_by_media_type(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
            media_type="mediaType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_object_definitions_by_media_type(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.get_object_definitions_by_media_type(
            media_type="mediaType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_object_definitions_by_media_type(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
                media_type="mediaType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_type` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
                media_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_oembed_domain(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_oembed_domain(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_oembed_domain(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_oembed_domain(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_oembed_domains(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.list_oembed_domains(
            "appId",
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_oembed_domains(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.list_oembed_domains(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_oembed_domains(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.list_oembed_domains(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_oembed_domains(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.list_oembed_domains(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_app_name(self, client: HubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            integrator_setting = client.cms.media_bridge.integrator_settings.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_app_name_with_all_params(self, client: HubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            integrator_setting = client.cms.media_bridge.integrator_settings.register_app_name(
                app_id="appId",
                updated_at=0,
                name="name",
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_app_name(self, client: HubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.cms.media_bridge.integrator_settings.with_raw_response.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_app_name(self, client: HubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            with client.cms.media_bridge.integrator_settings.with_streaming_response.register_app_name(
                app_id="appId",
                updated_at=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                integrator_setting = response.parse()
                assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_register_app_name(self, client: HubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
                client.cms.media_bridge.integrator_settings.with_raw_response.register_app_name(
                    app_id="",
                    updated_at=0,
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_app_name(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_app_name(
            app_id="appId",
            updated_at=0,
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_app_name_with_all_params(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_app_name(
            app_id="appId",
            updated_at=0,
            name="name",
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_app_name(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.update_app_name(
            app_id="appId",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_app_name(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.update_app_name(
            app_id="appId",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_app_name(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.update_app_name(
                app_id="",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_event_visibility_settings(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_event_visibility_settings_with_all_params(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
            show_in_reporting=True,
            show_in_timeline=True,
            show_in_workflows=True,
        )
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_event_visibility_settings(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = response.parse()
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_event_visibility_settings(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = response.parse()
            assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_event_visibility_settings(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.update_event_visibility_settings(
                app_id="",
                event_type="ALL",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_oembed_domain(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_oembed_domain_with_all_params(self, client: HubSpot) -> None:
        integrator_setting = client.cms.media_bridge.integrator_settings.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_oembed_domain(self, client: HubSpot) -> None:
        response = client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
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
        integrator_setting = response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_oembed_domain(self, client: HubSpot) -> None:
        with client.cms.media_bridge.integrator_settings.with_streaming_response.update_oembed_domain(
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

            integrator_setting = response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_oembed_domain(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )


class TestAsyncIntegratorSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_object_definition(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        )
        assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_object_definition(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_object_definition(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.create_object_definition(
            app_id="appId",
            media_types=["VIDEO"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(BulkIntegratorObjectCreationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_object_definition(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.create_object_definition(
                app_id="",
                media_types=["VIDEO"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_oembed_domain_with_all_params(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.create_oembed_domain(
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.create_oembed_domain(
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.delete_oembed_domain(
            "appId",
        )
        assert integrator_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.delete_oembed_domain(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert integrator_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.delete_oembed_domain(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert integrator_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.delete_oembed_domain(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.get_event_visibility_settings(
            "appId",
        )
        assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_event_visibility_settings(
                "appId",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.cms.media_bridge.integrator_settings.with_streaming_response.get_event_visibility_settings(
                "appId",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(EventVisibilityResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_event_visibility_settings(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_object_definitions_by_media_type(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = (
            await async_client.cms.media_bridge.integrator_settings.get_object_definitions_by_media_type(
                media_type="mediaType",
                app_id="appId",
            )
        )
        assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_object_definitions_by_media_type(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
            media_type="mediaType",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_object_definitions_by_media_type(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.get_object_definitions_by_media_type(
            media_type="mediaType",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(ObjectDefinitionResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_object_definitions_by_media_type(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
                media_type="mediaType",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_type` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_object_definitions_by_media_type(
                media_type="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.get_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.get_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_oembed_domains(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.list_oembed_domains(
            "appId",
        )
        assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_oembed_domains(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.list_oembed_domains(
            "appId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_oembed_domains(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.list_oembed_domains(
            "appId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(OEmbedDomainsCollectionResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_oembed_domains(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.list_oembed_domains(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_app_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            integrator_setting = await async_client.cms.media_bridge.integrator_settings.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_app_name_with_all_params(self, async_client: AsyncHubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            integrator_setting = await async_client.cms.media_bridge.integrator_settings.register_app_name(
                app_id="appId",
                updated_at=0,
                name="name",
            )

        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_app_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.register_app_name(
                app_id="appId",
                updated_at=0,
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_app_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.register_app_name(
                app_id="appId",
                updated_at=0,
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                integrator_setting = await response.parse()
                assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_register_app_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
                await async_client.cms.media_bridge.integrator_settings.with_raw_response.register_app_name(
                    app_id="",
                    updated_at=0,
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_app_name(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_app_name(
            app_id="appId",
            updated_at=0,
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_app_name_with_all_params(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_app_name(
            app_id="appId",
            updated_at=0,
            name="name",
        )
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_app_name(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_app_name(
            app_id="appId",
            updated_at=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_app_name(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.update_app_name(
            app_id="appId",
            updated_at=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(MediaBridgeProviderRegistrationResponse, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_app_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_app_name(
                app_id="",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
        )
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_event_visibility_settings_with_all_params(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_event_visibility_settings(
            app_id="appId",
            event_type="ALL",
            updated_at=0,
            show_in_reporting=True,
            show_in_timeline=True,
            show_in_workflows=True,
        )
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_event_visibility_settings(
                app_id="appId",
                event_type="ALL",
                updated_at=0,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integrator_setting = await response.parse()
        assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.cms.media_bridge.integrator_settings.with_streaming_response.update_event_visibility_settings(
                app_id="appId",
                event_type="ALL",
                updated_at=0,
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integrator_setting = await response.parse()
            assert_matches_type(EventVisibilityChange, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_event_visibility_settings(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_event_visibility_settings(
                app_id="",
                event_type="ALL",
                updated_at=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_oembed_domain_with_all_params(self, async_client: AsyncHubSpot) -> None:
        integrator_setting = await async_client.cms.media_bridge.integrator_settings.update_oembed_domain(
            o_embed_domain_id="oEmbedDomainId",
            app_id="appId",
            endpoints={
                "discovery": True,
                "schemes": ["string"],
                "url": "url",
            },
            portal_id=0,
        )
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
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
        integrator_setting = await response.parse()
        assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.media_bridge.integrator_settings.with_streaming_response.update_oembed_domain(
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

            integrator_setting = await response.parse()
            assert_matches_type(IntegratorOEmbedDomainModel, integrator_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_oembed_domain(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
                o_embed_domain_id="oEmbedDomainId",
                app_id="",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `o_embed_domain_id` but received ''"):
            await async_client.cms.media_bridge.integrator_settings.with_raw_response.update_oembed_domain(
                o_embed_domain_id="",
                app_id="appId",
                endpoints={
                    "discovery": True,
                    "schemes": ["string"],
                    "url": "url",
                },
            )
