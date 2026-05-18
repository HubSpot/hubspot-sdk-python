# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.posts.batch.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.posts.batch.with_raw_response.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.batch.with_streaming_response.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.posts.batch.update(
            inputs=[{}],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.posts.batch.update(
            inputs=[{}],
            archived=True,
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.posts.batch.with_raw_response.update(
            inputs=[{}],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.batch.with_streaming_response.update(
            inputs=[{}],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        batch = client.cms.blogs.posts.batch.delete(
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.cms.blogs.posts.batch.with_raw_response.delete(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.cms.blogs.posts.batch.with_streaming_response.delete(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.posts.batch.get(
            inputs=["string"],
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = client.cms.blogs.posts.batch.get(
            inputs=["string"],
            archived=True,
        )
        assert batch.is_closed
        assert batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = client.cms.blogs.posts.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert batch.json() == {"foo": "bar"}
        assert isinstance(batch, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.blogs.posts.batch.with_streaming_response.get(
            inputs=["string"],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, StreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.posts.batch.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.posts.batch.with_raw_response.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/create").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.batch.with_streaming_response.create(
            inputs=[
                {
                    "id": "id",
                    "ab_status": "automated_loser_variant",
                    "ab_test_id": "abTestId",
                    "archived_at": 0,
                    "archived_in_dashboard": True,
                    "attached_stylesheets": [{"foo": {}}],
                    "author_name": "authorName",
                    "blog_author_id": "blogAuthorId",
                    "campaign": "campaign",
                    "category_id": 0,
                    "content_group_id": "contentGroupId",
                    "content_type_category": "0",
                    "created": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "created_by_id": "createdById",
                    "currently_published": True,
                    "current_state": "AGENT_GENERATED",
                    "domain": "domain",
                    "dynamic_page_data_source_id": "dynamicPageDataSourceId",
                    "dynamic_page_data_source_type": 0,
                    "dynamic_page_hub_db_table_id": "dynamicPageHubDbTableId",
                    "enable_domain_stylesheets": True,
                    "enable_google_amp_output_override": True,
                    "enable_layout_stylesheets": True,
                    "featured_image": "featuredImage",
                    "featured_image_alt_text": "featuredImageAltText",
                    "folder_id": "folderId",
                    "footer_html": "footerHtml",
                    "head_html": "headHtml",
                    "html_title": "htmlTitle",
                    "include_default_custom_css": True,
                    "language": "aa",
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
                    "link_rel_canonical_url": "linkRelCanonicalUrl",
                    "mab_experiment_id": "mabExperimentId",
                    "meta_description": "metaDescription",
                    "name": "name",
                    "page_expiry_date": 0,
                    "page_expiry_enabled": True,
                    "page_expiry_redirect_id": 0,
                    "page_expiry_redirect_url": "pageExpiryRedirectUrl",
                    "password": "password",
                    "post_body": "postBody",
                    "post_summary": "postSummary",
                    "public_access_rules": [{}],
                    "public_access_rules_enabled": True,
                    "publish_date": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "publish_immediately": True,
                    "rss_body": "rssBody",
                    "rss_summary": "rssSummary",
                    "slug": "slug",
                    "state": "state",
                    "tag_ids": [0],
                    "theme_settings_values": {"foo": {}},
                    "translated_from_id": "translatedFromId",
                    "translations": {
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
                    "updated": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "updated_by_id": "updatedById",
                    "url": "url",
                    "use_featured_image": True,
                    "widget_containers": {"foo": {}},
                    "widgets": {"foo": {}},
                }
            ],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.posts.batch.update(
            inputs=[{}],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.posts.batch.update(
            inputs=[{}],
            archived=True,
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.posts.batch.with_raw_response.update(
            inputs=[{}],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/update").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.batch.with_streaming_response.update(
            inputs=[{}],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.cms.blogs.posts.batch.delete(
            inputs=["string"],
        )
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.blogs.posts.batch.with_raw_response.delete(
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert batch is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.blogs.posts.batch.with_streaming_response.delete(
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert batch is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.posts.batch.get(
            inputs=["string"],
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        batch = await async_client.cms.blogs.posts.batch.get(
            inputs=["string"],
            archived=True,
        )
        assert batch.is_closed
        assert await batch.json() == {"foo": "bar"}
        assert cast(Any, batch.is_closed) is True
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        batch = await async_client.cms.blogs.posts.batch.with_raw_response.get(
            inputs=["string"],
        )

        assert batch.is_closed is True
        assert batch.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await batch.json() == {"foo": "bar"}
        assert isinstance(batch, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.post("/cms/blogs/2026-03/posts/batch/read").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.blogs.posts.batch.with_streaming_response.get(
            inputs=["string"],
        ) as batch:
            assert not batch.is_closed
            assert batch.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await batch.json() == {"foo": "bar"}
            assert cast(Any, batch.is_closed) is True
            assert isinstance(batch, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, batch.is_closed) is True
