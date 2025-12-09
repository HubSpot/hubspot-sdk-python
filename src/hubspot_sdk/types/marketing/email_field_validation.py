# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailFieldValidation"]


class EmailFieldValidation(BaseModel):
    """Describes how an email address should be validated."""

    blocked_email_domains: List[str] = FieldInfo(alias="blockedEmailDomains")
    """A list of email domains to block."""

    use_default_block_list: bool = FieldInfo(alias="useDefaultBlockList")
    """Whether to block the free email providers."""
