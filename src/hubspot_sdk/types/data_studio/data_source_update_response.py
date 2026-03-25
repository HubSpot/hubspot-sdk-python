# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DataSourceUpdateResponse"]


class DataSourceUpdateResponse(BaseModel):
    datasource_id: int = FieldInfo(alias="datasourceId")
    """The unique identifier for the data source. It is an integer formatted as int64."""

    datasource_name: str = FieldInfo(alias="datasourceName")
    """The name of the data source. It is a string."""

    preview_link: str = FieldInfo(alias="previewLink")
    """A URL string that provides a preview link for the data source."""
