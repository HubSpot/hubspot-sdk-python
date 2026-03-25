# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import Hubspot, AsyncHubspot
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = client.cms.blogs.posts.with_raw_response.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.posts.with_streaming_response.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.update(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=0,
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                blog_author_id="blogAuthorId",
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
                enable_google_amp_output_override=True,
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
                password="password",
                post_body="postBody",
                post_summary="postSummary",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                rss_body="rssBody",
                rss_summary="rssSummary",
                slug="slug",
                state="state",
                tag_ids=[0],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.list()
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.list(
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
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = client.cms.blogs.posts.with_raw_response.list()

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.posts.with_streaming_response.list() as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.delete(
            object_id="objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.delete(
            object_id="objectId",
            archived=True,
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.cms.blogs.posts.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.cms.blogs.posts.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_attach_to_lang_group_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_attach_to_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_clone(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.clone(
            id="id",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_clone_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.clone(
            id="id",
            clone_name="cloneName",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_clone(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = client.cms.blogs.posts.with_raw_response.clone(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_clone(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.posts.with_streaming_response.clone(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.create_lang_variation(
            id="id",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_lang_variation_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.create_lang_variation(
            id="id",
            language="language",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.create_lang_variation(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create_lang_variation(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.create_lang_variation(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.detach_from_lang_group(
            id="id",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_detach_from_lang_group(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.get(
            object_id="objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = client.cms.blogs.posts.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = client.cms.blogs.posts.with_raw_response.get(
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.cms.blogs.posts.with_streaming_response.get(
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_draft_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.get_draft_by_id(
            "objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_draft_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.get_draft_by_id(
            "objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_draft_by_id(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.get_draft_by_id(
            "objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_draft_by_id(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.get_draft_by_id(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_previous_version(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.get_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.get_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.get_previous_versions(
            object_id="objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_previous_versions_with_all_params(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.get_previous_versions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.get_previous_versions(
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_previous_versions(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.get_previous_versions(
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_previous_versions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.get_previous_versions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_push_live(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.push_live(
            "objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_push_live(self, client: Hubspot) -> None:
        response = client.cms.blogs.posts.with_raw_response.push_live(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_push_live(self, client: Hubspot) -> None:
        with client.cms.blogs.posts.with_streaming_response.push_live(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_push_live(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.push_live(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.reset_draft(
            "objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: Hubspot) -> None:
        response = client.cms.blogs.posts.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: Hubspot) -> None:
        with client.cms.blogs.posts.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.reset_draft(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_restore_previous_version(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_restore_previous_version(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.restore_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.restore_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_restore_previous_version_to_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_restore_previous_version_to_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_restore_previous_version_to_draft(
        self, client: Hubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_restore_previous_version_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.restore_previous_version_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: Hubspot) -> None:
        response = client.cms.blogs.posts.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: Hubspot) -> None:
        with client.cms.blogs.posts.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_lang_primary(self, client: Hubspot) -> None:
        post = client.cms.blogs.posts.set_lang_primary(
            id="id",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_lang_primary(self, client: Hubspot) -> None:
        response = client.cms.blogs.posts.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_lang_primary(self, client: Hubspot) -> None:
        with client.cms.blogs.posts.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_draft(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            client.cms.blogs.posts.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=0,
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                blog_author_id="blogAuthorId",
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
                enable_google_amp_output_override=True,
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
                password="password",
                post_body="postBody",
                post_summary="postSummary",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                rss_body="rssBody",
                rss_summary="rssSummary",
                slug="slug",
                state="state",
                tag_ids=[0],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = client.cms.blogs.posts.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert post.is_closed
        assert post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = client.cms.blogs.posts.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert post.json() == {"foo": "bar"}
        assert isinstance(post, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update_langs(self, client: Hubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.with_streaming_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, StreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True


class TestAsyncPosts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = await async_client.cms.blogs.posts.with_raw_response.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.posts.with_streaming_response.create(
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.update(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.update(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=0,
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                blog_author_id="blogAuthorId",
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
                enable_google_amp_output_override=True,
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
                password="password",
                post_body="postBody",
                post_summary="postSummary",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                rss_body="rssBody",
                rss_summary="rssSummary",
                slug="slug",
                state="state",
                tag_ids=[0],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.list()
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.list(
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
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = await async_client.cms.blogs.posts.with_raw_response.list()

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.posts.with_streaming_response.list() as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.delete(
            object_id="objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.delete(
            object_id="objectId",
            archived=True,
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.posts.with_raw_response.delete(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.posts.with_streaming_response.delete(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.delete(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_attach_to_lang_group_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
            primary_language="aa",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_attach_to_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_attach_to_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/attach-to-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.attach_to_lang_group(
            id="id",
            language="aa",
            primary_id="primaryId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_clone(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.clone(
            id="id",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_clone_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.clone(
            id="id",
            clone_name="cloneName",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_clone(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = await async_client.cms.blogs.posts.with_raw_response.clone(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_clone(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/clone").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.posts.with_streaming_response.clone(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.create_lang_variation(
            id="id",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_lang_variation_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.create_lang_variation(
            id="id",
            language="language",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create_lang_variation(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.create_lang_variation(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create_lang_variation(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/create-language-variation").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.create_lang_variation(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_detach_from_lang_group(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.detach_from_lang_group(
            id="id",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.detach_from_lang_group(
            id="id",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_detach_from_lang_group(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/detach-from-lang-group").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.detach_from_lang_group(
            id="id",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.get(
            object_id="objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        post = await async_client.cms.blogs.posts.get(
            object_id="objectId",
            archived=True,
            property="property",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        post = await async_client.cms.blogs.posts.with_raw_response.get(
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.cms.blogs.posts.with_streaming_response.get(
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.get(
                object_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_draft_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.get_draft_by_id(
            "objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_draft_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.get_draft_by_id(
            "objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_draft_by_id(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.get_draft_by_id(
            "objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_draft_by_id(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.get_draft_by_id(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions/revisionId").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.get_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_previous_version(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.get_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.get_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_versions(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.get_previous_versions(
            object_id="objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_previous_versions_with_all_params(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.get_previous_versions(
            object_id="objectId",
            after="after",
            before="before",
            limit=0,
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_previous_versions(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.get_previous_versions(
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_previous_versions(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/blogs/2026-03/posts/objectId/revisions").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.get_previous_versions(
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_previous_versions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.get_previous_versions(
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_push_live(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.push_live(
            "objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_push_live(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.posts.with_raw_response.push_live(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_push_live(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.posts.with_streaming_response.push_live(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_push_live(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.push_live(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.reset_draft(
            "objectId",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.posts.with_raw_response.reset_draft(
            "objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.posts.with_streaming_response.reset_draft(
            "objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.reset_draft(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_restore_previous_version(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_restore_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_restore_previous_version(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/revisionId/restore").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.restore_previous_version(
            revision_id="revisionId",
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_restore_previous_version(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.restore_previous_version(
                revision_id="revisionId",
                object_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.restore_previous_version(
                revision_id="",
                object_id="objectId",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_restore_previous_version_to_draft(
        self, async_client: AsyncHubspot, respx_mock: MockRouter
    ) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/objectId/revisions/0/restore-to-draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.restore_previous_version_to_draft(
            revision_id=0,
            object_id="objectId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_restore_previous_version_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.restore_previous_version_to_draft(
                revision_id=0,
                object_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.posts.with_raw_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.posts.with_streaming_response.schedule(
            id="id",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        post = await async_client.cms.blogs.posts.set_lang_primary(
            id="id",
        )
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        response = await async_client.cms.blogs.posts.with_raw_response.set_lang_primary(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert post is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_lang_primary(self, async_client: AsyncHubspot) -> None:
        async with async_client.cms.blogs.posts.with_streaming_response.set_lang_primary(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert post is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_draft(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_draft(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_draft(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.patch("/cms/blogs/2026-03/posts/objectId/draft").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.update_draft(
            object_id="objectId",
            id="id",
            ab_status="automated_loser_variant",
            ab_test_id="abTestId",
            archived_at=0,
            archived_in_dashboard=True,
            attached_stylesheets=[{"foo": {}}],
            author_name="authorName",
            blog_author_id="blogAuthorId",
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
            enable_google_amp_output_override=True,
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
            password="password",
            post_body="postBody",
            post_summary="postSummary",
            public_access_rules=[{}],
            public_access_rules_enabled=True,
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            publish_immediately=True,
            rss_body="rssBody",
            rss_summary="rssSummary",
            slug="slug",
            state="state",
            tag_ids=[0],
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
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_id` but received ''"):
            await async_client.cms.blogs.posts.with_raw_response.update_draft(
                object_id="",
                id="id",
                ab_status="automated_loser_variant",
                ab_test_id="abTestId",
                archived_at=0,
                archived_in_dashboard=True,
                attached_stylesheets=[{"foo": {}}],
                author_name="authorName",
                blog_author_id="blogAuthorId",
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
                enable_google_amp_output_override=True,
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
                password="password",
                post_body="postBody",
                post_summary="postSummary",
                public_access_rules=[{}],
                public_access_rules_enabled=True,
                publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                publish_immediately=True,
                rss_body="rssBody",
                rss_summary="rssSummary",
                slug="slug",
                state="state",
                tag_ids=[0],
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

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        post = await async_client.cms.blogs.posts.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )
        assert post.is_closed
        assert await post.json() == {"foo": "bar"}
        assert cast(Any, post.is_closed) is True
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        post = await async_client.cms.blogs.posts.with_raw_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        )

        assert post.is_closed is True
        assert post.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await post.json() == {"foo": "bar"}
        assert isinstance(post, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update_langs(self, async_client: AsyncHubspot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/multi-language/update-languages").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.with_streaming_response.update_langs(
            languages={"foo": "aa"},
            primary_id="primaryId",
        ) as post:
            assert not post.is_closed
            assert post.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await post.json() == {"foo": "bar"}
            assert cast(Any, post.is_closed) is True
            assert isinstance(post, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, post.is_closed) is True
