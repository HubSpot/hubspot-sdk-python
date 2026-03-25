# Cms

## Blogs

Types:

```python
from hubspot_sdk.types.cms import (
    AttachToLangPrimaryRequestVNext,
    DetachFromLangGroupRequestVNext,
    PublicAccessRule,
    SetNewLanguagePrimaryRequestVNext,
    UpdateLanguagesRequestVNext,
    VersionUser,
)
```

### Posts

Types:

```python
from hubspot_sdk.types.cms.blogs import (
    Angle,
    BackgroundImage,
    BatchInputBlogPost,
    BatchInputJsonNode,
    BatchInputString,
    BatchResponseBlogPost,
    BatchResponseBlogPostWithErrors,
    BlogPost,
    BlogPostLanguageCloneRequestVNext,
    BlogPostVersion,
    BreakpointStyles,
    CollectionResponseWithTotalBlogPostForwardPaging,
    CollectionResponseWithTotalBlogPostVersion,
    ColorStop,
    ContentCloneRequestVNext,
    ContentLanguageVariation,
    ContentScheduleRequestVNext,
    Gradient,
    LayoutSection,
    Margin,
    Padding,
    RgbaColor,
    RowMetaData,
    SideOrCorner,
    Size,
    Styles,
    VersionBlogPost,
)
```

Methods:

- <code title="post /cms/blogs/2026-03/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="patch /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_list_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/attach-to-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/clone">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_clone_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/create-language-variation">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_create_lang_variation_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/detach-from-lang-group">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_draft_by_id</a>(object_id) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_version</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/posts/{objectId}/revisions">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_versions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_previous_versions_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/draft/push-live">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">push_live</a>(object_id) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/draft/reset">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">reset_draft</a>(object_id) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}/restore">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">restore_previous_version</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/{objectId}/revisions/{revisionId}/restore-to-draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">restore_previous_version_to_draft</a>(revision_id, \*, object_id) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/schedule">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">schedule</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_schedule_params.py">params</a>) -> None</code>
- <code title="put /cms/blogs/2026-03/posts/multi-language/set-new-lang-primary">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="patch /cms/blogs/2026-03/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update_draft</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_draft_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/multi-language/update-languages">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/post_update_langs_params.py">params</a>) -> BinaryAPIResponse</code>

#### Batch

Methods:

- <code title="post /cms/blogs/2026-03/posts/batch/create">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/batch/update">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/posts/batch/archive">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/posts/batch/read">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_get_params.py">params</a>) -> BinaryAPIResponse</code>

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
