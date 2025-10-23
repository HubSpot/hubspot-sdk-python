# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..public_access_rule_param import PublicAccessRuleParam
from ..content_language_variation_param import ContentLanguageVariationParam

__all__ = ["SitePageUpdateParams"]


class SitePageUpdateParams(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the page."""

    ab_status: Required[
        Annotated[
            Literal[
                "master",
                "variant",
                "loser_variant",
                "mab_master",
                "mab_variant",
                "automated_master",
                "automated_variant",
                "automated_loser_variant",
            ],
            PropertyInfo(alias="abStatus"),
        ]
    ]
    """The status of the AB test associated with this page, if applicable"""

    ab_test_id: Required[Annotated[str, PropertyInfo(alias="abTestId")]]
    """The ID of the AB test associated with this page, if applicable"""

    archived_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="archivedAt", format="iso8601")]]
    """The timestamp (ISO8601 format) when this page was deleted."""

    archived_in_dashboard: Required[Annotated[bool, PropertyInfo(alias="archivedInDashboard")]]
    """
    If True, the page will not show up in your dashboard, although the page could
    still be live.
    """

    attached_stylesheets: Required[Annotated[Iterable[Dict[str, object]], PropertyInfo(alias="attachedStylesheets")]]
    """List of stylesheets to attach to this page.

    These stylesheets are attached to just this page. Order of precedence is bottom
    to top, just like in the HTML.
    """

    author_name: Required[Annotated[str, PropertyInfo(alias="authorName")]]
    """The name of the user that updated this page."""

    campaign: Required[str]
    """The GUID of the marketing campaign this page is a part of."""

    category_id: Required[Annotated[int, PropertyInfo(alias="categoryId")]]
    """ID of the type of object this is. Should always ."""

    content_group_id: Required[Annotated[str, PropertyInfo(alias="contentGroupId")]]

    content_type_category: Required[
        Annotated[
            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
            PropertyInfo(alias="contentTypeCategory"),
        ]
    ]
    """An ENUM descibing the type of this object.

    Should be either LANDING_PAGE or SITE_PAGE.
    """

    created: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    created_by_id: Required[Annotated[str, PropertyInfo(alias="createdById")]]
    """The ID of the user that created this page."""

    currently_published: Required[Annotated[bool, PropertyInfo(alias="currentlyPublished")]]

    current_state: Required[
        Annotated[
            Literal[
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
            PropertyInfo(alias="currentState"),
        ]
    ]
    """A generated ENUM descibing the current state of this page."""

    domain: Required[str]
    """The domain this page will resolve to.

    If null, the page will default to the primary domain for this content type.
    """

    dynamic_page_data_source_id: Required[Annotated[str, PropertyInfo(alias="dynamicPageDataSourceId")]]

    dynamic_page_data_source_type: Required[Annotated[int, PropertyInfo(alias="dynamicPageDataSourceType")]]

    dynamic_page_hub_db_table_id: Required[Annotated[str, PropertyInfo(alias="dynamicPageHubDbTableId")]]
    """The ID of the HubDB table this page references, if applicable"""

    enable_domain_stylesheets: Required[Annotated[bool, PropertyInfo(alias="enableDomainStylesheets")]]
    """
    Boolean to determine whether or not the styles from the template should be
    applied.
    """

    enable_layout_stylesheets: Required[Annotated[bool, PropertyInfo(alias="enableLayoutStylesheets")]]
    """
    Boolean to determine whether or not the styles from the template should be
    applied.
    """

    featured_image: Required[Annotated[str, PropertyInfo(alias="featuredImage")]]
    """The featuredImage of this page."""

    featured_image_alt_text: Required[Annotated[str, PropertyInfo(alias="featuredImageAltText")]]
    """Alt Text of the featuredImage."""

    folder_id: Required[Annotated[str, PropertyInfo(alias="folderId")]]
    """
    The ID of the associated folder this landing page is organized under in the app
    dashboard.
    """

    footer_html: Required[Annotated[str, PropertyInfo(alias="footerHtml")]]
    """
    Custom HTML for embed codes, javascript that should be placed before the </body>
    tag of the page.
    """

    head_html: Required[Annotated[str, PropertyInfo(alias="headHtml")]]
    """Custom HTML for embed codes, javascript, etc.

    that goes in the <head> tag of the page.
    """

    html_title: Required[Annotated[str, PropertyInfo(alias="htmlTitle")]]
    """The html title of this page."""

    include_default_custom_css: Required[Annotated[bool, PropertyInfo(alias="includeDefaultCustomCss")]]
    """Boolean to determine whether or not the Primary CSS Files should be applied."""

    language: Required[
        Literal[
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
        ]
    ]
    """The explicitly defined ISO 639 language code of the page.

    If null, the page will default to the language of the Domain.
    """

    layout_sections: Required[Annotated[Dict[str, "LayoutSectionParam"], PropertyInfo(alias="layoutSections")]]

    link_rel_canonical_url: Required[Annotated[str, PropertyInfo(alias="linkRelCanonicalUrl")]]
    """
    Optional override to set the URL to be used in the rel=canonical link tag on the
    page.
    """

    mab_experiment_id: Required[Annotated[str, PropertyInfo(alias="mabExperimentId")]]
    """
    The ID of the MAB test (or dynamic test) associated with this page, if
    applicable
    """

    meta_description: Required[Annotated[str, PropertyInfo(alias="metaDescription")]]
    """A description that goes in <meta> tag on the page."""

    name: Required[str]
    """The internal name of the page."""

    page_expiry_date: Required[Annotated[int, PropertyInfo(alias="pageExpiryDate")]]
    """
    The date at which this page should expire and begin redirecting to another url
    or page.
    """

    page_expiry_enabled: Required[Annotated[bool, PropertyInfo(alias="pageExpiryEnabled")]]
    """Boolean describing if the page expiration feature is enabled for this page"""

    page_expiry_redirect_id: Required[Annotated[int, PropertyInfo(alias="pageExpiryRedirectId")]]
    """The ID of another page this page's url should redirect to once this page
    expires.

    Should only set this or pageExpiryRedirectUrl.
    """

    page_expiry_redirect_url: Required[Annotated[str, PropertyInfo(alias="pageExpiryRedirectUrl")]]
    """The URL this page's url should redirect to once this page expires.

    Should only set this or pageExpiryRedirectId.
    """

    page_redirected: Required[Annotated[bool, PropertyInfo(alias="pageRedirected")]]
    """
    A generated Boolean describing whether or not this page is currently expired and
    being redirected.
    """

    password: Required[str]
    """Set this to create a password protected page.

    Entering the password will be required to view the page.
    """

    public_access_rules: Required[Annotated[Iterable[PublicAccessRuleParam], PropertyInfo(alias="publicAccessRules")]]
    """Rules for require member registration to access private content."""

    public_access_rules_enabled: Required[Annotated[bool, PropertyInfo(alias="publicAccessRulesEnabled")]]
    """Boolean to determine whether or not to respect publicAccessRules."""

    publish_date: Required[Annotated[Union[str, datetime], PropertyInfo(alias="publishDate", format="iso8601")]]
    """The date (ISO8601 format) the page is to be published at."""

    publish_immediately: Required[Annotated[bool, PropertyInfo(alias="publishImmediately")]]
    """
    Set this to true if you want to be published immediately when the schedule
    publish endpoint is called, and to ignore the publish_date setting.
    """

    slug: Required[str]
    """The path of the this page.

    This field is appended to the domain to construct the url of this page.
    """

    state: Required[str]
    """An ENUM descibing the current state of this page."""

    subcategory: Required[str]
    """Details the type of page this is. Should always be landing_page or site_page"""

    template_path: Required[Annotated[str, PropertyInfo(alias="templatePath")]]
    """String detailing the path of the template used for this page."""

    theme_settings_values: Required[Annotated[Dict[str, object], PropertyInfo(alias="themeSettingsValues")]]

    translated_from_id: Required[Annotated[str, PropertyInfo(alias="translatedFromId")]]
    """ID of the primary page this object was translated from."""

    translations: Required[Dict[str, ContentLanguageVariationParam]]

    updated: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    updated_by_id: Required[Annotated[str, PropertyInfo(alias="updatedById")]]
    """The ID of the user that updated this page."""

    url: Required[str]
    """A generated field representing the URL of this page."""

    use_featured_image: Required[Annotated[bool, PropertyInfo(alias="useFeaturedImage")]]
    """Boolean to determine if this page should use a featuredImage."""

    widget_containers: Required[Annotated[Dict[str, object], PropertyInfo(alias="widgetContainers")]]
    """
    A data structure containing the data for all the modules inside the containers
    for this page. This will only be populated if the page has widget containers.
    """

    widgets: Required[Dict[str, object]]
    """A data structure containing the data for all the modules for this page."""

    archived: bool
    """Specifies whether to update deleted Site Pages. Defaults to `false`."""


from ..layout_section_param import LayoutSectionParam
