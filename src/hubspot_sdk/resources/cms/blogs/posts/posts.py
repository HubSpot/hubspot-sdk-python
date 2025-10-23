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
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPage, AsyncPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cms.blogs import (
    post_list_params,
    post_read_params,
    post_clone_params,
    post_create_params,
    post_delete_params,
    post_update_params,
    post_schedule_params,
    post_update_draft_params,
    post_update_langs_params,
    post_set_lang_primary_params,
    post_attach_to_lang_group_params,
    post_create_lang_variation_params,
    post_get_previous_versions_params,
    post_detach_from_lang_group_params,
)
from .....types.cms.blogs.blog_post import BlogPost
from .....types.cms.layout_section_param import LayoutSectionParam
from .....types.cms.blogs.version_blog_post import VersionBlogPost
from .....types.cms.public_access_rule_param import PublicAccessRuleParam
from .....types.cms.content_language_variation_param import ContentLanguageVariationParam

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """
        Create a new blog post, specifying its content in the request body.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/blogs/posts",
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
            cast_to=BlogPost,
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """Partially updates a single blog post by ID.

        You only need to specify the values
        that you want to update.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Specifies whether to update deleted blog posts. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._patch(
            f"/cms/v3/blogs/posts/{object_id}",
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
            cast_to=BlogPost,
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
    ) -> SyncPage[BlogPost]:
        """Retrieve all blog posts, with paging and filtering options.

        This method would be
        useful for an integration that ingests posts and suggests edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted blog posts. Defaults to `false`.

          created_after: Only return blog posts created after the specified time.

          created_at: Only return blog posts created at exactly the specified time.

          created_before: Only return blog posts created before the specified time.

          limit: The maximum number of results to return. Default is 20.

          sort: Specifies which fields to use for sorting results. Valid fields are `createdAt`
              (default), `name`, `updatedAt`, `createdBy`, `updatedBy`.

          updated_after: Only return blog posts last updated after the specified time.

          updated_at: Only return blog posts last updated at exactly the specified time.

          updated_before: Only return blog posts last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/blogs/posts",
            page=SyncPage[BlogPost],
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
            model=BlogPost,
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
          archived: Whether to return only results that have been deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/blogs/posts/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, post_delete_params.PostDeleteParams),
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
        Attach a blog post to a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

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
            "/cms/v3/blogs/posts/multi-language/attach-to-lang-group",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                post_attach_to_lang_group_params.PostAttachToLangGroupParams,
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
    ) -> BlogPost:
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
        return self._post(
            "/cms/v3/blogs/posts/clone",
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
            cast_to=BlogPost,
        )

    def create_lang_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlogPost:
        """
        Create a new language variation from an existing blog post

        Args:
          id: ID of blog post to clone.

          language: Target language of new variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/blogs/posts/multi-language/create-language-variation",
            body=maybe_transform(
                {
                    "id": id,
                    "language": language,
                },
                post_create_lang_variation_params.PostCreateLangVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
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
        Detach a blog post from a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/cms/v3/blogs/posts/multi-language/detach-from-lang-group",
            body=maybe_transform({"id": id}, post_detach_from_lang_group_params.PostDetachFromLangGroupParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> BlogPost:
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
        return self._get(
            f"/cms/v3/blogs/posts/{object_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
        )

    def get_previous_version(
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
    ) -> VersionBlogPost:
        """
        Retrieve a previous version of a blog post.

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
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionBlogPost,
        )

    def get_previous_versions(
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
    ) -> SyncPage[VersionBlogPost]:
        """
        Retrieve all the previous versions of a blog post.

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
        return self._get_api_list(
            f"/cms/v3/blogs/posts/{object_id}/revisions",
            page=SyncPage[VersionBlogPost],
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
                    post_get_previous_versions_params.PostGetPreviousVersionsParams,
                ),
            ),
            model=VersionBlogPost,
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
            f"/cms/v3/blogs/posts/{object_id}/draft/push-live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
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
    ) -> BlogPost:
        """
        Retrieve a blog post by the post ID.

        Args:
          archived: Specifies whether to return deleted blog posts. Defaults to `false`.

          property: Specific properties to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._get(
            f"/cms/v3/blogs/posts/{object_id}",
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
                    post_read_params.PostReadParams,
                ),
            ),
            cast_to=BlogPost,
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
            f"/cms/v3/blogs/posts/{object_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def restore_previous_version(
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
    ) -> BlogPost:
        """
        Restores a blog post to one of its previous versions.

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
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
        )

    def restore_previous_version_to_draft(
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
    ) -> BlogPost:
        """
        Takes a specified version of a blog post, sets it as the new draft version of
        the blog post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return self._post(
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
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
            "/cms/v3/blogs/posts/schedule",
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

    def set_lang_primary(
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
        Set the primary language of a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content)
        to the language of the provided post (specified as an ID in the request body)

        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            "/cms/v3/blogs/posts/multi-language/set-new-lang-primary",
            body=maybe_transform({"id": id}, post_set_lang_primary_params.PostSetLangPrimaryParams),
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """Partially updates the draft version of a single blog post by ID.

        You only need
        to specify the values that you want to update.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

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
        return self._patch(
            f"/cms/v3/blogs/posts/{object_id}/draft",
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
            cast_to=BlogPost,
        )

    def update_langs(
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
        Explicitly set new languages for each post in a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

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
            "/cms/v3/blogs/posts/multi-language/update-languages",
            body=maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                post_update_langs_params.PostUpdateLangsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPostsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """
        Create a new blog post, specifying its content in the request body.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/blogs/posts",
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
            cast_to=BlogPost,
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """Partially updates a single blog post by ID.

        You only need to specify the values
        that you want to update.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

          widget_containers: A data structure containing the data for all the modules inside the containers
              for this post. This will only be populated if the page has widget containers.

          widgets: A data structure containing the data for all the modules for this page.

          archived: Specifies whether to update deleted blog posts. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._patch(
            f"/cms/v3/blogs/posts/{object_id}",
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
            cast_to=BlogPost,
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
    ) -> AsyncPaginator[BlogPost, AsyncPage[BlogPost]]:
        """Retrieve all blog posts, with paging and filtering options.

        This method would be
        useful for an integration that ingests posts and suggests edits.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return deleted blog posts. Defaults to `false`.

          created_after: Only return blog posts created after the specified time.

          created_at: Only return blog posts created at exactly the specified time.

          created_before: Only return blog posts created before the specified time.

          limit: The maximum number of results to return. Default is 20.

          sort: Specifies which fields to use for sorting results. Valid fields are `createdAt`
              (default), `name`, `updatedAt`, `createdBy`, `updatedBy`.

          updated_after: Only return blog posts last updated after the specified time.

          updated_at: Only return blog posts last updated at exactly the specified time.

          updated_before: Only return blog posts last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/blogs/posts",
            page=AsyncPage[BlogPost],
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
            model=BlogPost,
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
          archived: Whether to return only results that have been deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/blogs/posts/{object_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, post_delete_params.PostDeleteParams),
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
        Attach a blog post to a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

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
            "/cms/v3/blogs/posts/multi-language/attach-to-lang-group",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                    "primary_id": primary_id,
                    "primary_language": primary_language,
                },
                post_attach_to_lang_group_params.PostAttachToLangGroupParams,
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
    ) -> BlogPost:
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
        return await self._post(
            "/cms/v3/blogs/posts/clone",
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
            cast_to=BlogPost,
        )

    async def create_lang_variation(
        self,
        *,
        id: str,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlogPost:
        """
        Create a new language variation from an existing blog post

        Args:
          id: ID of blog post to clone.

          language: Target language of new variant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/blogs/posts/multi-language/create-language-variation",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "language": language,
                },
                post_create_lang_variation_params.PostCreateLangVariationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
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
        Detach a blog post from a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

        Args:
          id: ID of the object to remove from a multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/cms/v3/blogs/posts/multi-language/detach-from-lang-group",
            body=await async_maybe_transform(
                {"id": id}, post_detach_from_lang_group_params.PostDetachFromLangGroupParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> BlogPost:
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
        return await self._get(
            f"/cms/v3/blogs/posts/{object_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
        )

    async def get_previous_version(
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
    ) -> VersionBlogPost:
        """
        Retrieve a previous version of a blog post.

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
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionBlogPost,
        )

    def get_previous_versions(
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
    ) -> AsyncPaginator[VersionBlogPost, AsyncPage[VersionBlogPost]]:
        """
        Retrieve all the previous versions of a blog post.

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
        return self._get_api_list(
            f"/cms/v3/blogs/posts/{object_id}/revisions",
            page=AsyncPage[VersionBlogPost],
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
                    post_get_previous_versions_params.PostGetPreviousVersionsParams,
                ),
            ),
            model=VersionBlogPost,
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
            f"/cms/v3/blogs/posts/{object_id}/draft/push-live",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
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
    ) -> BlogPost:
        """
        Retrieve a blog post by the post ID.

        Args:
          archived: Specifies whether to return deleted blog posts. Defaults to `false`.

          property: Specific properties to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._get(
            f"/cms/v3/blogs/posts/{object_id}",
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
                    post_read_params.PostReadParams,
                ),
            ),
            cast_to=BlogPost,
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
            f"/cms/v3/blogs/posts/{object_id}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def restore_previous_version(
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
    ) -> BlogPost:
        """
        Restores a blog post to one of its previous versions.

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
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}/restore",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
        )

    async def restore_previous_version_to_draft(
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
    ) -> BlogPost:
        """
        Takes a specified version of a blog post, sets it as the new draft version of
        the blog post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        return await self._post(
            f"/cms/v3/blogs/posts/{object_id}/revisions/{revision_id}/restore-to-draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlogPost,
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
            "/cms/v3/blogs/posts/schedule",
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

    async def set_lang_primary(
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
        Set the primary language of a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content)
        to the language of the provided post (specified as an ID in the request body)

        Args:
          id: ID of object to set as primary in multi-language group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            "/cms/v3/blogs/posts/multi-language/set-new-lang-primary",
            body=await async_maybe_transform({"id": id}, post_set_lang_primary_params.PostSetLangPrimaryParams),
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
        archived_at: int,
        archived_in_dashboard: bool,
        attached_stylesheets: Iterable[Dict[str, object]],
        author_name: str,
        blog_author_id: str,
        campaign: str,
        category_id: int,
        content_group_id: str,
        content_type_category: Literal[
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"
        ],
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
            "en-ee",
            "en-er",
            "en-fr",
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
    ) -> BlogPost:
        """Partially updates the draft version of a single blog post by ID.

        You only need
        to specify the values that you want to update.

        Args:
          id: The unique ID of the blog post.

          archived_at: The timestamp (ISO8601 format) when this Blog Post was deleted.

          archived_in_dashboard: If True, the post will not show up in your dashboard, although the post could
              still be live.

          attached_stylesheets: List of stylesheets to attach to this blog post. These stylesheets are attached
              to just this page. Order of precedence is bottom to top, just like in the HTML.

          author_name: The name of the blog author associated with the post.

          blog_author_id: The ID of the blog author associated with this post.

          campaign: The GUID of the marketing campaign the post is associated with.

          category_id: ID of the object type.

          content_group_id: The ID of the post's parent blog.

          content_type_category: An ENUM descibing the type of this object. Should always be BLOG_POST.

          created_by_id: The ID of the user that created the post.

          current_state: A generated ENUM descibing the current state of this Blog Post. Should always
              match state.

          domain: The domain that the post lives on. If null, the post will default to the domain
              of the parent blog.

          dynamic_page_hub_db_table_id: For dynamic HubDB pages, the ID of the HubDB table this post references.

          enable_domain_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          enable_google_amp_output_override: Boolean to allow overriding the AMP settings for the blog.

          enable_layout_stylesheets: Boolean to determine whether or not the styles from the template should be
              applied.

          featured_image: The featuredImage of this Blog Post.

          featured_image_alt_text: Alt Text of the featuredImage.

          footer_html: Custom HTML for embed codes, javascript that should be placed before the </body>
              tag of the page.

          head_html: Custom HTML for embed codes, javascript, etc. that goes in the <head> tag of the
              page.

          html_title: The HTML title of the post.

          include_default_custom_css: Boolean to determine whether or not the Primary CSS Files should be applied.

          language: The explicitly defined ISO 639 language code of the post. If null, the post will
              default to the language of the parent blog.

          link_rel_canonical_url: Optional override to set the URL to be used in the rel=canonical link tag on the
              page.

          meta_description: A description that goes in <meta> tag on the page.

          name: The internal name of the post.

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

          slug: The URL slug of the blog post. This field is appended to the domain to construct
              the url of this post.

          state: An enumeration describing the current publish state of the post.

          tag_ids: The IDs of the tags associated with this post.

          translated_from_id: ID of the primary blog post that this post was translated from.

          updated_by_id: The ID of the user that updated the post.

          url: A generated field representing the URL of this blog post.

          use_featured_image: Boolean to determine if this post should use a featured image.

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
        return await self._patch(
            f"/cms/v3/blogs/posts/{object_id}/draft",
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
            cast_to=BlogPost,
        )

    async def update_langs(
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
        Explicitly set new languages for each post in a
        [multi-language group](https://developers.hubspot.com/docs/guides/cms/content/multi-language-content).

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
            "/cms/v3/blogs/posts/multi-language/update-languages",
            body=await async_maybe_transform(
                {
                    "languages": languages,
                    "primary_id": primary_id,
                },
                post_update_langs_params.PostUpdateLangsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.attach_to_lang_group = to_raw_response_wrapper(
            posts.attach_to_lang_group,
        )
        self.clone = to_raw_response_wrapper(
            posts.clone,
        )
        self.create_lang_variation = to_raw_response_wrapper(
            posts.create_lang_variation,
        )
        self.detach_from_lang_group = to_raw_response_wrapper(
            posts.detach_from_lang_group,
        )
        self.get_draft_by_id = to_raw_response_wrapper(
            posts.get_draft_by_id,
        )
        self.get_previous_version = to_raw_response_wrapper(
            posts.get_previous_version,
        )
        self.get_previous_versions = to_raw_response_wrapper(
            posts.get_previous_versions,
        )
        self.push_live = to_raw_response_wrapper(
            posts.push_live,
        )
        self.read = to_raw_response_wrapper(
            posts.read,
        )
        self.reset_draft = to_raw_response_wrapper(
            posts.reset_draft,
        )
        self.restore_previous_version = to_raw_response_wrapper(
            posts.restore_previous_version,
        )
        self.restore_previous_version_to_draft = to_raw_response_wrapper(
            posts.restore_previous_version_to_draft,
        )
        self.schedule = to_raw_response_wrapper(
            posts.schedule,
        )
        self.set_lang_primary = to_raw_response_wrapper(
            posts.set_lang_primary,
        )
        self.update_draft = to_raw_response_wrapper(
            posts.update_draft,
        )
        self.update_langs = to_raw_response_wrapper(
            posts.update_langs,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._posts.batch)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.attach_to_lang_group = async_to_raw_response_wrapper(
            posts.attach_to_lang_group,
        )
        self.clone = async_to_raw_response_wrapper(
            posts.clone,
        )
        self.create_lang_variation = async_to_raw_response_wrapper(
            posts.create_lang_variation,
        )
        self.detach_from_lang_group = async_to_raw_response_wrapper(
            posts.detach_from_lang_group,
        )
        self.get_draft_by_id = async_to_raw_response_wrapper(
            posts.get_draft_by_id,
        )
        self.get_previous_version = async_to_raw_response_wrapper(
            posts.get_previous_version,
        )
        self.get_previous_versions = async_to_raw_response_wrapper(
            posts.get_previous_versions,
        )
        self.push_live = async_to_raw_response_wrapper(
            posts.push_live,
        )
        self.read = async_to_raw_response_wrapper(
            posts.read,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            posts.reset_draft,
        )
        self.restore_previous_version = async_to_raw_response_wrapper(
            posts.restore_previous_version,
        )
        self.restore_previous_version_to_draft = async_to_raw_response_wrapper(
            posts.restore_previous_version_to_draft,
        )
        self.schedule = async_to_raw_response_wrapper(
            posts.schedule,
        )
        self.set_lang_primary = async_to_raw_response_wrapper(
            posts.set_lang_primary,
        )
        self.update_draft = async_to_raw_response_wrapper(
            posts.update_draft,
        )
        self.update_langs = async_to_raw_response_wrapper(
            posts.update_langs,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._posts.batch)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.attach_to_lang_group = to_streamed_response_wrapper(
            posts.attach_to_lang_group,
        )
        self.clone = to_streamed_response_wrapper(
            posts.clone,
        )
        self.create_lang_variation = to_streamed_response_wrapper(
            posts.create_lang_variation,
        )
        self.detach_from_lang_group = to_streamed_response_wrapper(
            posts.detach_from_lang_group,
        )
        self.get_draft_by_id = to_streamed_response_wrapper(
            posts.get_draft_by_id,
        )
        self.get_previous_version = to_streamed_response_wrapper(
            posts.get_previous_version,
        )
        self.get_previous_versions = to_streamed_response_wrapper(
            posts.get_previous_versions,
        )
        self.push_live = to_streamed_response_wrapper(
            posts.push_live,
        )
        self.read = to_streamed_response_wrapper(
            posts.read,
        )
        self.reset_draft = to_streamed_response_wrapper(
            posts.reset_draft,
        )
        self.restore_previous_version = to_streamed_response_wrapper(
            posts.restore_previous_version,
        )
        self.restore_previous_version_to_draft = to_streamed_response_wrapper(
            posts.restore_previous_version_to_draft,
        )
        self.schedule = to_streamed_response_wrapper(
            posts.schedule,
        )
        self.set_lang_primary = to_streamed_response_wrapper(
            posts.set_lang_primary,
        )
        self.update_draft = to_streamed_response_wrapper(
            posts.update_draft,
        )
        self.update_langs = to_streamed_response_wrapper(
            posts.update_langs,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._posts.batch)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.attach_to_lang_group = async_to_streamed_response_wrapper(
            posts.attach_to_lang_group,
        )
        self.clone = async_to_streamed_response_wrapper(
            posts.clone,
        )
        self.create_lang_variation = async_to_streamed_response_wrapper(
            posts.create_lang_variation,
        )
        self.detach_from_lang_group = async_to_streamed_response_wrapper(
            posts.detach_from_lang_group,
        )
        self.get_draft_by_id = async_to_streamed_response_wrapper(
            posts.get_draft_by_id,
        )
        self.get_previous_version = async_to_streamed_response_wrapper(
            posts.get_previous_version,
        )
        self.get_previous_versions = async_to_streamed_response_wrapper(
            posts.get_previous_versions,
        )
        self.push_live = async_to_streamed_response_wrapper(
            posts.push_live,
        )
        self.read = async_to_streamed_response_wrapper(
            posts.read,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            posts.reset_draft,
        )
        self.restore_previous_version = async_to_streamed_response_wrapper(
            posts.restore_previous_version,
        )
        self.restore_previous_version_to_draft = async_to_streamed_response_wrapper(
            posts.restore_previous_version_to_draft,
        )
        self.schedule = async_to_streamed_response_wrapper(
            posts.schedule,
        )
        self.set_lang_primary = async_to_streamed_response_wrapper(
            posts.set_lang_primary,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            posts.update_draft,
        )
        self.update_langs = async_to_streamed_response_wrapper(
            posts.update_langs,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._posts.batch)
