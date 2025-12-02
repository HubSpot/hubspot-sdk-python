# Shared Types

```python
from hubspot_sdk.types import (
    AbTestCreateRequestVNext,
    ActionResponse,
    AssociationDefinition,
    AssociationDefinitionEgg,
    AssociationSpec,
    AutomationActionsOption,
    BatchInputPropertyCreate,
    BatchInputPropertyName,
    BatchInputPublicObjectID,
    BatchInputString,
    BatchReadInputPropertyName,
    BatchResponseProperty,
    Error,
    ErrorDetail,
    ForwardPaging,
    HubDBTableRowV3Wrapper,
    NextPage,
    ObjectTypeDefinitionLabels,
    Option,
    OptionInput,
    Paging,
    PreviousPage,
    Property,
    PropertyCreate,
    PropertyGroupCreate,
    PropertyGroupUpdate,
    PropertyModificationMetadata,
    PropertyName,
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
    PublicInListFilter,
    PublicInListFilterMetadata,
    PublicIndexOffset,
    PublicIndexedTimePoint,
    PublicIntegrationEventFilter,
    PublicMonthReference,
    PublicMultiStringPropertyOperation,
    PublicNotAllFilterBranch,
    PublicNotAnyFilterBranch,
    PublicNowReference,
    PublicNumAssociationsFilter,
    PublicNumOccurrencesRefineBy,
    PublicNumberPropertyOperation,
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
    APIUsage,
    CollectionResponseAPIUsage,
    PortalInformationResponse,
)
```

## Activity

Types:

```python
from hubspot_sdk.types.account import (
    ActingUser,
    CollectionResponseHydratedCriticalActionForwardPaging,
    CollectionResponsePublicAPIUserActionEventForwardPaging,
    CollectionResponsePublicLoginAuditForwardPaging,
    HydratedCriticalAction,
    PublicAPIUserActionEvent,
    PublicLoginAudit,
)
```

Methods:

- <code title="get /account-info/v3/activity/audit-logs">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_audit_logs</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_audit_logs_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_api_user_action_event.py">SyncPage[PublicAPIUserActionEvent]</a></code>
- <code title="get /account-info/v3/activity/login">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_login_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_login_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_login_audit.py">SyncPage[PublicLoginAudit]</a></code>
- <code title="get /account-info/v3/activity/security">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_security_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_security_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/hydrated_critical_action.py">SyncPage[HydratedCriticalAction]</a></code>

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
    SignedAccessToken,
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
- <code title="get /automation/v4/actions/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">get</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>

### Functions

Methods:

- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">list</a>(definition_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/automation/collection_response_public_action_function_identifier_no_paging.py">CollectionResponsePublicActionFunctionIdentifierNoPaging</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="put /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="delete /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">delete_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">get</a>(function_id, \*, app_id, definition_id, function_type) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>

### Revisions

Methods:

- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/revision_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">SyncPage[PublicActionRevision]</a></code>
- <code title="get /automation/v4/actions/{appId}/{definitionId}/revisions/{revisionId}">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">get</a>(revision_id, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">PublicActionRevision</a></code>

## Sequences

Types:

```python
from hubspot_sdk.types.automation import (
    CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging,
    EmailSettingsResponse,
    MeetingSettingsResponse,
    PublicEmailPatternResponse,
    PublicSequenceEnrollmentLiteResponse,
    PublicSequenceEnrollmentRequest,
    PublicSequenceEnrollmentResponse,
    PublicSequenceLiteResponse,
    PublicSequenceResponse,
    PublicSequenceSettingsResponse,
    PublicSequenceStepDependencyResponse,
    PublicSequenceStepResponse,
    PublicTaskPatternResponse,
    UnenrollmentSettingsResponse,
)
```

Methods:

- <code title="get /automation/v4/sequences/">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences/sequences.py">list</a>(\*\*<a href="src/hubspot_sdk/types/automation/sequence_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_lite_response.py">SyncPage[PublicSequenceLiteResponse]</a></code>
- <code title="get /automation/v4/sequences/{sequenceId}">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences/sequences.py">get</a>(sequence_id, \*\*<a href="src/hubspot_sdk/types/automation/sequence_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_response.py">PublicSequenceResponse</a></code>

### Enrollments

Methods:

- <code title="post /automation/v4/sequences/enrollments">client.automation.sequences.enrollments.<a href="./src/hubspot_sdk/resources/automation/sequences/enrollments.py">enroll</a>(\*\*<a href="src/hubspot_sdk/types/automation/sequences/enrollment_enroll_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_enrollment_lite_response.py">PublicSequenceEnrollmentLiteResponse</a></code>
- <code title="get /automation/v4/sequences/enrollments/contact/{contactId}">client.automation.sequences.enrollments.<a href="./src/hubspot_sdk/resources/automation/sequences/enrollments.py">get_by_contact_id</a>(contact_id) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_enrollment_response.py">PublicSequenceEnrollmentResponse</a></code>

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
    APITimeWindow,
    APITimestampValue,
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
- <code title="get /automation/v4/flows/email-campaigns">client.automation.workflows.<a href="./src/hubspot_sdk/resources/automation/workflows.py">list_email_campaigns</a>(\*\*<a href="src/hubspot_sdk/types/automation/workflow_list_email_campaigns_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/api_flow_email_campaign.py">SyncPage[APIFlowEmailCampaign]</a></code>

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
- <code title="get /cms/v3/url-redirects/{urlRedirectId}">client.cms.url_redirects.<a href="./src/hubspot_sdk/resources/cms/url_redirects.py">get</a>(url_redirect_id) -> <a href="./src/hubspot_sdk/types/cms/url_mapping.py">URLMapping</a></code>

# Conversations

Types:

```python
from hubspot_sdk.types.conversations import (
    AgentActor,
    BatchResponsePublicActor,
    BatchResponsePublicActorWithErrors,
    BotActor,
    CollectionResponsePublicMessageForwardPaging,
    CollectionResponsePublicThreadForwardPaging,
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
    CollectionResponseWithTotalPublicChannelForwardPaging,
    CollectionResponseWithTotalPublicInboxForwardPaging,
    ContactAddress,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactProfile,
    ContactURL,
    ConversationsPublicConversationsMessage,
    EmailActor,
    IntegratorActor,
    LlmActor,
    PublicActor,
    PublicAssignmentMessage,
    PublicChannel,
    PublicChannelAccount,
    PublicClient,
    PublicComment,
    PublicCommentEgg,
    PublicContact,
    PublicConversationsMessageEgg,
    PublicDeliveryIdentifier,
    PublicFile,
    PublicFileEgg,
    PublicInbox,
    PublicLocation,
    PublicMessage,
    PublicMessageContent,
    PublicMessageEgg,
    PublicMessageFailureDetails,
    PublicMessageHeader,
    PublicMessageStatus,
    PublicQuickReplies,
    PublicQuickRepliesEgg,
    PublicRecipient,
    PublicRecipientEgg,
    PublicSender,
    PublicSocialMediaEgg,
    PublicSocialMetadataAttachment,
    PublicThread,
    PublicThreadAssociations,
    PublicThreadInboxChange,
    PublicThreadStatusChange,
    PublicThreadUpdateRequest,
    PublicUnsupportedContent,
    PublicWelcomeMessage,
    PublicWhatsAppTemplateMetadata,
    QuickReply,
    SocialMetadata,
    SystemActor,
    VisitorActor,
)
```

## Actors

Methods:

- <code title="post /conversations/v3/conversations/actors/batch/read">client.conversations.actors.<a href="./src/hubspot_sdk/resources/conversations/actors.py">batch_read</a>(\*\*<a href="src/hubspot_sdk/types/conversations/actor_batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/batch_response_public_actor.py">BatchResponsePublicActor</a></code>
- <code title="get /conversations/v3/conversations/actors/{actorId}">client.conversations.actors.<a href="./src/hubspot_sdk/resources/conversations/actors.py">get</a>(actor_id, \*\*<a href="src/hubspot_sdk/types/conversations/actor_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_actor.py">PublicActor</a></code>

## ChannelAccounts

Methods:

- <code title="get /conversations/v3/conversations/channel-accounts">client.conversations.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/channel_accounts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/channel_account_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">SyncPage[PublicChannelAccount]</a></code>
- <code title="get /conversations/v3/conversations/channel-accounts/{channelAccountId}">client.conversations.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/channel_accounts.py">get</a>(channel_account_id, \*\*<a href="src/hubspot_sdk/types/conversations/channel_account_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

## Channels

Methods:

- <code title="get /conversations/v3/conversations/channels">client.conversations.channels.<a href="./src/hubspot_sdk/resources/conversations/channels.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/channel_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel.py">SyncPage[PublicChannel]</a></code>
- <code title="get /conversations/v3/conversations/channels/{channelId}">client.conversations.channels.<a href="./src/hubspot_sdk/resources/conversations/channels.py">get</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel.py">PublicChannel</a></code>

## CustomChannels

Types:

```python
from hubspot_sdk.types.conversations import (
    ChannelIntegrationMessageEgg,
    ChannelIntegrationParticipant,
    CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging,
    ContactAttachment,
    FileAttachment,
    LocationAttachment,
    MessageHeaderAttachment,
    PreResolvedContact,
    PreResolvedContacts,
    PublicChannelAccountEgg,
    PublicChannelAccountStagingToken,
    PublicChannelAccountStagingTokenUpdateRequest,
    PublicChannelAccountUpdateRequest,
    PublicChannelIntegrationChannel,
    PublicChannelIntegrationChannelCreate,
    PublicChannelIntegrationChannelPatch,
    PublicChannelIntegrationMessageUpdateRequest,
    PublicConversationsMessage,
    QuickRepliesAttachment,
    SocialMetadataIntegrationAttachment,
    UnsupportedContentAttachment,
)
```

Methods:

- <code title="post /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">create</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">update</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="get /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">SyncPage[PublicChannelIntegrationChannel]</a></code>
- <code title="delete /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">delete</a>(channel_id) -> None</code>
- <code title="get /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">get</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>

### ChannelAccountStagingTokens

Methods:

- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-account-staging-tokens/{accountToken}">client.conversations.custom_channels.channel_account_staging_tokens.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_account_staging_tokens.py">update</a>(account_token, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_staging_token_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account_staging_token.py">PublicChannelAccountStagingToken</a></code>

### ChannelAccounts

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">update</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">list</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">SyncPage[PublicChannelAccount]</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">get</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

### Messages

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/messages">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">update</a>(message_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">get</a>(message_id, \*, channel_id) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>

## Inboxes

Methods:

- <code title="get /conversations/v3/conversations/inboxes">client.conversations.inboxes.<a href="./src/hubspot_sdk/resources/conversations/inboxes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/inbox_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_inbox.py">SyncPage[PublicInbox]</a></code>
- <code title="get /conversations/v3/conversations/inboxes/{inboxId}">client.conversations.inboxes.<a href="./src/hubspot_sdk/resources/conversations/inboxes.py">get</a>(inbox_id, \*\*<a href="src/hubspot_sdk/types/conversations/inbox_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_inbox.py">PublicInbox</a></code>

## Messages

Methods:

- <code title="post /conversations/v3/conversations/threads/{threadId}/messages">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">create</a>(thread_id) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">PublicMessage</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">list</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">SyncPage[PublicMessage]</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages/{messageId}">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">get</a>(message_id, \*, thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">PublicMessage</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages/{messageId}/original-content">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">get_original_content</a>(message_id, \*, thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_get_original_content_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message_content.py">PublicMessageContent</a></code>

## Threads

Methods:

- <code title="patch /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">update</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/thread_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">PublicThread</a></code>
- <code title="get /conversations/v3/conversations/threads">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/thread_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">SyncPage[PublicThread]</a></code>
- <code title="delete /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">delete</a>(thread_id) -> None</code>
- <code title="get /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">get</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/thread_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">PublicThread</a></code>

## VisitorIdentification

Types:

```python
from hubspot_sdk.types.conversations import (
    IdentificationTokenGenerationRequest,
    IdentificationTokenResponse,
)
```

Methods:

- <code title="post /visitor-identification/v3/tokens/create">client.conversations.visitor_identification.<a href="./src/hubspot_sdk/resources/conversations/visitor_identification.py">generate_token</a>(\*\*<a href="src/hubspot_sdk/types/conversations/visitor_identification_generate_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/identification_token_response.py">IdentificationTokenResponse</a></code>

# Crm

Types:

```python
from hubspot_sdk.types.crm import (
    AssociatedID,
    AssociationSpecWithLabel,
    BatchInputSimplePublicObjectBatchInput,
    BatchInputSimplePublicObjectBatchInputForCreate,
    BatchInputSimplePublicObjectBatchInputUpsert,
    BatchInputSimplePublicObjectID,
    BatchReadInputSimplePublicObjectID,
    BatchResponsePublicDefaultAssociation,
    BatchResponseSimplePublicObject,
    BatchResponseSimplePublicUpsertObject,
    CollectionResponseAssociatedID,
    CollectionResponseMultiAssociatedObjectWithLabel,
    CollectionResponseSimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
    CreatedResponseLabelsBetweenObjectPair,
    CreatedResponseSimplePublicObject,
    Filter,
    FilterGroup,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    PublicAssociationsForObject,
    PublicDefaultAssociation,
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

## AppUninstalls

Methods:

- <code title="delete /appinstalls/v3/external-install">client.crm.app_uninstalls.<a href="./src/hubspot_sdk/resources/crm/app_uninstalls.py">uninstall</a>() -> None</code>

## Associations

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPublicAssociation,
    BatchResponsePublicAssociation,
    BatchResponsePublicAssociationMulti,
    BatchResponseVoid,
    PublicAssociation,
    PublicAssociationMulti,
)
```

### Batch

Methods:

- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association.py">BatchResponsePublicAssociation</a></code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">get</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_multi.py">BatchResponsePublicAssociationMulti</a></code>

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
    BatchResponsePublicAssociationDefinitionUserConfiguration,
    CollectionResponseAssociationSpecWithLabel,
    CollectionResponsePublicAssociationDefinitionUserConfiguration,
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

- <code title="get /crm/associations/v4/definitions/configurations/all">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">list</a>() -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_public_association_definition_user_configuration.py">CollectionResponsePublicAssociationDefinitionUserConfiguration</a></code>
- <code title="post /crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/batch_response_public_association_definition_user_configuration.py">BatchResponsePublicAssociationDefinitionUserConfiguration</a></code>
- <code title="post /crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_delete_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="post /crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">batch_update</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/configuration_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/batch_response_public_association_definition_configuration_update_result.py">BatchResponsePublicAssociationDefinitionConfigurationUpdateResult</a></code>
- <code title="get /crm/associations/v4/definitions/configurations/{fromObjectType}/{toObjectType}">client.crm.associations.schema.v4.configurations.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/configurations.py">get_by_object_types</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_public_association_definition_user_configuration.py">CollectionResponsePublicAssociationDefinitionUserConfiguration</a></code>

##### Definitions

Methods:

- <code title="post /crm/associations/v4/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">create_label</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/definition_create_label_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_association_spec_with_label.py">CollectionResponseAssociationSpecWithLabel</a></code>
- <code title="delete /crm/associations/v4/{fromObjectType}/{toObjectType}/labels/{associationTypeId}">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">delete_label</a>(association_type_id, \*, from_object_type, to_object_type) -> None</code>
- <code title="get /crm/associations/v4/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">list_labels</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/associations/schema/collection_response_association_spec_with_label.py">CollectionResponseAssociationSpecWithLabel</a></code>
- <code title="put /crm/associations/v4/{fromObjectType}/{toObjectType}/labels">client.crm.associations.schema.v4.definitions.<a href="./src/hubspot_sdk/resources/crm/associations/schema/v4/definitions.py">update_label</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/schema/v4/definition_update_label_params.py">params</a>) -> None</code>

### V4

Types:

```python
from hubspot_sdk.types.crm.associations import (
    BatchInputPublicAssociationMultiArchive,
    BatchInputPublicAssociationMultiPost,
    BatchInputPublicDefaultAssociationMultiPost,
    BatchInputPublicFetchAssociationsBatchRequest,
    BatchResponseLabelsBetweenObjectPair,
    BatchResponsePublicAssociationMultiWithLabel,
    DateTime,
    PublicAssociationMultiArchive,
    PublicAssociationMultiPost,
    PublicAssociationMultiWithLabel,
    PublicDefaultAssociationMultiPost,
    PublicFetchAssociationsBatchRequest,
    ReportCreationResponse,
)
```

#### Batch

Methods:

- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_labels_between_object_pair.py">BatchResponseLabelsBetweenObjectPair</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_delete_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">create_default</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_create_default_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/labels/archive">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">delete_labels</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_delete_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_void.py">BatchResponseVoid</a></code>
- <code title="post /crm/v4/associations/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.v4.batch.<a href="./src/hubspot_sdk/resources/crm/associations/v4/batch.py">get</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/v4/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associations/batch_response_public_association_multi_with_label.py">BatchResponsePublicAssociationMultiWithLabel</a></code>

#### Report

Methods:

- <code title="post /crm/v4/associations/usage/high-usage-report/{userId}">client.crm.associations.v4.report.<a href="./src/hubspot_sdk/resources/crm/associations/v4/report.py">request_high_usage_report</a>(user_id) -> <a href="./src/hubspot_sdk/types/crm/associations/report_creation_response.py">ReportCreationResponse</a></code>

## Exports

Types:

```python
from hubspot_sdk.types.crm import (
    ActionResponseWithSingleResultUri,
    PublicCrmSearchRequest,
    PublicExportListRequest,
    PublicExportRequest,
    PublicExportResponse,
    PublicExportViewRequest,
)
```

Methods:

- <code title="post /crm/v3/exports/export/async">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">create_async</a>() -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /crm/v3/exports/export/{exportId}">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">get</a>(export_id) -> <a href="./src/hubspot_sdk/types/crm/public_export_response.py">PublicExportResponse</a></code>
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

#### Transcripts

Types:

```python
from hubspot_sdk.types.crm.extensions.calling import (
    Speaker,
    TranscriptCreateRequest,
    TranscriptCreateResponse,
    TranscriptCreateUtterance,
    TranscriptResponse,
    TranscriptUtterance,
)
```

Methods:

- <code title="post /crm/v3/extensions/calling/transcripts">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/transcript_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/calling/transcript_create_response.py">TranscriptCreateResponse</a></code>
- <code title="delete /crm/v3/extensions/calling/transcripts/{transcriptId}">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">delete</a>(transcript_id) -> None</code>
- <code title="get /crm/v3/extensions/calling/transcripts/{transcriptId}">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">get</a>(transcript_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/calling/transcript_response.py">TranscriptResponse</a></code>

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

### VideoConferencing

Types:

```python
from hubspot_sdk.types.crm.extensions import ExternalSettings
```

#### Settings

Methods:

- <code title="put /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.video_conferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/video_conferencing/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>
- <code title="delete /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.video_conferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing/settings.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/v3/extensions/videoconferencing/settings/{appId}">client.crm.extensions.video_conferencing.settings.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>

## FeatureFlags

Types:

```python
from hubspot_sdk.types.crm import (
    BatchPortalEntry,
    FlagPutRequest,
    FlagResponse,
    PortalFlagStateBatchDeleteRequest,
    PortalFlagStateBatchPutRequest,
    PortalFlagStateBatchResponse,
    PortalFlagStatePutRequest,
    PortalFlagStateResponse,
)
```

### Apps

Methods:

- <code title="put /feature-flags/v3/{appId}/flags/{flagName}">client.crm.feature_flags.apps.<a href="./src/hubspot_sdk/resources/crm/feature_flags/apps.py">update</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/app_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="delete /feature-flags/v3/{appId}/flags/{flagName}">client.crm.feature_flags.apps.<a href="./src/hubspot_sdk/resources/crm/feature_flags/apps.py">delete</a>(flag_name, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="get /feature-flags/v3/{appId}/flags/{flagName}">client.crm.feature_flags.apps.<a href="./src/hubspot_sdk/resources/crm/feature_flags/apps.py">get</a>(flag_name, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="get /feature-flags/v3/{appId}/flags/{flagName}/portals">client.crm.feature_flags.apps.<a href="./src/hubspot_sdk/resources/crm/feature_flags/apps.py">list_portals</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/app_list_portals_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>

### Portals

Methods:

- <code title="put /feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.portals.<a href="./src/hubspot_sdk/resources/crm/feature_flags/portals.py">update</a>(portal_id, \*, app_id, flag_name, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/portal_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>
- <code title="delete /feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.portals.<a href="./src/hubspot_sdk/resources/crm/feature_flags/portals.py">delete</a>(portal_id, \*, app_id, flag_name) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>
- <code title="post /feature-flags/v3/{appId}/flags/{flagName}/portals/batch/delete">client.crm.feature_flags.portals.<a href="./src/hubspot_sdk/resources/crm/feature_flags/portals.py">batch_delete</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/portal_batch_delete_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>
- <code title="post /feature-flags/v3/{appId}/flags/{flagName}/portals/batch/upsert">client.crm.feature_flags.portals.<a href="./src/hubspot_sdk/resources/crm/feature_flags/portals.py">batch_upsert</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/portal_batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>
- <code title="get /feature-flags/v3/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.portals.<a href="./src/hubspot_sdk/resources/crm/feature_flags/portals.py">get</a>(portal_id, \*, app_id, flag_name) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>

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
- <code title="get /crm/v3/imports/{importId}/errors">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">list_errors</a>(import_id, \*\*<a href="src/hubspot_sdk/types/crm/import_list_errors_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_error.py">SyncPage[PublicImportError]</a></code>

## Limits

Types:

```python
from hubspot_sdk.types.crm import (
    AssociationLabelLimitResponse,
    AssociationRecordLimitResponse,
    AtLimitRecordSample,
    CalculatedPropertyLimitResponse,
    CollectionResponseAssociationLabelLimitResponseNoPaging,
    CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging,
    CustomObjectLimitResponse,
    CustomObjectRecordLimitResponse,
    CustomPropertyLimitResponse,
    LimitAndUsageForObjectType,
    NearLimitRecordSample,
    ObjectTypeDefinition,
    ObjectTypeNearOrAtAssociationLimit,
    PipelineLimitResponse,
    RecordLimitResponse,
    UsageForObjectType,
)
```

Methods:

- <code title="get /crm/v3/limits/associations/labels">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_label_limits</a>(\*\*<a href="src/hubspot_sdk/types/crm/limit_get_association_label_limits_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_association_label_limit_response_no_paging.py">CollectionResponseAssociationLabelLimitResponseNoPaging</a></code>
- <code title="get /crm/v3/limits/associations/records/{fromObjectTypeId}/{toObjectTypeId}">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_by_object_type</a>(to_object_type_id, \*, from_object_type_id) -> <a href="./src/hubspot_sdk/types/crm/association_record_limit_response.py">AssociationRecordLimitResponse</a></code>
- <code title="get /crm/v3/limits/associations/records/from">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_from_objects</a>() -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_type_near_or_at_association_limit_no_paging.py">CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging</a></code>
- <code title="get /crm/v3/limits/associations/records/{fromObjectTypeId}/to">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_to_objects</a>(from_object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_type_near_or_at_association_limit_no_paging.py">CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging</a></code>
- <code title="get /crm/v3/limits/calculated-properties">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_calculated_property_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/calculated_property_limit_response.py">CalculatedPropertyLimitResponse</a></code>
- <code title="get /crm/v3/limits/custom-object-types">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_custom_object_type_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/custom_object_limit_response.py">CustomObjectLimitResponse</a></code>
- <code title="get /crm/v3/limits/custom-properties">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_custom_property_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/custom_property_limit_response.py">CustomPropertyLimitResponse</a></code>
- <code title="get /crm/v3/limits/pipelines">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_pipeline_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/pipeline_limit_response.py">PipelineLimitResponse</a></code>
- <code title="get /crm/v3/limits/records">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_record_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/record_limit_response.py">RecordLimitResponse</a></code>

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
    ListSearchRequest,
    ListSearchResponse,
    ListUpdateResponse,
    ListsByIDResponse,
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

## ObjectLibrary

Types:

```python
from hubspot_sdk.types.crm import (
    ObjectTypeEnablementPublicResponse,
    PortalObjectTypeEnablementPublicResponse,
)
```

### Enablement

Methods:

- <code title="get /crm/v3/object-library/enablement">client.crm.object_library.enablement.<a href="./src/hubspot_sdk/resources/crm/object_library/enablement.py">list</a>() -> <a href="./src/hubspot_sdk/types/crm/portal_object_type_enablement_public_response.py">PortalObjectTypeEnablementPublicResponse</a></code>
- <code title="get /crm/v3/object-library/enablement/{objectTypeId}">client.crm.object_library.enablement.<a href="./src/hubspot_sdk/resources/crm/object_library/enablement.py">get</a>(object_type_id) -> <a href="./src/hubspot_sdk/types/crm/object_type_enablement_public_response.py">ObjectTypeEnablementPublicResponse</a></code>

## Objects

### Calls

Methods:

- <code title="post /crm/v3/objects/calls">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">update</a>(call_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/call_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/calls">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">delete</a>(call_id) -> None</code>
- <code title="get /crm/v3/objects/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">get</a>(call_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/call_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/calls/search">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/calls/batch/create">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/calls/batch/update">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/calls/batch/archive">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/calls/batch/read">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/calls/batch/upsert">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Carts

Methods:

- <code title="post /crm/v3/objects/carts">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">update</a>(cart_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/cart_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/carts">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">delete</a>(cart_id) -> None</code>
- <code title="get /crm/v3/objects/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">get</a>(cart_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/cart_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/carts/search">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/carts/batch/create">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/carts/batch/update">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/carts/batch/archive">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/carts/batch/read">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/carts/batch/upsert">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### CommercePayments

Methods:

- <code title="post /crm/v3/objects/commerce_payments">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">update</a>(commerce_payment_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/commerce_payments">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">delete</a>(commerce_payment_id) -> None</code>
- <code title="get /crm/v3/objects/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">get</a>(commerce_payment_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/commerce_payments/search">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/commerce_payments/batch/create">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/commerce_payments/batch/update">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/commerce_payments/batch/archive">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/commerce_payments/batch/read">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/commerce_payments/batch/upsert">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Communications

Methods:

- <code title="post /crm/v3/objects/communications">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">update</a>(communication_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/communication_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/communications">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">delete</a>(communication_id) -> None</code>
- <code title="get /crm/v3/objects/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">get</a>(communication_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/communication_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/communications/search">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/communications/batch/create">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/communications/batch/update">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/communications/batch/archive">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/communications/batch/read">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/communications/batch/upsert">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

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
- <code title="post /crm/v3/objects/companies/batch/read">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
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
- <code title="post /crm/v3/objects/contacts/batch/archive">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/contacts/batch/read">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contacts/batch/upsert">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Contracts

Methods:

- <code title="post /crm/v3/objects/contracts">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">update</a>(contract_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contract_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/contracts">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">delete</a>(contract_id) -> None</code>
- <code title="get /crm/v3/objects/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">get</a>(contract_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contract_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/contracts/search">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/contracts/batch/create">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contracts/batch/update">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contracts/batch/archive">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/contracts/batch/read">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/contracts/batch/upsert">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Courses

Methods:

- <code title="post /crm/v3/objects/0-410">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">update</a>(course_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/course_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-410">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">delete</a>(course_id) -> None</code>
- <code title="get /crm/v3/objects/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">get</a>(course_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/course_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-410/search">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/0-410/batch/create">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-410/batch/update">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-410/batch/archive">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/0-410/batch/read">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-410/batch/upsert">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Custom

Methods:

- <code title="post /crm/v3/objects/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="get /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">get</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/{objectType}/merge">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">merge</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/search">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/{objectType}/batch/create">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/update">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/archive">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/{objectType}/batch/read">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/upsert">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">upsert</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### DealSplits

Types:

```python
from hubspot_sdk.types.crm.objects import (
    BatchResponseDealToDealSplits,
    BatchResponseDealToDealSplitsWithErrors,
    DealToDealSplits,
    ObjectsDealSplitsSimplePublicObject,
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
- <code title="post /crm/v3/objects/0-3/batch/read">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-3/batch/upsert">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Discounts

Methods:

- <code title="post /crm/v3/objects/discounts">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">update</a>(discount_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/discount_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/discounts">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">delete</a>(discount_id) -> None</code>
- <code title="get /crm/v3/objects/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">get</a>(discount_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/discount_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/discounts/search">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/discounts/batch/create">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/discounts/batch/update">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/discounts/batch/archive">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/discounts/batch/read">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/discounts/batch/upsert">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Emails

Methods:

- <code title="post /crm/v3/objects/emails">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/emails">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">delete</a>(email_id) -> None</code>
- <code title="get /crm/v3/objects/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">get</a>(email_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/email_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/emails/search">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/emails/batch/create">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/emails/batch/update">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/emails/batch/archive">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/emails/batch/read">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/emails/batch/upsert">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### FeedbackSubmissions

Methods:

- <code title="get /crm/v3/objects/feedback_submissions">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="get /crm/v3/objects/feedback_submissions/{feedbackSubmissionId}">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">get</a>(feedback_submission_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/feedback_submissions/search">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/feedback_submissions/batch/read">client.crm.objects.feedback_submissions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submissions/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### Fees

Methods:

- <code title="post /crm/v3/objects/fees">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">update</a>(fee_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/fee_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/fees">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">delete</a>(fee_id) -> None</code>
- <code title="get /crm/v3/objects/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">get</a>(fee_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/fee_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/fees/search">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/fees/batch/create">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/fees/batch/update">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/fees/batch/archive">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/fees/batch/read">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/fees/batch/upsert">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### GoalTargets

Methods:

- <code title="post /crm/v3/objects/goal_targets">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">update</a>(goal_target_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/goal_targets">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">delete</a>(goal_target_id) -> None</code>
- <code title="get /crm/v3/objects/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">get</a>(goal_target_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/goal_targets/search">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/goal_targets/batch/create">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/goal_targets/batch/update">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/goal_targets/batch/archive">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/goal_targets/batch/read">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/goal_targets/batch/upsert">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Invoices

Methods:

- <code title="post /crm/v3/objects/invoices">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">update</a>(invoice_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/invoices">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">delete</a>(invoice_id) -> None</code>
- <code title="get /crm/v3/objects/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">get</a>(invoice_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/invoices/search">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/invoices/batch/create">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/invoices/batch/update">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/invoices/batch/archive">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/invoices/batch/read">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/invoices/batch/upsert">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Leads

Methods:

- <code title="post /crm/v3/objects/leads">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">update</a>(leads_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/lead_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/leads">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">delete</a>(leads_id) -> None</code>
- <code title="get /crm/v3/objects/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">get</a>(leads_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/lead_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/leads/search">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/leads/batch/create">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/leads/batch/update">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/leads/batch/archive">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/leads/batch/read">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### LineItems

Methods:

- <code title="post /crm/v3/objects/line_items">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">update</a>(line_item_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/line_items">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">delete</a>(line_item_id) -> None</code>
- <code title="get /crm/v3/objects/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">get</a>(line_item_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/line_items/search">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/line_items/batch/create">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/line_items/batch/update">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/line_items/batch/archive">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/line_items/batch/read">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/line_items/batch/upsert">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Listings

Methods:

- <code title="post /crm/v3/objects/0-420">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">update</a>(listing_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/listing_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-420">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">delete</a>(listing_id) -> None</code>
- <code title="get /crm/v3/objects/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">get</a>(listing_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/listing_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-420/search">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/0-420/batch/create">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-420/batch/update">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-420/batch/archive">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/0-420/batch/read">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-420/batch/upsert">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

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
- <code title="post /crm/v3/objects/meetings/batch/archive">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/meetings/batch/read">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/meetings/batch/upsert">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Notes

Methods:

- <code title="post /crm/v3/objects/notes">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">update</a>(note_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/note_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/notes">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">delete</a>(note_id) -> None</code>
- <code title="get /crm/v3/objects/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">get</a>(note_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/note_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/notes/search">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/notes/batch/create">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/notes/batch/update">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/notes/batch/archive">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/notes/batch/read">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/notes/batch/upsert">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Objects

Methods:

- <code title="post /crm/v3/objects/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="get /crm/v3/objects/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">get</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/{objectType}/search">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/{objectType}/batch/create">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">create</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/update">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">update</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/archive">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">delete</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/{objectType}/batch/read">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">get</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/{objectType}/batch/upsert">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">upsert</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Orders

Methods:

- <code title="post /crm/v3/objects/orders">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">update</a>(order_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/order_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/orders">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">delete</a>(order_id) -> None</code>
- <code title="get /crm/v3/objects/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">get</a>(order_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/order_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/orders/search">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/orders/batch/create">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/orders/batch/update">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/orders/batch/archive">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/orders/batch/read">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/orders/batch/upsert">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### PartnerClients

Methods:

- <code title="patch /crm/v3/objects/partner_clients/{partnerClientId}">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">update</a>(partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/partner_clients">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="get /crm/v3/objects/partner_clients/{partnerClientId}">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">get</a>(partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/partner_clients/search">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Associations

Methods:

- <code title="put /crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.partner_clients.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/associations.py">update</a>(association_type, \*, partner_client_id, to_object_type, to_object_id) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="get /crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}">client.crm.objects.partner_clients.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/associations.py">list</a>(to_object_type, \*, partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_clients/association_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associated_id.py">SyncPage[AssociatedID]</a></code>
- <code title="delete /crm/v3/objects/partner_clients/{partnerClientId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.partner_clients.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/associations.py">delete</a>(association_type, \*, partner_client_id, to_object_type, to_object_id) -> None</code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/partner_clients/batch/read">client.crm.objects.partner_clients.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/batch.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_clients/batch_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/partner_clients/batch/update">client.crm.objects.partner_clients.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/batch.py">batch_update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_clients/batch_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### PartnerServices

Methods:

- <code title="patch /crm/v3/objects/partner_services/{partnerServiceId}">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">update</a>(partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/partner_services">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="get /crm/v3/objects/partner_services/{partnerServiceId}">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">get</a>(partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/partner_services/search">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Associations

Methods:

- <code title="put /crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.partner_services.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/associations.py">update</a>(association_type, \*, partner_service_id, to_object_type, to_object_id) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="get /crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}">client.crm.objects.partner_services.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/associations.py">list</a>(to_object_type, \*, partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_services/association_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associated_id.py">SyncPage[AssociatedID]</a></code>
- <code title="delete /crm/v3/objects/partner_services/{partnerServiceId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.partner_services.associations.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/associations.py">delete</a>(association_type, \*, partner_service_id, to_object_type, to_object_id) -> None</code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/partner_services/batch/update">client.crm.objects.partner_services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_services/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/partner_services/batch/read">client.crm.objects.partner_services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_services/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### PostalMail

Methods:

- <code title="post /crm/v3/objects/postal_mail">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">update</a>(postal_mail_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/postal_mail">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">delete</a>(postal_mail_id) -> None</code>
- <code title="get /crm/v3/objects/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">get</a>(postal_mail_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/postal_mail/search">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/postal_mail/batch/create">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/postal_mail/batch/update">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/postal_mail/batch/archive">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/postal_mail/batch/read">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/postal_mail/batch/upsert">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Products

Methods:

- <code title="post /crm/v3/objects/products">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">update</a>(product_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/product_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/products">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">delete</a>(product_id) -> None</code>
- <code title="get /crm/v3/objects/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">get</a>(product_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/product_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/products/search">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/products/batch/create">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/products/batch/update">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/products/batch/archive">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/products/batch/read">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/products/batch/upsert">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Projects

Methods:

- <code title="post /crm/objects/v3/projects">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/objects/v3/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">update</a>(project_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/project_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/v3/projects">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/v3/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="get /crm/objects/v3/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">get</a>(project_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/project_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/v3/projects/merge">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/v3/projects/search">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Associations

Methods:

- <code title="put /crm/objects/v3/projects/{projectId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.projects.associations.<a href="./src/hubspot_sdk/resources/crm/objects/projects/associations.py">update</a>(association_type, \*, project_id, to_object_type, to_object_id) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="get /crm/objects/v3/projects/{projectId}/associations/{toObjectType}">client.crm.objects.projects.associations.<a href="./src/hubspot_sdk/resources/crm/objects/projects/associations.py">list</a>(to_object_type, \*, project_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/projects/association_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/associated_id.py">SyncPage[AssociatedID]</a></code>
- <code title="delete /crm/objects/v3/projects/{projectId}/associations/{toObjectType}/{toObjectId}/{associationType}">client.crm.objects.projects.associations.<a href="./src/hubspot_sdk/resources/crm/objects/projects/associations.py">delete</a>(association_type, \*, project_id, to_object_type, to_object_id) -> None</code>

#### Batch

Methods:

- <code title="post /crm/objects/v3/projects/batch/create">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/v3/projects/batch/update">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/v3/projects/batch/archive">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/v3/projects/batch/read">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/v3/projects/batch/upsert">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Quotes

Methods:

- <code title="post /crm/v3/objects/quotes">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">update</a>(quote_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/quote_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/quotes">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">delete</a>(quote_id) -> None</code>
- <code title="get /crm/v3/objects/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">get</a>(quote_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/quote_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/quotes/search">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/quotes/batch/create">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/quotes/batch/update">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/quotes/batch/archive">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/quotes/batch/read">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/quotes/batch/upsert">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Schemas

Types:

```python
from hubspot_sdk.types.crm.objects import (
    ObjectSchema,
    ObjectSchemaEgg,
    ObjectTypeDefinitionPatch,
    ObjectTypePropertyCreate,
    ObjectsSchemasObjectTypeDefinition,
    SchemaListResponse,
)
```

Methods:

- <code title="post /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>
- <code title="patch /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/objects_schemas_object_type_definition.py">ObjectsSchemasObjectTypeDefinition</a></code>
- <code title="get /crm-object-schemas/v3/schemas">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/objects/schema_list_response.py">SchemaListResponse</a></code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_delete_params.py">params</a>) -> None</code>
- <code title="post /crm-object-schemas/v3/schemas/{objectType}/associations">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">create_association</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/association_definition.py">AssociationDefinition</a></code>
- <code title="delete /crm-object-schemas/v3/schemas/{objectType}/associations/{associationIdentifier}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">delete_association</a>(association_identifier, \*, object_type) -> None</code>
- <code title="get /crm-object-schemas/v3/schemas/{objectType}">client.crm.objects.schemas.<a href="./src/hubspot_sdk/resources/crm/objects/schemas.py">get</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/objects/object_schema.py">ObjectSchema</a></code>

### Services

Methods:

- <code title="post /crm/v3/objects/0-162">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">update</a>(service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/service_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/0-162">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">delete</a>(service_id) -> None</code>
- <code title="get /crm/v3/objects/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">get</a>(service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/service_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/0-162/search">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/0-162/batch/create">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-162/batch/update">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-162/batch/archive">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/0-162/batch/read">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/0-162/batch/upsert">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Tasks

Methods:

- <code title="post /crm/v3/objects/tasks">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">update</a>(task_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/task_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/tasks">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">delete</a>(task_id) -> None</code>
- <code title="get /crm/v3/objects/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">get</a>(task_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/task_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/tasks/search">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/tasks/batch/create">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tasks/batch/update">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tasks/batch/archive">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/tasks/batch/read">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tasks/batch/upsert">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Taxes

Methods:

- <code title="post /crm/v3/objects/taxes">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">update</a>(tax_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/tax_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/taxes">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">delete</a>(tax_id) -> None</code>
- <code title="get /crm/v3/objects/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">get</a>(tax_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/tax_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/taxes/search">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/taxes/batch/create">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/taxes/batch/update">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/taxes/batch/archive">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/taxes/batch/read">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/taxes/batch/upsert">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Tickets

Methods:

- <code title="post /crm/v3/objects/tickets">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">update</a>(ticket_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/tickets">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">delete</a>(ticket_id) -> None</code>
- <code title="get /crm/v3/objects/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">get</a>(ticket_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/tickets/merge">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tickets/search">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/v3/objects/tickets/batch/create">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tickets/batch/update">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tickets/batch/archive">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/tickets/batch/read">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/tickets/batch/upsert">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

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
    CollectionResponseProperty,
    CollectionResponsePropertyGroup,
    CreatedResponseProperty,
    CreatedResponsePropertyGroup,
    PropertiesOptionInput,
    PropertyGroup,
    PropertyUpdate,
)
```

Methods:

- <code title="post /crm/v3/properties/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_property.py">CreatedResponseProperty</a></code>
- <code title="patch /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">update</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="get /crm/v3/properties/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property.py">CollectionResponseProperty</a></code>
- <code title="delete /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">delete</a>(property_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">get</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>

### Batch

Methods:

- <code title="post /crm/v3/properties/{objectType}/batch/create">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /crm/v3/properties/{objectType}/batch/archive">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/properties/{objectType}/batch/read">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_property.py">BatchResponseProperty</a></code>

### Groups

Methods:

- <code title="post /crm/v3/properties/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_property_group.py">CreatedResponsePropertyGroup</a></code>
- <code title="patch /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">update</a>(group_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>
- <code title="get /crm/v3/properties/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property_group.py">CollectionResponsePropertyGroup</a></code>
- <code title="delete /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">delete</a>(group_name, \*, object_type) -> None</code>
- <code title="get /crm/v3/properties/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">get</a>(group_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property_group.py">PropertyGroup</a></code>

## PropertyValidations

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePublicPropertyValidationRuleMapNoPaging,
    CollectionResponsePublicPropertyValidationRuleNoPaging,
    PublicPropertyValidationRule,
    PublicPropertyValidationRuleMap,
    PublicPropertyValidationRuleUpdate,
)
```

Methods:

- <code title="get /crm/v3/property-validations/{objectTypeId}">client.crm.property_validations.<a href="./src/hubspot_sdk/resources/crm/property_validations.py">list</a>(object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_property_validation_rule_map_no_paging.py">CollectionResponsePublicPropertyValidationRuleMapNoPaging</a></code>
- <code title="put /crm/v3/property-validations/{objectTypeId}/{propertyName}/rule-type/{ruleType}">client.crm.property_validations.<a href="./src/hubspot_sdk/resources/crm/property_validations.py">crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type</a>(rule_type, \*, object_type_id, property_name, \*\*<a href="src/hubspot_sdk/types/crm/property_validation_crm_v3_property_validations_object_type_id_property_name_rule_type_rule_type_params.py">params</a>) -> None</code>
- <code title="get /crm/v3/property-validations/{objectTypeId}/{propertyName}">client.crm.property_validations.<a href="./src/hubspot_sdk/resources/crm/property_validations.py">get</a>(property_name, \*, object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_property_validation_rule_no_paging.py">CollectionResponsePublicPropertyValidationRuleNoPaging</a></code>

## Subscriptions

Types:

```python
from hubspot_sdk.types.crm import PauseSubscriptionRequest, UnpauseRequest
```

Methods:

- <code title="post /payments-subscriptions/v1/subscriptions/crm/{objectId}/cancel">client.crm.subscriptions.<a href="./src/hubspot_sdk/resources/crm/subscriptions.py">cancel</a>(object_id) -> BinaryAPIResponse</code>
- <code title="post /payments-subscriptions/v1/subscriptions/crm/{objectId}/pause">client.crm.subscriptions.<a href="./src/hubspot_sdk/resources/crm/subscriptions.py">pause</a>(object_id, \*\*<a href="src/hubspot_sdk/types/crm/subscription_pause_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /payments-subscriptions/v1/subscriptions/crm/{objectId}/unpause">client.crm.subscriptions.<a href="./src/hubspot_sdk/resources/crm/subscriptions.py">unpause</a>(object_id, \*\*<a href="src/hubspot_sdk/types/crm/subscription_unpause_params.py">params</a>) -> BinaryAPIResponse</code>

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

## Users

Methods:

- <code title="post /crm/v3/objects/users">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/created_response_simple_public_object.py">CreatedResponseSimplePublicObject</a></code>
- <code title="patch /crm/v3/objects/users/{userId}">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">update</a>(user_id, \*\*<a href="src/hubspot_sdk/types/crm/user_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/v3/objects/users">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/v3/objects/users/{userId}">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">delete</a>(user_id) -> None</code>
- <code title="get /crm/v3/objects/users/{userId}">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">get</a>(user_id, \*\*<a href="src/hubspot_sdk/types/crm/user_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/v3/objects/users/search">client.crm.users.<a href="./src/hubspot_sdk/resources/crm/users/users.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/user_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

### Batch

Methods:

- <code title="post /crm/v3/objects/users/batch/create">client.crm.users.batch.<a href="./src/hubspot_sdk/resources/crm/users/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/users/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/users/batch/update">client.crm.users.batch.<a href="./src/hubspot_sdk/resources/crm/users/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/users/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/users/batch/archive">client.crm.users.batch.<a href="./src/hubspot_sdk/resources/crm/users/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/users/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/v3/objects/users/batch/read">client.crm.users.batch.<a href="./src/hubspot_sdk/resources/crm/users/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/users/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/v3/objects/users/batch/upsert">client.crm.users.batch.<a href="./src/hubspot_sdk/resources/crm/users/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/users/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

# Events

Types:

```python
from hubspot_sdk.types.events import (
    CollectionResponseExternalUnifiedEvent,
    ExternalUnifiedEvent,
    VisibleExternalEventTypeNames,
)
```

Methods:

- <code title="get /events/v3/events/">client.events.<a href="./src/hubspot_sdk/resources/events/events.py">list</a>(\*\*<a href="src/hubspot_sdk/types/events/event_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_unified_event.py">SyncPage[ExternalUnifiedEvent]</a></code>
- <code title="get /events/v3/events/event-types">client.events.<a href="./src/hubspot_sdk/resources/events/events.py">list_event_types</a>() -> <a href="./src/hubspot_sdk/types/events/visible_external_event_type_names.py">VisibleExternalEventTypeNames</a></code>

## EventDefinitions

Types:

```python
from hubspot_sdk.types.events import (
    AbsoluteComparativeTimestampRefineBy,
    AbsoluteRangedTimestampRefineBy,
    AllHistoryRefineBy,
    AllPropertyTypesOperation,
    AssociationDefinition,
    BehavioralEventTypeDefinitionLabels,
    BoolPropertyOperation,
    CalendarDatePropertyOperation,
    CollectionResponseWithTotalExternalBehavioralEventTypeDefinitionForwardPaging,
    ComboEventRule,
    ComboEventRuleBranch,
    ComparativeDatePropertyOperation,
    ComparativePropertyUpdatedOperation,
    DatePoint,
    DatePropertyOperation,
    DateTimePropertyOperation,
    EnumerationPropertyOperation,
    ExternalBehavioralEventPropertyCreate,
    ExternalBehavioralEventPropertyDefinitionPatch,
    ExternalBehavioralEventTypeDefinition,
    ExternalBehavioralEventTypeDefinitionEgg,
    ExternalBehavioralEventTypeDefinitionPatch,
    FiscalQuarter,
    FiscalYear,
    IndexOffset,
    IndexedTimePoint,
    MonthReference,
    MultiStringPropertyOperation,
    NowReference,
    NumOccurrencesRefineBy,
    NumberPropertyOperation,
    PropertyFilter,
    PropertyReferencedTime,
    QuarterReference,
    RangedDatePropertyOperation,
    RangedNumberPropertyOperation,
    RangedTimeOperation,
    RelativeComparativeTimestampRefineBy,
    RelativeRangedTimestampRefineBy,
    RollingDateRangePropertyOperation,
    RollingPropertyUpdatedOperation,
    SetOccurrencesRefineBy,
    StringPropertyOperation,
    TimeOffset,
    TimePointOperation,
    TodayReference,
    WeekReference,
    YearReference,
)
```

Methods:

- <code title="post /events/v3/event-definitions">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">create</a>(\*\*<a href="src/hubspot_sdk/types/events/event_definition_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="patch /events/v3/event-definitions/{eventName}">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">update</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/event_definition_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="get /events/v3/event-definitions">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/events/event_definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">SyncPage[ExternalBehavioralEventTypeDefinition]</a></code>
- <code title="delete /events/v3/event-definitions/{eventName}">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">delete</a>(event_name) -> None</code>
- <code title="post /events/v3/event-definitions/{eventName}/property">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">create_property</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/event_definition_create_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>
- <code title="delete /events/v3/event-definitions/{eventName}/property/{propertyName}">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">delete_property</a>(property_name, \*, event_name) -> None</code>
- <code title="get /events/v3/event-definitions/{eventName}">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">get</a>(event_name) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="patch /events/v3/event-definitions/{eventName}/property/{propertyName}">client.events.event_definitions.<a href="./src/hubspot_sdk/resources/events/event_definitions.py">update_property</a>(property_name, \*, event_name, \*\*<a href="src/hubspot_sdk/types/events/event_definition_update_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property.py">Property</a></code>

## Send

Types:

```python
from hubspot_sdk.types.events import (
    BatchedBehavioralEventHTTPCompletionRequest,
    BehavioralEventHTTPCompletionRequest,
)
```

Methods:

- <code title="post /events/v3/send">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">send</a>(\*\*<a href="src/hubspot_sdk/types/events/send_send_params.py">params</a>) -> None</code>
- <code title="post /events/v3/send/batch">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">send_batch</a>(\*\*<a href="src/hubspot_sdk/types/events/send_send_batch_params.py">params</a>) -> None</code>

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

Types:

```python
from hubspot_sdk.types.marketing import (
    EmailSendStatusView,
    EventIDView,
    PublicSingleSendEmail,
    PublicSingleSendRequestEgg,
)
```

## Campaigns

Types:

```python
from hubspot_sdk.types.marketing import (
    BatchInputPublicCampaignBatchUpdateItem,
    BatchInputPublicCampaignDeleteInput,
    BatchInputPublicCampaignInput,
    BatchInputPublicCampaignReadInput,
    BatchResponsePublicCampaign,
    BatchResponsePublicCampaignWithAssets,
    BatchResponsePublicCampaignWithAssetsWithErrors,
    BatchResponsePublicCampaignWithErrors,
    CollectionResponseContactReferenceForwardPaging,
    CollectionResponsePublicCampaignAsset,
    CollectionResponsePublicCampaignAssetForwardPaging,
    CollectionResponseWithTotalPublicCampaignForwardPaging,
    ContactReference,
    MetricsCounters,
    PublicBudgetItem,
    PublicBudgetItemInput,
    PublicBudgetTotals,
    PublicBusinessUnit,
    PublicCampaign,
    PublicCampaignAsset,
    PublicCampaignBatchUpdateItem,
    PublicCampaignDeleteInput,
    PublicCampaignInput,
    PublicCampaignReadInput,
    PublicCampaignWithAssets,
    PublicSpendItem,
    PublicSpendItemInput,
    RevenueAttributionAggregate,
)
```

Methods:

- <code title="post /marketing/v3/campaigns/">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaign_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">PublicCampaign</a></code>
- <code title="patch /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">update</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">PublicCampaign</a></code>
- <code title="get /marketing/v3/campaigns/">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaign_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">SyncPage[PublicCampaign]</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">delete</a>(campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">get</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign_with_assets.py">PublicCampaignWithAssets</a></code>

### Assets

Methods:

- <code title="put /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">update</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">list</a>(asset_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/asset_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_public_campaign_asset_forward_paging.py">CollectionResponsePublicCampaignAssetForwardPaging</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">delete</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>

### Batch

Methods:

- <code title="post /marketing/v3/campaigns/batch/create">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/v3/campaigns/batch/update">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/v3/campaigns/batch/archive">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/campaigns/batch/read">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign_with_assets.py">BatchResponsePublicCampaignWithAssets</a></code>

### Budget

Methods:

- <code title="post /marketing/v3/campaigns/{campaignGuid}/budget">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="put /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">update</a>(budget_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">delete</a>(budget_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get</a>(budget_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/budget/totals">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get_totals</a>(campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_totals.py">PublicBudgetTotals</a></code>

### Reports

Methods:

- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/metrics">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">get_attribution_metrics</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_get_attribution_metrics_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/metrics_counters.py">MetricsCounters</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/revenue">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">get_revenue_attribution</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_get_revenue_attribution_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/revenue_attribution_aggregate.py">RevenueAttributionAggregate</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">list_contact_ids_by_type</a>(contact_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_list_contact_ids_by_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/contact_reference.py">SyncPage[ContactReference]</a></code>

### Spend

Methods:

- <code title="post /marketing/v3/campaigns/{campaignGuid}/spend">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="put /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">update</a>(spend_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">delete</a>(spend_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">get</a>(spend_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>

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

- <code title="post /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="patch /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">SyncPage[PublicEmail]</a></code>
- <code title="delete /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">delete</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/emails/clone">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/ab-test/create-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/ab-test/get-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_ab_test_variation</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_draft</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions/{revisionId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_revision</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">VersionPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">list_revisions</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">SyncPage[VersionPublicEmail]</a></code>
- <code title="post /marketing/v3/emails/{emailId}/publish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">publish</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/draft/reset">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">reset_draft</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">restore_revision</a>(revision_id, \*, email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">restore_revision_to_draft</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/unpublish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">unpublish</a>(email_id) -> None</code>
- <code title="patch /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">update_draft</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>

### Statistics

Methods:

- <code title="get /marketing/v3/emails/statistics/list">client.marketing.emails.statistics.<a href="./src/hubspot_sdk/resources/marketing/emails/statistics.py">get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/emails/statistic_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/aggregate_email_statistics.py">AggregateEmailStatistics</a></code>
- <code title="get /marketing/v3/emails/statistics/histogram">client.marketing.emails.statistics.<a href="./src/hubspot_sdk/resources/marketing/emails/statistics.py">get_histogram</a>(\*\*<a href="src/hubspot_sdk/types/marketing/emails/statistic_get_histogram_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_email_statistic_interval_no_paging.py">CollectionResponseWithTotalEmailStatisticIntervalNoPaging</a></code>

## Events

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
    CrmPropertyWrapper,
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

- <code title="post /marketing/v3/marketing-events/events">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="patch /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response_v2.py">MarketingEventPublicDefaultResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">SyncPage[MarketingEventPublicReadResponseV2]</a></code>
- <code title="delete /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete</a>(object_id) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/cancel">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">cancel_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_cancel_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/complete">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">complete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_complete_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/batch/archive">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/delete">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_batch_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_delete_batch_by_external_event_id_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_delete_by_external_event_id_params.py">params</a>) -> None</code>
- <code title="get /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">get</a>(object_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">MarketingEventPublicReadResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">get_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_get_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response.py">MarketingEventPublicReadResponse</a></code>
- <code title="get /marketing/v3/marketing-events/events/search">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">search_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_search_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_search_public_response_wrapper_no_paging.py">CollectionResponseSearchPublicResponseWrapperNoPaging</a></code>
- <code title="get /marketing/v3/marketing-events/{externalEventId}/identifiers">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">search_identifiers_by_external_event_id</a>(external_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_marketing_event_identifiers_response_no_paging.py">CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging</a></code>
- <code title="post /marketing/v3/marketing-events/batch/update">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response_v2.py">BatchResponseMarketingEventPublicDefaultResponseV2</a></code>
- <code title="patch /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_update_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response.py">BatchResponseMarketingEventPublicDefaultResponse</a></code>
- <code title="put /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_by_external_event_id</a>(path_external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_subscriber_state_by_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_subscriber_state_by_email_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_subscriber_state_by_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_subscriber_state_by_id_params.py">params</a>) -> BinaryAPIResponse</code>

### Associations

Methods:

- <code title="get /marketing/v3/marketing-events/associations/{marketingEventId}/lists">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">list</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>
- <code title="delete /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">delete</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">associate</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">associate_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="delete /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">delete_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="get /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">list_by_external_account</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>

### Attendance

Methods:

- <code title="post /marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_event_id_and_contact_id</a>(subscriber_state, \*, object_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_event_id_and_contact_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_vid_response.py">BatchResponseSubscriberVidResponse</a></code>
- <code title="post /marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/email-create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_event_id_and_email</a>(subscriber_state, \*, object_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_event_id_and_email_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_email_response.py">BatchResponseSubscriberEmailResponse</a></code>
- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_external_event_id_and_contact_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_external_event_id_and_contact_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_vid_response.py">BatchResponseSubscriberVidResponse</a></code>
- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_external_event_id_and_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_external_event_id_and_email_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_email_response.py">BatchResponseSubscriberEmailResponse</a></code>

### Participations

Methods:

- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">get_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">get_by_id</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/contacts/{contactIdentifier}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_contact</a>(contact_identifier, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_contact_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_external_account_and_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_id</a>(marketing_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>

### Settings

Methods:

- <code title="post /marketing/v3/marketing-events/{appId}/settings">client.marketing.events.settings.<a href="./src/hubspot_sdk/resources/marketing/events/settings.py">create_or_update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/setting_create_or_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>
- <code title="get /marketing/v3/marketing-events/{appId}/settings">client.marketing.events.settings.<a href="./src/hubspot_sdk/resources/marketing/events/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>

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
- <code title="get /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">get</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="put /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">replace</a>(form_id) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>

## SingleSend

Methods:

- <code title="post /marketing/v4/email/single-send">client.marketing.single_send.<a href="./src/hubspot_sdk/resources/marketing/single_send.py">send</a>(\*\*<a href="src/hubspot_sdk/types/marketing/single_send_send_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/email_send_status_view.py">EmailSendStatusView</a></code>

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

- <code title="get /scheduler/v3/meetings/meeting-links">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">list</a>(\*\*<a href="src/hubspot_sdk/types/scheduler/meetings/meetings_link_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_link_metadata.py">SyncPage[ExternalLinkMetadata]</a></code>
- <code title="post /scheduler/v3/meetings/meeting-links/book">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">book</a>(\*\*<a href="src/hubspot_sdk/types/scheduler/meetings/meetings_link_book_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_meeting_booking_response.py">ExternalMeetingBookingResponse</a></code>
- <code title="get /scheduler/v3/meetings/meeting-links/book/availability-page/{slug}">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">get_availability_by_slug</a>(slug, \*\*<a href="src/hubspot_sdk/types/scheduler/meetings/meetings_link_get_availability_by_slug_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_link_availability_and_busy_times.py">ExternalLinkAvailabilityAndBusyTimes</a></code>
- <code title="get /scheduler/v3/meetings/meeting-links/book/{slug}">client.scheduler.meetings.meetings_links.<a href="./src/hubspot_sdk/resources/scheduler/meetings/meetings_links.py">get_booking_info_by_slug</a>(slug, \*\*<a href="src/hubspot_sdk/types/scheduler/meetings/meetings_link_get_booking_info_by_slug_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/scheduler/external_booking_info.py">ExternalBookingInfo</a></code>

# Settings

## Currencies

Types:

```python
from hubspot_sdk.types.settings import (
    BatchInputExchangeRateCreateRequest,
    BatchInputExchangeRateUpdateRequest,
    BatchResponseExchangeRate,
    BatchResponseExchangeRateWithErrors,
    CentralExchangeRatesInformation,
    CollectionResponseCurrencyCodeInfoNoPaging,
    CollectionResponseExchangeRateForwardPaging,
    CollectionResponseExchangeRateNoPaging,
    CompanyCurrency,
    CompanyCurrencyUpdateRequest,
    CurrencyCodeInfo,
    CurrencyCreateRequest,
    CurrencyPairUpdate,
    ExchangeRate,
    ExchangeRateCreateRequest,
    ExchangeRateMultiplier,
    ExchangeRateUpdateRequest,
)
```

Methods:

- <code title="post /settings/v3/currencies/exchange-rates/batch/create">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_create</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/batch/read">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/batch/update">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_update</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">create_exchange_rate</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_create_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">get_company_currency</a>() -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>
- <code title="get /settings/v3/currencies/exchange-rates/{exchangeRateId}">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">get_exchange_rate_by_id</a>(exchange_rate_id) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/codes">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_codes</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>
- <code title="get /settings/v3/currencies/exchange-rates/current">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_current_exchange_rates</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_exchange_rate_no_paging.py">CollectionResponseExchangeRateNoPaging</a></code>
- <code title="get /settings/v3/currencies/exchange-rates">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_exchange_rates</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_list_exchange_rates_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">SyncPage[ExchangeRate]</a></code>
- <code title="put /settings/v3/currencies/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_company_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_update_company_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>
- <code title="patch /settings/v3/currencies/exchange-rates/{exchangeRateId}">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_exchange_rate</a>(exchange_rate_id, \*\*<a href="src/hubspot_sdk/types/settings/currency_update_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/update-visibility">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_visibility</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_update_visibility_params.py">params</a>) -> None</code>

### CentralFxRates

Methods:

- <code title="post /settings/v3/currencies/central-fx-rates/add-currency">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">create_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/central_fx_rate_create_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/central-fx-rates/information">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_information</a>() -> <a href="./src/hubspot_sdk/types/settings/central_exchange_rates_information.py">CentralExchangeRatesInformation</a></code>
- <code title="get /settings/v3/currencies/central-fx-rates/unsupported-currencies">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_unsupported_currencies</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>

## TaxRates

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicTaxRateGroupForwardPaging,
    PublicTaxRateGroup,
)
```

Methods:

- <code title="get /tax-rates/v1/tax-rates">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/tax_rate_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">SyncPage[PublicTaxRateGroup]</a></code>
- <code title="get /tax-rates/v1/tax-rates/{taxRateGroupId}">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">get</a>(tax_rate_group_id) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">PublicTaxRateGroup</a></code>

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
