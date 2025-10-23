# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.cms import Page, VersionPage, BatchResponsePage, CollectionResponseWithTotalVersionPage
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSitePages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.create(
            id="id",
            ab_status="master",
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
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.create(
            id="id",
            ab_status="master",
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
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.create(
            id="id",
            ab_status="master",
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

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.update(
                object_id="",
                id="id",
                ab_status="master",
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
    def test_method_list(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.list()
        assert_matches_type(SyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.list(
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
        assert_matches_type(SyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(SyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(SyncPage[Page], site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.delete(
            object_id="objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_attach_to_lang_group_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_attach_to_lang_group(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_attach_to_lang_group(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.clone(
            id="id",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_ab_test_variation(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_ab_test_variation(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_ab_test_variation(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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
        site_page = response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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

            site_page = response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.create_language_variation(
            id="id",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_language_variation_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_language_variation(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_language_variation(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_batch(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.delete_batch(
            inputs=["string"],
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_batch(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_batch(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_detach_from_lang_group(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.detach_from_lang_group(
            id="id",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_detach_from_lang_group(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_detach_from_lang_group(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_end_ab_test(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_end_ab_test(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_end_ab_test(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get(
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get_draft(
            "objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(VersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(VersionPage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.publish_draft(
            "objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rerun_ab_test(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rerun_ab_test(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rerun_ab_test(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.reset_draft(
            "objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision_to_draft(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision_to_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision_to_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision_to_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_schedule(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_new_lang_primary(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.set_new_lang_primary(
            id="id",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_new_lang_primary(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_new_lang_primary(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch_with_all_params(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        site_page = response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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

            site_page = response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.pages.site_pages.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="master",
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
    def test_method_update_languages(self, client: HubSpot) -> None:
        site_page = client.cms.pages.site_pages.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_languages(self, client: HubSpot) -> None:
        response = client.cms.pages.site_pages.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_languages(self, client: HubSpot) -> None:
        with client.cms.pages.site_pages.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSitePages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.create(
            id="id",
            ab_status="master",
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
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.create(
            id="id",
            ab_status="master",
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
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.create(
            id="id",
            ab_status="master",
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

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.update(
            object_id="objectId",
            id="id",
            ab_status="master",
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

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.update(
                object_id="",
                id="id",
                ab_status="master",
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
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.list()
        assert_matches_type(AsyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.list(
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
        assert_matches_type(AsyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(AsyncPage[Page], site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(AsyncPage[Page], site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.delete(
            object_id="objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.delete(
            object_id="objectId",
            archived=True,
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.delete(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_attach_to_lang_group_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
            primary_language="primaryLanguage",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_attach_to_lang_group(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.attach_to_lang_group(
            id="id",
            language="language",
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.clone(
            id="id",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.clone(
            id="id",
            clone_name="cloneName",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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
        site_page = await response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.create_batch(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "master",
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

            site_page = await response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.create_language_variation(
            id="id",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_language_variation_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.create_language_variation(
            id="id",
            language="language",
            primary_language="primaryLanguage",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_language_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.create_language_variation(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_language_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.create_language_variation(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_batch(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.delete_batch(
            inputs=["string"],
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.delete_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.delete_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.detach_from_lang_group(
            id="id",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_detach_from_lang_group(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_end_ab_test(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_end_ab_test(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_end_ab_test(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.end_ab_test(
            ab_test_id="abTestId",
            winner_id="winnerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get(
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.get(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.get(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.get(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get_batch(
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get_batch(
            inputs=["string"],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.get_batch(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.get_batch(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get_draft(
            "objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.get_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.get_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(VersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(VersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.get_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(VersionPage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.get_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.get_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.list_revisions(
            object_id="objectId",
        )
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.list_revisions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.list_revisions(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.list_revisions(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(CollectionResponseWithTotalVersionPage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.list_revisions(
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.publish_draft(
            "objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.publish_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.publish_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.publish_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rerun_ab_test(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rerun_ab_test(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rerun_ab_test(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.rerun_ab_test(
            ab_test_id="abTestId",
            variation_id="variationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.reset_draft(
            "objectId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.restore_revision(
            revision_id="revisionId",
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.restore_revision(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.restore_revision(
                revision_id="",
                object_id="objectId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.set_new_lang_primary(
            id="id",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.set_new_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_new_lang_primary(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.set_new_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update_batch(
            inputs=[{}],
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update_batch(
            inputs=[{}],
            archived=True,
        )
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.update_batch(
            inputs=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert_matches_type(BatchResponsePage, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.update_batch(
            inputs=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert_matches_type(BatchResponsePage, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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
        site_page = await response.parse()
        assert_matches_type(Page, site_page, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="master",
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

            site_page = await response.parse()
            assert_matches_type(Page, site_page, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.pages.site_pages.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="master",
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
    async def test_method_update_languages(self, async_client: AsyncHubSpot) -> None:
        site_page = await async_client.cms.pages.site_pages.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_languages(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.pages.site_pages.with_raw_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site_page = await response.parse()
        assert site_page is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_languages(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.pages.site_pages.with_streaming_response.update_languages(
            languages={"foo": "string"},
            primary_id="primaryId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site_page = await response.parse()
            assert site_page is None

        assert cast(Any, response.is_closed) is True
