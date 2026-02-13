# Files

Types:

```python
from hubspot_sdk.types.files import (
    CollectionResponseFile,
    CollectionResponseFolder,
    File,
    FileActionResponse,
    FileStat,
    FileUpdateInput,
    Folder,
    FolderActionResponse,
    FolderInput,
    FolderUpdateInput,
    FolderUpdateInputWithID,
    FolderUpdateTaskLocator,
    ImportFromURLInput,
    ImportFromURLTaskLocator,
    SignedURL,
)
```

## FileOperations

Methods:

- <code title="patch /files/v3/files/{fileId}">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">update</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_operation_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="delete /files/v3/files/{fileId}">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">delete</a>(file_id) -> None</code>
- <code title="delete /files/v3/files/{fileId}/gdpr-delete">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">gdpr_delete</a>(file_id) -> None</code>
- <code title="get /files/v3/files/{fileId}">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">get</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_operation_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/v3/files/stat/{path}">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">get_by_path</a>(file_path, \*\*<a href="src/hubspot_sdk/types/files/file_operation_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file_stat.py">FileStat</a></code>
- <code title="get /files/v3/files/import-from-url/async/tasks/{taskId}/status">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">get_import_task_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files/file_action_response.py">FileActionResponse</a></code>
- <code title="get /files/v3/files/{fileId}/signed-url">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">get_signed_url</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_operation_get_signed_url_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/signed_url.py">SignedURL</a></code>
- <code title="post /files/v3/files/import-from-url/async">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">import_from_url_async</a>(\*\*<a href="src/hubspot_sdk/types/files/file_operation_import_from_url_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/import_from_url_task_locator.py">ImportFromURLTaskLocator</a></code>
- <code title="put /files/v3/files/{fileId}">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">replace</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_operation_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/v3/files/search">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/file_operation_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">SyncPage[File]</a></code>
- <code title="post /files/v3/files">client.files.file_operations.<a href="./src/hubspot_sdk/resources/files/file_operations.py">upload</a>(\*\*<a href="src/hubspot_sdk/types/files/file_operation_upload_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>

## Folders

Methods:

- <code title="post /files/v3/folders">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="delete /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_id</a>(folder_id) -> None</code>
- <code title="delete /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_path</a>(folder_path) -> None</code>
- <code title="get /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="get /files/v3/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_path</a>(folder_path, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="get /files/v3/folders/update/async/tasks/{taskId}/status">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_update_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files/folder_action_response.py">FolderActionResponse</a></code>
- <code title="get /files/v3/folders/search">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">SyncPage[Folder]</a></code>
- <code title="post /files/v3/folders/update/async">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_async_by_id</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_update_async_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder_update_task_locator.py">FolderUpdateTaskLocator</a></code>
- <code title="patch /files/v3/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_update_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
