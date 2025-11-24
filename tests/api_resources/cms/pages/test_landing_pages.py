# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import (
    Page,
    VersionPage,
    ContentFolder,
    BatchResponsePage,
    VersionContentFolder,
    BatchResponseContentFolder,
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLandingPages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                                "breakpoint_styles": {
                                    "foo": {
                                        "hidden": True,
                                        "margin": {},
                                        "padding": {},
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
                        "breakpoint_styles": {
                            "foo": {
                                "hidden": True,
                                "margin": {},
                                "padding": {},
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
                current_state="AUTOMATED",
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
                language="af",
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
                                            "units": "units",
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
                                            "horizontal_side": "horizontalSide",
                                            "vertical_side": "verticalSide",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "flexboxPositioning",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "verticalAlignment",
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
                                    "units": "units",
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
                                    "horizontal_side": "horizontalSide",
                                    "vertical_side": "verticalSide",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "flexboxPositioning",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "verticalAlignment",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list()
        assert_matches_type(SyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
        assert_matches_type(SyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(SyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(SyncPage[Page], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach_to_lang_group(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.clone(
            id="id",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_ab_test_variation(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_ab_test_variation(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_ab_test_variation(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_folder(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_folder(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_folder(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_folders_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_folders_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_folders_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_language_variation(
            id="id",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_language_variation(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_language_variation(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete_batch(
            inputs=["string"],
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_folder(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete_folder(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_folder_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete_folder(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_folder(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.delete_folder(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_folder(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.delete_folder(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_folder(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.delete_folder(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_folders_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.delete_folders_batch(
            inputs=["string"],
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_folders_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.delete_folders_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_folders_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.delete_folders_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach_from_lang_group(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.detach_from_lang_group(
            id="id",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach_from_lang_group(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_end_ab_test(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_end_ab_test(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_end_ab_test(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get(
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_draft(
            "objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_folder(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_folder(
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_folder_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_folder(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_folder(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_folder(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_folder(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_folder(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_folder(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_folder(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_folder_revision(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_folder_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(VersionContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_folder_revision(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(VersionContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_folder_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_folders_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_folders_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_folders_batch_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_folders_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_folders_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_folders_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_folders_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_folders_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionPage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(VersionPage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(VersionPage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_folder_revisions(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_folder_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_folder_revisions_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_folder_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_folder_revisions(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.list_folder_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(SyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_folder_revisions(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.list_folder_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(SyncPage[VersionContentFolder], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_folder_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.list_folder_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_folders(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_folders()
        assert_matches_type(SyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_folders_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_folders(
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
        assert_matches_type(SyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_folders(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(SyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_folders(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(SyncPage[ContentFolder], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(SyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(SyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(SyncPage[VersionPage], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.publish_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rerun_ab_test(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rerun_ab_test(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rerun_ab_test(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.reset_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_folder_revision(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_folder_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_folder_revision(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_folder_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision_to_draft(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision_to_draft(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision_to_draft(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.set_new_lang_primary(
            id="id",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
                current_state="AUTOMATED",
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
                language="af",
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
                                            "units": "units",
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
                                            "horizontal_side": "horizontalSide",
                                            "vertical_side": "verticalSide",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "flexboxPositioning",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "verticalAlignment",
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
                                    "units": "units",
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
                                    "horizontal_side": "horizontalSide",
                                    "vertical_side": "verticalSide",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "flexboxPositioning",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "verticalAlignment",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_folder(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_folder_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_folder(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_folder(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_folder(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.landing_pages.with_raw_response.update_folder(
                object_id="",
                id="id",
                category=0,
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                name="name",
                parent_folder_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_folders_batch(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_folders_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_folders_batch_with_all_params(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_folders_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_folders_batch(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update_folders_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_folders_batch(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update_folders_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_languages(self, client: Hubspot) -> None:
        landing_page = client.cms.pages.landing_pages.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_languages(self, client: Hubspot) -> None:
        response = client.cms.pages.landing_pages.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_languages(self, client: Hubspot) -> None:
        with client.cms.pages.landing_pages.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLandingPages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                                "breakpoint_styles": {
                                    "foo": {
                                        "hidden": True,
                                        "margin": {},
                                        "padding": {},
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
                        "breakpoint_styles": {
                            "foo": {
                                "hidden": True,
                                "margin": {},
                                "padding": {},
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
                current_state="AUTOMATED",
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
                language="af",
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
                                            "units": "units",
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
                                            "horizontal_side": "horizontalSide",
                                            "vertical_side": "verticalSide",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "flexboxPositioning",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "verticalAlignment",
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
                                    "units": "units",
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
                                    "horizontal_side": "horizontalSide",
                                    "vertical_side": "verticalSide",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "flexboxPositioning",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "verticalAlignment",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list()
        assert_matches_type(AsyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
        assert_matches_type(AsyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(AsyncPage[Page], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(AsyncPage[Page], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach_to_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.clone(
            id="id",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AUTOMATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "af",
                    "layout_sections": {
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
                                                "units": "units",
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
                                                "horizontal_side": "horizontalSide",
                                                "vertical_side": "verticalSide",
                                            },
                                        },
                                        "background_image": {
                                            "background_position": "backgroundPosition",
                                            "background_size": "backgroundSize",
                                            "image_url": "imageUrl",
                                        },
                                        "flexbox_positioning": "flexboxPositioning",
                                        "force_full_width_section": True,
                                        "max_width_section_centering": 0,
                                        "vertical_alignment": "verticalAlignment",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
                            },
                            "type": "type",
                            "w": 0,
                            "x": 0,
                        }
                    },
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "page_redirected": True,
                    "password": "password",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "slug": "slug",
                    "state": "state",
                    "subcategory": "subcategory",
                    "template_path": "templatePath",
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
                        "foo": {
                            "id": 0,
                            "archived_in_dashboard": True,
                            "author_name": "authorName",
                            "campaign": "campaign",
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_folder(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_folder(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_folder(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create_folder(
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_folders_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_folders_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_folders_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create_folders_batch(
            inputs=[
                {
                    "id": "id",
                    "category": 0,
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "deleted_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "name": "name",
                    "parent_folder_id": 0,
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_language_variation(
            id="id",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_language_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete_batch(
            inputs=["string"],
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_folder(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete_folder(
            object_id="objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_folder_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete_folder(
            object_id="objectId",
            archived=True,
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_folder(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.delete_folder(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_folder(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.delete_folder(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_folder(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.delete_folder(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_folders_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.delete_folders_batch(
            inputs=["string"],
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_folders_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.delete_folders_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_folders_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.delete_folders_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.detach_from_lang_group(
            id="id",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach_from_lang_group(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_end_ab_test(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_end_ab_test(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_end_ab_test(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get(
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_draft(
            "objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_folder(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_folder(
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_folder_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_folder(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_folder(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_folder(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_folder(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_folder(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_folder(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_folder(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_folder_revision(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_folder_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(VersionContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_folder_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(VersionContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_folder_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_folder_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_folders_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_folders_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_folders_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_folders_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_folders_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_folders_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_folders_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_folders_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionPage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(VersionPage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(VersionPage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_folder_revisions(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_folder_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_folder_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_folder_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_folder_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.list_folder_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(AsyncPage[VersionContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_folder_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.list_folder_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(AsyncPage[VersionContentFolder], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_folder_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.list_folder_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_folders(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_folders()
        assert_matches_type(AsyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_folders_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_folders(
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
        assert_matches_type(AsyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_folders(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.list_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(AsyncPage[ContentFolder], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_folders(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.list_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(AsyncPage[ContentFolder], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(AsyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(AsyncPage[VersionPage], landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(AsyncPage[VersionPage], landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.publish_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rerun_ab_test(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rerun_ab_test(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rerun_ab_test(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.reset_draft(
            "objectId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_folder_revision(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_folder_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_folder_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.restore_folder_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_folder_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.restore_folder_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.set_new_lang_primary(
            id="id",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponsePage, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponsePage, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
        assert_matches_type(Page, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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
            current_state="AUTOMATED",
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
            language="af",
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
                                        "units": "units",
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
                                        "horizontal_side": "horizontalSide",
                                        "vertical_side": "verticalSide",
                                    },
                                },
                                "background_image": {
                                    "background_position": "backgroundPosition",
                                    "background_size": "backgroundSize",
                                    "image_url": "imageUrl",
                                },
                                "flexbox_positioning": "flexboxPositioning",
                                "force_full_width_section": True,
                                "max_width_section_centering": 0,
                                "vertical_alignment": "verticalAlignment",
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
                                "units": "units",
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
                                "horizontal_side": "horizontalSide",
                                "vertical_side": "verticalSide",
                            },
                        },
                        "background_image": {
                            "background_position": "backgroundPosition",
                            "background_size": "backgroundSize",
                            "image_url": "imageUrl",
                        },
                        "flexbox_positioning": "flexboxPositioning",
                        "force_full_width_section": True,
                        "max_width_section_centering": 0,
                        "vertical_alignment": "verticalAlignment",
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
            assert_matches_type(Page, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
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
                current_state="AUTOMATED",
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
                language="af",
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
                                            "units": "units",
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
                                            "horizontal_side": "horizontalSide",
                                            "vertical_side": "verticalSide",
                                        },
                                    },
                                    "background_image": {
                                        "background_position": "backgroundPosition",
                                        "background_size": "backgroundSize",
                                        "image_url": "imageUrl",
                                    },
                                    "flexbox_positioning": "flexboxPositioning",
                                    "force_full_width_section": True,
                                    "max_width_section_centering": 0,
                                    "vertical_alignment": "verticalAlignment",
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
                                    "units": "units",
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
                                    "horizontal_side": "horizontalSide",
                                    "vertical_side": "verticalSide",
                                },
                            },
                            "background_image": {
                                "background_position": "backgroundPosition",
                                "background_size": "backgroundSize",
                                "image_url": "imageUrl",
                            },
                            "flexbox_positioning": "flexboxPositioning",
                            "force_full_width_section": True,
                            "max_width_section_centering": 0,
                            "vertical_alignment": "verticalAlignment",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_folder(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_folder_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived=True,
        )
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_folder(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(ContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_folder(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update_folder(
            object_id="objectId",
            id="id",
            category=0,
            created=parse_datetime("2019-12-27T18:11:19.117Z"),
            deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            parent_folder_id=0,
            updated=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(ContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_folder(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.landing_pages.with_raw_response.update_folder(
                object_id="",
                id="id",
                category=0,
                created=parse_datetime("2019-12-27T18:11:19.117Z"),
                deleted_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                name="name",
                parent_folder_id=0,
                updated=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_folders_batch(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_folders_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_folders_batch_with_all_params(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_folders_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_folders_batch(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update_folders_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_folders_batch(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update_folders_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert_matches_type(BatchResponseContentFolder, landing_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_languages(self, async_client: AsyncHubspot) -> None:
        landing_page = await async_client.cms.pages.landing_pages.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_languages(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.pages.landing_pages.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        landing_page = await response.parse()
        assert landing_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_languages(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.pages.landing_pages.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            landing_page = await response.parse()
            assert landing_page is None

        assert cast(Any, response.is_closed) is True
