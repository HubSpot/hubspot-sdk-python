# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Domain"]


class Domain(BaseModel):
    id: str
    """The unique ID of this domain."""

    correct_cname: str = FieldInfo(alias="correctCname")
    """The expected CNAME record for the domain."""

    created: datetime
    """The date and time when the domain was created."""

    domain: str
    """The actual domain or sub-domain. e.g. www.hubspot.com"""

    is_resolving: bool = FieldInfo(alias="isResolving")
    """Whether the DNS for this domain is optimally configured for use with HubSpot."""

    is_ssl_enabled: bool = FieldInfo(alias="isSslEnabled")
    """Indicates whether SSL is enabled for the domain."""

    is_ssl_only: bool = FieldInfo(alias="isSslOnly")
    """Indicates whether the domain is accessible only via SSL."""

    is_used_for_blog_post: bool = FieldInfo(alias="isUsedForBlogPost")
    """Whether the domain is used for CMS blog posts."""

    is_used_for_email: bool = FieldInfo(alias="isUsedForEmail")
    """Whether the domain is used for CMS email web pages."""

    is_used_for_knowledge: bool = FieldInfo(alias="isUsedForKnowledge")
    """Whether the domain is used for CMS knowledge pages."""

    is_used_for_landing_page: bool = FieldInfo(alias="isUsedForLandingPage")
    """Whether the domain is used for CMS landing pages."""

    is_used_for_site_page: bool = FieldInfo(alias="isUsedForSitePage")
    """Whether the domain is used for CMS site pages."""

    manually_marked_as_resolving: bool = FieldInfo(alias="manuallyMarkedAsResolving")
    """Indicates whether the domain has been manually marked as resolving."""

    primary_blog_post: bool = FieldInfo(alias="primaryBlogPost")
    """Indicates whether the domain is the primary domain for blog posts."""

    primary_email: bool = FieldInfo(alias="primaryEmail")
    """Indicates whether the domain is the primary domain for email pages."""

    primary_knowledge: bool = FieldInfo(alias="primaryKnowledge")
    """Indicates whether the domain is the primary domain for knowledge pages."""

    primary_landing_page: bool = FieldInfo(alias="primaryLandingPage")
    """Indicates whether the domain is the primary domain for landing pages."""

    primary_site_page: bool = FieldInfo(alias="primarySitePage")
    """Indicates whether the domain is the primary domain for site pages."""

    secondary_to_domain: str = FieldInfo(alias="secondaryToDomain")
    """Specifies the domain to which this domain is secondary."""

    updated: datetime
    """The date and time when the domain was last updated."""
