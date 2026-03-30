# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ObjectTypeIDProto"]


class ObjectTypeIDProto(BaseModel):
    inner_id: int = FieldInfo(alias="innerId")

    meta_type_id: int = FieldInfo(alias="metaTypeId")
