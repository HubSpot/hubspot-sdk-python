# Cms

Types:

```python
from hubspot_sdk.types.cms import (
    Angle,
    AttachToLangPrimaryRequestVNext,
    BackgroundImage,
    BatchInputJsonNode,
    BreakpointStyles,
    ColorStop,
    ContentCloneRequestVNext,
    ContentLanguageVariation,
    ContentScheduleRequestVNext,
    DetachFromLangGroupRequestVNext,
    Gradient,
    LayoutSection,
    Margin,
    Padding,
    PublicAccessRule,
    RgbaColor,
    RowMetaData,
    SetNewLanguagePrimaryRequestVNext,
    SideOrCorner,
    Size,
    Styles,
    UpdateLanguagesRequestVNext,
)
```

## AuditLogs

Types:

```python
from hubspot_sdk.types.cms import (
    CmsAuditLoggingExportFilters,
    CmsAuditLoggingExportSettings,
    CollectionResponsePublicAuditLog,
    PublicAuditLog,
)
```

Methods:

- <code title="get /cms/audit-logs/2026-03">client.cms.audit_logs.<a href="./src/hubspot_sdk/resources/cms/audit_logs.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/audit_log_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/public_audit_log.py">SyncPage[PublicAuditLog]</a></code>
- <code title="post /cms/audit-logs/2026-03/export">client.cms.audit_logs.<a href="./src/hubspot_sdk/resources/cms/audit_logs.py">export</a>(\*\*<a href="src/hubspot_sdk/types/cms/audit_log_export_params.py">params</a>) -> None</code>

## Blogs

Types:

```python
from hubspot_sdk.types.cms import (
    CursorPagedResultBlogAuthorLong,
    CursorPagedResultBlogPostLong,
    CursorPagedResultTagLong,
)
```

### Authors

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    BatchInputBlogAuthor,
    BatchResponseBlogAuthor,
    BatchResponseBlogAuthorWithErrors,
    BlogAuthor,
    BlogAuthorCloneRequestVNext,
    CollectionResponseWithTotalBlogAuthorForwardPaging,
)
```

Methods:

- <code title="post /cms/blogs/2026-03/authors">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="patch /cms/blogs/2026-03/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_list_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /cms/blogs/2026-03/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/authors/multi-language/attach-to-lang-group">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/authors/multi-language/create-language-variation">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_create_language_variation_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/authors/multi-language/detach-from-lang-group">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor/query">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/cursor">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_posts_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_posts_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/cursor/query">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_posts_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_posts_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_tags_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_tags_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor/query">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">get_tags_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_tags_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/blogs/2026-03/authors/multi-language/set-new-lang-primary">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/authors/multi-language/update-languages">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/authors.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_update_languages_params.py">params</a>) -> BinaryAPIResponse</code>

#### Batch

Methods:

- <code title="post /cms/blogs/2026-03/authors/batch/create">client.cms.blogs.authors.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/authors/batch_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/authors/batch/update">client.cms.blogs.authors.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/authors/batch_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/authors/batch/archive">client.cms.blogs.authors.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/authors/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/authors/batch/read">client.cms.blogs.authors.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/authors/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/authors/batch_get_params.py">params</a>) -> BinaryAPIResponse</code>

### Posts

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    BatchInputBlogPost,
    BatchResponseBlogPost,
    BatchResponseBlogPostWithErrors,
    BlogPost,
    BlogPostLanguageCloneRequestVNext,
    BlogPostVersion,
    CollectionResponseWithTotalBlogPostForwardPaging,
    CollectionResponseWithTotalBlogPostVersion,
    VersionBlogPost,
)
```

Methods:

- <code title="post /cms/blogs/2026-03/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="patch /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/cursor">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/clone">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_clone_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_draft_by_id</a>(object_id) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">list_authors</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_authors_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">list_tags</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_tags_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/draft/push-live">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">push_live</a>(object_id) -> None</code>
- <code title="get /cms/blogs/2026-03/posts/cursor/query">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor/query">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">query_authors</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_query_authors_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor/query">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">query_tags</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_query_tags_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/draft/reset">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/schedule">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_schedule_params.py">params</a>) -> None</code>
- <code title="patch /cms/blogs/2026-03/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_draft_params.py">params</a>) -> BinaryAPIResponse</code>

