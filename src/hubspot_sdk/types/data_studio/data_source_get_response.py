# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .file_column import FileColumn

__all__ = ["DataSourceGetResponse"]


class DataSourceGetResponse(BaseModel):
    columns: List[FileColumn]
    """An array of FileColumn objects representing the columns in the data source."""

    created_at: str = FieldInfo(alias="createdAt")
    """The creation date and time of the data source, represented as a string."""

    datasource_id: int = FieldInfo(alias="datasourceId")
    """The unique identifier for the data source, represented as a 64-bit integer."""

    datasource_name: str = FieldInfo(alias="datasourceName")
    """The name of the data source, represented as a string."""

    datasource_type: Literal["FILE"] = FieldInfo(alias="datasourceType")
    """The type of the data source, which is a string with a valid value of 'FILE'."""

    last_ingestion_status: Literal["FAILED", "IN_PROGRESS", "SUCCESSFUL"] = FieldInfo(alias="lastIngestionStatus")
    """The status of the last data ingestion process, represented as a string.

    Valid values include 'SUCCESSFUL', 'IN_PROGRESS', and 'FAILED'.
    """
