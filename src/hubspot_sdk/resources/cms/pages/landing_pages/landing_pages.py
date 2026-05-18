# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .draft import (
    DraftResource,
    AsyncDraftResource,
    DraftResourceWithRawResponse,
    AsyncDraftResourceWithRawResponse,
    DraftResourceWithStreamingResponse,
    AsyncDraftResourceWithStreamingResponse,
)
from .ab_test import (
    AbTestResource,
    AsyncAbTestResource,
    AbTestResourceWithRawResponse,
    AsyncAbTestResourceWithRawResponse,
    AbTestResourceWithStreamingResponse,
    AsyncAbTestResourceWithStreamingResponse,
)
from .folders import (
    FoldersResource,
    AsyncFoldersResource,
    FoldersResourceWithRawResponse,
    AsyncFoldersResourceWithRawResponse,
    FoldersResourceWithStreamingResponse,
    AsyncFoldersResourceWithStreamingResponse,
)
from .revisions import (
    RevisionsResource,
    AsyncRevisionsResource,
    RevisionsResourceWithRawResponse,
    AsyncRevisionsResourceWithRawResponse,
    RevisionsResourceWithStreamingResponse,
    AsyncRevisionsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPage, AsyncPage
from .multi_language import (
    MultiLanguageResource,
    AsyncMultiLanguageResource,
    MultiLanguageResourceWithRawResponse,
    AsyncMultiLanguageResourceWithRawResponse,
    MultiLanguageResourceWithStreamingResponse,
    AsyncMultiLanguageResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cms.pages import (
    landing_page_get_params,
    landing_page_list_params,
    landing_page_clone_params,
    landing_page_create_params,
    landing_page_delete_params,
    landing_page_update_params,
    landing_page_schedule_params,
)
from .....types.cms.pages_page import PagesPage
from .....types.cms.layout_section_param import LayoutSectionParam
from .....types.cms.public_access_rule_param import PublicAccessRuleParam
from .....types.cms.content_language_variation_param import ContentLanguageVariationParam

__all__ = ["LandingPagesResource", "AsyncLandingPagesResource"]


class LandingPagesResource(SyncAPIResource):
    @cached_property
    def ab_test(self) -> AbTestResource:
        return AbTestResource(self._client)

    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def draft(self) -> DraftResource:
        return DraftResource(self._client)

    @cached_property
    def folders(self) -> FoldersResource:
        return FoldersResource(self._client)

    @cached_property
    def multi_language(self) -> MultiLanguageResource:
        return MultiLanguageResource(self._client)

    @cached_property
    def revisions(self) -> RevisionsResource:
        return RevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> LandingPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LandingPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LandingPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return LandingPagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        ab_status: Literal[
            "automated_loser_variant",
            "automated_master",
            "automated_variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "master",
            "variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0",
            "1",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "2",
            "20",
            "21",
            "22",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
            "AGENT_GENERATED",
            "AUTOMATED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "AUTOMATED_LOSER_ABVARIANT",
            "AUTOMATED_SENDING",
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
            "aa",
            "ab",
            "ae",
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "an",
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "av",
            "ay",
            "az",
            "az-az",
            "ba",
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
            "bgc",
            "bgc-in",
            "bho",
            "bho-in",
            "bi",
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
            "ch",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "co",
            "cr",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
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
            "dv",
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
            "en-id",
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
            "en-pt",
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
            "en-th",
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
            "en-vn",
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
            "fj",
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
            "frr",
            "frr-de",
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
            "gn",
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
            "he-il",
            "hi",
            "hi-in",
            "hmn",
            "ho",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "ht",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "hz",
            "ia",
            "ia-001",
            "id",
            "id-id",
            "ie",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "ik",
            "io",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "iu",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
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
            "kar",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kg",
            "kgp",
            "kgp-br",
            "kh",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kj",
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
            "kr",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ku",
            "ku-tr",
            "kv",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "la",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "li",
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
            "mdf",
            "mdf-ru",
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
            "mh",
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
            "na",
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
            "ng",
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
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nr",
            "nus",
            "nus-ss",
            "nv",
            "ny",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "oj",
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
            "pi",
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
            "sc",
            "sc-it",
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
            "sm",
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
            "ss",
            "st",
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
            "tn",
            "to",
            "to-to",
            "tok",
            "tok-001",
            "tr",
            "tr-cy",
            "tr-tr",
            "ts",
            "tt",
            "tt-ru",
            "tw",
            "twq",
            "twq-ne",
            "ty",
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
            "ve",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wa",
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
            "yi",
            "yi-001",
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
            "za",
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
    ) -> PagesPage:
        """
        Create a new landing page.

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

          content_group_id: The unique identifier for the content group associated with the page.

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created: The timestamp indicating when the page was created.

          created_by_id: The ID of the user that created this page.

          currently_published: Indicates whether the page is currently published.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

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

          layout_sections: A structure detailing the layout sections of the page.

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

          theme_settings_values: A collection of settings specific to the theme applied to the page.

          translated_from_id: ID of the primary page this object was translated from.

          translations: A map of translations for the page, each associated with a specific language
              variation.

          updated: The timestamp indicating when the page was last updated.

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
        return self._post(
            "/cms/pages/2026-03/landing-pages",
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
            cast_to=PagesPage,
        )

    def update(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "automated_loser_variant",
            "automated_master",
            "automated_variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "master",
            "variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0",
            "1",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "2",
            "20",
            "21",
            "22",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
            "AGENT_GENERATED",
            "AUTOMATED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "AUTOMATED_LOSER_ABVARIANT",
            "AUTOMATED_SENDING",
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
            "aa",
            "ab",
            "ae",
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "an",
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "av",
            "ay",
            "az",
            "az-az",
            "ba",
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
            "bgc",
            "bgc-in",
            "bho",
            "bho-in",
            "bi",
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
            "ch",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "co",
            "cr",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
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
            "dv",
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
            "en-id",
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
            "en-pt",
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
            "en-th",
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
            "en-vn",
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
            "fj",
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
            "frr",
            "frr-de",
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
            "gn",
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
            "he-il",
            "hi",
            "hi-in",
            "hmn",
            "ho",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "ht",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "hz",
            "ia",
            "ia-001",
            "id",
            "id-id",
            "ie",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "ik",
            "io",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "iu",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
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
            "kar",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kg",
            "kgp",
            "kgp-br",
            "kh",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kj",
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
            "kr",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ku",
            "ku-tr",
            "kv",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "la",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "li",
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
            "mdf",
            "mdf-ru",
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
            "mh",
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
            "na",
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
            "ng",
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
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nr",
            "nus",
            "nus-ss",
            "nv",
            "ny",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "oj",
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
            "pi",
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
            "sc",
            "sc-it",
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
            "sm",
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
            "ss",
            "st",
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
            "tn",
            "to",
            "to-to",
            "tok",
            "tok-001",
            "tr",
            "tr-cy",
            "tr-tr",
            "ts",
            "tt",
            "tt-ru",
            "tw",
            "twq",
            "twq-ne",
            "ty",
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
            "ve",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wa",
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
            "yi",
            "yi-001",
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
            "za",
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
    ) -> PagesPage:
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

          content_group_id: The unique identifier for the content group associated with the page.

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created: The timestamp indicating when the page was created.

          created_by_id: The ID of the user that created this page.

          currently_published: Indicates whether the page is currently published.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

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

          layout_sections: A structure detailing the layout sections of the page.

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

          theme_settings_values: A collection of settings specific to the theme applied to the page.

          translated_from_id: ID of the primary page this object was translated from.

          translations: A map of translations for the page, each associated with a specific language
              variation.

          updated: The timestamp indicating when the page was last updated.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
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
            cast_to=PagesPage,
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
    ) -> SyncPage[PagesPage]:
        """Retrieve a list of landing pages in your HubSpot account.

        This endpoint allows
        you to filter landing pages based on creation and update timestamps, sort them,
        and paginate through results. You can also choose to include archived pages or
        specify certain properties to be included in the response.

        Args:
          after: A cursor token for pagination. Use the value from the previous response's
              paging.next.after field.

          archived: Whether to return only results that have been archived.

          created_after: Filter landing pages created after a specific date and time.

          created_at: Filter landing pages by their creation timestamp.

          created_before: Filter landing pages created before a specific date and time.

          limit: The maximum number of results to display per page.

          property: Specify which properties of the landing pages to include in the response.

          sort: Specify the order in which results are returned. Accepts an array of strings.

          updated_after: Filter landing pages updated after a specific date and time.

          updated_at: Filter landing pages by their last updated timestamp.

          updated_before: Filter landing pages updated before a specific date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/pages/2026-03/landing-pages",
            page=SyncPage[PagesPage],
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
            model=PagesPage,
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
        Delete a landing page, specified by its ID.

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
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, landing_page_delete_params.LandingPageDeleteParams),
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
    ) -> PagesPage:
        """
        Create a copy of an existing landing page.

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/pages/2026-03/landing-pages/clone",
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
            cast_to=PagesPage,
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
    ) -> PagesPage:
        """
        Retrieve a landing page, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          property: A specific property of the landing page to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
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
            cast_to=PagesPage,
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
        Schedule a landing page to be published.

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
            "/cms/pages/2026-03/landing-pages/schedule",
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