#### Batch

Methods:

- <code title="post /cms/blogs/2026-03/posts/batch/create">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/batch/update">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/batch/archive">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/batch/read">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_get_params.py">params</a>) -> BinaryAPIResponse</code>

#### MultiLanguage

Methods:

- <code title="post /cms/blogs/2026-03/posts/multi-language/attach-to-lang-group">client.cms.blogs.posts.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/multi_language.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/multi_language_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/create-language-variation">client.cms.blogs.posts.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/multi_language.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/multi_language_create_lang_variation_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/detach-from-lang-group">client.cms.blogs.posts.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/multi_language.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/multi_language_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/blogs/2026-03/posts/multi-language/set-new-lang-primary">client.cms.blogs.posts.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/multi_language.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/multi_language_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/update-languages">client.cms.blogs.posts.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/multi_language.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/multi_language_update_langs_params.py">params</a>) -> BinaryAPIResponse</code>

#### Revisions

Methods:

- <code title="get /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}">client.cms.blogs.posts.revisions.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/revisions.py">get_previous_version</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}/revisions">client.cms.blogs.posts.revisions.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/revisions.py">get_previous_versions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/revision_get_previous_versions_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}/restore">client.cms.blogs.posts.revisions.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/revisions.py">restore_previous_version</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.blogs.posts.revisions.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/revisions.py">restore_previous_version_to_draft</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>

### Settings

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    Blog,
    BlogLanguageCloneRequestVNext,
    BlogVersion,
    CollectionResponseWithTotalBlog,
    CollectionResponseWithTotalBlogVersion,
    VersionBlog,
)
```

Methods:

- <code title="get /cms/blog-settings/2026-03/settings">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/settings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">SyncPage[Blog]</a></code>
- <code title="get /cms/blog-settings/2026-03/settings/{blogId}">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/settings.py">get</a>(blog_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">Blog</a></code>
- <code title="get /cms/blog-settings/2026-03/settings/{blogId}/revisions/{revisionId}">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/settings.py">get_revision</a>(revision_id, \*, blog_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_version.py">BlogVersion</a></code>
- <code title="get /cms/blog-settings/2026-03/settings/{blogId}/revisions">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/settings.py">list_revisions</a>(blog_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog.py">SyncPage[VersionBlog]</a></code>

#### MultiLanguage

Methods:

- <code title="post /cms/blog-settings/2026-03/settings/multi-language/attach-to-lang-group">client.cms.blogs.settings.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/multi_language.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/settings/multi_language_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blog-settings/2026-03/settings/multi-language/create-language-variation">client.cms.blogs.settings.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/multi_language.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/settings/multi_language_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">Blog</a></code>
- <code title="post /cms/blog-settings/2026-03/settings/multi-language/detach-from-lang-group">client.cms.blogs.settings.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/multi_language.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/settings/multi_language_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/blog-settings/2026-03/settings/multi-language/set-new-lang-primary">client.cms.blogs.settings.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/multi_language.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/settings/multi_language_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/blog-settings/2026-03/settings/multi-language/update-languages">client.cms.blogs.settings.multi_language.<a href="./src/hubspot_sdk/resources/cms/blogs/settings/multi_language.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/settings/multi_language_update_languages_params.py">params</a>) -> BinaryAPIResponse</code>

### Tags

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    BatchInputTag,
    BatchResponseTag,
    BatchResponseTagWithErrors,
    CollectionResponseWithTotalTagForwardPaging,
    Tag,
    TagCloneRequestVNext,
)
```

Methods:

- <code title="post /cms/blogs/2026-03/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="patch /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_authors_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_authors_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/authors/cursor/query">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_authors_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_authors_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/cursor/query">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/cursor">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_posts_cursor</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_posts_cursor_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/cursor/query">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">list_posts_cursor_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_posts_cursor_by_query_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/blogs/2026-03/tags/multi-language/set-new-lang-primary">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/update-languages">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/tags.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_langs_params.py">params</a>) -> BinaryAPIResponse</code>

#### Batch

Methods:

