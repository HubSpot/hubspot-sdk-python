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
    Styles,
    UpdateLanguagesRequestVNext,
)
```

## AuditLogs

Types:

```python
from hubspot_sdk.types.cms import CollectionResponsePublicAuditLog, PublicAuditLog
```

Methods:

- <code title="get /cms/v3/audit-logs/">client.cms.audit_logs.<a href="./src/hubspot_sdk/resources/cms/audit_logs.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/audit_log_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/public_audit_log.py">SyncPage[PublicAuditLog]</a></code>

## Blogs

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

- <code title="post /cms/v3/blogs/authors">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_author.py">BlogAuthor</a></code>
- <code title="patch /cms/v3/blogs/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_author.py">BlogAuthor</a></code>
- <code title="get /cms/v3/blogs/authors">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_author.py">SyncPage[BlogAuthor]</a></code>
- <code title="delete /cms/v3/blogs/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/authors/multi-language/attach-to-lang-group">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/authors/batch/create">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_author.py">BatchResponseBlogAuthor</a></code>
- <code title="post /cms/v3/blogs/authors/multi-language/create-language-variation">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_author.py">BlogAuthor</a></code>
- <code title="post /cms/v3/blogs/authors/batch/archive">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/authors/multi-language/detach-from-lang-group">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/authors/{objectId}">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_author.py">BlogAuthor</a></code>
- <code title="post /cms/v3/blogs/authors/batch/read">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_author.py">BatchResponseBlogAuthor</a></code>
- <code title="put /cms/v3/blogs/authors/multi-language/set-new-lang-primary">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/authors/batch/update">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_author.py">BatchResponseBlogAuthor</a></code>
- <code title="post /cms/v3/blogs/authors/multi-language/update-languages">client.cms.blogs.authors.<a href="./src/hubspot_sdk/resources/cms/blogs/authors.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/author_update_languages_params.py">params</a>) -> None</code>

### Posts

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    BatchInputBlogPost,
    BatchResponseBlogPost,
    BatchResponseBlogPostWithErrors,
    BlogPost,
    BlogPostLanguageCloneRequestVNext,
    CollectionResponseWithTotalBlogPostForwardPaging,
    CollectionResponseWithTotalVersionBlogPost,
    ContentLanguageVariation,
    VersionBlogPost,
)
```

Methods:

- <code title="post /cms/v3/blogs/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="patch /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">SyncPage[BlogPost]</a></code>
- <code title="delete /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/posts/multi-language/attach-to-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/posts/clone">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/create-language-variation">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/detach-from-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_draft_by_id</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_version</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog_post.py">VersionBlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_versions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_previous_versions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog_post.py">SyncPage[VersionBlogPost]</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/draft/push-live">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">push_live</a>(object_id) -> None</code>
- <code title="post /cms/v3/blogs/posts/{objectId}/draft/reset">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">restore_previous_version</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">restore_previous_version_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/schedule">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/v3/blogs/posts/multi-language/set-new-lang-primary">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="patch /cms/v3/blogs/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/multi-language/update-languages">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_langs_params.py">params</a>) -> None</code>

#### Batch

Methods:

- <code title="post /cms/v3/blogs/posts/batch/create">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_post.py">BatchResponseBlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/batch/update">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_post.py">BatchResponseBlogPost</a></code>
- <code title="post /cms/v3/blogs/posts/batch/archive">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/posts/batch/read">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_post.py">BatchResponseBlogPost</a></code>

