# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import PageData
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLandingPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update(
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
                                        "units": "deg",
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
                                "breakpoint_styles": {
                                    "foo": {
                                        "hidden": True,
                                        "margin": {
                                            "bottom": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "top": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                        },
                                        "padding": {
                                            "bottom": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "left": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "right": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "top": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                        },
                                    }
                                },
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
                                "units": "deg",
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
                        "breakpoint_styles": {
                            "foo": {
                                "hidden": True,
                                "margin": {
                                    "bottom": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "top": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                },
                                "padding": {
                                    "bottom": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "left": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "right": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "top": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                },
                            }
                        },
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
                    "tag_ids": [0],
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
            archived=True,
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.update(
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
                                            "units": "deg",
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
                                    "units": "deg",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list()
        assert_matches_type(SyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(SyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(SyncPage[PageData], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.clone(
            id="id",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get(
            object_id="objectId",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_draft(
            "objectId",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_push_draft_live(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.push_draft_live(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_push_draft_live(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.push_draft_live(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_push_draft_live(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.push_draft_live(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_push_draft_live(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.push_draft_live(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.reset_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.update_draft(
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
                                            "units": "deg",
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
                                    "units": "deg",
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


class TestAsyncLandingPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update(
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
                                        "units": "deg",
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
                                "breakpoint_styles": {
                                    "foo": {
                                        "hidden": True,
                                        "margin": {
                                            "bottom": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "top": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                        },
                                        "padding": {
                                            "bottom": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "left": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "right": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                            "top": {
                                                "units": "%",
                                                "value": 0,
                                            },
                                        },
                                    }
                                },
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
                                "units": "deg",
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
                        "breakpoint_styles": {
                            "foo": {
                                "hidden": True,
                                "margin": {
                                    "bottom": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "top": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                },
                                "padding": {
                                    "bottom": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "left": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "right": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                    "top": {
                                        "units": "%",
                                        "value": 0,
                                    },
                                },
                            }
                        },
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
                    "tag_ids": [0],
                }
            },
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_by_id="updatedById",
            url="url",
            use_featured_image=True,
            widget_containers={"foo": {}},
            widgets={"foo": {}},
            archived=True,
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.update(
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
                                            "units": "deg",
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
                                    "units": "deg",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list()
        assert_matches_type(AsyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list(
            after="after",
            archived=True,
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=0,
            property="property",
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(AsyncPage[PageData], landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(AsyncPage[PageData], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.clone(
            id="id",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get(
            object_id="objectId",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_draft(
            "objectId",
        )
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_push_draft_live(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.push_draft_live(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_push_draft_live(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.push_draft_live(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_push_draft_live(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.push_draft_live(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_push_draft_live(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.push_draft_live(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.reset_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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
        landing_page = await response.parse()
        assert_matches_type(PageData, landing_page, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update_draft(
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
                                        "units": "deg",
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
                                "units": "deg",
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

            landing_page = await response.parse()
            assert_matches_type(PageData, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.update_draft(
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
                                            "units": "deg",
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
                                    "units": "deg",
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
