# Shared Types

```python
from hubspot_sdk.types import (
    AbTestCreateRequestVNext,
    ActionResponse,
    AssociationSpec,
    BatchInputString,
    Error,
    ErrorDetail,
    ForwardPaging,
    HubDBTableRowV3Wrapper,
    NextPage,
    Paging,
    PreviousPage,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAdsSearchFilter,
    PublicAdsTimeFilter,
    PublicAllHistoryRefineBy,
    PublicAllPropertyTypesOperation,
    PublicAndFilterBranch,
    PublicAssociationFilterBranch,
    PublicAssociationInListFilter,
    PublicBoolPropertyOperation,
    PublicCalendarDatePropertyOperation,
    PublicCampaignInfluencedFilter,
    PublicCommunicationSubscriptionFilter,
    PublicComparativeDatePropertyOperation,
    PublicComparativePropertyUpdatedOperation,
    PublicConstantFilter,
    PublicCtaAnalyticsFilter,
    PublicDatePoint,
    PublicDatePropertyOperation,
    PublicDateTimePropertyOperation,
    PublicEmailEventFilter,
    PublicEmailSubscriptionFilter,
    PublicEnumerationPropertyOperation,
    PublicEventAnalyticsFilter,
    PublicEventFilterMetadata,
    PublicFiscalQuarterReference,
    PublicFiscalYearReference,
    PublicFormSubmissionFilter,
    PublicFormSubmissionOnPageFilter,
    PublicIndexedTimePoint,
    PublicIndexOffset,
    PublicInListFilter,
    PublicInListFilterMetadata,
    PublicIntegrationEventFilter,
    PublicMonthReference,
    PublicMultiStringPropertyOperation,
    PublicNotAllFilterBranch,
    PublicNotAnyFilterBranch,
    PublicNowReference,
    PublicNumAssociationsFilter,
    PublicNumberPropertyOperation,
    PublicNumOccurrencesRefineBy,
    PublicObjectID,
    PublicOrFilterBranch,
    PublicPageViewAnalyticsFilter,
    PublicPrivacyAnalyticsFilter,
    PublicPropertyAssociationFilterBranch,
    PublicPropertyAssociationInListFilter,
    PublicPropertyFilter,
    PublicPropertyReferencedTime,
    PublicQuarterReference,
    PublicRangedDatePropertyOperation,
    PublicRangedNumberPropertyOperation,
    PublicRangedTimeOperation,
    PublicRelativeComparativeTimestampRefineBy,
    PublicRelativeRangedTimestampRefineBy,
    PublicRestrictedFilterBranch,
    PublicRollingDateRangePropertyOperation,
    PublicRollingPropertyUpdatedOperation,
    PublicSetOccurrencesRefineBy,
    PublicStringPropertyOperation,
    PublicSurveyMonkeyFilter,
    PublicSurveyMonkeyValueFilter,
    PublicTimeOffset,
    PublicTimePointOperation,
    PublicTodayReference,
    PublicUnifiedEventsFilter,
    PublicUnifiedEventsFilterBranch,
    PublicWebinarFilter,
    PublicWeekReference,
    PublicYearReference,
    StandardError,
    TaskLocator,
    VersionUser,
)
```

# Account

Types:

```python
from hubspot_sdk.types.account import (
    ActingUser,
    APIUsage,
    CollectionResponseAPIUsage,
    CollectionResponseHydratedCriticalActionForwardPaging,
    CollectionResponsePublicAPIUserActionEventForwardPaging,
    CollectionResponsePublicLoginAuditForwardPaging,
    HydratedCriticalAction,
    PortalInformationResponse,
    PublicAPIUserActionEvent,
    PublicLoginAudit,
)
```

## Activity

Methods:

- <code title="get /account-info/v3/activity/audit-logs">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_audit_logs</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_audit_logs_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/collection_response_public_api_user_action_event_forward_paging.py">CollectionResponsePublicAPIUserActionEventForwardPaging</a></code>
- <code title="get /account-info/v3/activity/login">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_login_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_login_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/collection_response_public_login_audit_forward_paging.py">CollectionResponsePublicLoginAuditForwardPaging</a></code>
- <code title="get /account-info/v3/activity/security">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_security_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_security_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/collection_response_hydrated_critical_action_forward_paging.py">CollectionResponseHydratedCriticalActionForwardPaging</a></code>

## Details

Methods:

- <code title="get /account-info/v3/details">client.account.details.<a href="./src/hubspot_sdk/resources/account/details.py">get</a>() -> <a href="./src/hubspot_sdk/types/account/portal_information_response.py">PortalInformationResponse</a></code>

## Usage

Methods:

- <code title="get /account-info/v3/api-usage/daily/private-apps">client.account.usage.<a href="./src/hubspot_sdk/resources/account/usage.py">get_daily_private_apps_usage</a>() -> <a href="./src/hubspot_sdk/types/account/collection_response_api_usage.py">CollectionResponseAPIUsage</a></code>

# Auth

## OAuth

Types:

```python
from hubspot_sdk.types.auth import (
    AccessTokenInfoResponse,
    RefreshTokenInfoResponse,
    TokenResponseIf,
)
```

Methods:

- <code title="post /oauth/v1/token">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">create_access_token</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_create_access_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/token_response_if.py">TokenResponseIf</a></code>
- <code title="delete /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">delete_refresh_token</a>(token) -> None</code>
- <code title="get /oauth/v1/access-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get_access_token</a>(token) -> <a href="./src/hubspot_sdk/types/auth/access_token_info_response.py">AccessTokenInfoResponse</a></code>
- <code title="get /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get_refresh_token</a>(token) -> <a href="./src/hubspot_sdk/types/auth/refresh_token_info_response.py">RefreshTokenInfoResponse</a></code>

# Automation

## Actions

Types:

```python
from hubspot_sdk.types.automation import (
    BatchInputCallbackCompletionBatchRequest,
    CallbackCompletionBatchRequest,
    CallbackCompletionRequest,
    CollectionResponsePublicActionDefinitionForwardPaging,
    CollectionResponsePublicActionFunctionIdentifierNoPaging,
    CollectionResponsePublicActionRevisionForwardPaging,
    FieldTypeDefinition,
    InputFieldDefinition,
    Option,
    OutputFieldDefinition,
    PublicActionDefinition,
    PublicActionDefinitionEgg,
    PublicActionDefinitionPatch,
    PublicActionFunction,
    PublicActionFunctionIdentifier,
    PublicActionLabels,
    PublicActionRevision,
    PublicConditionalSingleFieldDependency,
    PublicExecutionTranslationRule,
    PublicObjectRequestOptions,
    PublicSingleFieldDependency,
)
```

### Callbacks

Methods:

- <code title="post /automation/v4/actions/callbacks/{callbackId}/complete">client.automation.actions.callbacks.<a href="./src/hubspot_sdk/resources/automation/actions/callbacks.py">complete</a>(callback_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/callback_complete_params.py">params</a>) -> None</code>
- <code title="post /automation/v4/actions/callbacks/complete">client.automation.actions.callbacks.<a href="./src/hubspot_sdk/resources/automation/actions/callbacks.py">complete_batch</a>(\*\*<a href="src/hubspot_sdk/types/automation/actions/callback_complete_batch_params.py">params</a>) -> None</code>

### Definitions

Methods:

- <code title="post /automation/v4/actions/{appId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="patch /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">update</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="get /automation/v4/actions/{appId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">list</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">SyncPage[PublicActionDefinition]</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">delete</a>(definition_id, \*, app_id) -> None</code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">read</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>

### Functions

Methods:

- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">list</a>(definition_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/automation/collection_response_public_action_function_identifier_no_paging.py">CollectionResponsePublicActionFunctionIdentifierNoPaging</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">archive_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">read</a>(function_id, \*, app_id, definition_id, function_type) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>

### Revisions

Methods:

- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/revision_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">SyncPage[PublicActionRevision]</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">read</a>(revision_id, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">PublicActionRevision</a></code>

## Workflows

Types:

```python
from hubspot_sdk.types.automation import (
    APIAbTestBranchAction,
    APIActionDataValue,
    APIAppendObjectPropertyValue,
    APIAssociationDataSource,
    APIAssociationTimestampDataSource,
    APIAuthKeyWebhookAuthSettings,
    APIBlockedDate,
    APIConnection,
    APIContactFlow,
    APIContactFlowCreateRequest,
    APIContactFlowPutRequest,
    APIContactPropertyAnchor,
    APICustomCodeAction,
    APIDailyEnrollmentSchedule,
    APIDatasetFieldPropertyFilterDataSource,
    APIEnrolledArgumentPropertyFilterDataSource,
    APIEnrolledRecordPropertyFilterDataSource,
    APIEnrollmentEventPropertyValue,
    APIEnumerationOutputField,
    APIEventBasedEnrollmentCriteria,
    APIFetchedObjectPropertyValue,
    APIFlow,
    APIFlowBatchFetchFlowIDCoordinate,
    APIFlowBatchFetchMigrationFlowIDCoordinate,
    APIFlowBatchFetchMigrationWorkflowIDCoordinate,
    APIFlowBatchInput,
    APIFlowBatchMigrationInput,
    APIFlowCreateRequest,
    APIFlowEmailCampaign,
    APIFlowListing,
    APIFlowPutRequest,
    APIIncrementValue,
    APIInputVariable,
    APIListBasedEnrollmentCriteria,
    APIListBranch,
    APIListBranchAction,
    APIManualEnrollmentCriteria,
    APIMonthlyRelativeDaysEnrollmentSchedule,
    APIMonthlySpecificDaysEnrollmentSchedule,
    APIObjectPropertyValue,
    APIPlatformFlow,
    APIPlatformFlowCreateRequest,
    APIPlatformFlowPutRequest,
    APIPropertyBasedEnrollmentSchedule,
    APIRelativeDateTimeValue,
    APISignatureWebhookAuthSettings,
    APISingleConnectionAction,
    APISort,
    APIStaticAppendValue,
    APIStaticBranch,
    APIStaticBranchAction,
    APIStaticDateAnchor,
    APIStaticPropertyFilterDataSource,
    APIStaticTimeZoneStrategy,
    APIStaticValue,
    APITimeDelay,
    APITimeOfDay,
    APITimestampValue,
    APITimeWindow,
    APIUnEnrollmentSetting,
    APIWebhookAction,
    APIWeeklyEnrollmentSchedule,
    APIYearlyEnrollmentSchedule,
    BatchResponseAPIFlow,
    BatchResponseAPIFlowWithErrors,
    BatchResponseFlowIDWorkflowIDMappingResponse,
    BatchResponseFlowIDWorkflowIDMappingResponseWithErrors,
    CollectionResponseAPIFlowEmailCampaign,
    CollectionResponseAPIFlowListingForwardPaging,
    FlowIDWorkflowIDMappingResponse,
)
```

Methods:

- <code title="post /automation/v4/flows">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">create</a>() -> <a href="./src/hubspot_sdk/types/automation/api_flow.py">APIFlow</a></code>
- <code title="put /automation/v4/flows/{flowId}">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">update</a>(flow_id) -> <a href="./src/hubspot_sdk/types/automation/api_flow.py">APIFlow</a></code>
- <code title="get /automation/v4/flows">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">list</a>(\*\*<a href="src/hubspot_sdk/types/automation/workflow_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/api_flow_listing.py">SyncPage[APIFlowListing]</a></code>
- <code title="delete /automation/v4/flows/{flowId}">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">delete</a>(flow_id) -> None</code>
- <code title="post /automation/v4/flows/batch/read">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/automation/workflow_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/batch_response_api_flow.py">BatchResponseAPIFlow</a></code>
- <code title="post /automation/v4/workflow-id-mappings/batch/read">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">batch_get_id_mappings</a>(\*\*<a href="src/hubspot_sdk/types/automation/workflow_batch_get_id_mappings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/batch_response_flow_id_workflow_id_mapping_response.py">BatchResponseFlowIDWorkflowIDMappingResponse</a></code>
- <code title="get /automation/v4/flows/{flowId}">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">get</a>(flow_id) -> <a href="./src/hubspot_sdk/types/automation/api_flow.py">APIFlow</a></code>
- <code title="get /automation/v4/flows/email-campaigns">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">list_email_campaigns</a>(\*\*<a href="src/hubspot_sdk/types/automation/workflow_list_email_campaigns_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/collection_response_api_flow_email_campaign.py">CollectionResponseAPIFlowEmailCampaign</a></code>

# BusinessUnits

Types:

```python
from hubspot_sdk.types.business_units import (
    CollectionResponsePublicBusinessUnitNoPaging,
    PublicBusinessUnit,
    PublicBusinessUnitLogoMetadata,
)
```

Methods:

- <code title="get /business-units/v3/business-units/user/{userId}">client.business_units.<a href="./src/hubspot_sdk/resources/business_units.py">get_by_user_id</a>(user_id, \*\*<a href="src/hubspot_sdk/types/business_units/business_unit_get_by_user_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/business_units/collection_response_public_business_unit_no_paging.py">CollectionResponsePublicBusinessUnitNoPaging</a></code>

# Cms

Types:

```python
from hubspot_sdk.types.cms import (
    Angle,
    AttachToLangPrimaryRequestVNext,
    BackgroundImage,
    BatchInputJsonNode,
    ColorStop,
    ContentCloneRequestVNext,
    ContentScheduleRequestVNext,
    DetachFromLangGroupRequestVNext,
    Gradient,
    LayoutSection,
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
    BreakpointStyles,
    CollectionResponseWithTotalBlogPostForwardPaging,
    CollectionResponseWithTotalVersionBlogPost,
    ContentLanguageVariation,
    Margin,
    Padding,
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
- <code title="get /cms/v3/blogs/posts/{objectId}/draft">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_draft_by_id</a>(object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions/{revisionId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_version</a>(revision_id, \*, object_id) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog_post.py">VersionBlogPost</a></code>
- <code title="get /cms/v3/blogs/posts/{objectId}/revisions">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">get_previous_versions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_get_previous_versions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/version_blog_post.py">SyncPage[VersionBlogPost]</a></code>
- <code title="post /cms/v3/blogs/posts/{objectId}/draft/push-live">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">push_live</a>(object_id) -> None</code>
- <code title="get /cms/v3/blogs/posts/{objectId}">client.cms.blogs.posts.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/posts.py">read</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/post_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/blog_post.py">BlogPost</a></code>
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
- <code title="post /cms/v3/blogs/posts/batch/read">client.cms.blogs.posts.batch.<a href="./src/hubspot_sdk/resources/cms/blogs/posts/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/posts/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_blog_post.py">BatchResponseBlogPost</a></code>

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
- <code title="post /cms/v3/blogs/tags/batch/archive">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">archive_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_archive_batch_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/multi-language/attach-to-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">attach_to_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_attach_to_lang_group_params.py">params</a>) -> None</code>
- <code title="post /cms/v3/blogs/tags/batch/create">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/create-language-variation">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">create_lang_variation</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_create_lang_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/multi-language/detach-from-lang-group">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">detach_from_lang_group</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_detach_from_lang_group_params.py">params</a>) -> None</code>
- <code title="get /cms/v3/blogs/tags/{objectId}">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/tag.py">Tag</a></code>
- <code title="post /cms/v3/blogs/tags/batch/read">client.cms.blogs.tags.<a href="./src/hubspot_sdk/resources/cms/blogs/tags.py">read_batch</a>(\*\*<a href="src/hubspot_sdk/types/cms/blogs/tag_read_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/blogs/batch_response_tag.py">BatchResponseTag</a></code>
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
- <code title="get /cms/v3/domains/{domainId}">client.cms.domains.<a href="./src/hubspot_sdk/resources/cms/domains.py">read</a>(domain_id) -> <a href="./src/hubspot_sdk/types/cms/domain.py">Domain</a></code>

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
    StandardError,
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
- <code title="get /cms/v3/hubdb/tables/{tableIdOrName}/rows/draft">client.cms.hubdb.rows.<a href="./src/hubspot_sdk/resources/cms/hubdb/rows/rows.py">list_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/row_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/unified_collection_response_with_total_base_hub_db_table_row_v3.py">UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3</a></code>
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
- <code title="get /cms/v3/hubdb/tables/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">list_draft</a>(\*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_list_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_hub_db_table_v3_forward_paging.py">CollectionResponseWithTotalHubDBTableV3ForwardPaging</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/publish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">publish_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_publish_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/draft/reset">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">reset_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_reset_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="post /cms/v3/hubdb/tables/{tableIdOrName}/unpublish">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">unpublish</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_unpublish_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>
- <code title="patch /cms/v3/hubdb/tables/{tableIdOrName}/draft">client.cms.hubdb.tables.<a href="./src/hubspot_sdk/resources/cms/hubdb/tables.py">update_draft</a>(table_id_or_name, \*\*<a href="src/hubspot_sdk/types/cms/hubdb/table_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/hub_db_table_v3.py">HubDBTableV3</a></code>

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
    ContentLanguageVariation,
    Page,
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
- <code title="get /cms/v3/pages/landing-pages/folders/{objectId}/revisions">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_folder_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_folder_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_version_content_folder.py">CollectionResponseWithTotalVersionContentFolder</a></code>
- <code title="get /cms/v3/pages/landing-pages/folders">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_folders</a>(\*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_content_folder_forward_paging.py">CollectionResponseWithTotalContentFolderForwardPaging</a></code>
- <code title="get /cms/v3/pages/landing-pages/{objectId}/revisions">client.cms.pages.landing_pages.<a href="./src/hubspot_sdk/resources/cms/pages/landing_pages.py">list_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/landing_page_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_version_page.py">CollectionResponseWithTotalVersionPage</a></code>
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
- <code title="get /cms/v3/pages/site-pages/{objectId}/revisions">client.cms.pages.site_pages.<a href="./src/hubspot_sdk/resources/cms/pages/site_pages.py">list_revisions</a>(object_id, \*\*<a href="src/hubspot_sdk/types/cms/pages/site_page_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/collection_response_with_total_version_page.py">CollectionResponseWithTotalVersionPage</a></code>
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

- <code title="post /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">create</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="delete /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">delete</a>(path, \*, environment) -> None</code>
- <code title="post /cms/v3/source-code/extract/async">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">extract_async</a>(\*\*<a href="src/hubspot_sdk/types/cms/source_code_extract_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get</a>(path, \*, environment) -> BinaryAPIResponse</code>
- <code title="get /cms/v3/source-code/extract/async/tasks/{taskId}/status">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_extraction_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/shared/action_response.py">ActionResponse</a></code>
- <code title="get /cms/v3/source-code/{environment}/metadata/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">get_metadata</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_get_metadata_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="put /cms/v3/source-code/{environment}/content/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">upsert</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/cms/asset_file_metadata.py">AssetFileMetadata</a></code>
- <code title="post /cms/v3/source-code/{environment}/validate/{path}">client.cms.source_code.<a href="./src/hubspot_sdk/resources/cms/source_code.py">validate</a>(path, \*, environment, \*\*<a href="src/hubspot_sdk/types/cms/source_code_validate_params.py">params</a>) -> BinaryAPIResponse</code>

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
- <code title="get /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">read</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>

# Conversations

## CustomChannels

Types:

```python
from hubspot_sdk.types.conversations import (
    ChannelIntegrationMessageEgg,
    ChannelIntegrationParticipant,
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
    CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging,
    ContactAddress,
    ContactAttachment,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactProfile,
    ContactURL,
    FileAttachment,
    LocationAttachment,
    MessageHeaderAttachment,
    PreResolvedContact,
    PreResolvedContacts,
    PublicChannelAccount,
    PublicChannelAccountEgg,
    PublicChannelAccountStagingToken,
    PublicChannelAccountStagingTokenUpdateRequest,
    PublicChannelAccountUpdateRequest,
    PublicChannelIntegrationChannel,
    PublicChannelIntegrationChannelCreate,
    PublicChannelIntegrationChannelPatch,
    PublicChannelIntegrationMessageUpdateRequest,
    PublicClient,
    PublicContact,
    PublicConversationsMessage,
    PublicDeliveryIdentifier,
    PublicFile,
    PublicLocation,
    PublicMessageFailureDetails,
    PublicMessageHeader,
    PublicMessageStatus,
    PublicQuickReplies,
    PublicRecipient,
    PublicSender,
    PublicSocialMetadataAttachment,
    PublicUnsupportedContent,
    PublicWhatsAppTemplateMetadata,
    QuickRepliesAttachment,
    QuickReply,
    SocialMetadata,
    SocialMetadataIntegrationAttachment,
    UnsupportedContentAttachment,
)
```

Methods:

- <code title="post /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">create</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">update</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="get /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">list</a>() -> <a href="./src/hubspot_sdk/types/conversations/collection_response_with_total_public_channel_integration_channel_forward_paging.py">CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging</a></code>
- <code title="delete /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">delete</a>(channel_id) -> None</code>
- <code title="get /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">get</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>

### ChannelAccountStagingTokens

Methods:

- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-account-staging-tokens/{accountToken}">client.conversations.custom_channels.channel_account_staging_tokens.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_account_staging_tokens.py">update</a>(account_token, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_staging_token_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account_staging_token.py">PublicChannelAccountStagingToken</a></code>

### ChannelAccounts

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">update</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">list</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/collection_response_with_total_public_channel_account_forward_paging.py">CollectionResponseWithTotalPublicChannelAccountForwardPaging</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">get</a>(channel_account_id, \*, channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

### Messages

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/messages">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">update</a>(message_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">get</a>(message_id, \*, channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>

# CRM

Types:

```python
from hubspot_sdk.types.crm import (
    AssociatedID,
    AssociationSpecWithLabel,
    BatchInputPublicObjectID,
    BatchResponsePublicDefaultAssociation,
    CollectionResponseMultiAssociatedObjectWithLabel,
    CreatedResponseLabelsBetweenObjectPair,
    Filter,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    Option,
    Property,
    PropertyModificationMetadata,
    PublicDefaultAssociation,
)
```

## Associations

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPublicAssociation,
    BatchResponsePublicAssociation,
    BatchResponsePublicAssociationMulti,
    PublicAssociation,
    PublicAssociationMulti,
)
```

Methods:

- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association.py">BatchResponsePublicAssociation</a></code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">read</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_multi.py">BatchResponsePublicAssociationMulti</a></code>

### Schema

Types:

```python
from hubspot_sdk.types.crm.associations import (
    CollectionResponsePublicAssociationDefinitionNoPaging,
    PublicAssociationDefinition,
)
```

Methods:

- <code title="get /crm/v3/associations/{fromObjectType}/{toObjectType}/types">client.crm.associations.schema.<a href="./src/hubspot_sdk/resources/crm/associations/schema/schema.py">list</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/associations/collection_response_public_association_definition_no_paging.py">CollectionResponsePublicAssociationDefinitionNoPaging</a></code>

#### V4

Types:

```python
from hubspot_sdk.types.crm.associations.schema import (
    BatchInputPublicAssociationDefinitionConfigurationCreateRequest,
    BatchInputPublicAssociationDefinitionConfigurationUpdateRequest,
    BatchInputPublicAssociationSpec,
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResult,
    BatchResponsePublicAssociationDefinitionConfigurationUpdateResultWithErrors,
    BatchResponsePublicAssociationDefinitionUserConfiguration,
    BatchResponsePublicAssociationDefinitionUserConfigurationWithErrors,
    CollectionResponseAssociationSpecWithLabelNoPaging,
    CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging,
    PublicAssociationDefinitionConfigurationCreateRequest,
    PublicAssociationDefinitionConfigurationUpdateRequest,
    PublicAssociationDefinitionConfigurationUpdateResult,
    PublicAssociationDefinitionCreateRequest,
    PublicAssociationDefinitionUpdateRequest,
    PublicAssociationDefinitionUserConfiguration,
    PublicAssociationSpec,
)
```

##### Configurations

Methods:

- <code title="get /crm/v4/associations/definitions/configurations/all">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">list</a>() -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_public_association_definition_user_configuration_no_paging.py">CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging</a></code>
- <code title="post /crm/v4/associations/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_create_by_object_types</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_create_by_object_types_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/batch_response_public_association_definition_user_configuration.py">BatchResponsePublicAssociationDefinitionUserConfiguration</a></code>
- <code title="post /crm/v4/associations/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_delete_by_object_types</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_delete_by_object_types_params.py">params</a>) -> None</code>
- <code title="post /crm/v4/associations/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_update_by_object_types</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_update_by_object_types_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/batch_response_public_association_definition_configuration_update_result.py">BatchResponsePublicAssociationDefinitionConfigurationUpdateResult</a></code>
- <code title="get /crm/v4/associations/definitions/configurations/{fromObjectType}/{toObjectType}">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">get_by_object_types</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_public_association_definition_user_configuration_no_paging.py">CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging</a></code>

##### Definitions

Methods:

- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/definition_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_association_spec_with_label_no_paging.py">CollectionResponseAssociationSpecWithLabelNoPaging</a></code>
- <code title="put /crm/v4/associations/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">update</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/definition_update_params.py">params</a>) -> None</code>
- <code title="get /crm/v4/associations/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">list</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_association_spec_with_label_no_paging.py">CollectionResponseAssociationSpecWithLabelNoPaging</a></code>
- <code title="delete /crm/v4/associations/{fromObjectType}/{toObjectType}/labels/{associationTypeId}">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">delete</a>(association_type_id, \*, from_object_type, to_object_type) -> None</code>

### V4

Types:

```python
from hubspot_sdk.types.crm.associations import (
    AssociationSpec1,
    AssociationSpecWithLabel1,
    BatchInputPublicAssociationMultiArchive,
    BatchInputPublicAssociationMultiPost,
    BatchInputPublicDefaultAssociationMultiPost,
    BatchInputPublicFetchAssociationsBatchRequest,
    BatchResponseLabelsBetweenObjectPair,
    BatchResponsePublicAssociationMultiWithLabel,
    BatchResponseVoid,
    DateTime,
    NextPage1,
    PreviousPage1,
    PublicAssociationMultiArchive,
    PublicAssociationMultiPost,
    PublicAssociationMultiWithLabel,
    PublicDefaultAssociationMultiPost,
    PublicFetchAssociationsBatchRequest,
    ReportCreationResponse,
    StandardError1,
)
```

Methods:

- <code title="put /crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4/v4.py">create_default_association</a>(to_object_id, \*, from_object_type, from_object_id, to_object_type) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="delete /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4/v4.py">delete_association</a>(to_object_id, \*, object_type, object_id, to_object_type) -> None</code>
- <code title="get /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4/v4.py">list_associations_by_type</a>(to_object_type, \*, object_type, object_id, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_list_associations_by_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_multi_associated_object_with_label.py">CollectionResponseMultiAssociatedObjectWithLabel</a></code>
- <code title="put /crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.v4.<a href="./src/hubspot_sdk/resources/crm/associations/v4/v4.py">update_association_labels</a>(to_object_id, \*, object_type, object_id, to_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4_update_association_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_labels_between_object_pair.py">CreatedResponseLabelsBetweenObjectPair</a></code>

#### Batch

Methods:

- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">batch_associate_default</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_batch_associate_default_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">batch_create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_labels_between_object_pair.py">BatchResponseLabelsBetweenObjectPair</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">batch_delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_batch_delete_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">batch_delete_labels</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_batch_delete_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">batch_read</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_public_association_multi_with_label.py">BatchResponsePublicAssociationMultiWithLabel</a></code>

#### Report

Methods:

- <code title="post /crm/v4/associations/usage/high-usage-report/{userId}">client.crm.associations.v4.report.<a href="./src/hubspot_sdk/resources/crm/associations/v4/report.py">request_high_usage_report</a>(user_id) -> <a href="./src/hubspot_sdk/types/crm/associations/report_creation_response.py">ReportCreationResponse</a></code>

## Exports

Types:

```python
from hubspot_sdk.types.crm import (
    ActionResponseWithSingleResultUri,
    PublicCRMSearchRequest,
    PublicExportListRequest,
    PublicExportRequest,
    PublicExportViewRequest,
)
```

Methods:

- <code title="post /crm/v3/exports/export/async">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">create</a>() -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /crm/v3/exports/export/async/tasks/{taskId}/status">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">get_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/crm/action_response_with_single_result_uri.py">ActionResponseWithSingleResultUri</a></code>

## Extensions

### Calling

Types:

```python
from hubspot_sdk.types.crm.extensions import (
    ChannelConnectionSettingsPatchRequest,
    ChannelConnectionSettingsRequest,
    ChannelConnectionSettingsResponse,
    MarkRecordingAsReadyRequest,
    RecordingSettingsPatchRequest,
    RecordingSettingsRequest,
    RecordingSettingsResponse,
    SettingsPatchRequest,
    SettingsRequest,
    SettingsResponse,
)
```

#### ChannelConnectionSettings

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/channel_connection_setting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/channel_connection_setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings/channel-connection">client.crm.extensions.calling.channel_connection_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/channel_connection_settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>

#### RecordingSettings

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings/recording">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="post /crm/v3/extensions/calling/recordings/ready">client.crm.extensions.calling.recording_settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/recording_settings.py">mark_ready</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/recording_setting_mark_ready_params.py">params</a>) -> None</code>

#### Settings

Methods:

- <code title="post /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/setting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="patch /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/{appId}/settings">client.crm.extensions.calling.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>

### Cards

Types:

```python
from hubspot_sdk.types.crm.extensions import (
    ActionConfirmationBody,
    ActionHookActionBody,
    CardActions,
    CardAuditResponse,
    CardCreateRequest,
    CardDisplayBody,
    CardDisplayProperty,
    CardFetchBody,
    CardFetchBodyPatch,
    CardObjectTypeBody,
    CardPatchRequest,
    DisplayOption,
    IFrameActionBody,
    IntegratorCardPayloadResponse,
    IntegratorObjectResult,
    ObjectToken,
    PublicCardFetchBody,
    PublicCardListResponse,
    PublicCardResponse,
    TopLevelActions,
)
```

Methods:

- <code title="post /crm/v3/extensions/cards-dev/{appId}">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/card_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="patch /crm/v3/extensions/cards-dev/{appId}/{cardId}">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">update</a>(card_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/card_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="get /crm/v3/extensions/cards-dev/{appId}">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_list_response.py">PublicCardListResponse</a></code>
- <code title="delete /crm/v3/extensions/cards-dev/{appId}/{cardId}">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">delete</a>(card_id, \*, app_id) -> None</code>
- <code title="get /crm/v3/extensions/cards-dev/{appId}/{cardId}">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">get</a>(card_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="get /crm/v3/extensions/cards-dev/sample-response">client.crm.extensions.cards.<a href="./src/hubspot_sdk/resources/crm/extensions/cards.py">get_sample_response</a>() -> <a href="./src/hubspot_sdk/types/crm/extensions/integrator_card_payload_response.py">IntegratorCardPayloadResponse</a></code>

### Videoconferencing

Types:

```python
from hubspot_sdk.types.crm.extensions import ExternalSettings
```

#### Settings

Methods:

- <code title="put /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.videoconferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/videoconferencing/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/videoconferencing/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>
- <code title="delete /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.videoconferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/videoconferencing/settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.videoconferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/videoconferencing/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>

## Imports

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePublicImportErrorForwardPaging,
    CollectionResponsePublicImportResponse,
    ImportRowCore,
    ImportTemplate,
    PropertyValue,
    PublicImportError,
    PublicImportMetadata,
    PublicImportResponse,
    PublicObjectListRecord,
)
```

Methods:

- <code title="post /crm/v3/imports/">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/import_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">PublicImportResponse</a></code>
- <code title="get /crm/v3/imports/">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/import_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">SyncPage[PublicImportResponse]</a></code>
- <code title="post /crm/v3/imports/{importId}/cancel">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">cancel</a>(import_id) -> <a href="./src/hubspot_sdk/types/shared/action_response.py">ActionResponse</a></code>
- <code title="get /crm/v3/imports/{importId}">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">get</a>(import_id) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">PublicImportResponse</a></code>
- <code title="get /crm/v3/imports/{importId}/errors">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">list_errors</a>(import_id, \*\*<a href="src/hubspot_sdk/types/crm/import_list_errors_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_import_error_forward_paging.py">CollectionResponsePublicImportErrorForwardPaging</a></code>

## Lists

Types:

```python
from hubspot_sdk.types.crm import (
    APICollectionResponseJoinTimeAndRecordID,
    APICollectionResponseRecordListMembershipNoPaging,
    JoinTimeAndRecordID,
    ListCreateRequest,
    ListCreateResponse,
    ListFetchResponse,
    ListFilterUpdateRequest,
    ListFolderCreateRequest,
    ListFolderCreateResponse,
    ListFolderFetchResponse,
    ListMoveRequest,
    ListsByIDResponse,
    ListSearchRequest,
    ListSearchResponse,
    ListUpdateResponse,
    MembershipChangeRequest,
    MembershipsUpdateResponse,
    PublicBatchMigrationMapping,
    PublicListConversionDate,
    PublicListConversionInactivity,
    PublicListConversionResponse,
    PublicListConversionTime,
    PublicListFolder,
    PublicListPermissions,
    PublicMembershipSettings,
    PublicMigrationMapping,
    PublicObjectList,
    PublicObjectListSearchResult,
    RecordListMembership,
)
```

Methods:

- <code title="post /crm/v3/lists/">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_create_response.py">ListCreateResponse</a></code>
- <code title="get /crm/v3/lists/">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/lists_by_id_response.py">ListsByIDResponse</a></code>
- <code title="delete /crm/v3/lists/{listId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">delete</a>(list_id) -> None</code>
- <code title="delete /crm/v3/lists/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">delete_schedule_conversion</a>(list_id) -> None</code>
- <code title="get /crm/v3/lists/{listId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">get</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_fetch_response.py">ListFetchResponse</a></code>
- <code title="get /crm/v3/lists/object-type-id/{objectTypeId}/name/{listName}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">get_by_object_type_id_and_name</a>(list_name, \*, object_type_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_by_object_type_id_and_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_fetch_response.py">ListFetchResponse</a></code>
- <code title="get /crm/v3/lists/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">get_schedule_conversion</a>(list_id) -> <a href="./src/hubspot_sdk/types/crm/public_list_conversion_response.py">PublicListConversionResponse</a></code>
- <code title="put /crm/v3/lists/{listId}/restore">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">restore</a>(list_id) -> None</code>
- <code title="put /crm/v3/lists/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">schedule_conversion</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_schedule_conversion_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_list_conversion_response.py">PublicListConversionResponse</a></code>
- <code title="post /crm/v3/lists/search">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_search_response.py">ListSearchResponse</a></code>
- <code title="put /crm/v3/lists/{listId}/update-list-filters">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">update_filters</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_update_filters_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_update_response.py">ListUpdateResponse</a></code>
- <code title="put /crm/v3/lists/{listId}/update-list-name">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists/lists.py">update_name</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_update_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_update_response.py">ListUpdateResponse</a></code>

### Folders

Methods:

- <code title="post /crm/v3/lists/folders">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/lists/folder_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_create_response.py">ListFolderCreateResponse</a></code>
- <code title="delete /crm/v3/lists/folders/{folderId}">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">delete</a>(folder_id) -> None</code>
- <code title="get /crm/v3/lists/folders">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/lists/folder_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>
- <code title="put /crm/v3/lists/folders/{folderId}/move/{newParentFolderId}">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">move</a>(new_parent_folder_id, \*, folder_id) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>
- <code title="put /crm/v3/lists/folders/move-list">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">move_list</a>(\*\*<a href="src/hubspot_sdk/types/crm/lists/folder_move_list_params.py">params</a>) -> None</code>
- <code title="put /crm/v3/lists/folders/{folderId}/rename">client.crm.lists.folders.<a href="./src/hubspot_sdk/resources/crm/lists/folders.py">rename</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/folder_rename_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>

### Mapping

Methods:

- <code title="post /crm/v3/lists/idmapping">client.crm.lists.mapping.<a href="./src/hubspot_sdk/resources/crm/lists/mapping.py">batch_create_id_mapping</a>(\*\*<a href="src/hubspot_sdk/types/crm/lists/mapping_batch_create_id_mapping_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_batch_migration_mapping.py">PublicBatchMigrationMapping</a></code>
- <code title="get /crm/v3/lists/idmapping">client.crm.lists.mapping.<a href="./src/hubspot_sdk/resources/crm/lists/mapping.py">get_id_mapping</a>(\*\*<a href="src/hubspot_sdk/types/crm/lists/mapping_get_id_mapping_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_migration_mapping.py">PublicMigrationMapping</a></code>

### Memberships

Methods:

- <code title="get /crm/v3/lists/{listId}/memberships">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">list</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/membership_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/join_time_and_record_id.py">SyncPage[JoinTimeAndRecordID]</a></code>
- <code title="put /crm/v3/lists/{listId}/memberships/add">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">add</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/membership_add_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="put /crm/v3/lists/{listId}/memberships/add-from/{sourceListId}">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">add_all_from_list</a>(source_list_id, \*, list_id) -> None</code>
- <code title="put /crm/v3/lists/{listId}/memberships/add-and-remove">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">add_and_remove</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/membership_add_and_remove_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="get /crm/v3/lists/records/{objectTypeId}/{recordId}/memberships">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">get_lists</a>(record_id, \*, object_type_id) -> <a href="./src/hubspot_sdk/types/crm/api_collection_response_record_list_membership_no_paging.py">APICollectionResponseRecordListMembershipNoPaging</a></code>
- <code title="get /crm/v3/lists/{listId}/memberships/join-order">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">get_page_ordered_by_added_to_list_date</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/membership_get_page_ordered_by_added_to_list_date_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/join_time_and_record_id.py">SyncPage[JoinTimeAndRecordID]</a></code>
- <code title="put /crm/v3/lists/{listId}/memberships/remove">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">remove</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/lists/membership_remove_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="delete /crm/v3/lists/{listId}/memberships">client.crm.lists.memberships.<a href="./src/hubspot_sdk/resources/crm/lists/memberships.py">remove_all</a>(list_id) -> None</code>

## Objects

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputSimplePublicObjectBatchInput,
    BatchInputSimplePublicObjectBatchInputForCreate,
    BatchInputSimplePublicObjectBatchInputUpsert,
    BatchInputSimplePublicObjectID,
    BatchReadInputSimplePublicObjectID,
    BatchResponseSimplePublicObject,
    BatchResponseSimplePublicUpsertObject,
    CollectionResponseAssociatedID,
    CollectionResponseSimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
    CreatedResponseSimplePublicObject,
    FilterGroup,
    PublicAssociationsForObject,
    PublicGdprDeleteInput,
    PublicMergeInput,
    PublicObjectSearchRequest,
    SimplePublicObject,
    SimplePublicObjectBatchInput,
    SimplePublicObjectBatchInputForCreate,
    SimplePublicObjectBatchInputUpsert,
    SimplePublicObjectID,
    SimplePublicObjectInput,
    SimplePublicObjectInputForCreate,
    SimplePublicObjectWithAssociations,
    SimplePublicUpsertObject,
    ValueWithTimestamp,
)
```

### Companies

Methods:

- <code title="post /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">update</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">delete</a>(company_id) -> None</code>
- <code title="get /crm/v3/objects/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">get</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/companies/merge">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/search">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/companies/batch/create">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/update">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/archive">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/companies/batch/read">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/companies/batch/upsert">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Contacts

Methods:

- <code title="post /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">update</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">delete</a>(contact_id) -> None</code>
- <code title="post /crm/v3/objects/contacts/gdpr-delete">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">gdpr_delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_gdpr_delete_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/objects/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">get</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/contacts/merge">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/search">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/contacts/batch/create">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/update">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/archive">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">archive</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_archive_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/contacts/batch/read">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/upsert">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Custom

Methods:

- <code title="post /crm/v3/objects/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="post /crm/v3/objects/{objectType}/merge">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">merge</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">read</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/{objectType}/search">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/{objectType}/batch/create">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/update">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/archive">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/{objectType}/batch/read">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">read</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/upsert">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">upsert</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### DealSplits

Types:

```python
from hubspot_sdk.types.crm.objects import (
    BatchResponseDealToDealSplits,
    BatchResponseDealToDealSplitsWithErrors,
    DealToDealSplits,
    PublicDealSplitInput,
    PublicDealSplitsBatchCreateRequest,
    PublicDealSplitsCreateRequest,
)
```

Methods:

- <code title="post /crm/v3/objects/deals/splits/batch/read">client.crm.objects.deal_splits.<a href="./src/hubspot_sdk/resources/crm/objects/deal_splits.py">batch_read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_split_batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/batch_response_deal_to_deal_splits.py">BatchResponseDealToDealSplits</a></code>
- <code title="post /crm/v3/objects/deals/splits/batch/upsert">client.crm.objects.deal_splits.<a href="./src/hubspot_sdk/resources/crm/objects/deal_splits.py">batch_upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_split_batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/batch_response_deal_to_deal_splits.py">BatchResponseDealToDealSplits</a></code>

### Deals

Methods:

- <code title="post /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">update</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">delete</a>(deal_id) -> None</code>
- <code title="get /crm/v3/objects/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">get</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-3/merge">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/search">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/0-3/batch/create">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/update">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/archive">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/0-3/batch/read">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/upsert">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Meetings

Methods:

- <code title="post /crm/v3/objects/meetings">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">update</a>(meeting_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/meetings">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">delete</a>(meeting_id) -> None</code>
- <code title="get /crm/v3/objects/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">get</a>(meeting_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/meetings/search">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/meetings/batch/create">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/meetings/batch/update">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/meetings/batch/archive">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">archive</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_archive_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/meetings/batch/read">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/meetings/batch/upsert">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Objects

Methods:

- <code title="post /crm/v3/objects/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="get /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">read</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/{objectType}/search">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/{objectType}/batch/create">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">create</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/update">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">update</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/archive">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">delete</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/{objectType}/batch/read">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">read</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/upsert">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">upsert</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Schemas

Types:

```python
from hubspot_sdk.types.crm.objects import (
    AssociationDefinition,
    AssociationDefinitionEgg,
    CollectionResponseObjectSchemaNoPaging,
    ObjectSchema,
    ObjectSchemaEgg,
    ObjectTypeDefinition,
    ObjectTypeDefinitionLabels,
    ObjectTypeDefinitionPatch,
    ObjectTypePropertyCreate,
    OptionInput,
)
```

Methods:

- <code title="post /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>
- <code title="patch /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/object_type_definition.py">ObjectTypeDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_delete_params.py">params</a>) -> None</code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}/associations/{associationIdentifier}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">archive_association</a>(association_identifier, \*, object_type) -> None</code>
- <code title="post /crm-object-schemas/v3/schemas/{objectType}/associations">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create_association</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/association_definition.py">AssociationDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">read</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>

## Owners

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePublicOwnerForwardPaging,
    PublicOwner,
    PublicTeam,
)
```

Methods:

- <code title="get /crm/v3/owners/">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/owner_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">SyncPage[PublicOwner]</a></code>
- <code title="get /crm/v3/owners/{ownerId}">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">get</a>(owner_id, \*\*<a href="src/hubspot_sdk/types/crm/owner_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">PublicOwner</a></code>

## Pipelines

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePipelineNoPaging,
    CollectionResponsePipelineStageNoPaging,
    CollectionResponsePublicAuditInfoNoPaging,
    Pipeline,
    PipelineInput,
    PipelinePatchInput,
    PipelineStage,
    PipelineStageInput,
    PipelineStagePatchInput,
    PublicAuditInfo,
)
```

Methods:

- <code title="post /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="patch /crm/v3/pipelines/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">update</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="get /crm/v3/pipelines/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_pipeline_no_paging.py">CollectionResponsePipelineNoPaging</a></code>
- <code title="delete /crm/v3/pipelines/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">delete</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_delete_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">get</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/audit">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">get_audit</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_audit_info_no_paging.py">CollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="put /crm/v3/pipelines/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines/pipelines.py">replace</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>

### Stages

Methods:

- <code title="post /crm/v3/pipelines/{objectType}/{pipelineId}/stages">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">create</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipelines/stage_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="patch /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">update</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipelines/stage_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/stages">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">list</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_pipeline_stage_no_paging.py">CollectionResponsePipelineStageNoPaging</a></code>
- <code title="delete /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">delete</a>(stage_id, \*, object_type, pipeline_id) -> None</code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">get</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="get /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}/audit">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">get_audit</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_audit_info_no_paging.py">CollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="put /crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.stages.<a href="./src/hubspot_sdk/resources/crm/pipelines/stages.py">replace</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipelines/stage_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>

## Properties

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPropertyCreate,
    BatchInputPropertyName,
    BatchReadInputPropertyName,
    BatchResponseProperty,
    CollectionResponseProperty,
    CollectionResponsePropertyGroup,
    CreatedResponseProperty,
    CreatedResponsePropertyGroup,
    OptionInput,
    PropertyCreate,
    PropertyGroup,
    PropertyGroupCreate,
    PropertyGroupUpdate,
    PropertyName,
    PropertyUpdate,
)
```

Methods:

- <code title="post /crm/v3/properties/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_property.py">CreatedResponseProperty</a></code>
- <code title="patch /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">update</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property.py">Property</a></code>
- <code title="get /crm/v3/properties/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property.py">CollectionResponseProperty</a></code>
- <code title="delete /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">delete</a>(property_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">get</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property.py">Property</a></code>

### Batch

Methods:

- <code title="post /crm/v3/properties/{objectType}/batch/create">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /crm/v3/properties/{objectType}/batch/archive">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/properties/{objectType}/batch/read">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">read</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_property.py">BatchResponseProperty</a></code>

### Groups

Methods:

- <code title="post /crm/v3/properties/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_property_group.py">CreatedResponsePropertyGroup</a></code>
- <code title="patch /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">update</a>(group_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>
- <code title="get /crm/v3/properties/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property_group.py">CollectionResponsePropertyGroup</a></code>
- <code title="delete /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">delete</a>(group_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">get</a>(group_name, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>

## Timeline

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputTimelineEvent,
    BatchResponseTimelineEventResponse,
    BatchResponseTimelineEventResponseWithErrors,
    CollectionResponseTimelineEventTemplateNoPaging,
    EventDetail,
    TimelineEvent,
    TimelineEventIFrame,
    TimelineEventResponse,
    TimelineEventTemplate,
    TimelineEventTemplateCreateRequest,
    TimelineEventTemplateToken,
    TimelineEventTemplateTokenOption,
    TimelineEventTemplateTokenUpdateRequest,
    TimelineEventTemplateUpdateRequest,
)
```

### Events

Methods:

- <code title="post /integrators/timeline/v3/events">client.crm.timeline.events.<a href="./src/hubspot_sdk/resources/crm/timeline/events.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/timeline/event_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_response.py">TimelineEventResponse</a></code>
- <code title="post /integrators/timeline/v3/events/batch/create">client.crm.timeline.events.<a href="./src/hubspot_sdk/resources/crm/timeline/events.py">batch_create</a>(\*\*<a href="src/hubspot_sdk/types/crm/timeline/event_batch_create_params.py">params</a>) -> None</code>
- <code title="get /integrators/timeline/v3/events/{eventTemplateId}/{eventId}">client.crm.timeline.events.<a href="./src/hubspot_sdk/resources/crm/timeline/events.py">get</a>(event_id, \*, event_template_id) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_response.py">TimelineEventResponse</a></code>
- <code title="get /integrators/timeline/v3/events/{eventTemplateId}/{eventId}/detail">client.crm.timeline.events.<a href="./src/hubspot_sdk/resources/crm/timeline/events.py">get_detail</a>(event_id, \*, event_template_id) -> <a href="./src/hubspot_sdk/types/crm/event_detail.py">EventDetail</a></code>

### Templates

Methods:

- <code title="post /integrators/timeline/v3/{appId}/event-templates">client.crm.timeline.templates.<a href="./src/hubspot_sdk/resources/crm/timeline/templates.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/timeline/template_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_template.py">TimelineEventTemplate</a></code>
- <code title="put /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}">client.crm.timeline.templates.<a href="./src/hubspot_sdk/resources/crm/timeline/templates.py">update</a>(event_template_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/timeline/template_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_template.py">TimelineEventTemplate</a></code>
- <code title="get /integrators/timeline/v3/{appId}/event-templates">client.crm.timeline.templates.<a href="./src/hubspot_sdk/resources/crm/timeline/templates.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_timeline_event_template_no_paging.py">CollectionResponseTimelineEventTemplateNoPaging</a></code>
- <code title="delete /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}">client.crm.timeline.templates.<a href="./src/hubspot_sdk/resources/crm/timeline/templates.py">delete</a>(event_template_id, \*, app_id) -> None</code>
- <code title="get /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}">client.crm.timeline.templates.<a href="./src/hubspot_sdk/resources/crm/timeline/templates.py">get</a>(event_template_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_template.py">TimelineEventTemplate</a></code>

### Tokens

Methods:

- <code title="post /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens">client.crm.timeline.tokens.<a href="./src/hubspot_sdk/resources/crm/timeline/tokens.py">create</a>(event_template_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/timeline/token_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_template_token.py">TimelineEventTemplateToken</a></code>
- <code title="put /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}">client.crm.timeline.tokens.<a href="./src/hubspot_sdk/resources/crm/timeline/tokens.py">update</a>(token_name, \*, app_id, event_template_id, \*\*<a href="src/hubspot_sdk/types/crm/timeline/token_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/timeline_event_template_token.py">TimelineEventTemplateToken</a></code>
- <code title="delete /integrators/timeline/v3/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}">client.crm.timeline.tokens.<a href="./src/hubspot_sdk/resources/crm/timeline/tokens.py">delete</a>(token_name, \*, app_id, event_template_id) -> None</code>

# Events

Types:

```python
from hubspot_sdk.types.events import (
    BatchedBehavioralEventHTTPCompletionRequest,
    BehavioralEventHTTPCompletionRequest,
)
```

Methods:

- <code title="post /events/v3/send">client.events.<a href="./src/hubspot_sdk/resources/events/events.py">send</a>(\*\*<a href="src/hubspot_sdk/types/events/event_send_params.py">params</a>) -> None</code>

## Batch

Methods:

- <code title="post /events/v3/send/batch">client.events.batch.<a href="./src/hubspot_sdk/resources/events/batch.py">send</a>(\*\*<a href="src/hubspot_sdk/types/events/batch_send_params.py">params</a>) -> None</code>

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

- <code title="patch /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">update</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="delete /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">delete</a>(file_id) -> None</code>
- <code title="delete /files/v3/files/{fileId}/gdpr-delete">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">gdpr_delete</a>(file_id) -> None</code>
- <code title="get /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/v3/files/stat/{path}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_by_path</a>(path, \*\*<a href="src/hubspot_sdk/types/files/file_get_by_path_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file_stat.py">FileStat</a></code>
- <code title="get /files/v3/files/import-from-url/async/tasks/{taskId}/status">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_import_task_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/files/file_action_response.py">FileActionResponse</a></code>
- <code title="get /files/v3/files/{fileId}/signed-url">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">get_signed_url</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_get_signed_url_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/signed_url.py">SignedURL</a></code>
- <code title="post /files/v3/files/import-from-url/async">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">import_from_url_async</a>(\*\*<a href="src/hubspot_sdk/types/files/file_import_from_url_async_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/import_from_url_task_locator.py">ImportFromURLTaskLocator</a></code>
- <code title="put /files/v3/files/{fileId}">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">replace</a>(file_id, \*\*<a href="src/hubspot_sdk/types/files/file_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>
- <code title="get /files/v3/files/search">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">search</a>(\*\*<a href="src/hubspot_sdk/types/files/file_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">SyncPage[File]</a></code>
- <code title="post /files/v3/files">client.files.files.<a href="./src/hubspot_sdk/resources/files/files_.py">upload</a>(\*\*<a href="src/hubspot_sdk/types/files/file_upload_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/files/file.py">File</a></code>

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

# Marketing

## Emails

Types:

```python
from hubspot_sdk.types.marketing import (
    AggregateEmailStatistics,
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
    CollectionResponseWithTotalPublicEmailForwardPaging,
    CollectionResponseWithTotalVersionPublicEmail,
    EmailCloneRequestVNext,
    EmailCreateRequest,
    EmailStatisticInterval,
    EmailStatisticsData,
    EmailUpdateRequest,
    Interval,
    Paging,
    PublicButtonStyleSettings,
    PublicDividerStyleSettings,
    PublicEmail,
    PublicEmailContent,
    PublicEmailFromDetails,
    PublicEmailRecipients,
    PublicEmailStyleSettings,
    PublicEmailSubscriptionDetails,
    PublicEmailTestingDetails,
    PublicEmailToDetails,
    PublicFontStyle,
    PublicRssEmailDetails,
    PublicWebversionDetails,
    SmartEmailField,
    VersionPublicEmail,
)
```

Methods:

- <code title="post /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="patch /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">SyncPage[PublicEmail]</a></code>
- <code title="delete /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">delete</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/emails/clone">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/ab-test/create-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/ab-test/get-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_ab_test_variation</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_draft</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/statistics/list">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_emails_list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_emails_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/aggregate_email_statistics.py">AggregateEmailStatistics</a></code>
- <code title="get /marketing/v3/emails/statistics/histogram">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_histogram</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_get_histogram_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_email_statistic_interval_no_paging.py">CollectionResponseWithTotalEmailStatisticIntervalNoPaging</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions/{revisionId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revision_by_id</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">VersionPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">get_revisions</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">SyncPage[VersionPublicEmail]</a></code>
- <code title="post /marketing/v3/emails/{emailId}/publish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">publish_or_send</a>(email_id) -> None</code>
- <code title="get /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">read</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/draft/reset">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">reset_draft</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_draft_revision</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">restore_revision</a>(revision_id, \*, email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/unpublish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">unpublish_or_cancel</a>(email_id) -> None</code>
- <code title="patch /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails.py">upsert_draft</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_upsert_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>

## Forms

Types:

```python
from hubspot_sdk.types.marketing import (
    CollectionResponseFormDefinitionBaseForwardPaging,
    DatepickerField,
    DependentField,
    DependentFieldFilter,
    DropdownField,
    EmailField,
    EmailFieldValidation,
    EnumeratedFieldOption,
    FieldGroup,
    FileField,
    FormDefinitionBase,
    FormDefinitionCreateRequestBase,
    FormDisplayOptions,
    FormPostSubmitAction,
    FormStyle,
    HubSpotFormConfiguration,
    HubSpotFormDefinition,
    HubSpotFormDefinitionCreateRequest,
    HubSpotFormDefinitionPatchRequest,
    LegalConsentCheckbox,
    LegalConsentOptionsExplicitConsentToProcess,
    LegalConsentOptionsImplicitConsentToProcess,
    LegalConsentOptionsLegitimateInterest,
    LegalConsentOptionsNone,
    LifecycleStage,
    MobilePhoneField,
    MultiLineTextField,
    MultipleCheckboxesField,
    NumberField,
    NumberFieldValidation,
    PaymentLinkRadioField,
    PhoneField,
    PhoneFieldValidation,
    RadioField,
    SingleCheckboxField,
    SingleLineTextField,
)
```

Methods:

- <code title="post /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">create</a>() -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="patch /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">update</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="get /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/form_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">SyncPage[HubSpotFormDefinition]</a></code>
- <code title="delete /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">delete</a>(form_id) -> None</code>
- <code title="get /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">read</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="put /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">replace</a>(form_id) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>

## MarketingEvents

Types:

```python
from hubspot_sdk.types.marketing import (
    AppInfo,
    AttendanceCounters,
    BatchInputMarketingEventCreateRequestParams,
    BatchInputMarketingEventEmailSubscriber,
    BatchInputMarketingEventExternalUniqueIdentifier,
    BatchInputMarketingEventPublicObjectIDDeleteRequest,
    BatchInputMarketingEventPublicUpdateRequestFullV2,
    BatchInputMarketingEventSubscriber,
    BatchResponseMarketingEventPublicDefaultResponse,
    BatchResponseMarketingEventPublicDefaultResponseV2,
    BatchResponseMarketingEventPublicDefaultResponseV2WithErrors,
    BatchResponseSubscriberEmailResponse,
    BatchResponseSubscriberVidResponse,
    CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging,
    CollectionResponseSearchPublicResponseWrapperNoPaging,
    CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging,
    CollectionResponseWithTotalParticipationBreakdownForwardPaging,
    CollectionResponseWithTotalPublicListNoPaging,
    ContactAssociation,
    CRMPropertyWrapper,
    EventDetailSettings,
    EventDetailSettingsURL,
    MarketingEventAssociation,
    MarketingEventCompleteRequestParams,
    MarketingEventCreateRequestParams,
    MarketingEventDefaultResponse,
    MarketingEventEmailSubscriber,
    MarketingEventExternalUniqueIdentifier,
    MarketingEventIdentifiersResponse,
    MarketingEventPublicDefaultResponse,
    MarketingEventPublicDefaultResponseV2,
    MarketingEventPublicObjectIDDeleteRequest,
    MarketingEventPublicReadResponse,
    MarketingEventPublicReadResponseV2,
    MarketingEventPublicUpdateRequestFullV2,
    MarketingEventPublicUpdateRequestV2,
    MarketingEventSubscriber,
    MarketingEventUpdateRequestParams,
    ParticipationAssociations,
    ParticipationBreakdown,
    ParticipationProperties,
    PropertyValue,
    PublicList,
    SearchPublicResponseWrapper,
    SubscriberEmailResponse,
    SubscriberVidResponse,
)
```

Methods:

- <code title="post /marketing/v3/marketing-events/events">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="patch /marketing/v3/marketing-events/{objectId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response_v2.py">MarketingEventPublicDefaultResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">SyncPage[MarketingEventPublicReadResponseV2]</a></code>
- <code title="delete /marketing/v3/marketing-events/{objectId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">delete</a>(object_id) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/cancel">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">cancel_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_cancel_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/complete">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">complete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_complete_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/batch/archive">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/delete">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">delete_batch_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_delete_batch_by_external_event_id_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">delete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_delete_by_external_event_id_params.py">params</a>) -> None</code>
- <code title="get /marketing/v3/marketing-events/{objectId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">get</a>(object_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">MarketingEventPublicReadResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">get_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_get_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response.py">MarketingEventPublicReadResponse</a></code>
- <code title="get /marketing/v3/marketing-events/events/search">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">search_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_search_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_search_public_response_wrapper_no_paging.py">CollectionResponseSearchPublicResponseWrapperNoPaging</a></code>
- <code title="get /marketing/v3/marketing-events/{externalEventId}/identifiers">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">search_identifiers_by_external_event_id</a>(external_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_marketing_event_identifiers_response_no_paging.py">CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging</a></code>
- <code title="post /marketing/v3/marketing-events/batch/update">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response_v2.py">BatchResponseMarketingEventPublicDefaultResponseV2</a></code>
- <code title="patch /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">update_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_update_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/upsert">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">upsert_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_upsert_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response.py">BatchResponseMarketingEventPublicDefaultResponse</a></code>
- <code title="put /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">upsert_by_external_event_id</a>(path_external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_upsert_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">upsert_subscriber_state_by_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_upsert_subscriber_state_by_email_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert">client.marketing.marketing_events.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/marketing_events.py">upsert_subscriber_state_by_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_event_upsert_subscriber_state_by_id_params.py">params</a>) -> BinaryAPIResponse</code>

### Associations

Methods:

- <code title="get /marketing/v3/marketing-events/associations/{marketingEventId}/lists">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">list</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>
- <code title="delete /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">delete</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">associate</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">associate_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="delete /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">delete_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="get /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists">client.marketing.marketing_events.associations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/associations.py">list_by_external_account</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>

### Attendance

Methods:

- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create">client.marketing.marketing_events.attendance.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/attendance.py">create_by_contact_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/attendance_create_by_contact_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_vid_response.py">BatchResponseSubscriberVidResponse</a></code>
- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create">client.marketing.marketing_events.attendance.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/attendance.py">create_by_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/attendance_create_by_email_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_email_response.py">BatchResponseSubscriberEmailResponse</a></code>

### Participations

Methods:

- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}">client.marketing.marketing_events.participations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/participations.py">get_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}">client.marketing.marketing_events.participations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/participations.py">get_by_id</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/contacts/{contactIdentifier}/breakdown">client.marketing.marketing_events.participations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/participations.py">list_breakdown_by_contact</a>(contact_identifier, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/participation_list_breakdown_by_contact_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_participation_breakdown_forward_paging.py">CollectionResponseWithTotalParticipationBreakdownForwardPaging</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}/breakdown">client.marketing.marketing_events.participations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/participations.py">list_breakdown_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/participation_list_breakdown_by_external_account_and_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_participation_breakdown_forward_paging.py">CollectionResponseWithTotalParticipationBreakdownForwardPaging</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}/breakdown">client.marketing.marketing_events.participations.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/participations.py">list_breakdown_by_id</a>(marketing_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/participation_list_breakdown_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_participation_breakdown_forward_paging.py">CollectionResponseWithTotalParticipationBreakdownForwardPaging</a></code>

### Settings

Methods:

- <code title="post /marketing/v3/marketing-events/{appId}/settings">client.marketing.marketing_events.settings.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/settings.py">create_or_update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/marketing/marketing_events/setting_create_or_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>
- <code title="get /marketing/v3/marketing-events/{appId}/settings">client.marketing.marketing_events.settings.<a href="./src/hubspot_sdk/resources/marketing/marketing_events/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>

## Subscriptions

Types:

```python
from hubspot_sdk.types.marketing import (
    PublicSubscriptionStatus,
    PublicSubscriptionStatusesResponse,
    PublicUpdateSubscriptionStatusRequest,
    SubscriptionDefinition,
    SubscriptionDefinitionsResponse,
)
```

Methods:

- <code title="get /communication-preferences/v3/definitions">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">list</a>() -> <a href="./src/hubspot_sdk/types/marketing/subscription_definitions_response.py">SubscriptionDefinitionsResponse</a></code>
- <code title="get /communication-preferences/v3/status/email/{emailAddress}">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">get_email_status</a>(email_address) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_statuses_response.py">PublicSubscriptionStatusesResponse</a></code>
- <code title="post /communication-preferences/v3/subscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">subscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_subscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/v3/unsubscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">unsubscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_unsubscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>

### V4

Types:

```python
from hubspot_sdk.types.marketing.subscriptions import (
    ActionResponseWithResultsPublicStatus,
    ActionResponseWithResultsPublicWideStatus,
    ActionResponseWithResultsSubscriptionDefinition,
    BatchInputPublicStatusRequest,
    BatchResponsePublicBulkOptOutFromAllResponse,
    BatchResponsePublicStatus,
    BatchResponsePublicStatusBulkResponse,
    BatchResponsePublicStatusBulkResponseWithErrors,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicWideStatusBulkResponseWithErrors,
    LinkGenerationRequest,
    LinkGenerationResponse,
    PartialPublicStatusRequest,
    PublicBulkOptOutFromAllResponse,
    PublicStatus,
    PublicStatusBulkResponse,
    PublicStatusRequest,
    PublicSubscriptionTranslation,
    PublicWideStatus,
    PublicWideStatusBulkResponse,
)
```

#### Definitions

Methods:

- <code title="get /communication-preferences/v4/definitions">client.marketing.subscriptions.v4.definitions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/definitions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_subscription_definition.py">ActionResponseWithResultsSubscriptionDefinition</a></code>

#### Links

Methods:

- <code title="post /communication-preferences/v4/links/generate">client.marketing.subscriptions.v4.links.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/links.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/link_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/link_generation_response.py">LinkGenerationResponse</a></code>

#### Statuses

Methods:

- <code title="post /communication-preferences/v4/statuses/{subscriberIdString}">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">update</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/read">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_status_bulk_response.py">BatchResponsePublicStatusBulkResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/unsubscribe-all/read">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_get_unsubscribe_all_status</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_get_unsubscribe_all_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_wide_status_bulk_response.py">BatchResponsePublicWideStatusBulkResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_unsubscribe_all</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_bulk_opt_out_from_all_response.py">BatchResponsePublicBulkOptOutFromAllResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/write">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_update</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_status.py">BatchResponsePublicStatus</a></code>
- <code title="get /communication-preferences/v4/statuses/{subscriberIdString}">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">get</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="get /communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">get_unsubscribe_all_status</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_get_unsubscribe_all_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_wide_status.py">ActionResponseWithResultsPublicWideStatus</a></code>
- <code title="post /communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">unsubscribe_all</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>

## Transactional

Types:

```python
from hubspot_sdk.types.marketing import (
    CollectionResponseSmtpAPITokenViewForwardPaging,
    EmailSendStatusView,
    EventIDView,
    PublicSingleSendEmail,
    PublicSingleSendRequestEgg,
    SmtpAPITokenRequestEgg,
    SmtpAPITokenView,
)
```

### SingleEmail

Methods:

- <code title="post /marketing/v3/transactional/single-email/send">client.marketing.transactional.single_email.<a href="./src/hubspot_sdk/resources/marketing/transactional/single_email.py">send</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/single_email_send_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/email_send_status_view.py">EmailSendStatusView</a></code>

### SmtpTokens

Methods:

- <code title="post /marketing/v3/transactional/smtp-tokens">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/smtp_token_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>
- <code title="get /marketing/v3/transactional/smtp-tokens">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/smtp_token_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SyncPage[SmtpAPITokenView]</a></code>
- <code title="delete /marketing/v3/transactional/smtp-tokens/{tokenId}">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">delete</a>(token_id) -> None</code>
- <code title="get /marketing/v3/transactional/smtp-tokens/{tokenId}">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">get</a>(token_id) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>
- <code title="post /marketing/v3/transactional/smtp-tokens/{tokenId}/password-reset">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">reset_password</a>(token_id) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>

# Scheduler

## Meetings

Types:

```python
from hubspot_sdk.types.scheduler import (
    CollectionResponseWithTotalExternalLinkMetadataForwardPaging,
    ExternalAssociationCreateRequest,
    ExternalBookingFormField,
    ExternalBookingInfo,
    ExternalBrandingMetadata,
    ExternalCalendarMeetingEventCreateProperties,
    ExternalCalendarMeetingEventCreateRequest,
    ExternalCalendarMeetingEventResponseProperties,
    ExternalCalenderMeetingEventResponse,
    ExternalClosedRange,
    ExternalCommunicationConsentCheckbox,
    ExternalEmailReminderSchedule,
    ExternalGuestSettings,
    ExternalLegalConsentOptions,
    ExternalLegalConsentResponse,
    ExternalLinkAvailability,
    ExternalLinkAvailabilityAndBusyTimes,
    ExternalLinkAvailabilityForDuration,
    ExternalLinkDisplayInfo,
    ExternalLinkFormField,
    ExternalLinkMetadata,
    ExternalMeetingAvailability,
    ExternalMeetingBooking,
    ExternalMeetingBookingResponse,
    ExternalMeetingsLinkSettings,
    ExternalMeetingsUser,
    ExternalMeetingsWelcomeScreenInfo,
    ExternalOption,
    ExternalReminder,
    ExternalTimeRange,
    ExternalUserBusyTimes,
    ExternalUserProfile,
    ExternalValidatedFormField,
)
```

### Calendar

Methods:

- <code title="post /scheduler/v3/meetings/calendar">client.scheduler.meetings.calendar.<a href="./src/hubspot_sdk/resources/scheduler/meetings/calendar.py">create</a>(\*\*<a href="src/hubspot_sdk/types/scheduler/meetings/calendar_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_calender_meeting_event_response.py">ExternalCalenderMeetingEventResponse</a></code>

### MeetingsLinks

Methods:

- <code title="get /scheduler/v3/meetings/meeting-links">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">list</a>() -> <a href="./src/hubspot_sdk/types/scheduler/collection_response_with_total_external_link_metadata_forward_paging.py">CollectionResponseWithTotalExternalLinkMetadataForwardPaging</a></code>
- <code title="post /scheduler/v3/meetings/meeting-links/book">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">book</a>(\*\*<a href="src/hubspot_sdk/types/scheduler/meetings/meetings_link_book_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_meeting_booking_response.py">ExternalMeetingBookingResponse</a></code>
- <code title="get /scheduler/v3/meetings/meeting-links/book/availability-page/{slug}">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">get_availability_by_slug</a>(slug) -> <a href="./src/hubspot_sdk/types/scheduler/external_link_availability_and_busy_times.py">ExternalLinkAvailabilityAndBusyTimes</a></code>
- <code title="get /scheduler/v3/meetings/meeting-links/book/{slug}">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">get_booking_info_by_slug</a>(slug) -> <a href="./src/hubspot_sdk/types/scheduler/external_booking_info.py">ExternalBookingInfo</a></code>

# Settings

## Users

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicPermissionSetNoPaging,
    CollectionResponsePublicTeamNoPaging,
    CollectionResponsePublicUserForwardPaging,
    PublicPermissionSet,
    PublicTeam,
    PublicUser,
    PublicUserUpdate,
    UserProvisionRequest,
)
```

Methods:

- <code title="post /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="put /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">update</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">SyncPage[PublicUser]</a></code>
- <code title="delete /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">delete</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_delete_params.py">params</a>) -> None</code>
- <code title="get /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">get</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/v3/users/roles">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_roles</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_permission_set_no_paging.py">CollectionResponsePublicPermissionSetNoPaging</a></code>
- <code title="get /settings/v3/users/teams">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_teams</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_team_no_paging.py">CollectionResponsePublicTeamNoPaging</a></code>

# Webhooks

Types:

```python
from hubspot_sdk.types.webhooks import (
    BatchInputSubscriptionBatchUpdateRequest,
    BatchResponseSubscriptionResponse,
    BatchResponseSubscriptionResponseWithErrors,
    SettingsChangeRequest,
    SettingsResponse,
    SubscriptionBatchUpdateRequest,
    SubscriptionCreateRequest,
    SubscriptionListResponse,
    SubscriptionPatchRequest,
    SubscriptionResponse,
    ThrottlingSettings,
)
```

## Settings

Methods:

- <code title="put /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="get /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">delete</a>(app_id) -> None</code>

## Subscriptions

Methods:

- <code title="post /webhooks/v3/{appId}/subscriptions">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="patch /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">update</a>(subscription_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">delete</a>(subscription_id, \*, app_id) -> None</code>
- <code title="get /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">get</a>(subscription_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="post /webhooks/v3/{appId}/subscriptions/batch/update">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">update_batch</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/batch_response_subscription_response.py">BatchResponseSubscriptionResponse</a></code>
