# Cms

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
    AttachToLangPrimaryRequestVNext,
    BatchInputJsonNode,
    DetachFromLangGroupRequestVNext,
    PublicAccessRule,
    SetNewLanguagePrimaryRequestVNext,
    UpdateLanguagesRequestVNext,
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
    Angle,
    BackgroundImage,
    BatchInputBlogPost,
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

- <code title="post /cms/blogs/2026-03/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="patch /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_list_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/batch/create">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_batch_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/batch/archive">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /cms/blogs/2026-03/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">get</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_get_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/batch/read">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">get_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_get_batch_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="put /cms/blogs/2026-03/tags/multi-language/set-new-lang-primary">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">set_lang_primary</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_set_lang_primary_params.py">params</a>) -> None</code>
- <code title="post /cms/blogs/2026-03/tags/batch/update">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_batch_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /cms/blogs/2026-03/tags/multi-language/update-languages">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">update_langs</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_update_langs_params.py">params</a>) -> BinaryAPIResponse</code>

## Domains

Types:

```python
from hubspot_sdk.types.cms import CollectionResponseWithTotalDomain, Domain
```

Methods:

- <code title="get /cms/domains/2026-03">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">list</a>(\*\*<a href="src/hubspot_sdk/types/cms/domain_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/domain.py">SyncPage[Domain]</a></code>
- <code title="get /cms/domains/2026-03/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">get</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/domain.py">Domain</a></code>

## MediaBridge

Types:

```python
from hubspot_sdk.types.cms import (
    AbsoluteValue,
    AddNumbers,
    AddTime,
    And,
    AttentionSpanCalculatedValues,
    AttentionSpanEventRequest,
    BeginsWith,
    BooleanPropertyVariable,
    BooleanTargetPropertyVariable,
    BulkIntegratorObjectCreationResponse,
    CaseChangeTestExtensionData,
    CollectionResponseMediaBridgeObjectForwardPaging,
    ConcatStrings,
    ConstantBoolean,
    ConstantNumber,
    ConstantString,
    Contains,
    CreateAudioObjectRequest,
    CreateDocumentObjectRequest,
    CreateImageObjectRequest,
    CreateMBObjectRequest,
    CreateOtherObjectRequest,
    CreateVideoObjectRequest,
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
    MediaBridgeObject,
    MediaBridgePropertyUpdate,
    MediaBridgeProviderPartial,
    MediaBridgeProviderRegistrationResponse,
    MediaPlayedEventRequest,
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
    UpdateAudioObjectRequest,
    UpdateDocumentObjectRequest,
    UpdateImageObjectRequest,
    UpdateMBObjectRequest,
    UpdateOtherObjectRequest,
    UpdateVideoObjectRequest,
    UpperCase,
    VideoObject,
    Xor,
    Year,
)
```

Methods:

- <code title="post /media-bridge/2026-03/objects">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create</a>() -> <a href="./src/hubspot_sdk/types/cms/media_bridge_object.py">MediaBridgeObject</a></code>
- <code title="patch /media-bridge/2026-03/objects/{objectId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_object.py">MediaBridgeObject</a></code>
- <code title="get /media-bridge/2026-03/objects/{mediaType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list</a>(media_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_object.py">SyncPage[MediaBridgeObject]</a></code>
- <code title="delete /media-bridge/2026-03/objects/{mediaType}/{objectId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete</a>(object_id, \*, media_type) -> None</code>
- <code title="post /media-bridge/2026-03/{appId}/schemas/{objectType}/associations">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_association</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/association_definition.py">AssociationDefinition</a></code>
- <code title="post /media-bridge/2026-03/events/attention-span">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_attention_span_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_attention_span_event_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /media-bridge/2026-03/events/media-played">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_media_played_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_media_played_event_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /media-bridge/2026-03/events/media-played-percent">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_media_played_percent_event</a>(\*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_media_played_percent_event_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /media-bridge/2026-03/{appId}/settings/object-definitions">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_object_type</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_object_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/bulk_integrator_object_creation_response.py">BulkIntegratorObjectCreationResponse</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_property</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/groups">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_property_group</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_create_property_group_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/video-association-definition">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">create_video_association_definition</a>(app_id) -> <a href="./src/hubspot_sdk/types/events/association_definition.py">AssociationDefinition</a></code>
- <code title="delete /media-bridge/2026-03/{appId}/schemas/{objectType}/associations/{associationId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_association</a>(association_id, \*, app_id, object_type) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_oembed_domain</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_delete_oembed_domain_params.py">params</a>) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_property</a>(property_name, \*, app_id, object_type) -> None</code>
- <code title="delete /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">delete_property_group</a>(group_name, \*, app_id, object_type) -> None</code>
- <code title="get /media-bridge/2026-03/objects/{mediaType}/{objectId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get</a>(object_id, \*, media_type) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_object.py">MediaBridgeObject</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/event-visibility">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_event_visibility_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_response.py">EventVisibilityResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_oembed_domain</a>(o_embed_domain_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_property</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_get_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_property_group</a>(group_name, \*, app_id, object_type) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="get /media-bridge/2026-03/{appId}/schemas/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">get_schema</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/shared/object_schema.py">ObjectSchema</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/object-definitions/{mediaType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_object_types_by_media_type</a>(media_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_object_types_by_media_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/object_definition_response.py">ObjectDefinitionResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/settings/oembed-domains">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_oembed_domains</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_oembed_domains_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/o_embed_domains_collection_response.py">OEmbedDomainsCollectionResponse</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_properties</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_properties_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/collection_response_property_no_paging.py">CollectionResponsePropertyNoPaging</a></code>
- <code title="get /media-bridge/2026-03/{appId}/properties/{objectType}/groups">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_property_groups</a>(object_type, \*, app_id) -> <a href="./src/hubspot_sdk/types/shared/collection_response_property_group_no_paging.py">CollectionResponsePropertyGroupNoPaging</a></code>
- <code title="get /media-bridge/2026-03/{appId}/schemas">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">list_schemas</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_list_schemas_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>
- <code title="post /media-bridge/2026-03/{appId}/settings/register">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">register_app_name</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_register_app_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/settings/event-visibility">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_event_visibility_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_event_visibility_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/event_visibility_change.py">EventVisibilityChange</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/settings/oembed-domains/{oEmbedDomainId}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_oembed_domain</a>(o_embed_domain_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_oembed_domain_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/integrator_o_embed_domain_model.py">IntegratorOEmbedDomainModel</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/properties/{objectType}/{propertyName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_property</a>(property_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/properties/{objectType}/groups/{groupName}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_property_group</a>(group_name, \*, app_id, object_type, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_property_group_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="patch /media-bridge/2026-03/{appId}/schemas/{objectType}">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_schema</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_schema_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/object_type_definition.py">ObjectTypeDefinition</a></code>
- <code title="put /media-bridge/2026-03/{appId}/settings">client.cms.media_bridge.<a href="./src/hubspot_sdk/resources/cms/media_bridge/media_bridge.py">update_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge_update_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/media_bridge_provider_registration_response.py">MediaBridgeProviderRegistrationResponse</a></code>

### Batch

Methods:

- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/create">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">create</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/archive">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">delete</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /media-bridge/2026-03/{appId}/properties/{objectType}/batch/read">client.cms.media_bridge.batch.<a href="./src/hubspot_sdk/resources/cms/media_bridge/batch.py">get</a>(object_type, \*, app_id, \*\*<a href="src/hubspot_sdk/types/cms/media_bridge/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>

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