- <code title="post /cms/blogs/2026-03/tags/batch/archive">client.cms.blogs.tags.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tags/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/batch/create">client.cms.blogs.tags.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/batch.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tags/batch_create_batch_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/batch/read">client.cms.blogs.tags.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/batch.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tags/batch_get_batch_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/batch/update">client.cms.blogs.tags.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/tags/batch.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tags/batch_update_batch_params.py">params</a>) -> BinaryAPIResponse</code>

## Domains

Types:

```python
from hubspot_sdk.types.cms import CollectionResponseWithTotalDomain, Domain
```

Methods:

- <code title="get /cms/domains/2026-03">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/domain_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/domain.py">SyncPage[Domain]</a></code>
- <code title="get /cms/domains/2026-03/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">get</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/domain.py">Domain</a></code>

## Hubdb

Types:

```python
from hubspot_sdk.types.cms import (
    BatchInputHubDBTableRowBatchCloneRequest,
    BatchInputHubDBTableRowV3BatchUpdateRequest,
    BatchInputHubDBTableRowV3Request,
    BatchResponseHubDBTableRowV3,
    BatchResponseHubDBTableRowV3WithErrors,
    BoundedNextPage,
    BoundedPaging,
    CollectionResponseWithTotalHubDBTableV3,
    Column,
    ColumnRequest,
    ForeignID,
    HubDBTableCloneRequest,
    HubDBTableRowBatchCloneRequest,
    HubDBTableRowV3,
    HubDBTableRowV3BatchUpdateRequest,
    HubDBTableRowV3Request,
    HubDBTableRowV3Wrapper,
    HubDBTableV3,
    HubDBTableV3Request,
    ImportResult,
    Option,
    RandomAccessCollectionResponseWithTotalHubDBTableRowV3,
    SimpleUser,
    StreamingCollectionResponseWithTotalHubDBTableRowV3,
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
    Variant,
)
```

### Rows

Methods:

- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">create</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">list</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3_wrapper.py">SyncPage[object]</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/clone">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">clone_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_clone_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}/draft/clone">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">clone_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/create">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">create_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="delete /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">delete_draft</a>(row_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">get</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/batch/read">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">get_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">get_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/read">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">get_draft_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_draft_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/purge">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">purge_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_purge_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">replace_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_replace_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="put /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">replace_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_replace_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/draft/batch/update">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">update_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="patch /cms/hubdb/2026-03/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows.py">update_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>

### Tables

Methods:

