# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cms.page import Page
from ....types.cms.pages import (
    landing_page_get_params,
    landing_page_list_params,
    landing_page_clone_params,
    landing_page_create_params,
    landing_page_delete_params,
    landing_page_update_params,
    landing_page_schedule_params,
    landing_page_get_batch_params,
    landing_page_get_folder_params,
    landing_page_end_ab_test_params,
    landing_page_create_batch_params,
    landing_page_delete_batch_params,
    landing_page_list_folders_params,
    landing_page_update_batch_params,
    landing_page_update_draft_params,
    landing_page_create_folder_params,
    landing_page_delete_folder_params,
    landing_page_rerun_ab_test_params,
    landing_page_update_folder_params,
    landing_page_list_revisions_params,
    landing_page_update_languages_params,
    landing_page_get_folders_batch_params,
    landing_page_attach_to_lang_group_params,
    landing_page_create_folders_batch_params,
    landing_page_delete_folders_batch_params,
    landing_page_set_new_lang_primary_params,
    landing_page_update_folders_batch_params,
    landing_page_list_folder_revisions_params,
    landing_page_detach_from_lang_group_params,
    landing_page_create_ab_test_variation_params,
    landing_page_create_language_variation_params,
)
from ....types.cms.page_param import PageParam
from ....types.cms.version_page import VersionPage
from ....types.cms.content_folder import ContentFolder
from ....types.cms.batch_response_page import BatchResponsePage
from ....types.cms.content_folder_param import ContentFolderParam
from ....types.cms.layout_section_param import LayoutSectionParam
from ....types.cms.version_content_folder import VersionContentFolder
from ....types.cms.public_access_rule_param import PublicAccessRuleParam
from ....types.cms.batch_response_content_folder import BatchResponseContentFolder
from ....types.cms.content_language_variation_param import ContentLanguageVariationParam
from ....types.cms.collection_response_with_total_version_page import CollectionResponseWithTotalVersionPage
from ....types.cms.collection_response_with_total_version_content_folder import (
    CollectionResponseWithTotalVersionContentFolder,
)
from ....types.cms.collection_response_with_total_content_folder_forward_paging import (
    CollectionResponseWithTotalContentFolderForwardPaging,
)

__all__ = ["LandingPagesResource", "AsyncLandingPagesResource"]


class LandingPagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LandingPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LandingPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LandingPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return LandingPagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new Landing Page

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages",
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_create_params.LandingPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Sparse updates a single Landing Page object identified by the id in the path.
        You only need to specify the column values that you are modifying.

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Specifies whether to update deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            f"/cms/v3/pages/landing-pages/{object_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_update_params.LandingPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, landing_page_update_params.LandingPageUpdateParams),
            ),
            cast_to=Page,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Page]:
        """Get the list of landing pages.

        Supports paging and filtering. This method would
        be useful for an integration that examined these models and used an external
        service to suggest edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          created_after: Only return Landing Pages created after the specified time.

          created_at: Only return Landing Pages created at exactly the specified time.

          created_before: Only return Landing Pages created before the specified time.

          limit: The maximum number of results to return. Default is 100.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return Landing Pages last updated after the specified time.

          updated_at: Only return Landing Pages last updated at exactly the specified time.

          updated_before: Only return Landing Pages last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/pages/landing-pages",
            page=SyncPage[Page],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    landing_page_list_params.LandingPageListParams,
                ),
            ),
            model=Page,
        )

    def delete(
        self,
        object_id: str,
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
        Delete the Landing Page object identified by the id in the path.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/pages/landing-pages/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, landing_page_delete_params.LandingPageDeleteParams),
            ),
            cast_to=NoneType,
        )

    def attach_to_lang_group(
        self,
        *,
        id: str,
        language: str,
        primary_id: str,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a landing page to a multi-language group.

        Args:
          id: ID of the object to add to a multi-language group.

          language: Designated language of the object to add to a multi-language group.

          primary_id: ID of primary language object in multi-language group.

          primary_language: Primary language of the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/multi-language/attach-to-lang-group",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                landing_page_attach_to_lang_group_params.LandingPageAttachToLangGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clone(
        self,
        *,
        id: str,
        clone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Clone a Landing Page

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/clone",
            body=maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                },
                landing_page_clone_params.LandingPageCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
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
    ) -> Page:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/ab-test/create-variation",
            body=maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                landing_page_create_ab_test_variation_params.LandingPageCreateAbTestVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def create_batch(
        self,
        *,
        inputs: Iterable[PageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create the Landing Page objects detailed in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/batch/create",
            body=maybe_transform({"inputs": inputs}, landing_page_create_batch_params.LandingPageCreateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    def create_folder(
        self,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Create a new Folder

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/folders",
            body=maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                landing_page_create_folder_params.LandingPageCreateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    def create_folders_batch(
        self,
        *,
        inputs: Iterable[ContentFolderParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Create the Folder objects detailed in the request body.

        Args:
          inputs: Content folders to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/folders/batch/create",
            body=maybe_transform(
                {"inputs": inputs}, landing_page_create_folders_batch_params.LandingPageCreateFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseContentFolder,
        )

    def create_language_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Create a new language variation from an existing landing page

        Args:
          id: ID of content to clone.

          language: Target language of new variant.

          primary_language: Language of primary content to clone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/multi-language/create-language-variation",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_language": primary_language,
                },
                landing_page_create_language_variation_params.LandingPageCreateLanguageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def delete_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the Landing Page objects identified in the request body.

        Note: This is
        not the same as the dashboard `archive` function. To perform a dashboard
        `archive` send an normal update with the `archivedInDashboard` field set to
        true.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/batch/archive",
            body=maybe_transform({"inputs": inputs}, landing_page_delete_batch_params.LandingPageDeleteBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_folder(
        self,
        object_id: str,
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
        Delete the Folder object identified by the id in the path.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, landing_page_delete_folder_params.LandingPageDeleteFolderParams
                ),
            ),
            cast_to=NoneType,
        )

    def delete_folders_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the Folder objects identified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/folders/batch/archive",
            body=maybe_transform(
                {"inputs": inputs}, landing_page_delete_folders_batch_params.LandingPageDeleteFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def detach_from_lang_group(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Detach a landing page from a multi-language group.

        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/multi-language/detach-from-lang-group",
            body=maybe_transform(
                {"id": id}, landing_page_detach_from_lang_group_params.LandingPageDetachFromLangGroupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def end_ab_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/ab-test/end",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                landing_page_end_ab_test_params.LandingPageEndAbTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Retrieve the Landing Page object identified by the id in the path.

        Args:
          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    landing_page_get_params.LandingPageGetParams,
                ),
            ),
            cast_to=Page,
        )

    def get_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve the Landing Page objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/batch/read",
            body=maybe_transform({"inputs": inputs}, landing_page_get_batch_params.LandingPageGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, landing_page_get_batch_params.LandingPageGetBatchParams),
            ),
            cast_to=BatchResponsePage,
        )

    def get_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Retrieve the full draft version of the Landing Page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def get_folder(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Retrieve the Folder object identified by the id in the path.

        Args:
          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    landing_page_get_folder_params.LandingPageGetFolderParams,
                ),
            ),
            cast_to=ContentFolder,
        )

    def get_folder_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionContentFolder:
        """
        Retrieves a previous version of a Folder

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionContentFolder,
        )

    def get_folders_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update the Folder objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/folders/batch/read",
            body=maybe_transform(
                {"inputs": inputs}, landing_page_get_folders_batch_params.LandingPageGetFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, landing_page_get_folders_batch_params.LandingPageGetFoldersBatchParams
                ),
            ),
            cast_to=BatchResponseContentFolder,
        )

    def get_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionPage:
        """
        Retrieves a previous version of a Landing Page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPage,
        )

    def list_folder_revisions(
        self,
        object_id: str,
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
    ) -> CollectionResponseWithTotalVersionContentFolder:
        """
        Retrieves all the previous versions of a Folder.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions",
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
                    landing_page_list_folder_revisions_params.LandingPageListFolderRevisionsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalVersionContentFolder,
        )

    def list_folders(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalContentFolderForwardPaging:
        """Get the list of Landing Page Folders.

        Supports paging and filtering. This method
        would be useful for an integration that examined these models and used an
        external service to suggest edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          created_after: Only return Folders created after the specified time.

          created_at: Only return Folders created at exactly the specified time.

          created_before: Only return Folders created before the specified time.

          limit: The maximum number of results to return. Default is 100.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return Folders last updated after the specified time.

          updated_at: Only return Folders last updated at exactly the specified time.

          updated_before: Only return Folders last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cms/v3/pages/landing-pages/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    landing_page_list_folders_params.LandingPageListFoldersParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalContentFolderForwardPaging,
        )

    def list_revisions(
        self,
        object_id: str,
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
    ) -> CollectionResponseWithTotalVersionPage:
        """
        Retrieves all the previous versions of a Landing Page.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions",
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
                    landing_page_list_revisions_params.LandingPageListRevisionsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalVersionPage,
        )

    def publish_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Take any changes from the draft version of the Landing Page and apply them to
        the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/draft/push-live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rerun_ab_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/ab-test/rerun",
            body=maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                landing_page_rerun_ab_test_params.LandingPageRerunAbTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def reset_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discards any edits and resets the draft to the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore_folder_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Takes a specified version of a Folder and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._post(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    def restore_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Takes a specified version of a Landing Page and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def restore_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Takes a specified version of a Landing Page, sets it as the new draft version of
        the Landing Page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def schedule(
        self,
        *,
        id: str,
        publish_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Schedule a Landing Page to be Published

        Args:
          id: The ID of the object to be scheduled.

          publish_date: The date the object should transition from scheduled to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/schedule",
            body=maybe_transform(
                {
                    "id": id,
                    "publish_date": publish_date,
                },
                landing_page_schedule_params.LandingPageScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_new_lang_primary(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set a landing page as the primary language of a multi-language group.

        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/cms/v3/pages/landing-pages/multi-language/set-new-lang-primary",
            body=maybe_transform(
                {"id": id}, landing_page_set_new_lang_primary_params.LandingPageSetNewLangPrimaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_batch(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update the Landing Page objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Specifies whether to update deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/batch/update",
            body=maybe_transform({"inputs": inputs}, landing_page_update_batch_params.LandingPageUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, landing_page_update_batch_params.LandingPageUpdateBatchParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    def update_draft(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Sparse updates the draft version of a single Landing Page object identified by
        the id in the path. You only need to specify the column values that you are
        modifying.

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            f"/cms/v3/pages/landing-pages/{object_id}/draft",
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_update_draft_params.LandingPageUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    def update_folder(
        self,
        object_id: str,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """Sparse updates a single Folder object identified by the id in the path.

        You only
        need to specify the column values that you are modifying.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          archived: Specifies whether to update deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                landing_page_update_folder_params.LandingPageUpdateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, landing_page_update_folder_params.LandingPageUpdateFolderParams
                ),
            ),
            cast_to=ContentFolder,
        )

    def update_folders_batch(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update the Folder objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/pages/landing-pages/folders/batch/update",
            body=maybe_transform(
                {"inputs": inputs}, landing_page_update_folders_batch_params.LandingPageUpdateFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, landing_page_update_folders_batch_params.LandingPageUpdateFoldersBatchParams
                ),
            ),
            cast_to=BatchResponseContentFolder,
        )

    def update_languages(
        self,
        *,
        languages: Dict[str, str],
        primary_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Explicitly set new languages for each landing page in a multi-language group.

        Args:
          languages: Map of object IDs to associated languages of object in the multi-language group.

          primary_id: ID of the primary object in the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/pages/landing-pages/multi-language/update-languages",
            body=maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                landing_page_update_languages_params.LandingPageUpdateLanguagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLandingPagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLandingPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLandingPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLandingPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncLandingPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create a new Landing Page

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_create_params.LandingPageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Sparse updates a single Landing Page object identified by the id in the path.
        You only need to specify the column values that you are modifying.

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Specifies whether to update deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            f"/cms/v3/pages/landing-pages/{object_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_update_params.LandingPageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_update_params.LandingPageUpdateParams
                ),
            ),
            cast_to=Page,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Page, AsyncPage[Page]]:
        """Get the list of landing pages.

        Supports paging and filtering. This method would
        be useful for an integration that examined these models and used an external
        service to suggest edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          created_after: Only return Landing Pages created after the specified time.

          created_at: Only return Landing Pages created at exactly the specified time.

          created_before: Only return Landing Pages created before the specified time.

          limit: The maximum number of results to return. Default is 100.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return Landing Pages last updated after the specified time.

          updated_at: Only return Landing Pages last updated at exactly the specified time.

          updated_before: Only return Landing Pages last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/pages/landing-pages",
            page=AsyncPage[Page],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    landing_page_list_params.LandingPageListParams,
                ),
            ),
            model=Page,
        )

    async def delete(
        self,
        object_id: str,
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
        Delete the Landing Page object identified by the id in the path.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/pages/landing-pages/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_delete_params.LandingPageDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def attach_to_lang_group(
        self,
        *,
        id: str,
        language: str,
        primary_id: str,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Attach a landing page to a multi-language group.

        Args:
          id: ID of the object to add to a multi-language group.

          language: Designated language of the object to add to a multi-language group.

          primary_id: ID of primary language object in multi-language group.

          primary_language: Primary language of the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/multi-language/attach-to-lang-group",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                landing_page_attach_to_lang_group_params.LandingPageAttachToLangGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clone(
        self,
        *,
        id: str,
        clone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Clone a Landing Page

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/clone",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                },
                landing_page_clone_params.LandingPageCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
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
    ) -> Page:
        """
        Create a new A/B test variation based on the information provided in the request
        body.

        Args:
          content_id: ID of the object to test.

          variation_name: Name of A/B test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/ab-test/create-variation",
            body=await async_maybe_transform(
                {
                    "content_id": content_id,
                    "variation_name": variation_name,
                },
                landing_page_create_ab_test_variation_params.LandingPageCreateAbTestVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def create_batch(
        self,
        *,
        inputs: Iterable[PageParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Create the Landing Page objects detailed in the request body.

        Args:
          inputs: Pages to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_create_batch_params.LandingPageCreateBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePage,
        )

    async def create_folder(
        self,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Create a new Folder

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/folders",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                landing_page_create_folder_params.LandingPageCreateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    async def create_folders_batch(
        self,
        *,
        inputs: Iterable[ContentFolderParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Create the Folder objects detailed in the request body.

        Args:
          inputs: Content folders to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/folders/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_create_folders_batch_params.LandingPageCreateFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def create_language_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        primary_language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Create a new language variation from an existing landing page

        Args:
          id: ID of content to clone.

          language: Target language of new variant.

          primary_language: Language of primary content to clone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/multi-language/create-language-variation",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_language": primary_language,
                },
                landing_page_create_language_variation_params.LandingPageCreateLanguageVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def delete_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the Landing Page objects identified in the request body.

        Note: This is
        not the same as the dashboard `archive` function. To perform a dashboard
        `archive` send an normal update with the `archivedInDashboard` field set to
        true.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/batch/archive",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_delete_batch_params.LandingPageDeleteBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_folder(
        self,
        object_id: str,
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
        Delete the Folder object identified by the id in the path.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_delete_folder_params.LandingPageDeleteFolderParams
                ),
            ),
            cast_to=NoneType,
        )

    async def delete_folders_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the Folder objects identified in the request body.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/folders/batch/archive",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_delete_folders_batch_params.LandingPageDeleteFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def detach_from_lang_group(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Detach a landing page from a multi-language group.

        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/multi-language/detach-from-lang-group",
            body=await async_maybe_transform(
                {"id": id}, landing_page_detach_from_lang_group_params.LandingPageDetachFromLangGroupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def end_ab_test(
        self,
        *,
        ab_test_id: str,
        winner_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        End an active A/B test and designate a winner.

        Args:
          ab_test_id: ID of the test to end.

          winner_id: ID of the object to designate as the test winner.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/ab-test/end",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "winner_id": winner_id,
                },
                landing_page_end_ab_test_params.LandingPageEndAbTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Retrieve the Landing Page object identified by the id in the path.

        Args:
          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    landing_page_get_params.LandingPageGetParams,
                ),
            ),
            cast_to=Page,
        )

    async def get_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Retrieve the Landing Page objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Specifies whether to return deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_get_batch_params.LandingPageGetBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_get_batch_params.LandingPageGetBatchParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    async def get_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Retrieve the full draft version of the Landing Page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def get_folder(
        self,
        object_id: str,
        *,
        archived: bool | Omit = omit,
        property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Retrieve the Folder object identified by the id in the path.

        Args:
          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "property": property,
                    },
                    landing_page_get_folder_params.LandingPageGetFolderParams,
                ),
            ),
            cast_to=ContentFolder,
        )

    async def get_folder_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionContentFolder:
        """
        Retrieves a previous version of a Folder

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionContentFolder,
        )

    async def get_folders_batch(
        self,
        *,
        inputs: SequenceNotStr[str],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update the Folder objects identified in the request body.

        Args:
          inputs: Strings to input.

          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/folders/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_get_folders_batch_params.LandingPageGetFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_get_folders_batch_params.LandingPageGetFoldersBatchParams
                ),
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def get_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionPage:
        """
        Retrieves a previous version of a Landing Page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionPage,
        )

    async def list_folder_revisions(
        self,
        object_id: str,
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
    ) -> CollectionResponseWithTotalVersionContentFolder:
        """
        Retrieves all the previous versions of a Folder.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    landing_page_list_folder_revisions_params.LandingPageListFolderRevisionsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalVersionContentFolder,
        )

    async def list_folders(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        property: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalContentFolderForwardPaging:
        """Get the list of Landing Page Folders.

        Supports paging and filtering. This method
        would be useful for an integration that examined these models and used an
        external service to suggest edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted Folders. Defaults to `false`.

          created_after: Only return Folders created after the specified time.

          created_at: Only return Folders created at exactly the specified time.

          created_before: Only return Folders created before the specified time.

          limit: The maximum number of results to return. Default is 100.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return Folders last updated after the specified time.

          updated_at: Only return Folders last updated at exactly the specified time.

          updated_before: Only return Folders last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cms/v3/pages/landing-pages/folders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "property": property,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    landing_page_list_folders_params.LandingPageListFoldersParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalContentFolderForwardPaging,
        )

    async def list_revisions(
        self,
        object_id: str,
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
    ) -> CollectionResponseWithTotalVersionPage:
        """
        Retrieves all the previous versions of a Landing Page.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    landing_page_list_revisions_params.LandingPageListRevisionsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalVersionPage,
        )

    async def publish_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Take any changes from the draft version of the Landing Page and apply them to
        the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/draft/push-live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rerun_ab_test(
        self,
        *,
        ab_test_id: str,
        variation_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Rerun a previous A/B test.

        Args:
          ab_test_id: ID of the test to rerun.

          variation_id: ID of the object to reactivate as a test variation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/ab-test/rerun",
            body=await async_maybe_transform(
                {
                    "ab_test_id": ab_test_id,
                    "variation_id": variation_id,
                },
                landing_page_rerun_ab_test_params.LandingPageRerunAbTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def reset_draft(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Discards any edits and resets the draft to the live version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore_folder_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """
        Takes a specified version of a Folder and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._post(
            f"/cms/v3/pages/landing-pages/folders/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentFolder,
        )

    async def restore_revision(
        self,
        revision_id: str,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Takes a specified version of a Landing Page and restores it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def restore_revision_to_draft(
        self,
        revision_id: int,
        *,
        object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Takes a specified version of a Landing Page, sets it as the new draft version of
        the Landing Page.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            f"/cms/v3/pages/landing-pages/{object_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def schedule(
        self,
        *,
        id: str,
        publish_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Schedule a Landing Page to be Published

        Args:
          id: The ID of the object to be scheduled.

          publish_date: The date the object should transition from scheduled to published.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/schedule",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "publish_date": publish_date,
                },
                landing_page_schedule_params.LandingPageScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_new_lang_primary(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Set a landing page as the primary language of a multi-language group.

        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/cms/v3/pages/landing-pages/multi-language/set-new-lang-primary",
            body=await async_maybe_transform(
                {"id": id}, landing_page_set_new_lang_primary_params.LandingPageSetNewLangPrimaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_batch(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePage:
        """
        Update the Landing Page objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Specifies whether to update deleted Landing Pages. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_update_batch_params.LandingPageUpdateBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_update_batch_params.LandingPageUpdateBatchParams
                ),
            ),
            cast_to=BatchResponsePage,
        )

    async def update_draft(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
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
        ],
        domain: str,
        dynamic_page_data_source_id: str,
        dynamic_page_data_source_type: int,
        dynamic_page_hub_db_table_id: str,
        enable_domain_stylesheets: bool,
        enable_layout_stylesheets: bool,
        featured_image: str,
        featured_image_alt_text: str,
        folder_id: str,
        footer_html: str,
        head_html: str,
        html_title: str,
        include_default_custom_css: bool,
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
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
            "ce-ru",
            "ceb",
            "ceb-ph",
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
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
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
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
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
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
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
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
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
            "he-il",
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
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
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
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
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
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
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
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
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
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
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
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ],
        layout_sections: Dict[str, LayoutSectionParam],
        link_rel_canonical_url: str,
        mab_experiment_id: str,
        meta_description: str,
        name: str,
        page_expiry_date: int,
        page_expiry_enabled: bool,
        page_expiry_redirect_id: int,
        page_expiry_redirect_url: str,
        page_redirected: bool,
        password: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        slug: str,
        state: str,
        subcategory: str,
        template_path: str,
        theme_settings_values: Dict[str, object],
        translated_from_id: str,
        translations: Dict[str, ContentLanguageVariationParam],
        updated: Union[str, datetime],
        updated_by_id: str,
        url: str,
        use_featured_image: bool,
        widget_containers: Dict[str, object],
        widgets: Dict[str, object],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Page:
        """
        Sparse updates the draft version of a single Landing Page object identified by
        the id in the path. You only need to specify the column values that you are
        modifying.

        Args:
          id: The unique ID of the page.

          ab_status: The status of the AB test associated with this page, if applicable

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this page was deleted.

          archived_in_dashboard: If True, the page will not show up in your dashboard, although the page could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this page. These stylesheets are attached to
              just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this page.

          campaign: The GUID of the marketing campaign this page is a part of.

          category_id: ID of the type of object this is. Should always .

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created_by_id: The ID of the user that created this page.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this page references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this page.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: The ID of the associated folder this landing page is organized under in the app
              dashboard.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this page.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the page. If null, the page will
              default to the language of the Domain.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: The ID of the MAB test (or dynamic test) associated with this page, if
              applicable

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the page.

          page_expiry_date: The date at which this page should expire and begin redirecting to another url
              or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this page

          page_expiry_redirect_id: The ID of another page this page's url should redirect to once this page
              expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this page's url should redirect to once this page expires. Should only
              set this or pageExpiryRedirectId.

          page_redirected: A generated Boolean describing whether or not this page is currently expired and
              being redirected.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the page is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          slug: The path of the this page. This field is appended to the domain to construct the
              url of this page.

          state: An ENUM descibing the current state of this page.

          subcategory: Details the type of page this is. Should always be landing_page or site_page

          template_path: String detailing the path of the template used for this page.

          translated_from_id: ID of the primary page this object was translated from.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            f"/cms/v3/pages/landing-pages/{object_id}/draft",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "campaign": campaign,
                    "category_id": category_id,
                    "content_group_id": content_group_id,
                    "content_type_category": content_type_category,
                    "created": created,
                    "created_by_id": created_by_id,
                    "currently_published": currently_published,
                    "current_state": current_state,
                    "domain": domain,
                    "dynamic_page_data_source_id": dynamic_page_data_source_id,
                    "dynamic_page_data_source_type": dynamic_page_data_source_type,
                    "dynamic_page_hub_db_table_id": dynamic_page_hub_db_table_id,
                    "enable_domain_stylesheets": enable_domain_stylesheets,
                    "enable_layout_stylesheets": enable_layout_stylesheets,
                    "featured_image": featured_image,
                    "featured_image_alt_text": featured_image_alt_text,
                    "folder_id": folder_id,
                    "footer_html": footer_html,
                    "head_html": head_html,
                    "html_title": html_title,
                    "include_default_custom_css": include_default_custom_css,
                    "language": language,
                    "layout_sections": layout_sections,
                    "link_rel_canonical_url": link_rel_canonical_url,
                    "mab_experiment_id": mab_experiment_id,
                    "meta_description": meta_description,
                    "name": name,
                    "page_expiry_date": page_expiry_date,
                    "page_expiry_enabled": page_expiry_enabled,
                    "page_expiry_redirect_id": page_expiry_redirect_id,
                    "page_expiry_redirect_url": page_expiry_redirect_url,
                    "page_redirected": page_redirected,
                    "password": password,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "slug": slug,
                    "state": state,
                    "subcategory": subcategory,
                    "template_path": template_path,
                    "theme_settings_values": theme_settings_values,
                    "translated_from_id": translated_from_id,
                    "translations": translations,
                    "updated": updated,
                    "updated_by_id": updated_by_id,
                    "url": url,
                    "use_featured_image": use_featured_image,
                    "widget_containers": widget_containers,
                    "widgets": widgets,
                },
                landing_page_update_draft_params.LandingPageUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Page,
        )

    async def update_folder(
        self,
        object_id: str,
        *,
        id: str,
        category: int,
        created: Union[str, datetime],
        deleted_at: Union[str, datetime],
        name: str,
        parent_folder_id: int,
        updated: Union[str, datetime],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContentFolder:
        """Sparse updates a single Folder object identified by the id in the path.

        You only
        need to specify the column values that you are modifying.

        Args:
          id: The unique ID of the content folder.

          category: The type of object this folder applies to. Should always be LANDING_PAGE.

          deleted_at: The timestamp (ISO8601 format) when this content folder was deleted.

          name: The name of the folder which will show up in the app dashboard

          parent_folder_id: The ID of the content folder this folder is nested under

          archived: Specifies whether to update deleted Folders. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            f"/cms/v3/pages/landing-pages/folders/{object_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "category": category,
                    "created": created,
                    "deleted_at": deleted_at,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "updated": updated,
                },
                landing_page_update_folder_params.LandingPageUpdateFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_update_folder_params.LandingPageUpdateFolderParams
                ),
            ),
            cast_to=ContentFolder,
        )

    async def update_folders_batch(
        self,
        *,
        inputs: Iterable[object],
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseContentFolder:
        """
        Update the Folder objects identified in the request body.

        Args:
          inputs: JSON nodes to input.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/pages/landing-pages/folders/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, landing_page_update_folders_batch_params.LandingPageUpdateFoldersBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, landing_page_update_folders_batch_params.LandingPageUpdateFoldersBatchParams
                ),
            ),
            cast_to=BatchResponseContentFolder,
        )

    async def update_languages(
        self,
        *,
        languages: Dict[str, str],
        primary_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Explicitly set new languages for each landing page in a multi-language group.

        Args:
          languages: Map of object IDs to associated languages of object in the multi-language group.

          primary_id: ID of the primary object in the multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/pages/landing-pages/multi-language/update-languages",
            body=await async_maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                landing_page_update_languages_params.LandingPageUpdateLanguagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class LandingPagesResourceWithRawResponse:
    def __init__(self, landing_pages: LandingPagesResource) -> None:
        self._landing_pages = landing_pages

        self.create = to_raw_response_wrapper(
            landing_pages.create,
        )
        self.update = to_raw_response_wrapper(
            landing_pages.update,
        )
        self.list = to_raw_response_wrapper(
            landing_pages.list,
        )
        self.delete = to_raw_response_wrapper(
            landing_pages.delete,
        )
        self.attach_to_lang_group = to_raw_response_wrapper(
            landing_pages.attach_to_lang_group,
        )
        self.clone = to_raw_response_wrapper(
            landing_pages.clone,
        )
        self.create_ab_test_variation = to_raw_response_wrapper(
            landing_pages.create_ab_test_variation,
        )
        self.create_batch = to_raw_response_wrapper(
            landing_pages.create_batch,
        )
        self.create_folder = to_raw_response_wrapper(
            landing_pages.create_folder,
        )
        self.create_folders_batch = to_raw_response_wrapper(
            landing_pages.create_folders_batch,
        )
        self.create_language_variation = to_raw_response_wrapper(
            landing_pages.create_language_variation,
        )
        self.delete_batch = to_raw_response_wrapper(
            landing_pages.delete_batch,
        )
        self.delete_folder = to_raw_response_wrapper(
            landing_pages.delete_folder,
        )
        self.delete_folders_batch = to_raw_response_wrapper(
            landing_pages.delete_folders_batch,
        )
        self.detach_from_lang_group = to_raw_response_wrapper(
            landing_pages.detach_from_lang_group,
        )
        self.end_ab_test = to_raw_response_wrapper(
            landing_pages.end_ab_test,
        )
        self.get = to_raw_response_wrapper(
            landing_pages.get,
        )
        self.get_batch = to_raw_response_wrapper(
            landing_pages.get_batch,
        )
        self.get_draft = to_raw_response_wrapper(
            landing_pages.get_draft,
        )
        self.get_folder = to_raw_response_wrapper(
            landing_pages.get_folder,
        )
        self.get_folder_revision = to_raw_response_wrapper(
            landing_pages.get_folder_revision,
        )
        self.get_folders_batch = to_raw_response_wrapper(
            landing_pages.get_folders_batch,
        )
        self.get_revision = to_raw_response_wrapper(
            landing_pages.get_revision,
        )
        self.list_folder_revisions = to_raw_response_wrapper(
            landing_pages.list_folder_revisions,
        )
        self.list_folders = to_raw_response_wrapper(
            landing_pages.list_folders,
        )
        self.list_revisions = to_raw_response_wrapper(
            landing_pages.list_revisions,
        )
        self.publish_draft = to_raw_response_wrapper(
            landing_pages.publish_draft,
        )
        self.rerun_ab_test = to_raw_response_wrapper(
            landing_pages.rerun_ab_test,
        )
        self.reset_draft = to_raw_response_wrapper(
            landing_pages.reset_draft,
        )
        self.restore_folder_revision = to_raw_response_wrapper(
            landing_pages.restore_folder_revision,
        )
        self.restore_revision = to_raw_response_wrapper(
            landing_pages.restore_revision,
        )
        self.restore_revision_to_draft = to_raw_response_wrapper(
            landing_pages.restore_revision_to_draft,
        )
        self.schedule = to_raw_response_wrapper(
            landing_pages.schedule,
        )
        self.set_new_lang_primary = to_raw_response_wrapper(
            landing_pages.set_new_lang_primary,
        )
        self.update_batch = to_raw_response_wrapper(
            landing_pages.update_batch,
        )
        self.update_draft = to_raw_response_wrapper(
            landing_pages.update_draft,
        )
        self.update_folder = to_raw_response_wrapper(
            landing_pages.update_folder,
        )
        self.update_folders_batch = to_raw_response_wrapper(
            landing_pages.update_folders_batch,
        )
        self.update_languages = to_raw_response_wrapper(
            landing_pages.update_languages,
        )


class AsyncLandingPagesResourceWithRawResponse:
    def __init__(self, landing_pages: AsyncLandingPagesResource) -> None:
        self._landing_pages = landing_pages

        self.create = async_to_raw_response_wrapper(
            landing_pages.create,
        )
        self.update = async_to_raw_response_wrapper(
            landing_pages.update,
        )
        self.list = async_to_raw_response_wrapper(
            landing_pages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            landing_pages.delete,
        )
        self.attach_to_lang_group = async_to_raw_response_wrapper(
            landing_pages.attach_to_lang_group,
        )
        self.clone = async_to_raw_response_wrapper(
            landing_pages.clone,
        )
        self.create_ab_test_variation = async_to_raw_response_wrapper(
            landing_pages.create_ab_test_variation,
        )
        self.create_batch = async_to_raw_response_wrapper(
            landing_pages.create_batch,
        )
        self.create_folder = async_to_raw_response_wrapper(
            landing_pages.create_folder,
        )
        self.create_folders_batch = async_to_raw_response_wrapper(
            landing_pages.create_folders_batch,
        )
        self.create_language_variation = async_to_raw_response_wrapper(
            landing_pages.create_language_variation,
        )
        self.delete_batch = async_to_raw_response_wrapper(
            landing_pages.delete_batch,
        )
        self.delete_folder = async_to_raw_response_wrapper(
            landing_pages.delete_folder,
        )
        self.delete_folders_batch = async_to_raw_response_wrapper(
            landing_pages.delete_folders_batch,
        )
        self.detach_from_lang_group = async_to_raw_response_wrapper(
            landing_pages.detach_from_lang_group,
        )
        self.end_ab_test = async_to_raw_response_wrapper(
            landing_pages.end_ab_test,
        )
        self.get = async_to_raw_response_wrapper(
            landing_pages.get,
        )
        self.get_batch = async_to_raw_response_wrapper(
            landing_pages.get_batch,
        )
        self.get_draft = async_to_raw_response_wrapper(
            landing_pages.get_draft,
        )
        self.get_folder = async_to_raw_response_wrapper(
            landing_pages.get_folder,
        )
        self.get_folder_revision = async_to_raw_response_wrapper(
            landing_pages.get_folder_revision,
        )
        self.get_folders_batch = async_to_raw_response_wrapper(
            landing_pages.get_folders_batch,
        )
        self.get_revision = async_to_raw_response_wrapper(
            landing_pages.get_revision,
        )
        self.list_folder_revisions = async_to_raw_response_wrapper(
            landing_pages.list_folder_revisions,
        )
        self.list_folders = async_to_raw_response_wrapper(
            landing_pages.list_folders,
        )
        self.list_revisions = async_to_raw_response_wrapper(
            landing_pages.list_revisions,
        )
        self.publish_draft = async_to_raw_response_wrapper(
            landing_pages.publish_draft,
        )
        self.rerun_ab_test = async_to_raw_response_wrapper(
            landing_pages.rerun_ab_test,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            landing_pages.reset_draft,
        )
        self.restore_folder_revision = async_to_raw_response_wrapper(
            landing_pages.restore_folder_revision,
        )
        self.restore_revision = async_to_raw_response_wrapper(
            landing_pages.restore_revision,
        )
        self.restore_revision_to_draft = async_to_raw_response_wrapper(
            landing_pages.restore_revision_to_draft,
        )
        self.schedule = async_to_raw_response_wrapper(
            landing_pages.schedule,
        )
        self.set_new_lang_primary = async_to_raw_response_wrapper(
            landing_pages.set_new_lang_primary,
        )
        self.update_batch = async_to_raw_response_wrapper(
            landing_pages.update_batch,
        )
        self.update_draft = async_to_raw_response_wrapper(
            landing_pages.update_draft,
        )
        self.update_folder = async_to_raw_response_wrapper(
            landing_pages.update_folder,
        )
        self.update_folders_batch = async_to_raw_response_wrapper(
            landing_pages.update_folders_batch,
        )
        self.update_languages = async_to_raw_response_wrapper(
            landing_pages.update_languages,
        )


class LandingPagesResourceWithStreamingResponse:
    def __init__(self, landing_pages: LandingPagesResource) -> None:
        self._landing_pages = landing_pages

        self.create = to_streamed_response_wrapper(
            landing_pages.create,
        )
        self.update = to_streamed_response_wrapper(
            landing_pages.update,
        )
        self.list = to_streamed_response_wrapper(
            landing_pages.list,
        )
        self.delete = to_streamed_response_wrapper(
            landing_pages.delete,
        )
        self.attach_to_lang_group = to_streamed_response_wrapper(
            landing_pages.attach_to_lang_group,
        )
        self.clone = to_streamed_response_wrapper(
            landing_pages.clone,
        )
        self.create_ab_test_variation = to_streamed_response_wrapper(
            landing_pages.create_ab_test_variation,
        )
        self.create_batch = to_streamed_response_wrapper(
            landing_pages.create_batch,
        )
        self.create_folder = to_streamed_response_wrapper(
            landing_pages.create_folder,
        )
        self.create_folders_batch = to_streamed_response_wrapper(
            landing_pages.create_folders_batch,
        )
        self.create_language_variation = to_streamed_response_wrapper(
            landing_pages.create_language_variation,
        )
        self.delete_batch = to_streamed_response_wrapper(
            landing_pages.delete_batch,
        )
        self.delete_folder = to_streamed_response_wrapper(
            landing_pages.delete_folder,
        )
        self.delete_folders_batch = to_streamed_response_wrapper(
            landing_pages.delete_folders_batch,
        )
        self.detach_from_lang_group = to_streamed_response_wrapper(
            landing_pages.detach_from_lang_group,
        )
        self.end_ab_test = to_streamed_response_wrapper(
            landing_pages.end_ab_test,
        )
        self.get = to_streamed_response_wrapper(
            landing_pages.get,
        )
        self.get_batch = to_streamed_response_wrapper(
            landing_pages.get_batch,
        )
        self.get_draft = to_streamed_response_wrapper(
            landing_pages.get_draft,
        )
        self.get_folder = to_streamed_response_wrapper(
            landing_pages.get_folder,
        )
        self.get_folder_revision = to_streamed_response_wrapper(
            landing_pages.get_folder_revision,
        )
        self.get_folders_batch = to_streamed_response_wrapper(
            landing_pages.get_folders_batch,
        )
        self.get_revision = to_streamed_response_wrapper(
            landing_pages.get_revision,
        )
        self.list_folder_revisions = to_streamed_response_wrapper(
            landing_pages.list_folder_revisions,
        )
        self.list_folders = to_streamed_response_wrapper(
            landing_pages.list_folders,
        )
        self.list_revisions = to_streamed_response_wrapper(
            landing_pages.list_revisions,
        )
        self.publish_draft = to_streamed_response_wrapper(
            landing_pages.publish_draft,
        )
        self.rerun_ab_test = to_streamed_response_wrapper(
            landing_pages.rerun_ab_test,
        )
        self.reset_draft = to_streamed_response_wrapper(
            landing_pages.reset_draft,
        )
        self.restore_folder_revision = to_streamed_response_wrapper(
            landing_pages.restore_folder_revision,
        )
        self.restore_revision = to_streamed_response_wrapper(
            landing_pages.restore_revision,
        )
        self.restore_revision_to_draft = to_streamed_response_wrapper(
            landing_pages.restore_revision_to_draft,
        )
        self.schedule = to_streamed_response_wrapper(
            landing_pages.schedule,
        )
        self.set_new_lang_primary = to_streamed_response_wrapper(
            landing_pages.set_new_lang_primary,
        )
        self.update_batch = to_streamed_response_wrapper(
            landing_pages.update_batch,
        )
        self.update_draft = to_streamed_response_wrapper(
            landing_pages.update_draft,
        )
        self.update_folder = to_streamed_response_wrapper(
            landing_pages.update_folder,
        )
        self.update_folders_batch = to_streamed_response_wrapper(
            landing_pages.update_folders_batch,
        )
        self.update_languages = to_streamed_response_wrapper(
            landing_pages.update_languages,
        )


class AsyncLandingPagesResourceWithStreamingResponse:
    def __init__(self, landing_pages: AsyncLandingPagesResource) -> None:
        self._landing_pages = landing_pages

        self.create = async_to_streamed_response_wrapper(
            landing_pages.create,
        )
        self.update = async_to_streamed_response_wrapper(
            landing_pages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            landing_pages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            landing_pages.delete,
        )
        self.attach_to_lang_group = async_to_streamed_response_wrapper(
            landing_pages.attach_to_lang_group,
        )
        self.clone = async_to_streamed_response_wrapper(
            landing_pages.clone,
        )
        self.create_ab_test_variation = async_to_streamed_response_wrapper(
            landing_pages.create_ab_test_variation,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            landing_pages.create_batch,
        )
        self.create_folder = async_to_streamed_response_wrapper(
            landing_pages.create_folder,
        )
        self.create_folders_batch = async_to_streamed_response_wrapper(
            landing_pages.create_folders_batch,
        )
        self.create_language_variation = async_to_streamed_response_wrapper(
            landing_pages.create_language_variation,
        )
        self.delete_batch = async_to_streamed_response_wrapper(
            landing_pages.delete_batch,
        )
        self.delete_folder = async_to_streamed_response_wrapper(
            landing_pages.delete_folder,
        )
        self.delete_folders_batch = async_to_streamed_response_wrapper(
            landing_pages.delete_folders_batch,
        )
        self.detach_from_lang_group = async_to_streamed_response_wrapper(
            landing_pages.detach_from_lang_group,
        )
        self.end_ab_test = async_to_streamed_response_wrapper(
            landing_pages.end_ab_test,
        )
        self.get = async_to_streamed_response_wrapper(
            landing_pages.get,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            landing_pages.get_batch,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            landing_pages.get_draft,
        )
        self.get_folder = async_to_streamed_response_wrapper(
            landing_pages.get_folder,
        )
        self.get_folder_revision = async_to_streamed_response_wrapper(
            landing_pages.get_folder_revision,
        )
        self.get_folders_batch = async_to_streamed_response_wrapper(
            landing_pages.get_folders_batch,
        )
        self.get_revision = async_to_streamed_response_wrapper(
            landing_pages.get_revision,
        )
        self.list_folder_revisions = async_to_streamed_response_wrapper(
            landing_pages.list_folder_revisions,
        )
        self.list_folders = async_to_streamed_response_wrapper(
            landing_pages.list_folders,
        )
        self.list_revisions = async_to_streamed_response_wrapper(
            landing_pages.list_revisions,
        )
        self.publish_draft = async_to_streamed_response_wrapper(
            landing_pages.publish_draft,
        )
        self.rerun_ab_test = async_to_streamed_response_wrapper(
            landing_pages.rerun_ab_test,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            landing_pages.reset_draft,
        )
        self.restore_folder_revision = async_to_streamed_response_wrapper(
            landing_pages.restore_folder_revision,
        )
        self.restore_revision = async_to_streamed_response_wrapper(
            landing_pages.restore_revision,
        )
        self.restore_revision_to_draft = async_to_streamed_response_wrapper(
            landing_pages.restore_revision_to_draft,
        )
        self.schedule = async_to_streamed_response_wrapper(
            landing_pages.schedule,
        )
        self.set_new_lang_primary = async_to_streamed_response_wrapper(
            landing_pages.set_new_lang_primary,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            landing_pages.update_batch,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            landing_pages.update_draft,
        )
        self.update_folder = async_to_streamed_response_wrapper(
            landing_pages.update_folder,
        )
        self.update_folders_batch = async_to_streamed_response_wrapper(
            landing_pages.update_folders_batch,
        )
        self.update_languages = async_to_streamed_response_wrapper(
            landing_pages.update_languages,
        )
