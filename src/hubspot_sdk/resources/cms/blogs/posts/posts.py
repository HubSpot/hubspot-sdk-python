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
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .multi_language import (
    MultiLanguageResource,
    AsyncMultiLanguageResource,
    MultiLanguageResourceWithRawResponse,
    AsyncMultiLanguageResourceWithRawResponse,
    MultiLanguageResourceWithStreamingResponse,
    AsyncMultiLanguageResourceWithStreamingResponse,
)
from ....._base_client import make_request_options
from .....types.cms.blogs import (
    post_get_params,
    post_list_params,
    post_clone_params,
    post_query_params,
    post_create_params,
    post_delete_params,
    post_update_params,
    post_schedule_params,
    post_list_tags_params,
    post_query_tags_params,
    post_list_authors_params,
    post_update_draft_params,
    post_query_authors_params,
)
from .....types.cms.layout_section_param import LayoutSectionParam
from .....types.cms.public_access_rule_param import PublicAccessRuleParam
from .....types.cms.content_language_variation_param import ContentLanguageVariationParam

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def multi_language(self) -> MultiLanguageResource:
        return MultiLanguageResource(self._client)

    @cached_property
    def revisions(self) -> RevisionsResource:
        return RevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> BinaryAPIResponse:
        """
        Create a new blog post, specifying its content in the request body.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/posts",
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> BinaryAPIResponse:
        """Partially updates a single blog post by ID.

        You only need to specify the values
        that you want to update.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, post_update_params.PostUpdateParams),
            ),
            cast_to=BinaryAPIResponse,
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/posts/cursor",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
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
        Delete a blog post by ID.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, post_delete_params.PostDeleteParams),
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
    ) -> BinaryAPIResponse:
        """
        Clone a blog post, making a copy of it in a new blog post.

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/blogs/2026-03/posts/clone",
            body=maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                },
                post_clone_params.PostCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
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
    ) -> BinaryAPIResponse:
        """
        Retrieve a blog post by the post ID.

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
        return self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
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
                    post_get_params.PostGetParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_draft_by_id(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Retrieve the full draft version of a blog post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_authors(
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/authors/cursor",
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
                    post_list_authors_params.PostListAuthorsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_tags(
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/tags/cursor",
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
                    post_list_tags_params.PostListTagsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def push_live(
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
        Publish the draft version of the blog post, sending its content to the live
        page.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft/push-live", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/posts/cursor/query",
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
                    post_query_params.PostQueryParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def query_authors(
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/authors/cursor/query",
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
                    post_query_authors_params.PostQueryAuthorsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def query_tags(
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
    ) -> BinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/cms/blogs/2026-03/tags/cursor/query",
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
                    post_query_tags_params.PostQueryTagsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
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
        Discard all drafted content, resetting the draft to contain the content in the
        currently published version.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft/reset", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Schedule a blog post to be published at a specified time.

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
            "/cms/blogs/2026-03/posts/schedule",
            body=maybe_transform(
                {
                    "id": id,
                    "publish_date": publish_date,
                },
                post_schedule_params.PostScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_draft(
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> BinaryAPIResponse:
        """Partially updates the draft version of a single blog post by ID.

        You only need
        to specify the values that you want to update.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft", object_id=object_id),
            body=maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_update_draft_params.PostUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResource:
        return AsyncMultiLanguageResource(self._client)

    @cached_property
    def revisions(self) -> AsyncRevisionsResource:
        return AsyncRevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> AsyncBinaryAPIResponse:
        """
        Create a new blog post, specifying its content in the request body.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/posts",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> AsyncBinaryAPIResponse:
        """Partially updates a single blog post by ID.

        You only need to specify the values
        that you want to update.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, post_update_params.PostUpdateParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/posts/cursor",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
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
        Delete a blog post by ID.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, post_delete_params.PostDeleteParams),
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
    ) -> AsyncBinaryAPIResponse:
        """
        Clone a blog post, making a copy of it in a new blog post.

        Args:
          id: ID of the object to be cloned.

          clone_name: Name of the cloned object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/blogs/2026-03/posts/clone",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "clone_name": clone_name,
                },
                post_clone_params.PostCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
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
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve a blog post by the post ID.

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
        return await self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}", object_id=object_id),
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
                    post_get_params.PostGetParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_draft_by_id(
        self,
        object_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Retrieve the full draft version of a blog post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_authors(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/authors/cursor",
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
                    post_list_authors_params.PostListAuthorsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_tags(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/tags/cursor",
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
                    post_list_tags_params.PostListTagsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def push_live(
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
        Publish the draft version of the blog post, sending its content to the live
        page.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft/push-live", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/posts/cursor/query",
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
                    post_query_params.PostQueryParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def query_authors(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/authors/cursor/query",
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
                    post_query_authors_params.PostQueryAuthorsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def query_tags(
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
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          after: The paging cursor token of the last successfully read resource will be returned
              as the `paging.next.after` JSON property of a paged response containing more
              results.

          archived: Whether to return only results that have been archived.

          limit: The maximum number of results to display per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/cms/blogs/2026-03/tags/cursor/query",
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
                    post_query_tags_params.PostQueryTagsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
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
        Discard all drafted content, resetting the draft to contain the content in the
        currently published version.

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
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft/reset", object_id=object_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Schedule a blog post to be published at a specified time.

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
            "/cms/blogs/2026-03/posts/schedule",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "publish_date": publish_date,
                },
                post_schedule_params.PostScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_draft(
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
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
        enable_google_amp_output_override: bool,
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
        password: str,
        post_body: str,
        post_summary: str,
        public_access_rules: Iterable[PublicAccessRuleParam],
        public_access_rules_enabled: bool,
        publish_date: Union[str, datetime],
        publish_immediately: bool,
        rss_body: str,
        rss_summary: str,
        slug: str,
        state: str,
        tag_ids: Iterable[int],
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
    ) -> AsyncBinaryAPIResponse:
        """Partially updates the draft version of a single blog post by ID.

        You only need
        to specify the values that you want to update.

        Args:
          id: The unique ID of the Blog Post.

          ab_status: The status of the AB test associated with this blog post, if applicable

              Available options: automated_loser_variant, automated_master, automated_variant,
              loser_variant, mab_master, mab_variant, master, variant

          ab_test_id: The ID of the AB test associated with this page, if applicable

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the user that updated this Blog Post.

          blog_author_id: The ID of the Blog Author associated with this Blog Post.

          campaign: The GUID of the marketing campaign this Blog Post is a part of.

          category_id: ID of the type of object this is. Should always .

          content_group_id: The ID of the parent Blog this Blog Post is associated with.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created: The timestamp (ISO8601 format) when this Blog Post was created.

          created_by_id: The ID of the user that created this Blog Post.

          currently_published: Whether the post is published (true or false)

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain this Blog Post will resolve to. If null, the Blog Post will default
              to the domain of the ParentBlog.

          dynamic_page_data_source_id: The identifier for the data source used by the dynamic page.

          dynamic_page_data_source_type: The type of data source used by the dynamic page.

          dynamic_page_hub_db_table_id: The ID of the HubDB table this Blog Post references, if applicable

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          folder_id: Unique identifier of associated folder

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The html title of this Blog Post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the Blog Post. If null, the Blog
              Post will default to the language of the ParentBlog.

          layout_sections: A structure detailing the layout sections of the blog post.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          mab_experiment_id: Unique identifier of the MAB Experiment

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the Blog Post.

          page_expiry_date: The date at which this blog post should expire and begin redirecting to another
              url or page.

          page_expiry_enabled: Boolean describing if the page expiration feature is enabled for this blog post.

          page_expiry_redirect_id: The ID of another page this blog post's url should redirect to once this blog
              post expires. Should only set this or pageExpiryRedirectUrl.

          page_expiry_redirect_url: The URL this blog post's url should redirect to once it expires. Should only set
              this or pageExpiryRedirectId.

          password: Set this to create a password protected page. Entering the password will be
              required to view the page.

          post_body: The HTML of the main post body.

          post_summary: The summary of the blog post that will appear on the main listing page.

          public_access_rules: Rules for require member registration to access private content.

          public_access_rules_enabled: Boolean to determine whether or not to respect publicAccessRules.

          publish_date: The date (ISO8601 format) the blog post is to be published at.

          publish_immediately: Set this to true if you want to be published immediately when the schedule
              publish endpoint is called, and to ignore the publish_date setting.

          rss_body: The contents of the RSS body for this Blog Post.

          rss_summary: The contents of the RSS summary for this Blog Post.

          slug: The path of the this blog post. This field is appended to the domain to
              construct the url of this post.

          state: An ENUM descibing the current state of this Blog Post.

          tag_ids: List of IDs for the tags associated with this Blog Post.

          theme_settings_values: A collection of settings specific to the theme applied to the blog post.

          translated_from_id: ID of the primary blog post this object was translated from.

          translations: A map of translations for the blog post, each associated with a specific
              language variation.

          updated: The timestamp (ISO8601 format) when this Blog Post was updated.

          updated_by_id: The ID of the user that updated this Blog Post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featuredImage.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/cms/blogs/2026-03/posts/{object_id}/draft", object_id=object_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "ab_status": ab_status,
                    "ab_test_id": ab_test_id,
                    "archived_at": archived_at,
                    "archived_in_dashboard": archived_in_dashboard,
                    "attached_stylesheets": attached_stylesheets,
                    "author_name": author_name,
                    "blog_author_id": blog_author_id,
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
                    "enable_google_amp_output_override": enable_google_amp_output_override,
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
                    "password": password,
                    "post_body": post_body,
                    "post_summary": post_summary,
                    "public_access_rules": public_access_rules,
                    "public_access_rules_enabled": public_access_rules_enabled,
                    "publish_date": publish_date,
                    "publish_immediately": publish_immediately,
                    "rss_body": rss_body,
                    "rss_summary": rss_summary,
                    "slug": slug,
                    "state": state,
                    "tag_ids": tag_ids,
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
                post_update_draft_params.PostUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_custom_raw_response_wrapper(
            posts.create,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            posts.update,
            BinaryAPIResponse,
        )
        self.list = to_custom_raw_response_wrapper(
            posts.list,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.clone = to_custom_raw_response_wrapper(
            posts.clone,
            BinaryAPIResponse,
        )
        self.get = to_custom_raw_response_wrapper(
            posts.get,
            BinaryAPIResponse,
        )
        self.get_draft_by_id = to_custom_raw_response_wrapper(
            posts.get_draft_by_id,
            BinaryAPIResponse,
        )
        self.list_authors = to_custom_raw_response_wrapper(
            posts.list_authors,
            BinaryAPIResponse,
        )
        self.list_tags = to_custom_raw_response_wrapper(
            posts.list_tags,
            BinaryAPIResponse,
        )
        self.push_live = to_raw_response_wrapper(
            posts.push_live,
        )
        self.query = to_custom_raw_response_wrapper(
            posts.query,
            BinaryAPIResponse,
        )
        self.query_authors = to_custom_raw_response_wrapper(
            posts.query_authors,
            BinaryAPIResponse,
        )
        self.query_tags = to_custom_raw_response_wrapper(
            posts.query_tags,
            BinaryAPIResponse,
        )
        self.reset_draft = to_raw_response_wrapper(
            posts.reset_draft,
        )
        self.schedule = to_raw_response_wrapper(
            posts.schedule,
        )
        self.update_draft = to_custom_raw_response_wrapper(
            posts.update_draft,
            BinaryAPIResponse,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._posts.batch)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithRawResponse:
        return MultiLanguageResourceWithRawResponse(self._posts.multi_language)

    @cached_property
    def revisions(self) -> RevisionsResourceWithRawResponse:
        return RevisionsResourceWithRawResponse(self._posts.revisions)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_custom_raw_response_wrapper(
            posts.create,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            posts.update,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_custom_raw_response_wrapper(
            posts.list,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.clone = async_to_custom_raw_response_wrapper(
            posts.clone,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_custom_raw_response_wrapper(
            posts.get,
            AsyncBinaryAPIResponse,
        )
        self.get_draft_by_id = async_to_custom_raw_response_wrapper(
            posts.get_draft_by_id,
            AsyncBinaryAPIResponse,
        )
        self.list_authors = async_to_custom_raw_response_wrapper(
            posts.list_authors,
            AsyncBinaryAPIResponse,
        )
        self.list_tags = async_to_custom_raw_response_wrapper(
            posts.list_tags,
            AsyncBinaryAPIResponse,
        )
        self.push_live = async_to_raw_response_wrapper(
            posts.push_live,
        )
        self.query = async_to_custom_raw_response_wrapper(
            posts.query,
            AsyncBinaryAPIResponse,
        )
        self.query_authors = async_to_custom_raw_response_wrapper(
            posts.query_authors,
            AsyncBinaryAPIResponse,
        )
        self.query_tags = async_to_custom_raw_response_wrapper(
            posts.query_tags,
            AsyncBinaryAPIResponse,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            posts.reset_draft,
        )
        self.schedule = async_to_raw_response_wrapper(
            posts.schedule,
        )
        self.update_draft = async_to_custom_raw_response_wrapper(
            posts.update_draft,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._posts.batch)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithRawResponse:
        return AsyncMultiLanguageResourceWithRawResponse(self._posts.multi_language)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithRawResponse:
        return AsyncRevisionsResourceWithRawResponse(self._posts.revisions)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_custom_streamed_response_wrapper(
            posts.create,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            posts.update,
            StreamedBinaryAPIResponse,
        )
        self.list = to_custom_streamed_response_wrapper(
            posts.list,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.clone = to_custom_streamed_response_wrapper(
            posts.clone,
            StreamedBinaryAPIResponse,
        )
        self.get = to_custom_streamed_response_wrapper(
            posts.get,
            StreamedBinaryAPIResponse,
        )
        self.get_draft_by_id = to_custom_streamed_response_wrapper(
            posts.get_draft_by_id,
            StreamedBinaryAPIResponse,
        )
        self.list_authors = to_custom_streamed_response_wrapper(
            posts.list_authors,
            StreamedBinaryAPIResponse,
        )
        self.list_tags = to_custom_streamed_response_wrapper(
            posts.list_tags,
            StreamedBinaryAPIResponse,
        )
        self.push_live = to_streamed_response_wrapper(
            posts.push_live,
        )
        self.query = to_custom_streamed_response_wrapper(
            posts.query,
            StreamedBinaryAPIResponse,
        )
        self.query_authors = to_custom_streamed_response_wrapper(
            posts.query_authors,
            StreamedBinaryAPIResponse,
        )
        self.query_tags = to_custom_streamed_response_wrapper(
            posts.query_tags,
            StreamedBinaryAPIResponse,
        )
        self.reset_draft = to_streamed_response_wrapper(
            posts.reset_draft,
        )
        self.schedule = to_streamed_response_wrapper(
            posts.schedule,
        )
        self.update_draft = to_custom_streamed_response_wrapper(
            posts.update_draft,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._posts.batch)

    @cached_property
    def multi_language(self) -> MultiLanguageResourceWithStreamingResponse:
        return MultiLanguageResourceWithStreamingResponse(self._posts.multi_language)

    @cached_property
    def revisions(self) -> RevisionsResourceWithStreamingResponse:
        return RevisionsResourceWithStreamingResponse(self._posts.revisions)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_custom_streamed_response_wrapper(
            posts.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            posts.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_custom_streamed_response_wrapper(
            posts.list,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.clone = async_to_custom_streamed_response_wrapper(
            posts.clone,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_custom_streamed_response_wrapper(
            posts.get,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_draft_by_id = async_to_custom_streamed_response_wrapper(
            posts.get_draft_by_id,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_authors = async_to_custom_streamed_response_wrapper(
            posts.list_authors,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_tags = async_to_custom_streamed_response_wrapper(
            posts.list_tags,
            AsyncStreamedBinaryAPIResponse,
        )
        self.push_live = async_to_streamed_response_wrapper(
            posts.push_live,
        )
        self.query = async_to_custom_streamed_response_wrapper(
            posts.query,
            AsyncStreamedBinaryAPIResponse,
        )
        self.query_authors = async_to_custom_streamed_response_wrapper(
            posts.query_authors,
            AsyncStreamedBinaryAPIResponse,
        )
        self.query_tags = async_to_custom_streamed_response_wrapper(
            posts.query_tags,
            AsyncStreamedBinaryAPIResponse,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            posts.reset_draft,
        )
        self.schedule = async_to_streamed_response_wrapper(
            posts.schedule,
        )
        self.update_draft = async_to_custom_streamed_response_wrapper(
            posts.update_draft,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._posts.batch)

    @cached_property
    def multi_language(self) -> AsyncMultiLanguageResourceWithStreamingResponse:
        return AsyncMultiLanguageResourceWithStreamingResponse(self._posts.multi_language)

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithStreamingResponse:
        return AsyncRevisionsResourceWithStreamingResponse(self._posts.revisions)
