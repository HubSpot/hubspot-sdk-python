# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import PagesPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        draft = client.cms.pages.site_pages.draft.get_draft(
            "objectId",
        )
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.draft.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.draft.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PagesPage, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.draft.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish_draft(self, client: HubSpot) -> None:
        draft = client.cms.pages.site_pages.draft.publish_draft(
            "objectId",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.draft.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.draft.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.draft.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_site_page_draft(self, client: HubSpot) -> None:
        draft = client.cms.pages.site_pages.draft.reset_site_page_draft(
            "objectId",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_site_page_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.draft.with_raw_response.reset_site_page_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_site_page_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.draft.with_streaming_response.reset_site_page_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset_site_page_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.draft.with_raw_response.reset_site_page_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        draft = client.cms.pages.site_pages.draft.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        )
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.draft.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.draft.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(PagesPage, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.draft.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                campaign="campaign",
                category_id=0,
                content_group_id="contentGroupId",
                content_type_category="0",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                created_by_id="createdById",
                currently_published=True,
                current_state="AGENT_GENERATED",
                domain="domain",
                dynamic_page_data_source_id="dynamicPageDataSourceId",
                dynamic_page_data_source_type=0,
                dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
                enable_domain_stylesheets=True,
                enable_layout_stylesheets=True,
                featured_image="featuredImage",
                featured_image_alt_text="featuredImageAltText",
                folder_id="folderId",
                footer_html="footerHtml",
                head_html="headHtml",
                html_title="htmlTitle",
                include_default_custom_css=True,
                language="aa",
                layout_sections={
                    "foo": {
                        "cells": [],
                        "css_class": "cssClass",
                        "css_id": "cssId",
                        "css_style": "cssStyle",
                        "label": "label",
                        "name": "name",
                        "params": {"foo": {}},
                        "row_meta_data": [
                            {
                                "css_class": "cssClass",
                                "styles": {
                                    "background_color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    },
                                    "background_gradient": {
                                        "angle": {
                                            "units": "DEGREES",
                                            "value": 0,
                                        },
                                        "colors": [
                                            {
                                                "color": {
                                                    "a": 0,
                                                    "b": 0,
                                                    "g": 0,
                                                    "r": 0,
                                                }
                                            }
                                        ],
                                        "side_or_corner": {
                                            "horizontal_side": "CENTER",
                                            "vertical_side": "BOTTOM",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "BOTTOM_CENTER",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "BOTTOM",
                                },
                            }
                        ],
                        "rows": [{}],
                        "styles": {
                            "background_color": {
                                "a": 0,
                                "b": 0,
                                "g": 0,
                                "r": 0,
                            },
                            "background_gradient": {
                                "angle": {
                                    "units": "DEGREES",
                                    "value": 0,
                                },
                                "colors": [
                                    {
                                        "color": {
                                            "a": 0,
                                            "b": 0,
                                            "g": 0,
                                            "r": 0,
                                        }
                                    }
                                ],
                                "side_or_corner": {
                                    "horizontal_side": "CENTER",
                                    "vertical_side": "BOTTOM",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "BOTTOM_CENTER",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "BOTTOM",
                        },
                        "type": "type",
                        "w": 0,
                        "x": 0,
                    }
                },
                link_rel_canonical_url="linkRelCanonicalUrl",
                mab_experiment_id="mabExperimentId",
                meta_description="metaDescription",
                name="name",
                page_expiry_date=0,
                page_expiry_enabled=True,
                page_expiry_redirect_id=0,
                page_expiry_redirect_url="pageExpiryRedirectUrl",
                page_redirected=True,
                password="password",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                slug="slug",
                state="state",
                subcategory="subcategory",
                template_path="templatePath",
                theme_settings_values={"foo": {}},
                translated_from_id="translatedFromId",
                translations={
                    "foo": {
                        "id": 0,
                        "archived_in_dashboard": True,
                        "author_name": "authorName",
                        "campaign": "campaign",
                        "campaign_name": "campaignName",
                        "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "name": "name",
                        "password": "password",
                        "public_access_rules": [{}],
                        "public_access_rules_enabled": True,
                        "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "slug": "slug",
                        "state": "state",
                        "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    }
                },
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_by_id="updatedById",
                url="url",
                use_featured_image=True,
                widget_containers={"foo": {}},
                widgets={"foo": {}},
            )


class TestAsyncDraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        draft = await async_client.cms.pages.site_pages.draft.get_draft(
            "objectId",
        )
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.draft.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.draft.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PagesPage, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.draft.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish_draft(self, async_client: AsyncHubSpot) -> None:
        draft = await async_client.cms.pages.site_pages.draft.publish_draft(
            "objectId",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.draft.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.draft.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.draft.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_site_page_draft(self, async_client: AsyncHubSpot) -> None:
        draft = await async_client.cms.pages.site_pages.draft.reset_site_page_draft(
            "objectId",
        )
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_site_page_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.draft.with_raw_response.reset_site_page_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert draft is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_site_page_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.draft.with_streaming_response.reset_site_page_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert draft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset_site_page_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.draft.with_raw_response.reset_site_page_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        draft = await async_client.cms.pages.site_pages.draft.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        )
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.draft.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(PagesPage, draft, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.draft.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            campaign="campaign",
            category_id=0,
            content_group_id="contentGroupId",
            content_type_category="0",
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_by_id="createdById",
            currently_published=True,
            current_state="AGENT_GENERATED",
            domain="domain",
            dynamic_page_data_source_id="dynamicPageDataSourceId",
            dynamic_page_data_source_type=0,
            dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
            enable_domain_stylesheets=True,
            enable_layout_stylesheets=True,
            featured_image="featuredImage",
            featured_image_alt_text="featuredImageAltText",
            folder_id="folderId",
            footer_html="footerHtml",
            head_html="headHtml",
            html_title="htmlTitle",
            include_default_custom_css=True,
            language="aa",
            layout_sections={
                "foo": {
                    "cells": [],
                    "css_class": "cssClass",
                    "css_id": "cssId",
                    "css_style": "cssStyle",
                    "label": "label",
                    "name": "name",
                    "params": {"foo": {}},
                    "row_meta_data": [
                        {
                            "css_class": "cssClass",
                            "styles": {
                                "background_color": {
                                    "a": 0,
                                    "b": 0,
                                    "g": 0,
                                    "r": 0,
                                },
                                "background_gradient": {
                                    "angle": {
                                        "units": "DEGREES",
                                        "value": 0,
                                    },
                                    "colors": [
                                        {
                                            "color": {
                                                "a": 0,
                                                "b": 0,
                                                "g": 0,
                                                "r": 0,
                                            }
                                        }
                                    ],
                                    "side_or_corner": {
                                        "horizontal_side": "CENTER",
                                        "vertical_side": "BOTTOM",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "BOTTOM_CENTER",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "BOTTOM",
                            },
                        }
                    ],
                    "rows": [{}],
                    "styles": {
                        "background_color": {
                            "a": 0,
                            "b": 0,
                            "g": 0,
                            "r": 0,
                        },
                        "background_gradient": {
                            "angle": {
                                "units": "DEGREES",
                                "value": 0,
                            },
                            "colors": [
                                {
                                    "color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    }
                                }
                            ],
                            "side_or_corner": {
                                "horizontal_side": "CENTER",
                                "vertical_side": "BOTTOM",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "BOTTOM_CENTER",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "BOTTOM",
                    },
                    "type": "type",
                    "w": 0,
                    "x": 0,
                }
            },
            link_rel_canonical_url="linkRelCanonicalUrl",
            mab_experiment_id="mabExperimentId",
            meta_description="metaDescription",
            name="name",
            page_expiry_date=0,
            page_expiry_enabled=True,
            page_expiry_redirect_id=0,
            page_expiry_redirect_url="pageExpiryRedirectUrl",
            page_redirected=True,
            password="password",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            slug="slug",
            state="state",
            subcategory="subcategory",
            template_path="templatePath",
            theme_settings_values={"foo": {}},
            translated_from_id="translatedFromId",
            translations={
                "foo": {
                    "id": 0,
                    "archived_in_dashboard": True,
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "campaign_name": "campaignName",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "slug": "slug",
                    "state": "state",
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(PagesPage, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.draft.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                campaign="campaign",
                category_id=0,
                content_group_id="contentGroupId",
                content_type_category="0",
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                created_by_id="createdById",
                currently_published=True,
                current_state="AGENT_GENERATED",
                domain="domain",
                dynamic_page_data_source_id="dynamicPageDataSourceId",
                dynamic_page_data_source_type=0,
                dynamic_page_hub_db_table_id="dynamicPageHubDbTableId",
                enable_domain_stylesheets=True,
                enable_layout_stylesheets=True,
                featured_image="featuredImage",
                featured_image_alt_text="featuredImageAltText",
                folder_id="folderId",
                footer_html="footerHtml",
                head_html="headHtml",
                html_title="htmlTitle",
                include_default_custom_css=True,
                language="aa",
                layout_sections={
                    "foo": {
                        "cells": [],
                        "css_class": "cssClass",
                        "css_id": "cssId",
                        "css_style": "cssStyle",
                        "label": "label",
                        "name": "name",
                        "params": {"foo": {}},
                        "row_meta_data": [
                            {
                                "css_class": "cssClass",
                                "styles": {
                                    "background_color": {
                                        "a": 0,
                                        "b": 0,
                                        "g": 0,
                                        "r": 0,
                                    },
                                    "background_gradient": {
                                        "angle": {
                                            "units": "DEGREES",
                                            "value": 0,
                                        },
                                        "colors": [
                                            {
                                                "color": {
                                                    "a": 0,
                                                    "b": 0,
                                                    "g": 0,
                                                    "r": 0,
                                                }
                                            }
                                        ],
                                        "side_or_corner": {
                                            "horizontal_side": "CENTER",
                                            "vertical_side": "BOTTOM",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "BOTTOM_CENTER",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "BOTTOM",
                                },
                            }
                        ],
                        "rows": [{}],
                        "styles": {
                            "background_color": {
                                "a": 0,
                                "b": 0,
                                "g": 0,
                                "r": 0,
                            },
                            "background_gradient": {
                                "angle": {
                                    "units": "DEGREES",
                                    "value": 0,
                                },
                                "colors": [
                                    {
                                        "color": {
                                            "a": 0,
                                            "b": 0,
                                            "g": 0,
                                            "r": 0,
                                        }
                                    }
                                ],
                                "side_or_corner": {
                                    "horizontal_side": "CENTER",
                                    "vertical_side": "BOTTOM",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "BOTTOM_CENTER",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "BOTTOM",
                        },
                        "type": "type",
                        "w": 0,
                        "x": 0,
                    }
                },
                link_rel_canonical_url="linkRelCanonicalUrl",
                mab_experiment_id="mabExperimentId",
                meta_description="metaDescription",
                name="name",
                page_expiry_date=0,
                page_expiry_enabled=True,
                page_expiry_redirect_id=0,
                page_expiry_redirect_url="pageExpiryRedirectUrl",
                page_redirected=True,
                password="password",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                slug="slug",
                state="state",
                subcategory="subcategory",
                template_path="templatePath",
                theme_settings_values={"foo": {}},
                translated_from_id="translatedFromId",
                translations={
                    "foo": {
                        "id": 0,
                        "archived_in_dashboard": True,
                        "author_name": "authorName",
                        "campaign": "campaign",
                        "campaign_name": "campaignName",
                        "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "name": "name",
                        "password": "password",
                        "public_access_rules": [{}],
                        "public_access_rules_enabled": True,
                        "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                        "slug": "slug",
                        "state": "state",
                        "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    }
                },
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
                updated_by_id="updatedById",
                url="url",
                use_featured_image=True,
                widget_containers={"foo": {}},
                widgets={"foo": {}},
            )
