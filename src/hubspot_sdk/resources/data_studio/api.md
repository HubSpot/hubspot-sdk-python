# DataStudio

## Datasource

Types:

```python
from hubspot_sdk.types.data_studio import (
    BodyPart,
    ContentDisposition,
    DataSourceGetResponse,
    DataSourceUpdateResponse,
    FileColumn,
    FormDataBodyPart,
    FormDataContentDisposition,
    FormDataMultiPart,
    MediaType,
    MultiPart,
    ParameterizedHeader,
)
```

Methods:

- <code title="post /data-studio/2026-03/data-source">client.data_studio.datasource.<a href="./src/hubspot_sdk/resources/data_studio/datasource.py">create</a>(\*\*<a href="src/hubspot_sdk/types/data_studio/datasource_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /data-studio/2026-03/data-source/{datasourceId}">client.data_studio.datasource.<a href="./src/hubspot_sdk/resources/data_studio/datasource.py">update</a>(datasource_id, \*\*<a href="src/hubspot_sdk/types/data_studio/datasource_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/data_studio/data_source_update_response.py">DataSourceUpdateResponse</a></code>
- <code title="delete /data-studio/2026-03/data-source/{datasourceId}">client.data_studio.datasource.<a href="./src/hubspot_sdk/resources/data_studio/datasource.py">delete</a>(datasource_id) -> BinaryAPIResponse</code>
- <code title="get /data-studio/2026-03/data-source/{datasourceId}">client.data_studio.datasource.<a href="./src/hubspot_sdk/resources/data_studio/datasource.py">get</a>(datasource_id) -> <a href="./src/hubspot_sdk/types/data_studio/data_source_get_response.py">DataSourceGetResponse</a></code>