### Settings

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    Blog,
    BlogLanguageCloneRequestVNext,
    CollectionResponseWithTotalBlogForwardPaging,
    CollectionResponseWithTotalVersionBlog,
    VersionBlog,
)
```

Methods:

- <code title="get /cms/v3/blog-settings/settings">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">SyncPage[Blog]</a></code>
- <code title="post /cms/v3/blog-settings/settings/multi-language/attach-to-lang-group">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blog-settings/settings/multi-language/create-language-variation">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">Blog</a></code>
- <code title="post /cms/v3/blog-settings/settings/multi-language/detach-from-lang-group">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blog-settings/settings/{blogId}">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">get</a>(blog_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog.py">Blog</a></code>
- <code title="get /cms/v3/blog-settings/settings/{blogId}/revisions/{revisionId}">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">get_revision</a>(revision_id, \*, blog_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog.py">VersionBlog</a></code>
- <code title="get /cms/v3/blog-settings/settings/{blogId}/revisions">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">list_revisions</a>(blog_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog.py">SyncPage[VersionBlog]</a></code>
- <code title="put /cms/v3/blog-settings/settings/multi-language/set-new-lang-primary">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blog-settings/settings/multi-language/update-languages">client.cms.blogs.settings.<a href="./src/hubspot_sdk/resources/cms/blogs/settings.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/setting_update_languages_params.py">params</a>) -> None</code>

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

- <code title="post /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="patch /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="get /cms/v3/blogs/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">SyncPage[Tag]</a></code>
- <code title="delete /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/create">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/batch/archive">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/batch/read">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="put /cms/v3/blogs/tags/multi-language/set-new-lang-primary">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/update">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/update-languages">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_langs_params.py">params</a>) -> None</code>

## Domains

Types:

```python
from hubspot_sdk.types.cms import CollectionResponseWithTotalDomainForwardPaging, Domain
```

Methods:

- <code title="get /cms/v3/domains/">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/domain_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/domain.py">SyncPage[Domain]</a></code>
- <code title="get /cms/v3/domains/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">get</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/domain.py">Domain</a></code>

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
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
    Column,
    ColumnRequest,
    ForeignID,
    HubDBTableCloneRequest,
    HubDBTableRowBatchCloneRequest,
    HubDBTableRowV3,
    HubDBTableRowV3BatchUpdateRequest,
    HubDBTableRowV3Request,
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

- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">create</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">list</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/hub_db_table_row_v3_wrapper.py">SyncPage[object]</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft/clone">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">clone_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">delete_draft</a>(row_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">get</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">get_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">list_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/hub_db_table_row_v3_wrapper.py">SyncPage[object]</a></code>
- <code title="put /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">replace_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_replace_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/rows/{rowId}/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">update_draft</a>(row_id, \*, table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_row_v3.py">HubDBTableRowV3</a></code>

#### Batch

Methods:

- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/clone">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">clone_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_clone_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/create">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">create_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/batch/read">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">get_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/read">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">get_draft_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_get_draft_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/purge">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">purge_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_purge_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/replace">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">replace_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_replace_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft/batch/update">client.cms.hubdb.rows.batch.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/batch.py">update_batch</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/rows/batch_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_hub_db_table_row_v3.py">BatchResponseHubDBTableRowV3</a></code>

### Tables

Methods:

- <code title="post /cms/v3/hubdb/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">SyncPage[HubDBTableV3]</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">delete</a>(table_id_or_name) -> None</code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/clone">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">clone_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_clone_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="delete /cms/v3/hubdb/tables/{tableIdOrName}/versions/{versionId}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">delete_version</a>(version_id, \*, table_id_or_name) -> None</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft/export">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">export_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_export_draft_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">get_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_get_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/import">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">import_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_import_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/import_result.py">ImportResult</a></code>
- <code title="get /cms/v3/hubdb/tables/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list_draft</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">SyncPage[HubDBTableV3]</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">publish_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_publish_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">reset_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_reset_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/unpublish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">unpublish</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_unpublish_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">update_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>

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
    BatchResponsePropertyWithErrors,
    BeginsWith,
    BooleanPropertyVariable,
    BooleanTargetPropertyVariable,
    BulkIntegratorObjectCreationResponse,
    CaseChangeTestExtensionData,
    CollectionResponsePropertyGroupNoPaging,
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
    Expression,
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
    ObjectTypeDefinition,
    ObjectTypeDefinitionPatch,
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
    PropertyDefinition,
    PropertyDefinitionSource,
    PropertyGroup,
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
    TimestampOfPropertyVariable,
    TimestampOfTargetPropertyVariable,
    UpperCase,
    Xor,
    Year,
)
```

### Events

Methods:

