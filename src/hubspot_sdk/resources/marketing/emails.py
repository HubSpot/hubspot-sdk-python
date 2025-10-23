# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.marketing import (
    email_list_params,
    email_read_params,
    email_clone_params,
    email_create_params,
    email_delete_params,
    email_update_params,
    email_upsert_draft_params,
    email_get_histogram_params,
    email_get_revisions_params,
    email_get_emails_list_params,
    email_create_ab_test_variation_params,
)
from ...types.marketing.public_email import PublicEmail
from ...types.marketing.version_public_email import VersionPublicEmail
from ...types.marketing.aggregate_email_statistics import AggregateEmailStatistics
from ...types.marketing.public_email_content_param import PublicEmailContentParam
from ...types.marketing.public_email_to_details_param import PublicEmailToDetailsParam
from ...types.marketing.public_rss_email_details_param import PublicRssEmailDetailsParam
from ...types.marketing.public_email_from_details_param import PublicEmailFromDetailsParam
from ...types.marketing.public_webversion_details_param import PublicWebversionDetailsParam
from ...types.marketing.public_email_testing_details_param import PublicEmailTestingDetailsParam
from ...types.marketing.public_email_subscription_details_param import PublicEmailSubscriptionDetailsParam
from ...types.marketing.collection_response_with_total_email_statistic_interval_no_paging import (
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
)

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        active_domain: str | Omit = omit,
        archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        feedback_survey_id: str | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Use this endpoint to create a new marketing email.

        Args:
          name: The name of the email, as displayed on the email dashboard.

          active_domain: The active domain of the email.

          archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          feedback_survey_id: The ID of the feedback survey linked to the email.

          from_: Data structure representing the from fields on the email.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/emails/",
            body=maybe_transform(
                {
                    "name": name,
                    "active_domain": active_domain,
                    "archived": archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "feedback_survey_id": feedback_survey_id,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def update(
        self,
        email_id: str,
        *,
        query_archived: bool | Omit = omit,
        active_domain: str | Omit = omit,
        body_archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Change properties of a marketing email.

        Args:
          query_archived: Whether to return only results that have been archived.

          active_domain: The active domain of the email.

          body_archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          from_: Data structure representing the from fields on the email.

          name: The name of the email, as displayed on the email dashboard.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._patch(
            f"/marketing/v3/emails/{email_id}",
            body=maybe_transform(
                {
                    "active_domain": active_domain,
                    "body_archived": body_archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "name": name,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_update_params.EmailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_archived": query_archived}, email_update_params.EmailUpdateParams),
            ),
            cast_to=PublicEmail,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        campaign: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        included_properties: SequenceNotStr[str] | Omit = omit,
        include_stats: bool | Omit = omit,
        is_published: bool | Omit = omit,
        limit: int | Omit = omit,
        marketing_campaign_names: bool | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: Literal[
            "AB_EMAIL",
            "BATCH_EMAIL",
            "LOCALTIME_EMAIL",
            "AUTOMATED_AB_EMAIL",
            "BLOG_EMAIL",
            "BLOG_EMAIL_CHILD",
            "RSS_EMAIL",
            "RSS_EMAIL_CHILD",
            "RESUBSCRIBE_EMAIL",
            "OPTIN_EMAIL",
            "OPTIN_FOLLOWUP_EMAIL",
            "AUTOMATED_EMAIL",
            "FEEDBACK_CES_EMAIL",
            "FEEDBACK_CUSTOM_EMAIL",
            "FEEDBACK_CUSTOM_SURVEY_EMAIL",
            "FEEDBACK_NPS_EMAIL",
            "FOLLOWUP_EMAIL",
            "LEADFLOW_EMAIL",
            "SINGLE_SEND_API",
            "MARKETING_SINGLE_SEND_API",
            "SMTP_TOKEN",
            "TICKET_EMAIL",
            "MEMBERSHIP_REGISTRATION_EMAIL",
            "MEMBERSHIP_PASSWORD_SAVED_EMAIL",
            "MEMBERSHIP_PASSWORD_RESET_EMAIL",
            "MEMBERSHIP_EMAIL_VERIFICATION_EMAIL",
            "MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL",
            "MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL",
            "MEMBERSHIP_OTP_LOGIN_EMAIL",
            "MEMBERSHIP_FOLLOW_UP_EMAIL",
            "MEMBERSHIP_VERIFICATION_EMAIL",
        ]
        | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        workflow_names: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PublicEmail]:
        """The results can be filtered, allowing you to find a specific set of emails.

        See
        the table below for a full list of filtering options.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived emails. Defaults to `false`.

          campaign: Filter by campaign GUID. All emails will be returned if not present.

          created_after: Only return emails created after the specified time.

          created_at: Only return emails created at exactly the specified time.

          created_before: Only return emails created before the specified time.

          included_properties: Limit the response to only include this specified list of properties.

          include_stats: Include statistics with emails.

          is_published: Filter by published/draft emails. All emails will be returned if not present.

          limit: The maximum number of results to return. Default is 10.

          marketing_campaign_names: Include the names for any associated marketing campaigns.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          type: Email types to be filtered by. Multiple types can be included. All emails will
              be returned if not present.

          updated_after: Only return emails last updated after the specified time.

          updated_at: Only return emails last updated at exactly the specified time.

          updated_before: Only return emails last updated before the specified time.

          workflow_names: Include the names of any workflows associated with the returned emails.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/v3/emails/",
            page=SyncPage[PublicEmail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "campaign": campaign,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "included_properties": included_properties,
                        "include_stats": include_stats,
                        "is_published": is_published,
                        "limit": limit,
                        "marketing_campaign_names": marketing_campaign_names,
                        "sort": sort,
                        "type": type,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                        "workflow_names": workflow_names,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            model=PublicEmail,
        )

    def delete(
        self,
        email_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a marketing email by its ID

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/marketing/v3/emails/{email_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, email_delete_params.EmailDeleteParams),
            ),
            cast_to=NoneType,
        )

    def clone(
        self,
        *,
        id: str,
        clone_name: str | Omit = omit,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        This will create a duplicate email with the same properties as the original,
        with the exception of a unique ID.

        Args:
          id: The unique identifier of the email to be cloned.

          clone_name: The name to assign to the cloned email.

          language: The language code for the cloned email, such as 'en' for English.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/emails/clone",
            body=maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                    "language": language,
                },
                email_clone_params.EmailCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def create_ab_test_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Create a variation of a marketing email for an A/B test.

        The new variation will
        be created as a draft. If an active variation already exists, a new one won't be
        created.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/marketing/v3/emails/ab-test/create-variation",
            body=maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                email_create_ab_test_variation_params.EmailCreateAbTestVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def get_ab_test_variation(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """This endpoint lets you obtain the variation of an A/B marketing email.

        If the
        email is variation A (master) it will return variation B (variant) and vice
        versa.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get(
            f"/marketing/v3/emails/{email_id}/ab-test/get-variation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def get_draft(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Get the draft version of an email (if it exists).

        If no draft version exists,
        the published email is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get(
            f"/marketing/v3/emails/{email_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def get_emails_list(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        property: str | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateEmailStatistics:
        """
        Use this endpoint to get aggregated statistics of emails sent in a specified
        time span. It also returns the list of emails that were sent during the time
        span.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          property: Specifies which email properties should be returned. All properties will be
              returned by default.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketing/v3/emails/statistics/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "property": property,
                        "start_timestamp": start_timestamp,
                    },
                    email_get_emails_list_params.EmailGetEmailsListParams,
                ),
            ),
            cast_to=AggregateEmailStatistics,
        )

    def get_histogram(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        interval: Literal["YEAR", "QUARTER", "MONTH", "WEEK", "DAY", "HOUR", "QUARTER_HOUR", "MINUTE", "SECOND"]
        | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalEmailStatisticIntervalNoPaging:
        """Get aggregated statistics in intervals for a specified time span.

        Each interval
        contains aggregated statistics of the emails that were sent in that time.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          interval: The interval to aggregate statistics for.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketing/v3/emails/statistics/histogram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "interval": interval,
                        "start_timestamp": start_timestamp,
                    },
                    email_get_histogram_params.EmailGetHistogramParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
        )

    def get_revision_by_id(
        self,
        revision_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionPublicEmail:
        """
        Get a specific revision of a marketing email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPublicEmail,
        )

    def get_revisions(
        self,
        email_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[VersionPublicEmail]:
        """
        Get a list of all versions of a marketing email, with each entry including the
        full state of that particular version. To view the most recent version, sort by
        the updatedAt parameter.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          before: The cursor token value to get the previous set of results. You can get this from
              the `paging.prev.before` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to return. Default is 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            f"/marketing/v3/emails/{email_id}/revisions",
            page=SyncPage[VersionPublicEmail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    email_get_revisions_params.EmailGetRevisionsParams,
                ),
            ),
            model=VersionPublicEmail,
        )

    def publish_or_send(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If you have a Marketing Hub Enterprise account or the transactional email
        add-on, you can use this endpoint to publish an automated email or send/schedule
        a regular email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/marketing/v3/emails/{email_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
        self,
        email_id: str,
        *,
        archived: bool | Omit = omit,
        included_properties: SequenceNotStr[str] | Omit = omit,
        include_stats: bool | Omit = omit,
        marketing_campaign_names: bool | Omit = omit,
        workflow_names: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Get the details for a marketing email.

        Args:
          archived: Whether to return only results that have been archived.

          included_properties: Limit the response to only include the specified properties.

          include_stats: Include statistics with email.

          marketing_campaign_names: If set to true, loads `campaignName` and `campaignUtm`.

          workflow_names: If set to true, loads workflows in which the email is used within a "send email"
              action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get(
            f"/marketing/v3/emails/{email_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "included_properties": included_properties,
                        "include_stats": include_stats,
                        "marketing_campaign_names": marketing_campaign_names,
                        "workflow_names": workflow_names,
                    },
                    email_read_params.EmailReadParams,
                ),
            ),
            cast_to=PublicEmail,
        )

    def reset_draft(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets the draft back to a copy of the live object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/marketing/v3/emails/{email_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore_draft_revision(
        self,
        revision_id: int,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Restores a previous revision of a marketing email to DRAFT state.

        If there is
        currently something in the draft for that object, it is overwritten.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._post(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    def restore_revision(
        self,
        revision_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Restores a previous revision of a marketing email.

        The current revision becomes
        old, and the restored revision is given a new version number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unpublish_or_cancel(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If you have a Marketing Hub Enterprise account or the transactional email
        add-on, you can use this endpoint to unpublish an automated email or cancel a
        regular email. If the email is already in the process of being sent, canceling
        might not be possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/marketing/v3/emails/{email_id}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upsert_draft(
        self,
        email_id: str,
        *,
        active_domain: str | Omit = omit,
        archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Create or update the draft version of a marketing email.

        If no draft exists, the
        system creates a draft from the current “live” email then applies the request
        body to that draft. The draft version only lives on the buffer—the email is not
        cloned.

        Args:
          active_domain: The active domain of the email.

          archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          from_: Data structure representing the from fields on the email.

          name: The name of the email, as displayed on the email dashboard.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._patch(
            f"/marketing/v3/emails/{email_id}/draft",
            body=maybe_transform(
                {
                    "active_domain": active_domain,
                    "archived": archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "name": name,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_upsert_draft_params.EmailUpsertDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        active_domain: str | Omit = omit,
        archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        feedback_survey_id: str | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Use this endpoint to create a new marketing email.

        Args:
          name: The name of the email, as displayed on the email dashboard.

          active_domain: The active domain of the email.

          archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          feedback_survey_id: The ID of the feedback survey linked to the email.

          from_: Data structure representing the from fields on the email.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/emails/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "active_domain": active_domain,
                    "archived": archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "feedback_survey_id": feedback_survey_id,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def update(
        self,
        email_id: str,
        *,
        query_archived: bool | Omit = omit,
        active_domain: str | Omit = omit,
        body_archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Change properties of a marketing email.

        Args:
          query_archived: Whether to return only results that have been archived.

          active_domain: The active domain of the email.

          body_archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          from_: Data structure representing the from fields on the email.

          name: The name of the email, as displayed on the email dashboard.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._patch(
            f"/marketing/v3/emails/{email_id}",
            body=await async_maybe_transform(
                {
                    "active_domain": active_domain,
                    "body_archived": body_archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "name": name,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_update_params.EmailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_archived": query_archived}, email_update_params.EmailUpdateParams
                ),
            ),
            cast_to=PublicEmail,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        campaign: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        included_properties: SequenceNotStr[str] | Omit = omit,
        include_stats: bool | Omit = omit,
        is_published: bool | Omit = omit,
        limit: int | Omit = omit,
        marketing_campaign_names: bool | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: Literal[
            "AB_EMAIL",
            "BATCH_EMAIL",
            "LOCALTIME_EMAIL",
            "AUTOMATED_AB_EMAIL",
            "BLOG_EMAIL",
            "BLOG_EMAIL_CHILD",
            "RSS_EMAIL",
            "RSS_EMAIL_CHILD",
            "RESUBSCRIBE_EMAIL",
            "OPTIN_EMAIL",
            "OPTIN_FOLLOWUP_EMAIL",
            "AUTOMATED_EMAIL",
            "FEEDBACK_CES_EMAIL",
            "FEEDBACK_CUSTOM_EMAIL",
            "FEEDBACK_CUSTOM_SURVEY_EMAIL",
            "FEEDBACK_NPS_EMAIL",
            "FOLLOWUP_EMAIL",
            "LEADFLOW_EMAIL",
            "SINGLE_SEND_API",
            "MARKETING_SINGLE_SEND_API",
            "SMTP_TOKEN",
            "TICKET_EMAIL",
            "MEMBERSHIP_REGISTRATION_EMAIL",
            "MEMBERSHIP_PASSWORD_SAVED_EMAIL",
            "MEMBERSHIP_PASSWORD_RESET_EMAIL",
            "MEMBERSHIP_EMAIL_VERIFICATION_EMAIL",
            "MEMBERSHIP_PASSWORDLESS_AUTH_EMAIL",
            "MEMBERSHIP_REGISTRATION_FOLLOW_UP_EMAIL",
            "MEMBERSHIP_OTP_LOGIN_EMAIL",
            "MEMBERSHIP_FOLLOW_UP_EMAIL",
            "MEMBERSHIP_VERIFICATION_EMAIL",
        ]
        | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        workflow_names: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PublicEmail, AsyncPage[PublicEmail]]:
        """The results can be filtered, allowing you to find a specific set of emails.

        See
        the table below for a full list of filtering options.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived emails. Defaults to `false`.

          campaign: Filter by campaign GUID. All emails will be returned if not present.

          created_after: Only return emails created after the specified time.

          created_at: Only return emails created at exactly the specified time.

          created_before: Only return emails created before the specified time.

          included_properties: Limit the response to only include this specified list of properties.

          include_stats: Include statistics with emails.

          is_published: Filter by published/draft emails. All emails will be returned if not present.

          limit: The maximum number of results to return. Default is 10.

          marketing_campaign_names: Include the names for any associated marketing campaigns.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          type: Email types to be filtered by. Multiple types can be included. All emails will
              be returned if not present.

          updated_after: Only return emails last updated after the specified time.

          updated_at: Only return emails last updated at exactly the specified time.

          updated_before: Only return emails last updated before the specified time.

          workflow_names: Include the names of any workflows associated with the returned emails.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/marketing/v3/emails/",
            page=AsyncPage[PublicEmail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "campaign": campaign,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "included_properties": included_properties,
                        "include_stats": include_stats,
                        "is_published": is_published,
                        "limit": limit,
                        "marketing_campaign_names": marketing_campaign_names,
                        "sort": sort,
                        "type": type,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                        "workflow_names": workflow_names,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            model=PublicEmail,
        )

    async def delete(
        self,
        email_id: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a marketing email by its ID

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/marketing/v3/emails/{email_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, email_delete_params.EmailDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def clone(
        self,
        *,
        id: str,
        clone_name: str | Omit = omit,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        This will create a duplicate email with the same properties as the original,
        with the exception of a unique ID.

        Args:
          id: The unique identifier of the email to be cloned.

          clone_name: The name to assign to the cloned email.

          language: The language code for the cloned email, such as 'en' for English.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/emails/clone",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                    "language": language,
                },
                email_clone_params.EmailCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def create_ab_test_variation(
        self,
        *,
        content_id: str,
        variation_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Create a variation of a marketing email for an A/B test.

        The new variation will
        be created as a draft. If an active variation already exists, a new one won't be
        created.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/marketing/v3/emails/ab-test/create-variation",
            body=await async_maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                email_create_ab_test_variation_params.EmailCreateAbTestVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def get_ab_test_variation(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """This endpoint lets you obtain the variation of an A/B marketing email.

        If the
        email is variation A (master) it will return variation B (variant) and vice
        versa.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._get(
            f"/marketing/v3/emails/{email_id}/ab-test/get-variation",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def get_draft(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Get the draft version of an email (if it exists).

        If no draft version exists,
        the published email is returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._get(
            f"/marketing/v3/emails/{email_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def get_emails_list(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        property: str | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateEmailStatistics:
        """
        Use this endpoint to get aggregated statistics of emails sent in a specified
        time span. It also returns the list of emails that were sent during the time
        span.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          property: Specifies which email properties should be returned. All properties will be
              returned by default.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketing/v3/emails/statistics/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "property": property,
                        "start_timestamp": start_timestamp,
                    },
                    email_get_emails_list_params.EmailGetEmailsListParams,
                ),
            ),
            cast_to=AggregateEmailStatistics,
        )

    async def get_histogram(
        self,
        *,
        email_ids: Iterable[int] | Omit = omit,
        end_timestamp: str | Omit = omit,
        interval: Literal["YEAR", "QUARTER", "MONTH", "WEEK", "DAY", "HOUR", "QUARTER_HOUR", "MINUTE", "SECOND"]
        | Omit = omit,
        start_timestamp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalEmailStatisticIntervalNoPaging:
        """Get aggregated statistics in intervals for a specified time span.

        Each interval
        contains aggregated statistics of the emails that were sent in that time.

        Args:
          email_ids: Filter by email IDs. Only include statistics of emails with these IDs.

          end_timestamp: The end timestamp of the time span, in ISO8601 representation.

          interval: The interval to aggregate statistics for.

          start_timestamp: The start timestamp of the time span, in ISO8601 representation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketing/v3/emails/statistics/histogram",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email_ids": email_ids,
                        "end_timestamp": end_timestamp,
                        "interval": interval,
                        "start_timestamp": start_timestamp,
                    },
                    email_get_histogram_params.EmailGetHistogramParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
        )

    async def get_revision_by_id(
        self,
        revision_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionPublicEmail:
        """
        Get a specific revision of a marketing email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPublicEmail,
        )

    def get_revisions(
        self,
        email_id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VersionPublicEmail, AsyncPage[VersionPublicEmail]]:
        """
        Get a list of all versions of a marketing email, with each entry including the
        full state of that particular version. To view the most recent version, sort by
        the updatedAt parameter.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          before: The cursor token value to get the previous set of results. You can get this from
              the `paging.prev.before` JSON property of a paged response containing more
              results.

          limit: The maximum number of results to return. Default is 10.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return self._get_api_list(
            f"/marketing/v3/emails/{email_id}/revisions",
            page=AsyncPage[VersionPublicEmail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    email_get_revisions_params.EmailGetRevisionsParams,
                ),
            ),
            model=VersionPublicEmail,
        )

    async def publish_or_send(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If you have a Marketing Hub Enterprise account or the transactional email
        add-on, you can use this endpoint to publish an automated email or send/schedule
        a regular email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/marketing/v3/emails/{email_id}/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
        self,
        email_id: str,
        *,
        archived: bool | Omit = omit,
        included_properties: SequenceNotStr[str] | Omit = omit,
        include_stats: bool | Omit = omit,
        marketing_campaign_names: bool | Omit = omit,
        workflow_names: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """
        Get the details for a marketing email.

        Args:
          archived: Whether to return only results that have been archived.

          included_properties: Limit the response to only include the specified properties.

          include_stats: Include statistics with email.

          marketing_campaign_names: If set to true, loads `campaignName` and `campaignUtm`.

          workflow_names: If set to true, loads workflows in which the email is used within a "send email"
              action.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._get(
            f"/marketing/v3/emails/{email_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "included_properties": included_properties,
                        "include_stats": include_stats,
                        "marketing_campaign_names": marketing_campaign_names,
                        "workflow_names": workflow_names,
                    },
                    email_read_params.EmailReadParams,
                ),
            ),
            cast_to=PublicEmail,
        )

    async def reset_draft(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Resets the draft back to a copy of the live object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/marketing/v3/emails/{email_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore_draft_revision(
        self,
        revision_id: int,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Restores a previous revision of a marketing email to DRAFT state.

        If there is
        currently something in the draft for that object, it is overwritten.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._post(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )

    async def restore_revision(
        self,
        revision_id: str,
        *,
        email_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Restores a previous revision of a marketing email.

        The current revision becomes
        old, and the restored revision is given a new version number.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/marketing/v3/emails/{email_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unpublish_or_cancel(
        self,
        email_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If you have a Marketing Hub Enterprise account or the transactional email
        add-on, you can use this endpoint to unpublish an automated email or cancel a
        regular email. If the email is already in the process of being sent, canceling
        might not be possible.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/marketing/v3/emails/{email_id}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upsert_draft(
        self,
        email_id: str,
        *,
        active_domain: str | Omit = omit,
        archived: bool | Omit = omit,
        business_unit_id: int | Omit = omit,
        campaign: str | Omit = omit,
        content: PublicEmailContentParam | Omit = omit,
        folder_id_v2: int | Omit = omit,
        from_: PublicEmailFromDetailsParam | Omit = omit,
        jitter_send_time: bool | Omit = omit,
        language: Literal[
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ann",
            "ann-ng",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "as-in",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "be-by",
            "bg",
            "bgc",
            "bgc-in",
            "bg-bg",
            "bho",
            "bho-in",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "brx",
            "brx-in",
            "br-fr",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ceb",
            "ceb-ph",
            "ce-ru",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
            "cy",
            "cy-gb",
            "da",
            "dav",
            "dav-ke",
            "da-dk",
            "da-gl",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-ee",
            "en-eg",
            "en-er",
            "en-es",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-fr",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mv",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-tn",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fil",
            "fil-ph",
            "fi-fi",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "frr",
            "frr-de",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "guz",
            "guz-ke",
            "gu-in",
            "gv",
            "gv-im",
            "ha",
            "haw",
            "haw-us",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "he",
            "he-il",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "ka-ge",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kgp",
            "kgp-br",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kkj",
            "kkj-cm",
            "kk-kz",
            "kl",
            "kln",
            "kln-ke",
            "kl-gl",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "kok",
            "kok-in",
            "ko-kp",
            "ko-kr",
            "ks",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ks-in",
            "ku",
            "ku-tr",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lu-cd",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mdf",
            "mdf-ru",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mg-mg",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mni",
            "mni-in",
            "mn-mn",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nds",
            "nds-de",
            "nds-nl",
            "nd-zw",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-bq",
            "nl-ch",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nnh",
            "nnh-cm",
            "nn-no",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pis",
            "pis-sb",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "raj",
            "raj-in",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "rof",
            "rof-tz",
            "ro-md",
            "ro-ro",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rwk",
            "rwk-tz",
            "rw-rw",
            "sa",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sa-in",
            "sbp",
            "sbp-tz",
            "sc",
            "sc-it",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "se-fi",
            "se-no",
            "se-se",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sms",
            "sms-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "teo",
            "teo-ke",
            "teo-ug",
            "te-in",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "tok",
            "tok-001",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yrl",
            "yrl-br",
            "yrl-co",
            "yrl-ve",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hans",
            "zh-hant",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zu",
            "zu-za",
        ]
        | Omit = omit,
        name: str | Omit = omit,
        publish_date: Union[str, datetime] | Omit = omit,
        rss_data: PublicRssEmailDetailsParam | Omit = omit,
        send_on_publish: bool | Omit = omit,
        state: Literal[
            "AUTOMATED",
            "AUTOMATED_DRAFT",
            "AUTOMATED_SENDING",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "BLOG_EMAIL_DRAFT",
            "BLOG_EMAIL_PUBLISHED",
            "DRAFT",
            "DRAFT_AB",
            "DRAFT_AB_VARIANT",
            "ERROR",
            "LOSER_AB_VARIANT",
            "PAGE_STUB",
            "PRE_PROCESSING",
            "PROCESSING",
            "PUBLISHED",
            "PUBLISHED_AB",
            "PUBLISHED_AB_VARIANT",
            "PUBLISHED_OR_SCHEDULED",
            "RSS_TO_EMAIL_DRAFT",
            "RSS_TO_EMAIL_PUBLISHED",
            "SCHEDULED",
            "SCHEDULED_AB",
            "SCHEDULED_OR_PUBLISHED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_LOSER_ABVARIANT",
            "AGENT_GENERATED",
        ]
        | Omit = omit,
        subcategory: Literal[
            "ab_master",
            "ab_variant",
            "ab_loser_variant",
            "page_stub",
            "landing_page",
            "site_page",
            "legacy_page",
            "ab_master_site_page",
            "ab_variant_site_page",
            "ab_loser_variant_site_page",
            "performable_landing_page",
            "performable_landing_page_cutover",
            "staged_page",
            "automated",
            "automated_for_deal",
            "automated_for_form",
            "automated_for_form_legacy",
            "automated_for_form_buffer",
            "automated_for_form_draft",
            "automated_for_crm",
            "rss_to_email",
            "rss_to_email_child",
            "blog_email",
            "blog_email_child",
            "optin_email",
            "optin_followup_email",
            "batch",
            "resubscribe_email",
            "unsubscribe_confirmation_email",
            "resubscribe_confirmation_email",
            "single_send_api",
            "marketing_single_send_api",
            "smtp_token",
            "localtime",
            "automated_for_ticket",
            "automated_for_leadflow",
            "automated_for_feedback_ces",
            "automated_for_feedback_nps",
            "automated_for_feedback_custom",
            "membership_registration",
            "membership_password_saved",
            "membership_password_reset",
            "membership_otp_login",
            "membership_passwordless_auth",
            "membership_email_verification",
            "membership_registration_follow_up",
            "membership_verification",
            "membership_follow_up",
            "ticket_closed_kickback_email",
            "ticket_opened_kickback_email",
            "automated_for_custom_survey",
            "discardable_stub",
            "normal_blog_post",
            "legacy_blog_post",
            "imported_blog_post",
            "automated_ab_master",
            "automated_ab_variant",
            "web_interactive",
            "portal_content",
            "page_instance_layout",
            "kb_article_instance_layout",
            "kb_listing",
            "kb_search_results",
            "kb_support_form",
            "kb_404_page",
            "case_study",
            "case_study_listing",
            "case_study_instance_layout",
            "scp_static_page",
            "scp_instance_layout_page",
            "podcast_instance_layout",
            "podcast_listing",
            "blog_article_instance_layout",
            "blog_article_listing",
            "blog_author_detail",
            "UNKNOWN",
        ]
        | Omit = omit,
        subject: str | Omit = omit,
        subscription_details: PublicEmailSubscriptionDetailsParam | Omit = omit,
        testing: PublicEmailTestingDetailsParam | Omit = omit,
        to: PublicEmailToDetailsParam | Omit = omit,
        webversion: PublicWebversionDetailsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicEmail:
        """Create or update the draft version of a marketing email.

        If no draft exists, the
        system creates a draft from the current “live” email then applies the request
        body to that draft. The draft version only lives on the buffer—the email is not
        cloned.

        Args:
          active_domain: The active domain of the email.

          archived: Determines if the email is archived or not.

          campaign: The ID of the campaign this email is associated to.

          content: Data structure representing the content of the email.

          from_: Data structure representing the from fields on the email.

          name: The name of the email, as displayed on the email dashboard.

          publish_date: The date and time the email is scheduled for, in ISO8601 representation. This is
              only used in local time or scheduled emails.

          rss_data: RSS related data if it is a blog or rss email.

          send_on_publish: Determines whether the email will be sent immediately on publish.

          state: The email state.

          subcategory: The email subcategory.

          subject: The subject of the email.

          subscription_details: Data structure representing the subscription fields of the email.

          testing: AB testing related data. This property is only returned for AB type emails.

          to: Data structure representing the to fields of the email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_id:
            raise ValueError(f"Expected a non-empty value for `email_id` but received {email_id!r}")
        return await self._patch(
            f"/marketing/v3/emails/{email_id}/draft",
            body=await async_maybe_transform(
                {
                    "active_domain": active_domain,
                    "archived": archived,
                    "business_unit_id": business_unit_id,
                    "campaign": campaign,
                    "content": content,
                    "folder_id_v2": folder_id_v2,
                    "from_": from_,
                    "jitter_send_time": jitter_send_time,
                    "language": language,
                    "name": name,
                    "publish_date": publish_date,
                    "rss_data": rss_data,
                    "send_on_publish": send_on_publish,
                    "state": state,
                    "subcategory": subcategory,
                    "subject": subject,
                    "subscription_details": subscription_details,
                    "testing": testing,
                    "to": to,
                    "webversion": webversion,
                },
                email_upsert_draft_params.EmailUpsertDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicEmail,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_raw_response_wrapper(
            emails.create,
        )
        self.update = to_raw_response_wrapper(
            emails.update,
        )
        self.list = to_raw_response_wrapper(
            emails.list,
        )
        self.delete = to_raw_response_wrapper(
            emails.delete,
        )
        self.clone = to_raw_response_wrapper(
            emails.clone,
        )
        self.create_ab_test_variation = to_raw_response_wrapper(
            emails.create_ab_test_variation,
        )
        self.get_ab_test_variation = to_raw_response_wrapper(
            emails.get_ab_test_variation,
        )
        self.get_draft = to_raw_response_wrapper(
            emails.get_draft,
        )
        self.get_emails_list = to_raw_response_wrapper(
            emails.get_emails_list,
        )
        self.get_histogram = to_raw_response_wrapper(
            emails.get_histogram,
        )
        self.get_revision_by_id = to_raw_response_wrapper(
            emails.get_revision_by_id,
        )
        self.get_revisions = to_raw_response_wrapper(
            emails.get_revisions,
        )
        self.publish_or_send = to_raw_response_wrapper(
            emails.publish_or_send,
        )
        self.read = to_raw_response_wrapper(
            emails.read,
        )
        self.reset_draft = to_raw_response_wrapper(
            emails.reset_draft,
        )
        self.restore_draft_revision = to_raw_response_wrapper(
            emails.restore_draft_revision,
        )
        self.restore_revision = to_raw_response_wrapper(
            emails.restore_revision,
        )
        self.unpublish_or_cancel = to_raw_response_wrapper(
            emails.unpublish_or_cancel,
        )
        self.upsert_draft = to_raw_response_wrapper(
            emails.upsert_draft,
        )


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_raw_response_wrapper(
            emails.create,
        )
        self.update = async_to_raw_response_wrapper(
            emails.update,
        )
        self.list = async_to_raw_response_wrapper(
            emails.list,
        )
        self.delete = async_to_raw_response_wrapper(
            emails.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            emails.clone,
        )
        self.create_ab_test_variation = async_to_raw_response_wrapper(
            emails.create_ab_test_variation,
        )
        self.get_ab_test_variation = async_to_raw_response_wrapper(
            emails.get_ab_test_variation,
        )
        self.get_draft = async_to_raw_response_wrapper(
            emails.get_draft,
        )
        self.get_emails_list = async_to_raw_response_wrapper(
            emails.get_emails_list,
        )
        self.get_histogram = async_to_raw_response_wrapper(
            emails.get_histogram,
        )
        self.get_revision_by_id = async_to_raw_response_wrapper(
            emails.get_revision_by_id,
        )
        self.get_revisions = async_to_raw_response_wrapper(
            emails.get_revisions,
        )
        self.publish_or_send = async_to_raw_response_wrapper(
            emails.publish_or_send,
        )
        self.read = async_to_raw_response_wrapper(
            emails.read,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            emails.reset_draft,
        )
        self.restore_draft_revision = async_to_raw_response_wrapper(
            emails.restore_draft_revision,
        )
        self.restore_revision = async_to_raw_response_wrapper(
            emails.restore_revision,
        )
        self.unpublish_or_cancel = async_to_raw_response_wrapper(
            emails.unpublish_or_cancel,
        )
        self.upsert_draft = async_to_raw_response_wrapper(
            emails.upsert_draft,
        )


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_streamed_response_wrapper(
            emails.create,
        )
        self.update = to_streamed_response_wrapper(
            emails.update,
        )
        self.list = to_streamed_response_wrapper(
            emails.list,
        )
        self.delete = to_streamed_response_wrapper(
            emails.delete,
        )
        self.clone = to_streamed_response_wrapper(
            emails.clone,
        )
        self.create_ab_test_variation = to_streamed_response_wrapper(
            emails.create_ab_test_variation,
        )
        self.get_ab_test_variation = to_streamed_response_wrapper(
            emails.get_ab_test_variation,
        )
        self.get_draft = to_streamed_response_wrapper(
            emails.get_draft,
        )
        self.get_emails_list = to_streamed_response_wrapper(
            emails.get_emails_list,
        )
        self.get_histogram = to_streamed_response_wrapper(
            emails.get_histogram,
        )
        self.get_revision_by_id = to_streamed_response_wrapper(
            emails.get_revision_by_id,
        )
        self.get_revisions = to_streamed_response_wrapper(
            emails.get_revisions,
        )
        self.publish_or_send = to_streamed_response_wrapper(
            emails.publish_or_send,
        )
        self.read = to_streamed_response_wrapper(
            emails.read,
        )
        self.reset_draft = to_streamed_response_wrapper(
            emails.reset_draft,
        )
        self.restore_draft_revision = to_streamed_response_wrapper(
            emails.restore_draft_revision,
        )
        self.restore_revision = to_streamed_response_wrapper(
            emails.restore_revision,
        )
        self.unpublish_or_cancel = to_streamed_response_wrapper(
            emails.unpublish_or_cancel,
        )
        self.upsert_draft = to_streamed_response_wrapper(
            emails.upsert_draft,
        )


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_streamed_response_wrapper(
            emails.create,
        )
        self.update = async_to_streamed_response_wrapper(
            emails.update,
        )
        self.list = async_to_streamed_response_wrapper(
            emails.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            emails.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            emails.clone,
        )
        self.create_ab_test_variation = async_to_streamed_response_wrapper(
            emails.create_ab_test_variation,
        )
        self.get_ab_test_variation = async_to_streamed_response_wrapper(
            emails.get_ab_test_variation,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            emails.get_draft,
        )
        self.get_emails_list = async_to_streamed_response_wrapper(
            emails.get_emails_list,
        )
        self.get_histogram = async_to_streamed_response_wrapper(
            emails.get_histogram,
        )
        self.get_revision_by_id = async_to_streamed_response_wrapper(
            emails.get_revision_by_id,
        )
        self.get_revisions = async_to_streamed_response_wrapper(
            emails.get_revisions,
        )
        self.publish_or_send = async_to_streamed_response_wrapper(
            emails.publish_or_send,
        )
        self.read = async_to_streamed_response_wrapper(
            emails.read,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            emails.reset_draft,
        )
        self.restore_draft_revision = async_to_streamed_response_wrapper(
            emails.restore_draft_revision,
        )
        self.restore_revision = async_to_streamed_response_wrapper(
            emails.restore_revision,
        )
        self.unpublish_or_cancel = async_to_streamed_response_wrapper(
            emails.unpublish_or_cancel,
        )
        self.upsert_draft = async_to_streamed_response_wrapper(
            emails.upsert_draft,
        )
