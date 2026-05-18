# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .pre_resolved_contact_param import PreResolvedContactParam

__all__ = ["PreResolvedContactsParam"]


class PreResolvedContactsParam(TypedDict, total=False):
    contacts: Required[Iterable[PreResolvedContactParam]]
