# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import Hubspot, AsyncHubspot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.pagination import SyncPage, AsyncPage
from hubspot_sdk.types.marketing import (
    PublicEmail,
    VersionPublicEmail,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Hubspot) -> None:
        email = client.marketing.emails.create(
            name="My subject",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.create(
            name="My subject",
            active_domain="test.hs-sites.com",
            archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            feedback_survey_id="feedbackSurveyId",
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.create(
            name="My subject",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.create(
            name="My subject",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Hubspot) -> None:
        email = client.marketing.emails.update(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.update(
            email_id="emailId",
            query_archived=True,
            active_domain="test.hs-sites.com",
            body_archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            name="My subject",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.update(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.update(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.update(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Hubspot) -> None:
        email = client.marketing.emails.list()
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Hubspot) -> None:
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
            sort=["string"],
            type="AB_EMAIL",
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            workflow_names=True,
        )
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncPage[PublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Hubspot) -> None:
        email = client.marketing.emails.delete(
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.delete(
            email_id="emailId",
            archived=True,
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.delete(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.delete(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.delete(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone(self, client: Hubspot) -> None:
        email = client.marketing.emails.clone(
            id="id",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.clone(
            id="id",
            clone_name="cloneName",
            language="language",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_ab_test_variation(self, client: Hubspot) -> None:
        email = client.marketing.emails.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_ab_test_variation(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_ab_test_variation(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: Hubspot) -> None:
        email = client.marketing.emails.get(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.get(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.get(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.get(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_ab_test_variation(self, client: Hubspot) -> None:
        email = client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_ab_test_variation_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_ab_test_variation(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.get_ab_test_variation(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_ab_test_variation(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.get_ab_test_variation(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_ab_test_variation(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get_ab_test_variation(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: Hubspot) -> None:
        email = client.marketing.emails.get_draft(
            "emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.get_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.get_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_revision(self, client: Hubspot) -> None:
        email = client.marketing.emails.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert_matches_type(VersionPublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_revision(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(VersionPublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_revision(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(VersionPublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_revision(self, client: Hubspot) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions(self, client: Hubspot) -> None:
        email = client.marketing.emails.list_revisions(
            email_id="emailId",
        )
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_revisions_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.list_revisions(
            email_id="emailId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_revisions(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.list_revisions(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_revisions(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.list_revisions(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(SyncPage[VersionPublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_revisions(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.list_revisions(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish(self, client: Hubspot) -> None:
        email = client.marketing.emails.publish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.publish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.publish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.publish(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: Hubspot) -> None:
        email = client.marketing.emails.reset_draft(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.reset_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.reset_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision(self, client: Hubspot) -> None:
        email = client.marketing.emails.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision(self, client: Hubspot) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_revision_to_draft(self, client: Hubspot) -> None:
        email = client.marketing.emails.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_revision_to_draft(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_revision_to_draft(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_revision_to_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish(self, client: Hubspot) -> None:
        email = client.marketing.emails.unpublish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unpublish(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.unpublish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unpublish(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.unpublish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unpublish(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.unpublish(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: Hubspot) -> None:
        email = client.marketing.emails.update_draft(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_with_all_params(self, client: Hubspot) -> None:
        email = client.marketing.emails.update_draft(
            email_id="emailId",
            active_domain="test.hs-sites.com",
            archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            name="My subject",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: Hubspot) -> None:
        response = client.marketing.emails.with_raw_response.update_draft(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: Hubspot) -> None:
        with client.marketing.emails.with_streaming_response.update_draft(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: Hubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            client.marketing.emails.with_raw_response.update_draft(
                email_id="",
            )


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.create(
            name="My subject",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.create(
            name="My subject",
            active_domain="test.hs-sites.com",
            archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            feedback_survey_id="feedbackSurveyId",
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.create(
            name="My subject",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.create(
            name="My subject",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.update(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.update(
            email_id="emailId",
            query_archived=True,
            active_domain="test.hs-sites.com",
            body_archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            name="My subject",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.update(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.update(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.update(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.list()
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubspot) -> None:
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
            sort=["string"],
            type="AB_EMAIL",
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            workflow_names=True,
        )
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncPage[PublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.delete(
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.delete(
            email_id="emailId",
            archived=True,
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.delete(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.delete(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.delete(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.clone(
            id="id",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.clone(
            id="id",
            clone_name="cloneName",
            language="language",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.create_ab_test_variation(
            content_id="contentId",
            variation_name="variationName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_ab_test_variation_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get_ab_test_variation(
            email_id="emailId",
            archived=True,
            included_properties=["string"],
            include_stats=True,
            marketing_campaign_names=True,
            workflow_names=True,
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_ab_test_variation(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_ab_test_variation(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_ab_test_variation(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_ab_test_variation(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get_draft(
            "emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.get_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_revision(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert_matches_type(VersionPublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(VersionPublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.get_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(VersionPublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_revision(self, async_client: AsyncHubspot) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.list_revisions(
            email_id="emailId",
        )
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_revisions_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.list_revisions(
            email_id="emailId",
            after="after",
            before="before",
            limit=0,
        )
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.list_revisions(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_revisions(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.list_revisions(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(AsyncPage[VersionPublicEmail], email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_revisions(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.list_revisions(
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.publish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.publish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.publish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.publish(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.reset_draft(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.reset_draft(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.reset_draft(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.reset_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.restore_revision(
            revision_id="revisionId",
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision(self, async_client: AsyncHubspot) -> None:
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.restore_revision_to_draft(
            revision_id=0,
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_revision_to_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.restore_revision_to_draft(
                revision_id=0,
                email_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.unpublish(
            "emailId",
        )
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.unpublish(
            "emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert email is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.unpublish(
            "emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert email is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unpublish(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.unpublish(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.update_draft(
            email_id="emailId",
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_with_all_params(self, async_client: AsyncHubspot) -> None:
        email = await async_client.marketing.emails.update_draft(
            email_id="emailId",
            active_domain="test.hs-sites.com",
            archived=False,
            business_unit_id=0,
            campaign="1b7f51a6-33c1-44d6-ba28-fe81f655dced",
            content={
                "flex_areas": {"main": {}},
                "plain_text_version": "This is custom! View in browser ({{view_as_page_url}})\n\nHello {{ contact.firstname }},\n\nPlain text emails have minimal formatting so your reader can really focus on what you have to say. Introduce yourself and explain why you’re reaching out.\n\nEvery email should try to lead the reader to some kind of action. Use this space to describe why the reader should want to click on the link below. Put the link on its own line to really draw their eye to it.\n\nLink text\n\nNow it’s time to wrap up your email. Before your signature, thank the recipient for reading. You can also invite them to send this email to any of their colleagues who might be interested.\n\nAll the best,\n\nYour full name\n\nYour job title\n\nOther contact information\n\n{{site_settings.company_name}}, {{site_settings.company_street_address_1}}, {{site_settings.company_street_address_2}}, {{site_settings.company_city}}, {{site_settings.company_state}} {{site_settings.company_zip}}, {{site_settings.company_country}}, {{site_settings.company_phone}}\n\nUnsubscribe ({{unsubscribe_link_all}})\n\nManage preferences ({{unsubscribe_link}})",
                "smart_fields": {"foo": {}},
                "style_settings": {
                    "background_color": "backgroundColor",
                    "background_image": "backgroundImage",
                    "background_image_type": "backgroundImageType",
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
                "widgets": {
                    "module-0-1-1": {},
                    "module-1-1-1": {},
                    "module_160676180617911": {},
                    "preview_text": {},
                },
            },
            folder_id_v2=0,
            from_={
                "custom_reply_to": "customReplyTo",
                "from_name": "Bruce Wayne",
                "reply_to": "test@hubspot.com",
            },
            jitter_send_time=True,
            language="af",
            name="My subject",
            publish_date=parse_datetime("2023-11-30T18:44:20.387Z"),
            rss_data={
                "blog_email_type": "blogEmailType",
                "blog_image_max_width": 0,
                "blog_layout": "blogLayout",
                "hubspot_blog_id": "hubspotBlogId",
                "max_entries": 0,
                "rss_entry_template": "rssEntryTemplate",
                "timing": {"foo": {}},
                "url": "url",
                "use_headline_as_subject": True,
            },
            send_on_publish=True,
            state="DRAFT",
            subcategory="batch",
            subject="My subject",
            subscription_details={
                "office_location_id": "5449392956",
                "preferences_group_id": "preferencesGroupId",
                "subscription_id": "subscriptionId",
                "subscription_name": "subscriptionName",
            },
            testing={
                "ab_sample_size_default": "master",
                "ab_sampling_default": "master",
                "ab_status": "master",
                "ab_success_metric": "CLICKS_BY_OPENS",
                "ab_test_percentage": 0,
                "hours_to_wait": 0,
                "is_ab_variation": True,
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
                "expires_at": parse_datetime("2020-11-30T18:44:20.387Z"),
                "is_page_redirected": True,
                "meta_description": "",
                "page_expiry_enabled": True,
                "redirect_to_page_id": "redirectToPageId",
                "redirect_to_url": "http://www.example.org",
                "slug": "slug",
                "title": "title",
                "url": "url",
            },
        )
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubspot) -> None:
        response = await async_client.marketing.emails.with_raw_response.update_draft(
            email_id="emailId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(PublicEmail, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubspot) -> None:
        async with async_client.marketing.emails.with_streaming_response.update_draft(
            email_id="emailId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(PublicEmail, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubspot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `email_id` but received ''"):
            await async_client.marketing.emails.with_raw_response.update_draft(
                email_id="",
            )