- <code title="post /cms/hubdb/2026-03/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/hubdb/2026-03/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">SyncPage[HubDBTableV3]</a></code>
- <code title="delete /cms/hubdb/2026-03/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">delete</a>(table_id_or_name) -> None</code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/draft/clone">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">clone_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="delete /cms/hubdb/2026-03/tables/{tableIdOrName}/versions/{versionId}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">delete_version</a>(version_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/draft/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_draft_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/hubdb/2026-03/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/draft/import">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">import_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_import_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/import_result.py">ImportResult</a></code>
- <code title="get /cms/hubdb/2026-03/tables/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list_draft</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">SyncPage[HubDBTableV3]</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">publish_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_publish_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">reset_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_reset_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/hubdb/2026-03/tables/{tableIdOrName}/unpublish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">unpublish</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_unpublish_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/hubdb/2026-03/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">update_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>

## MediaBridge

Types:

```python
from hubspot_sdk.types.cms import (
    AbsoluteValue,
    AddNumbers,
    AddTime,
    And,
    AttentionSpanCalculatedValues,
    AttentionSpanEvent,
    AttentionSpanEventRequest,
    BatchInputPropertyCreate,
    BatchResponseProperty,
    BatchResponsePropertyWithErrors,
    BeginsWith,
    BooleanPropertyVariable,
    BooleanTargetPropertyVariable,
    BulkIntegratorObjectCreationResponse,
    CaseChangeTestExtensionData,
    CollectionResponseObjectSchemaNoPaging,
    CollectionResponsePropertyNoPaging,
    ConcatStrings,
    ConstantBoolean,
    ConstantNumber,
    ConstantString,
    Contains,
    Date,
    DatedExchangeRate,
    DefaultRequirements,
    DefinitionSource,
    DivideNumbers,
    Endpoints,
    Euler,
    EventVisibilityChange,
    EventVisibilityResponse,
    ExtensionData,
    ExternalOptionsMetaData,
    ExtractMostRecentEmailReplyHTML,
    ExtractMostRecentEmailReplyText,
    ExtractMostRecentPlainTextEmailReply,
    FetchCurrencyDecimalPlaces,
    FetchExchangeRate,
    FetchSingleCurrencyPortalCurrency,
    FieldLevelPermission,
    FilteringMetaData,
    FormatFullName,
    FormatPhoneNumber,
    FormatSearchablePhoneNumber,
    Group,
    GroupView,
    HasEmailReply,
    HasPlainTextEmailReply,
    IfBoolean,
    IfNumber,
    IfString,
    InboundDBObjectType,
    IntegratorOEmbedDomainModel,
    IntegratorOEmbedDomainRequest,
    IntegratorObjectCreationRequest,
    IntegratorObjectCreationResponse,
    IsEngagementType,
    IsPipelineStageClosed,
    IsPresent,
    LessThan,
    LessThanOrEqual,
    LowerCase,
    MaxNumbers,
    MediaBridgePropertyUpdate,
    MediaBridgeProviderPartial,
    MediaBridgeProviderRegistrationResponse,
    MediaPlayedEvent,
    MediaPlayedEventRequest,
    MediaPlayedPercentageEvent,
    MediaPlayedPercentageEventRequest,
    MinNumbers,
    Month,
    MoreThan,
    MoreThanOrEqual,
    MultiplyNumbers,
    Not,
    Now,
    NumberEquals,
    NumberPropertyVariable,
    NumberTargetPropertyVariable,
    NumberToString,
    OEmbedDomainsCollectionResponse,
    ObjectDefinitionResponse,
    ObjectSchema,
    ObjectTypeIDProto,
    Option1,
    OptionDecorations,
    OptionDecoratorsExtensionData,
    Or,
    ParseNumber,
    PeriodToMonths,
    PeriodToWeeks,
    PipelineProbability,
    Power,
    Property,
    Property1,
    PropertyCreate,
    PropertyDefinition,
    PropertyDefinitionSource,
    RequiredPropertiesExtensionData,
    RollupExpression,
    RoundDownNumbers,
    RoundNearestNumbers,
    RoundUpNumbers,
    ScopeMapping,
    SetContainsString,
    SoftRequiredPropertiesExtensionData,
    SquareRoot,
    StringEquals,
    StringLength,
    StringPropertyVariable,
    StringTargetPropertyVariable,
    Substring,
    SubtractNumbers,
    SubtractTime,
    TimeBetween,
    TimeBetweenSkipWeekends,
    TimestampOfPropertyVariable,
    TimestampOfTargetPropertyVariable,
    UpperCase,
    Xor,
    Year,
)
```

Methods:

- <code title="post /media-bridge/2026-03/{appId}/schemas/{objectType}/associations">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_association</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/association_definition.py">AssociationDefinition</a></code>
- <code title="post /media-bridge/2026-03/events/attention-span">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_attention_span_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_attention_span_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/attention_span_event.py">AttentionSpanEvent</a></code>
- <code title="post /media-bridge/2026-03/events/media-played">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_media_played_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_media_played_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_played_event.py">MediaPlayedEvent</a></code>
- <code title="post /media-bridge/2026-03/events/media-played-percent">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_media_played_percent_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_media_played_percent_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_played_percentage_event.py">MediaPlayedPercentageEvent</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/object-definitions">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_object_type</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_object_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/bulk_integrator_object_creation_response.py">BulkIntegratorObjectCreationResponse</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_property</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/property.py">Property</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/groups">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_property_group</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_property_group_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/video-association-definition">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_video_association_definition</a>(app_id) -> <a href="./src/hubspot_sdk/types/shared/association_definition.py">AssociationDefinition</a></code>
- <code title="delete /media-bridge/2026-03/{appId}/schemas/{objectType}/associations/{associationId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_association</a>(association_id, \*, app_id, object_type) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_delete_oembed_domain_params.py">params</a>) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_property</a>(property_name, \*, app_id, object_type) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_property_group</a>(group_name, \*, app_id, object_type) -> None</code>
- <code title="get /media-bridge/2026-03/{appId}/settings/event-visibility">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_event_visibility_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_response.py">EventVisibilityResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_oembed_domain</a>(o_embed_domain_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_property</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_get_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/property.py">Property</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_property_group</a>(group_name, \*, app_id, object_type) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="get /media-bridge/2026-03/{appId}/schemas/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_schema</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/cms/object_schema.py">ObjectSchema</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/object-definitions/{mediaType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_object_types_by_media_type</a>(media_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_object_types_by_media_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/object_definition_response.py">ObjectDefinitionResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_oembed_domains</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_oembed_domains_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/o_embed_domains_collection_response.py">OEmbedDomainsCollectionResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_properties</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_properties_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_property_no_paging.py">CollectionResponsePropertyNoPaging</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/groups">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_property_groups</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/shared/collection_response_property_group_no_paging.py">CollectionResponsePropertyGroupNoPaging</a></code>
- <code title="get /media-bridge/2026-03/{appId}/schemas">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_schemas</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_schemas_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/register">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">register_app_name</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_register_app_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/settings/event-visibility">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_event_visibility_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_event_visibility_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_change.py">EventVisibilityChange</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_oembed_domain</a>(o_embed_domain_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_property</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/property.py">Property</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_property_group</a>(group_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_property_group_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/schemas/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_schema</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_schema_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/object_type_definition.py">ObjectTypeDefinition</a></code>
- <code title="put /media-bridge/2026-03/{appId}/settings">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>

### Batch

Methods:

- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/create">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">create</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/archive">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">delete</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/read">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">get</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_property.py">BatchResponseProperty</a></code>

## Pages

Types:

```python
from hubspot_sdk.types.cms import (
    AbTestEndRequestVNext,
    AbTestRerunRequestVNext,
    BatchInputContentFolder,
    BatchInputPage,
    BatchResponseContentFolder,
    BatchResponseContentFolderWithErrors,
    BatchResponsePage,
    BatchResponsePageWithErrors,
    CollectionResponseWithTotalContentFolderForwardPaging,
    CollectionResponseWithTotalContentFolderVersion,
    CollectionResponseWithTotalPageForwardPaging,
    CollectionResponseWithTotalPageVersion,
    ContentFolder,
    ContentFolderVersion,
    ContentLanguageCloneRequestVNext,
    CursorPagedResultContentFolderLong,
    CursorPagedResultPageLong,
    Page,
    PageVersion,
)
```

Methods:

- <code title="get /cms/pages/2026-03/landing-pages/folders/cursor">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_landing_page_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_landing_page_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_content_folder_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/folders/cursor/query">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_landing_page_folders_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_landing_page_folders_by_query_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_content_folder_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/{objectId}/revisions/{revisionId}">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_landing_page_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page_version.py">PageVersion</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/cursor">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_landing_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_landing_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_page_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/cursor/query">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_landing_pages_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_landing_pages_by_query_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_page_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/site-pages/{objectId}/revisions/{revisionId}">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_site_page_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page_version.py">PageVersion</a></code>
- <code title="get /cms/pages/2026-03/site-pages/cursor">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_site_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_site_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_page_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/site-pages/cursor/query">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">get_site_pages_by_query</a>(\*\*<a href="src/hubspot_sdk/types/cms/page_get_site_pages_by_query_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/cursor_paged_result_page_long.py">object</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/{objectId}/revisions">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">list_landing_page_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/page_list_landing_page_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page_version.py">SyncPage[PageVersion]</a></code>
- <code title="get /cms/pages/2026-03/site-pages/{objectId}/revisions">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">list_site_page_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/page_list_site_page_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page_version.py">SyncPage[PageVersion]</a></code>
- <code title="post /cms/pages/2026-03/site-pages/{objectId}/draft/reset">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">reset_site_page_draft</a>(object_id) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/{objectId}/revisions/{revisionId}/restore">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">restore_landing_page_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">restore_landing_page_revision_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/site-pages/{objectId}/revisions/{revisionId}/restore">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">restore_site_page_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/site-pages/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.pages.<a href="./src/hubspot_sdk/resources/cms/pages/pages.py">restore_site_page_revision_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>

### ABTests

Methods:

- <code title="post /cms/pages/2026-03/landing-pages/ab-test/create-variation">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">create_landing_page_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_create_landing_page_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/site-pages/ab-test/create-variation">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">create_site_page_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_create_site_page_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/ab-test/end">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">end_landing_page_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_end_landing_page_test_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/ab-test/end">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">end_site_page_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_end_site_page_test_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/ab-test/rerun">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">rerun_landing_page_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_rerun_landing_page_test_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/ab-test/rerun">client.cms.pages.a_b_tests.<a href="./src/hubspot_sdk/resources/cms/pages/a_b_tests.py">rerun_site_page_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/a_b_test_rerun_site_page_test_params.py">params</a>) -> None</code>

### Batch

Methods:

- <code title="post /cms/pages/2026-03/landing-pages/folders/batch/create">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">create_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_create_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/batch/create">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">create_landing_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_create_landing_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/pages/2026-03/site-pages/batch/create">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">create_site_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_create_site_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/folders/batch/archive">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">delete_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_delete_folders_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/batch/archive">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">delete_landing_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_delete_landing_pages_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/batch/archive">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">delete_site_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_delete_site_pages_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/batch/read">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">get_landing_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_get_landing_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/pages/2026-03/site-pages/batch/read">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">get_site_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_get_site_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/folders/batch/update">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">update_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_update_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/batch/update">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">update_landing_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_update_landing_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/pages/2026-03/site-pages/batch/update">client.cms.pages.batch.<a href="./src/hubspot_sdk/resources/cms/pages/batch.py">update_site_pages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/batch_update_site_pages_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>

### Folders

Methods:

- <code title="post /cms/pages/2026-03/landing-pages/folders">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/folder_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="patch /cms/pages/2026-03/landing-pages/folders/{objectId}">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/folder_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/folders">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/folder_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">SyncPage[ContentFolder]</a></code>
- <code title="delete /cms/pages/2026-03/landing-pages/folders/{objectId}">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/folder_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/folders/batch/read">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/folder_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/folders/{objectId}">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/folder_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/folders/{objectId}/revisions/{revisionId}">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">get_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/content_folder_version.py">ContentFolderVersion</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/folders/{objectId}/revisions">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">list_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/folder_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder_version.py">SyncPage[ContentFolderVersion]</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/folders/{objectId}/revisions/{revisionId}/restore">client.cms.pages.folders.<a href="./src/hubspot_sdk/resources/cms/pages/folders.py">restore_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>

### LandingPages

Methods:

- <code title="post /cms/pages/2026-03/landing-pages">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="patch /cms/pages/2026-03/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/landing-pages">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">SyncPage[Page]</a></code>
- <code title="delete /cms/pages/2026-03/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/clone">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/landing-pages/{objectId}/draft">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_draft</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/landing-pages/{objectId}/draft/push-live">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">push_draft_live</a>(object_id) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/{objectId}/draft/reset">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/pages/2026-03/landing-pages/schedule">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_schedule_params.py">params</a>) -> None</code>
- <code title="patch /cms/pages/2026-03/landing-pages/{objectId}/draft">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>

### MultiLanguage

Methods:

- <code title="post /cms/pages/2026-03/site-pages/multi-language/attach-to-lang-group">client.cms.pages.multi_language.<a href="./src/hubspot_sdk/resources/cms/pages/multi_language.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/multi_language_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/pages/2026-03/site-pages/multi-language/create-language-variation">client.cms.pages.multi_language.<a href="./src/hubspot_sdk/resources/cms/pages/multi_language.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/multi_language_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/site-pages/multi-language/detach-from-lang-group">client.cms.pages.multi_language.<a href="./src/hubspot_sdk/resources/cms/pages/multi_language.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/multi_language_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/pages/2026-03/site-pages/multi-language/set-new-lang-primary">client.cms.pages.multi_language.<a href="./src/hubspot_sdk/resources/cms/pages/multi_language.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/multi_language_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/multi-language/update-languages">client.cms.pages.multi_language.<a href="./src/hubspot_sdk/resources/cms/pages/multi_language.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/multi_language_update_languages_params.py">params</a>) -> BinaryAPIResponse</code>

### WebsitePages

Methods:

- <code title="post /cms/pages/2026-03/site-pages">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="patch /cms/pages/2026-03/site-pages/{objectId}">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/site-pages">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">SyncPage[Page]</a></code>
- <code title="delete /cms/pages/2026-03/site-pages/{objectId}">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/clone">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/site-pages/{objectId}">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/pages/2026-03/site-pages/{objectId}/draft">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">get_draft</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/pages/2026-03/site-pages/{objectId}/draft/push-live">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">publish_draft</a>(object_id) -> None</code>
- <code title="post /cms/pages/2026-03/site-pages/schedule">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/pages/2026-03/landing-pages/multi-language/set-new-lang-primary">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="patch /cms/pages/2026-03/site-pages/{objectId}/draft">client.cms.pages.website_pages.<a href="./src/hubspot_sdk/resources/cms/pages/website_pages.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/website_page_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>

## SiteSearch

Types:

```python
from hubspot_sdk.types.cms import (
    ContentSearchResult,
    IndexedData,
    IndexedField,
    PublicSearchResults,
)
```

Methods:

- <code title="get /cms/site-search/2026-03/indexed-data/{contentId}">client.cms.site_search.<a href="./src/hubspot_sdk/resources/cms/site_search.py">get_indexed_data</a>(content_id, \*\*<a href="src/hubspot_sdk/types/cms/site_search_get_indexed_data_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/indexed_data.py">IndexedData</a></code>
- <code title="get /cms/site-search/2026-03/search">client.cms.site_search.<a href="./src/hubspot_sdk/resources/cms/site_search.py">search</a>(\*\*<a href="src/hubspot_sdk/types/cms/site_search_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/public_search_results.py">PublicSearchResults</a></code>

## SourceCode

Types:

```python
from hubspot_sdk.types.cms import AssetFileMetadata, FileExtractRequest
```

Methods:

- <code title="post /cms/source-code/2026-03/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">create</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="delete /cms/source-code/2026-03/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">delete</a>(path, \*, environment) -> None</code>
- <code title="post /cms/source-code/2026-03/extract/async">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">extract_async</a>(\*\*<a href="src/hubspot_sdk/types/cms/source_code_extract_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /cms/source-code/2026-03/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get</a>(path, \*, environment) -> BinaryAPIResponse</code>
- <code title="get /cms/source-code/2026-03/extract/async/tasks/{taskId}/status">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_extraction_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/shared/action_response.py">ActionResponse</a></code>
- <code title="get /cms/source-code/2026-03/{environment}/metadata/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_metadata</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_get_metadata_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="put /cms/source-code/2026-03/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">upsert</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="post /cms/source-code/2026-03/{environment}/validate/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">validate</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_validate_params.py">params</a>) -> BinaryAPIResponse</code>

## URLMappings

Types:

```python
from hubspot_sdk.types.cms import URLMappingsURLMapping
```

Methods:

- <code title="post /url-mappings/2026-03/url-mappings">client.cms.url_mappings.<a href="./src/hubspot_sdk/resources/cms/url_mappings.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_mapping_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /url-mappings/2026-03/url-mappings">client.cms.url_mappings.<a href="./src/hubspot_sdk/resources/cms/url_mappings.py">list</a>() -> BinaryAPIResponse</code>
- <code title="delete /url-mappings/2026-03/url-mappings/{id}">client.cms.url_mappings.<a href="./src/hubspot_sdk/resources/cms/url_mappings.py">delete</a>(id) -> None</code>
- <code title="get /url-mappings/2026-03/url-mappings/{id}">client.cms.url_mappings.<a href="./src/hubspot_sdk/resources/cms/url_mappings.py">get</a>(id) -> BinaryAPIResponse</code>

## URLRedirects

Types:

```python
from hubspot_sdk.types.cms import (
    CollectionResponseWithTotalURLMappingForwardPaging,
    URLMapping,
    URLMappingCreateRequestBody,
)
```

Methods:

- <code title="post /cms/url-redirects/2026-03">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="patch /cms/url-redirects/2026-03/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">update</a>(url_redirect_id, \*\*<a href="src/hubspot_sdk/types/cms/url_redirect_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="get /cms/url-redirects/2026-03">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">SyncPage[URLMapping]</a></code>
- <code title="delete /cms/url-redirects/2026-03/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">delete</a>(url_redirect_id) -> None</code>
- <code title="get /cms/url-redirects/2026-03/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">get</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
