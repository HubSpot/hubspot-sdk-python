# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import (
    PublicEmail,
    PublicEmailVersion,
    VersionPublicEmail,
    AggregateEmailStatistics,
    CollectionResponseWithTotalEmailStatisticInterval,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        email = client.marketing.emails.create()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.create(
            active_domain="activeDomain",
            archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            feedback_survey_id="feedbackSurveyId",
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        email = client.marketing.emails.update(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.update(
            email_id="emailId",
            query_archived=True,
            active_domain="activeDomain",
            body_archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.update(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.update(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.update(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        email = client.marketing.emails.list()
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.list(
            after="after",
            archived=True,
            campaign="campaign",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            included_properties=["string"],
            include_stats=True,
            is_published=True,
            limit=0,
            marketing_campaign_names=True,
            published_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
            type="AB_EMAIL",
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            variant_stats=True,
            workflow_names=True,
        )
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        email = client.marketing.emails.delete(
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.delete(
            email_id="emailId",
            archived=True,
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.delete(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.delete(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.delete(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: HubSpot) -> None:
        email = client.marketing.emails.clone(
            id="id",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.clone(
            id="id",
            clone_name="cloneName",
            language="language",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_ab_test_variation(self, client: HubSpot) -> None:
        email = client.marketing.emails.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_ab_test_variation(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_ab_test_variation(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        email = client.marketing.emails.get()
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.get(
            email_ids=[0],
            end_timestamp="endTimestamp",
            property="property",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(AggregateEmailStatistics, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_ab_test_variation(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_ab_test_variation_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            variant_stats=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_ab_test_variation(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.get_ab_test_variation(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_ab_test_variation(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.get_ab_test_variation(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_ab_test_variation(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get_ab_test_variation(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_draft(
            "emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.get_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.get_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_histogram(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_histogram()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_histogram_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_histogram(
            email_ids=[0],
            end_timestamp="endTimestamp",
            interval="DAY",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_histogram(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.get_histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_histogram(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.get_histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: HubSpot) -> None:
        email = client.marketing.emails.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert_matches_type(PublicEmailVersion, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmailVersion, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmailVersion, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get_revision(
                revision_id="revisionId",
                email_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.marketing.emails.with_raw_response.get_revision(
                revision_id="",
                email_id="emailId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: HubSpot) -> None:
        email = client.marketing.emails.list_revisions(
            email_id="emailId",
        )
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.list_revisions(
            email_id="emailId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.list_revisions(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.list_revisions(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.list_revisions(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: HubSpot) -> None:
        email = client.marketing.emails.publish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.publish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.publish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.publish(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: HubSpot) -> None:
        email = client.marketing.emails.reset_draft(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.reset_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.reset_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_revision(self, client: HubSpot) -> None:
        email = client.marketing.emails.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_revision(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_revision(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.restore_revision(
                revision_id="revisionId",
                email_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.marketing.emails.with_raw_response.restore_revision(
                revision_id="",
                email_id="emailId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_revision_to_draft(self, client: HubSpot) -> None:
        email = client.marketing.emails.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_revision_to_draft(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision_to_draft(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_revision_to_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpublish(self, client: HubSpot) -> None:
        email = client.marketing.emails.unpublish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpublish(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.unpublish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpublish(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.unpublish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpublish(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.unpublish(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        email = client.marketing.emails.update_draft(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_draft_with_all_params(self, client: HubSpot) -> None:
        email = client.marketing.emails.update_draft(
            email_id="emailId",
            active_domain="activeDomain",
            archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.marketing.emails.with_raw_response.update_draft(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.marketing.emails.with_streaming_response.update_draft(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.update_draft(
                email_id="",
            )


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.create()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.create(
            active_domain="activeDomain",
            archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            feedback_survey_id="feedbackSurveyId",
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.update(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.update(
            email_id="emailId",
            query_archived=True,
            active_domain="activeDomain",
            body_archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.update(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.update(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.update(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.list()
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.list(
            after="after",
            archived=True,
            campaign="campaign",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            included_properties=["string"],
            include_stats=True,
            is_published=True,
            limit=0,
            marketing_campaign_names=True,
            published_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            sort=["string"],
            type="AB_EMAIL",
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            variant_stats=True,
            workflow_names=True,
        )
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.delete(
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.delete(
            email_id="emailId",
            archived=True,
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.delete(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.delete(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.delete(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.clone(
            id="id",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.clone(
            id="id",
            clone_name="cloneName",
            language="language",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get()
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get(
            email_ids=[0],
            end_timestamp="endTimestamp",
            property="property",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AggregateEmailStatistics, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AggregateEmailStatistics, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_ab_test_variation_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            variant_stats=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_ab_test_variation(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_ab_test_variation(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_ab_test_variation(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_ab_test_variation(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_draft(
            "emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_histogram(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_histogram()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_histogram_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_histogram(
            email_ids=[0],
            end_timestamp="endTimestamp",
            interval="DAY",
            start_timestamp="startTimestamp",
        )
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_histogram(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_histogram()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_histogram(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_histogram() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(CollectionResponseWithTotalEmailStatisticInterval, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert_matches_type(PublicEmailVersion, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmailVersion, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmailVersion, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_revision(
                revision_id="revisionId",
                email_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_revision(
                revision_id="",
                email_id="emailId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.list_revisions(
            email_id="emailId",
        )
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.list_revisions(
            email_id="emailId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.list_revisions(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.list_revisions(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.list_revisions(
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.publish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.publish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.publish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.publish(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.reset_draft(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.reset_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.reset_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_revision(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_revision(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.restore_revision(
                revision_id="revisionId",
                email_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.restore_revision(
                revision_id="",
                email_id="emailId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_revision_to_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                email_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpublish(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.unpublish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.unpublish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.unpublish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpublish(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.unpublish(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.update_draft(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        email = await async_client.marketing.emails.update_draft(
            email_id="emailId",
            active_domain="activeDomain",
            archived=True,
            business_unit_id=0,
            campaign="campaign",
            content={
                "flex_areas": {"foo": {}},
                "plain_text_version": "plainTextVersion",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "REPEAT",
                    "body_border_color": "bodyBorderColor",
                    "body_border_color_choice": "bodyBorderColorChoice",
                    "body_border_width": 0,
                    "body_color": "bodyColor",
                    "button_style_settings": {
                        "background_color": {},
                        "corner_radius": 0,
                        "font_style": {
                            "bold": True,
                            "color": "color",
                            "font": "font",
                            "italic": True,
                            "size": 0,
                            "underline": True,
                        },
                    },
                    "color_picker_favorite1": "colorPickerFavorite1",
                    "color_picker_favorite2": "colorPickerFavorite2",
                    "color_picker_favorite3": "colorPickerFavorite3",
                    "color_picker_favorite4": "colorPickerFavorite4",
                    "color_picker_favorite5": "colorPickerFavorite5",
                    "color_picker_favorite6": "colorPickerFavorite6",
                    "divider_style_settings": {
                        "color": {},
                        "height": 0,
                        "line_type": "lineType",
                    },
                    "email_body_padding": "emailBodyPadding",
                    "email_body_width": "emailBodyWidth",
                    "heading_one_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "heading_two_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "links_font": {
                        "bold": True,
                        "color": "color",
                        "font": "font",
                        "italic": True,
                        "size": 0,
                        "underline": True,
                    },
                    "primary_accent_color": "primaryAccentColor",
                    "primary_font": "primaryFont",
                    "primary_font_color": "primaryFontColor",
                    "primary_font_line_height": "primaryFontLineHeight",
                    "primary_font_size": 0,
                    "secondary_accent_color": "secondaryAccentColor",
                    "secondary_font": "secondaryFont",
                    "secondary_font_color": "secondaryFontColor",
                    "secondary_font_line_height": "secondaryFontLineHeight",
                    "secondary_font_size": 0,
                },
                "template_path": "templatePath",
                "theme_settings_values": {"foo": {}},
                "widget_containers": {"foo": {}},
                "widgets": {"foo": {}},
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "fromName",
                "reply_to": "replyTo",
            },
            jitter_send_time=True,
            language="aa",
            name="name",
            publish_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "FULL_POST",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="AGENT_GENERATED",
            subcategory="ab_loser_variant",
            subject="subject",
            subscription_details={
                "office_location_id": "officeLocationId",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "is_ab_variation": True,
                "ab_sample_size_default": "automated_loser_variant",
                "ab_sampling_default": "automated_loser_variant",
                "ab_status": "automated_loser_variant",
                "ab_success_metric": "CLICKS_BY_DELIVERED",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "test_id": "testId",
            },
            to={
                "contact_ids": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_ils_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "contact_lists": {
                    "exclude": ["string"],
                    "include": ["string"],
                },
                "limit_send_frequency": True,
                "suppress_graymail": True,
            },
            webversion={
                "domain": "domain",
                "enabled": True,
                "expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "is_page_redirected": True,
                "meta_description": "metaDescription",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "redirectToUrl",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.emails.with_raw_response.update_draft(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.emails.with_streaming_response.update_draft(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.update_draft(
                email_id="",
            )
