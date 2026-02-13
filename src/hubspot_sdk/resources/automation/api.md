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