class AsyncLandingPagesResource(AsyncAPIResource):
    @cached_property
    def ab_test(self) -> AsyncAbTestResource:
        return AsyncAbTestResource(self._client)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def draft(self) -> AsyncDraftResource:
        return AsyncDraftResource(self._client)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        return AsyncFoldersResource(self._client)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResource:
        return AsyncMultiLanguageResource(self._client)

    @cached_property
    def revisions(self) -> AsyncRevisionsResource:
        return AsyncRevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLandingPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLandingPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLandingPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/HubSpot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncLandingPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        ab_status: Literal[
            "automated_loser_variant",
            "automated_master",
            "automated_variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "master",
            "variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0",
            "1",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "2",
            "20",
            "21",
            "22",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
            "AGENT_GENERATED",
            "AUTOMATED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "AUTOMATED_LOSER_ABVARIANT",
            "AUTOMATED_SENDING",
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
            "aa",
            "ab",
            "ae",
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "an",
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "av",
            "ay",
            "az",
            "az-az",
            "ba",
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
            "bgc",
            "bgc-in",
            "bho",
            "bho-in",
            "bi",
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
            "ch",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "co",
            "cr",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
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
            "dv",
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
            "en-id",
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
            "en-pt",
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
            "en-th",
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
            "en-vn",
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
            "fj",
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
            "frr",
            "frr-de",
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
            "gn",
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
            "he-il",
            "hi",
            "hi-in",
            "hmn",
            "ho",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "ht",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "hz",
            "ia",
            "ia-001",
            "id",
            "id-id",
            "ie",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "ik",
            "io",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "iu",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
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
            "kar",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kg",
            "kgp",
            "kgp-br",
            "kh",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kj",
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
            "kr",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ku",
            "ku-tr",
            "kv",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "la",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "li",
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
            "mdf",
            "mdf-ru",
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
            "mh",
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
            "na",
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
            "ng",
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
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nr",
            "nus",
            "nus-ss",
            "nv",
            "ny",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "oj",
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
            "pi",
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
            "sc",
            "sc-it",
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
            "sm",
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
            "ss",
            "st",
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
            "tn",
            "to",
            "to-to",
            "tok",
            "tok-001",
            "tr",
            "tr-cy",
            "tr-tr",
            "ts",
            "tt",
            "tt-ru",
            "tw",
            "twq",
            "twq-ne",
            "ty",
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
            "ve",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wa",
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
            "yi",
            "yi-001",
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
            "za",
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
    ) -> PagesPage:
        """
        Create a new landing page.

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

          content_group_id: The unique identifier for the content group associated with the page.

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created: The timestamp indicating when the page was created.

          created_by_id: The ID of the user that created this page.

          currently_published: Indicates whether the page is currently published.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

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

          layout_sections: A structure detailing the layout sections of the page.

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

          theme_settings_values: A collection of settings specific to the theme applied to the page.

          translated_from_id: ID of the primary page this object was translated from.

          translations: A map of translations for the page, each associated with a specific language
              variation.

          updated: The timestamp indicating when the page was last updated.

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
        return await self._post(
            "/cms/pages/2026-03/landing-pages",
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
            cast_to=PagesPage,
        )

    async def update(
        self,
        object_id: str,
        *,
        id: str,
        ab_status: Literal[
            "automated_loser_variant",
            "automated_master",
            "automated_variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "master",
            "variant",
        ],
        ab_test_id: str,
        archived_at: Union[str, datetime],
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0",
            "1",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "2",
            "20",
            "21",
            "22",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ],
        created: Union[str, datetime],
        created_by_id: str,
        currently_published: bool,
        current_state: Literal[
            "AGENT_GENERATED",
            "AUTOMATED",
            "AUTOMATED_AB",
            "AUTOMATED_AB_VARIANT",
            "AUTOMATED_DRAFT",
            "AUTOMATED_DRAFT_AB",
            "AUTOMATED_DRAFT_ABVARIANT",
            "AUTOMATED_FOR_FORM",
            "AUTOMATED_FOR_FORM_BUFFER",
            "AUTOMATED_FOR_FORM_DRAFT",
            "AUTOMATED_FOR_FORM_LEGACY",
            "AUTOMATED_LOSER_ABVARIANT",
            "AUTOMATED_SENDING",
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
            "aa",
            "ab",
            "ae",
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "an",
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
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "av",
            "ay",
            "az",
            "az-az",
            "ba",
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
            "bgc",
            "bgc-in",
            "bho",
            "bho-in",
            "bi",
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
            "ch",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "co",
            "cr",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cv",
            "cv-ru",
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
            "dv",
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
            "en-id",
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
            "en-pt",
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
            "en-th",
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
            "en-vn",
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
            "fj",
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
            "frr",
            "frr-de",
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
            "gn",
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
            "he-il",
            "hi",
            "hi-in",
            "hmn",
            "ho",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "ht",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "hz",
            "ia",
            "ia-001",
            "id",
            "id-id",
            "ie",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "ik",
            "io",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "iu",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
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
            "kar",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "kg",
            "kgp",
            "kgp-br",
            "kh",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kj",
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
            "kr",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "ku",
            "ku-tr",
            "kv",
            "kw",
            "kw-gb",
            "ky",
            "ky-kg",
            "la",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "li",
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
            "mdf",
            "mdf-ru",
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
            "mh",
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
            "na",
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
            "ng",
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
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nr",
            "nus",
            "nus-ss",
            "nv",
            "ny",
            "nyn",
            "nyn-ug",
            "oc",
            "oc-es",
            "oc-fr",
            "oj",
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
            "pi",
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
            "sc",
            "sc-it",
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
            "sm",
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
            "ss",
            "st",
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
            "tn",
            "to",
            "to-to",
            "tok",
            "tok-001",
            "tr",
            "tr-cy",
            "tr-tr",
            "ts",
            "tt",
            "tt-ru",
            "tw",
            "twq",
            "twq-ne",
            "ty",
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
            "ve",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wa",
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
            "yi",
            "yi-001",
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
            "za",
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
    ) -> PagesPage:
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

          content_group_id: The unique identifier for the content group associated with the page.

          content_type_category: An ENUM descibing the type of this object. Should be either LANDING_PAGE or
              SITE_PAGE.

          created: The timestamp indicating when the page was created.

          created_by_id: The ID of the user that created this page.

          currently_published: Indicates whether the page is currently published.

          current_state: A generated ENUM descibing the current state of this page.

          domain: The domain this page will resolve to. If null, the page will default to the
              primary domain for this content type.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

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

          layout_sections: A structure detailing the layout sections of the page.

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

          theme_settings_values: A collection of settings specific to the theme applied to the page.

          translated_from_id: ID of the primary page this object was translated from.

          translations: A map of translations for the page, each associated with a specific language
              variation.

          updated: The timestamp indicating when the page was last updated.

          updated_by_id: The ID of the user that updated this page.

          url: A generated field representing the URL of this page.

          use_featured_image: Boolean to determine if this page should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this page. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
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
            cast_to=PagesPage,
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
    ) -> AsyncPaginator[PagesPage, AsyncPage[PagesPage]]:
        """Retrieve a list of landing pages in your HubSpot account.

        This endpoint allows
        you to filter landing pages based on creation and update timestamps, sort them,
        and paginate through results. You can also choose to include archived pages or
        specify certain properties to be included in the response.

        Args:
          after: A cursor token for pagination. Use the value from the previous response's
              paging.next.after field.

          archived: Whether to return only results that have been archived.

          created_after: Filter landing pages created after a specific date and time.

          created_at: Filter landing pages by their creation timestamp.

          created_before: Filter landing pages created before a specific date and time.

          limit: The maximum number of results to display per page.

          property: Specify which properties of the landing pages to include in the response.

          sort: Specify the order in which results are returned. Accepts an array of strings.

          updated_after: Filter landing pages updated after a specific date and time.

          updated_at: Filter landing pages by their last updated timestamp.

          updated_before: Filter landing pages updated before a specific date and time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/pages/2026-03/landing-pages",
            page=AsyncPage[PagesPage],
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
            model=PagesPage,
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
        Delete a landing page, specified by its ID.

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
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
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
    ) -> PagesPage:
        """
        Create a copy of an existing landing page.

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/pages/2026-03/landing-pages/clone",
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
            cast_to=PagesPage,
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
    ) -> PagesPage:
        """
        Retrieve a landing page, specified by its ID.

        Args:
          archived: Whether to return only results that have been archived.

          property: A specific property of the landing page to include in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            path_template("/cms/pages/2026-03/landing-pages/{object_id}", object_id=object_id),
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
            cast_to=PagesPage,
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
        Schedule a landing page to be published.

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
            "/cms/pages/2026-03/landing-pages/schedule",
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
        self.clone = to_raw_response_wrapper(
            landing_pages.clone,
        )
        self.get = to_raw_response_wrapper(
            landing_pages.get,
        )
        self.schedule = to_raw_response_wrapper(
            landing_pages.schedule,
        )

    @cached_property
    def ab_test(self) -> AbTestResourceWithRawResponse:
        return AbTestResourceWithRawResponse(self._landing_pages.ab_test)

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._landing_pages.batch)

    @cached_property
    def draft(self) -> DraftResourceWithRawResponse:
        return DraftResourceWithRawResponse(self._landing_pages.draft)

    @cached_property
    def folders(self) -> FoldersResourceWithRawResponse:
        return FoldersResourceWithRawResponse(self._landing_pages.folders)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithRawResponse:
        return MultiLanguageResourceWithRawResponse(self._landing_pages.multi_language)

    @cached_property
    def revisions(self) -> RevisionsResourceWithRawResponse:
        return RevisionsResourceWithRawResponse(self._landing_pages.revisions)


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
        self.clone = async_to_raw_response_wrapper(
            landing_pages.clone,
        )
        self.get = async_to_raw_response_wrapper(
            landing_pages.get,
        )
        self.schedule = async_to_raw_response_wrapper(
            landing_pages.schedule,
        )

    @cached_property
    def ab_test(self) -> AsyncAbTestResourceWithRawResponse:
        return AsyncAbTestResourceWithRawResponse(self._landing_pages.ab_test)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._landing_pages.batch)

    @cached_property
    def draft(self) -> AsyncDraftResourceWithRawResponse:
        return AsyncDraftResourceWithRawResponse(self._landing_pages.draft)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithRawResponse:
        return AsyncFoldersResourceWithRawResponse(self._landing_pages.folders)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithRawResponse:
        return AsyncMultiLanguageResourceWithRawResponse(self._landing_pages.multi_language)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithRawResponse:
        return AsyncRevisionsResourceWithRawResponse(self._landing_pages.revisions)


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
        self.clone = to_streamed_response_wrapper(
            landing_pages.clone,
        )
        self.get = to_streamed_response_wrapper(
            landing_pages.get,
        )
        self.schedule = to_streamed_response_wrapper(
            landing_pages.schedule,
        )

    @cached_property
    def ab_test(self) -> AbTestResourceWithStreamingResponse:
        return AbTestResourceWithStreamingResponse(self._landing_pages.ab_test)

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._landing_pages.batch)

    @cached_property
    def draft(self) -> DraftResourceWithStreamingResponse:
        return DraftResourceWithStreamingResponse(self._landing_pages.draft)

    @cached_property
    def folders(self) -> FoldersResourceWithStreamingResponse:
        return FoldersResourceWithStreamingResponse(self._landing_pages.folders)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithStreamingResponse:
        return MultiLanguageResourceWithStreamingResponse(self._landing_pages.multi_language)

    @cached_property
    def revisions(self) -> RevisionsResourceWithStreamingResponse:
        return RevisionsResourceWithStreamingResponse(self._landing_pages.revisions)


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
        self.clone = async_to_streamed_response_wrapper(
            landing_pages.clone,
        )
        self.get = async_to_streamed_response_wrapper(
            landing_pages.get,
        )
        self.schedule = async_to_streamed_response_wrapper(
            landing_pages.schedule,
        )

    @cached_property
    def ab_test(self) -> AsyncAbTestResourceWithStreamingResponse:
        return AsyncAbTestResourceWithStreamingResponse(self._landing_pages.ab_test)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._landing_pages.batch)

    @cached_property
    def draft(self) -> AsyncDraftResourceWithStreamingResponse:
        return AsyncDraftResourceWithStreamingResponse(self._landing_pages.draft)

    @cached_property
    def folders(self) -> AsyncFoldersResourceWithStreamingResponse:
        return AsyncFoldersResourceWithStreamingResponse(self._landing_pages.folders)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithStreamingResponse:
        return AsyncMultiLanguageResourceWithStreamingResponse(self._landing_pages.multi_language)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithStreamingResponse:
        return AsyncRevisionsResourceWithStreamingResponse(self._landing_pages.revisions)
