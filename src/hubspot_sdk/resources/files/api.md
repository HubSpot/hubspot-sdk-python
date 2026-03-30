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

## Files

Methods:

- <code title="post /files/2026-03/folders">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">create</a>(\*\*<a href="src/hubspot_sdk/types/files/file_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="patch /files/2026-03/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">update</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="delete /files/2026-03/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">delete</a>(file_id) -> None</code>
- <code title="delete /files/2026-03/files/{fileId}/gdpr-delete">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">gdpr_delete</a>(file_id) -> None</code>
- <code title="get /files/2026-03/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/2026-03/files/stat/{path}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_by_path</a>(path, \*\*<a href="src/hubspot_sdk/types/files/file_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file_stat.py">FileStat</a></code>
- <code title="get /files/2026-03/files/import-from-url/async/tasks/{taskId}/status">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_import_task_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files/file_action_response.py">FileActionResponse</a></code>
- <code title="get /files/2026-03/files/{fileId}/signed-url">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_signed_url</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_signed_url_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/signed_url.py">SignedURL</a></code>
- <code title="post /files/2026-03/files/import-from-url/async">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">import_from_url_async</a>(\*\*<a href="src/hubspot_sdk/types/files/file_import_from_url_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/import_from_url_task_locator.py">ImportFromURLTaskLocator</a></code>
- <code title="put /files/2026-03/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">replace</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/2026-03/files/search">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/file_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">SyncPage[File]</a></code>
- <code title="post /files/2026-03/files">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">upload</a>(\*\*<a href="src/hubspot_sdk/types/files/file_upload_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>

## Folders

Methods:

- <code title="delete /files/2026-03/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_id</a>(folder_id) -> None</code>
- <code title="delete /files/2026-03/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">delete_by_path</a>(folder_path) -> None</code>
- <code title="get /files/2026-03/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="get /files/2026-03/folders/{folderPath}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_by_path</a>(folder_path, \*\*<a href="src/hubspot_sdk/types/files/folder_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
- <code title="get /files/2026-03/folders/update/async/tasks/{taskId}/status">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">get_update_async_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files/folder_action_response.py">FolderActionResponse</a></code>
- <code title="get /files/2026-03/folders/search">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">SyncPage[Folder]</a></code>
- <code title="post /files/2026-03/folders/update/async">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_async_by_id</a>(\*\*<a href="src/hubspot_sdk/types/files/folder_update_async_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder_update_task_locator.py">FolderUpdateTaskLocator</a></code>
- <code title="patch /files/2026-03/folders/{folderId}">client.files.folders.<a href="./src/hubspot_sdk/resources/files/folders.py">update_by_id</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/files/folder_update_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/folder.py">Folder</a></code>