- <code title="post /media-bridge/v1/events/attention-span">client.cms.media_bridge.events.<a href="./src/hubspot_sdk/resources/cms/media_bridge/events.py">create_attention_span_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge/event_create_attention_span_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/attention_span_event.py">AttentionSpanEvent</a></code>
- <code title="post /media-bridge/v1/events/media-played">client.cms.media_bridge.events.<a href="./src/hubspot_sdk/resources/cms/media_bridge/events.py">create_media_played_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge/event_create_media_played_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_played_event.py">MediaPlayedEvent</a></code>
- <code title="post /media-bridge/v1/events/media-played-percent">client.cms.media_bridge.events.<a href="./src/hubspot_sdk/resources/cms/media_bridge/events.py">create_media_played_percent_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge/event_create_media_played_percent_event_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_played_percentage_event.py">MediaPlayedPercentageEvent</a></code>

### Groups

Methods:

- <code title="post /media-bridge/v1/{appId}/properties/{objectType}/groups">client.cms.media_bridge.groups.<a href="./src/hubspot_sdk/resources/cms/media_bridge/groups.py">create</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/group_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>
- <code title="get /media-bridge/v1/{appId}/properties/{objectType}/groups">client.cms.media_bridge.groups.<a href="./src/hubspot_sdk/resources/cms/media_bridge/groups.py">list</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/cms/collection_response_property_group_no_paging.py">CollectionResponsePropertyGroupNoPaging</a></code>
- <code title="delete /media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.groups.<a href="./src/hubspot_sdk/resources/cms/media_bridge/groups.py">delete_by_name</a>(group_name, \*, app_id, object_type) -> None</code>
- <code title="get /media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.groups.<a href="./src/hubspot_sdk/resources/cms/media_bridge/groups.py">get_by_name</a>(group_name, \*, app_id, object_type) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>
- <code title="patch /media-bridge/v1/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.groups.<a href="./src/hubspot_sdk/resources/cms/media_bridge/groups.py">update_by_name</a>(group_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/group_update_by_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>

### IntegratorSettings

Methods:

- <code title="post /media-bridge/v1/{appId}/settings/object-definitions">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">create_object_definition</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_create_object_definition_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/bulk_integrator_object_creation_response.py">BulkIntegratorObjectCreationResponse</a></code>
- <code title="post /media-bridge/v1/{appId}/settings/oembed-domains">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">create_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_create_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="delete /media-bridge/v1/{appId}/settings/oembed-domains">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">delete_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_delete_oembed_domain_params.py">params</a>) -> None</code>
- <code title="get /media-bridge/v1/{appId}/settings/event-visibility">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">get_event_visibility_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_response.py">EventVisibilityResponse</a></code>
- <code title="get /media-bridge/v1/{appId}/settings/object-definitions/{mediaType}">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">get_object_definitions_by_media_type</a>(media_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_get_object_definitions_by_media_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/object_definition_response.py">ObjectDefinitionResponse</a></code>
- <code title="get /media-bridge/v1/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">get_oembed_domain</a>(o_embed_domain_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="get /media-bridge/v1/{appId}/settings/oembed-domains">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">list_oembed_domains</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_list_oembed_domains_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/o_embed_domains_collection_response.py">OEmbedDomainsCollectionResponse</a></code>
- <code title="post /media-bridge/v1/{appId}/settings/register">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">register_app_name</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_register_app_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>
- <code title="put /media-bridge/v1/{appId}/settings">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">update_app_name</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_update_app_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>
- <code title="patch /media-bridge/v1/{appId}/settings/event-visibility">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">update_event_visibility_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_update_event_visibility_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_change.py">EventVisibilityChange</a></code>
- <code title="patch /media-bridge/v1/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.integrator_settings.<a href="./src/hubspot_sdk/resources/cms/media_bridge/integrator_settings.py">update_oembed_domain</a>(o_embed_domain_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/integrator_setting_update_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>

### Properties

Methods:

- <code title="post /media-bridge/v1/{appId}/properties/{objectType}">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">create</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="patch /media-bridge/v1/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">update</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="get /media-bridge/v1/{appId}/properties/{objectType}">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">list</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_property_no_paging.py">CollectionResponsePropertyNoPaging</a></code>
- <code title="delete /media-bridge/v1/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">delete</a>(property_name, \*, app_id, object_type) -> None</code>
- <code title="post /media-bridge/v1/{appId}/properties/{objectType}/batch/create">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">create_batch</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /media-bridge/v1/{appId}/properties/{objectType}/batch/archive">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">delete_batch</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_delete_batch_params.py">params</a>) -> None</code>
- <code title="get /media-bridge/v1/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">get</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="post /media-bridge/v1/{appId}/properties/{objectType}/batch/read">client.cms.media_bridge.properties.<a href="./src/hubspot_sdk/resources/cms/media_bridge/properties.py">get_batch</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/property_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>

### Schemas

Types:

```python
from hubspot_sdk.types.cms.media_bridge import SchemaListResponse
```

Methods:

- <code title="patch /media-bridge/v1/{appId}/schemas/{objectType}">client.cms.media_bridge.schemas.<a href="./src/hubspot_sdk/resources/cms/media_bridge/schemas.py">update</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/objects_schemas_object_type_definition.py">ObjectsSchemasObjectTypeDefinition</a></code>
- <code title="get /media-bridge/v1/{appId}/schemas">client.cms.media_bridge.schemas.<a href="./src/hubspot_sdk/resources/cms/media_bridge/schemas.py">list</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge/schema_list_response.py">SchemaListResponse</a></code>
- <code title="post /media-bridge/v1/{appId}/schemas/{objectType}/associations">client.cms.media_bridge.schemas.<a href="./src/hubspot_sdk/resources/cms/media_bridge/schemas.py">create_association</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/association_definition.py">AssociationDefinition</a></code>
- <code title="delete /media-bridge/v1/{appId}/schemas/{objectType}/associations/{associationId}">client.cms.media_bridge.schemas.<a href="./src/hubspot_sdk/resources/cms/media_bridge/schemas.py">delete_association</a>(association_id, \*, app_id, object_type) -> None</code>
- <code title="get /media-bridge/v1/{appId}/schemas/{objectType}">client.cms.media_bridge.schemas.<a href="./src/hubspot_sdk/resources/cms/media_bridge/schemas.py">get</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>

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
    CollectionResponseWithTotalPageForwardPaging,
    CollectionResponseWithTotalVersionContentFolder,
    CollectionResponseWithTotalVersionPage,
    ContentFolder,
    ContentLanguageCloneRequestVNext,
    Page,
    PagesContentLanguageVariation,
    VersionContentFolder,
    VersionPage,
)
```

### LandingPages

Methods:

- <code title="post /cms/v3/pages/landing-pages">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_params.py">params</a>) -> None</code>
- <code title="patch /cms/v3/pages/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/v3/pages/landing-pages">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">SyncPage[Page]</a></code>
- <code title="delete /cms/v3/pages/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/multi-language/attach-to-lang-group">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/clone">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/ab-test/create-variation">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/batch/create">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/v3/pages/landing-pages/folders">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create_folder</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_folder_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/folders/batch/create">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create_folders_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_folders_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/multi-language/create-language-variation">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/batch/archive">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_delete_batch_params.py">params</a>) -> None</code>
- <code title="delete /cms/v3/pages/landing-pages/folders/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">delete_folder</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_delete_folder_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/folders/batch/archive">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">delete_folders_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_delete_folders_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/multi-language/detach-from-lang-group">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/ab-test/end">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">end_ab_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_end_ab_test_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/pages/landing-pages/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/batch/read">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="get /cms/v3/pages/landing-pages/{objectId}/draft">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_draft</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/v3/pages/landing-pages/folders/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_folder</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_get_folder_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="get /cms/v3/pages/landing-pages/folders/{objectId}/revisions/{revisionId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_folder_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/version_content_folder.py">VersionContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/folders/batch/read">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_folders_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_get_folders_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="get /cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">get_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/version_page.py">VersionPage</a></code>
- <code title="get /cms/v3/pages/landing-pages/folders/{objectId}/revisions">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_folder_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_folder_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/version_content_folder.py">SyncPage[VersionContentFolder]</a></code>
- <code title="get /cms/v3/pages/landing-pages/folders">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">SyncPage[ContentFolder]</a></code>
- <code title="get /cms/v3/pages/landing-pages/{objectId}/revisions">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/version_page.py">SyncPage[VersionPage]</a></code>
- <code title="post /cms/v3/pages/landing-pages/{objectId}/draft/push-live">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">publish_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/ab-test/rerun">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">rerun_ab_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_rerun_ab_test_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/{objectId}/draft/reset">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/folders/{objectId}/revisions/{revisionId}/restore">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">restore_folder_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}/restore">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">restore_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">restore_revision_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/landing-pages/schedule">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/v3/pages/landing-pages/multi-language/set-new-lang-primary">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/landing-pages/batch/update">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="patch /cms/v3/pages/landing-pages/{objectId}/draft">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="patch /cms/v3/pages/landing-pages/folders/{objectId}">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_folder</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_folder_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/content_folder.py">ContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/folders/batch/update">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_folders_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_folders_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_content_folder.py">BatchResponseContentFolder</a></code>
- <code title="post /cms/v3/pages/landing-pages/multi-language/update-languages">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_update_languages_params.py">params</a>) -> None</code>

### SitePages

Methods:

- <code title="post /cms/v3/pages/site-pages">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_create_params.py">params</a>) -> None</code>
- <code title="patch /cms/v3/pages/site-pages/{objectId}">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/v3/pages/site-pages">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">SyncPage[Page]</a></code>
- <code title="delete /cms/v3/pages/site-pages/{objectId}">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/multi-language/attach-to-lang-group">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/clone">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/ab-test/create-variation">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/batch/create">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="post /cms/v3/pages/site-pages/multi-language/create-language-variation">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">create_language_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_create_language_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/batch/archive">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/multi-language/detach-from-lang-group">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/ab-test/end">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">end_ab_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_end_ab_test_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/pages/site-pages/{objectId}">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/batch/read">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_get_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="get /cms/v3/pages/site-pages/{objectId}/draft">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">get_draft</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="get /cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">get_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/version_page.py">VersionPage</a></code>
- <code title="get /cms/v3/pages/site-pages/{objectId}/revisions">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">list_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/version_page.py">SyncPage[VersionPage]</a></code>
- <code title="post /cms/v3/pages/site-pages/{objectId}/draft/push-live">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">publish_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/pages/site-pages/ab-test/rerun">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">rerun_ab_test</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_rerun_ab_test_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/{objectId}/draft/reset">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}/restore">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">restore_revision</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">restore_revision_to_draft</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/schedule">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/v3/pages/site-pages/multi-language/set-new-lang-primary">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">set_new_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_set_new_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/pages/site-pages/batch/update">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/batch_response_page.py">BatchResponsePage</a></code>
- <code title="patch /cms/v3/pages/site-pages/{objectId}/draft">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/page.py">Page</a></code>
- <code title="post /cms/v3/pages/site-pages/multi-language/update-languages">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">update_languages</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_update_languages_params.py">params</a>) -> None</code>

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

- <code title="get /cms/v3/site-search/indexed-data/{contentId}">client.cms.site_search.<a href="./src/hubspot_sdk/resources/cms/site_search.py">get_indexed_data</a>(content_id, \*\*<a href="src/hubspot_sdk/types/cms/site_search_get_indexed_data_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/indexed_data.py">IndexedData</a></code>
- <code title="get /cms/v3/site-search/search">client.cms.site_search.<a href="./src/hubspot_sdk/resources/cms/site_search.py">search</a>(\*\*<a href="src/hubspot_sdk/types/cms/site_search_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/public_search_results.py">PublicSearchResults</a></code>

## SourceCode

Types:

```python
from hubspot_sdk.types.cms import AssetFileMetadata, FileExtractRequest
```

Methods:

- <code title="post /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">create</a>(file_path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="delete /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">delete</a>(file_path, \*, environment) -> None</code>
- <code title="post /cms/v3/source-code/extract/async">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">extract_async</a>(\*\*<a href="src/hubspot_sdk/types/cms/source_code_extract_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get</a>(file_path, \*, environment) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/source-code/extract/async/tasks/{taskId}/status">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_extraction_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/shared/action_response.py">ActionResponse</a></code>
- <code title="get /cms/v3/source-code/{environment}/metadata/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_metadata</a>(file_path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_get_metadata_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="put /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">upsert</a>(file_path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="post /cms/v3/source-code/{environment}/validate/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">validate</a>(file_path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_validate_params.py">params</a>) -> BinaryAPIResponse</code>

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

- <code title="post /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="patch /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">update</a>(url_redirect_id, \*\*<a href="src/hubspot_sdk/types/cms/url_redirect_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
- <code title="get /cms/v3/url-redirects/">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/url_redirect_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">SyncPage[URLMapping]</a></code>
- <code title="delete /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">delete</a>(url_redirect_id) -> None</code>
- <code title="get /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">get</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>
