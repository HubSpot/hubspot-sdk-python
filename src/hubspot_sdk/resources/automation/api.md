# Automation

## Actions

Types:

```python
from hubspot_sdk.types.automation import (
    ActionExecutionIndexIdentifier,
    AgentRequestContext,
    ArrayFieldSchema,
    BatchInputCallbackCompletionBatchRequest,
    BooleanFieldSchema,
    CallbackCompletionBatchRequest,
    CallbackCompletionRequest,
    ChirpAIContextObject,
    CollectionResponsePublicActionDefinitionForwardPaging,
    CollectionResponsePublicActionFunctionIdentifierNoPaging,
    CollectionResponsePublicActionRevisionForwardPaging,
    ComplianceIDs,
    ContactID,
    CopilotRequestContext,
    DoubleFieldSchema,
    FieldTypeDefinition,
    IntegerFieldSchema,
    LongFieldSchema,
    ObjectFieldSchema,
    OutputFieldDefinition,
    PublicActionDefinition,
    PublicActionDefinitionEgg,
    PublicActionDefinitionPatch,
    PublicActionDefinitionRequiresObjectRequest,
    PublicActionDefinitionRequiresObjectResponse,
    PublicActionFunction,
    PublicActionFunctionIdentifier,
    PublicActionLabels,
    PublicActionRevision,
    PublicConditionalSingleFieldDependency,
    PublicExecutionTranslationRule,
    PublicFieldTypeDefinition,
    PublicInputFieldDefinition,
    PublicObjectRequestOptions,
    PublicOption,
    PublicSingleFieldDependency,
    StandaloneRequestContext,
    StringFieldSchema,
    TestRequestContext,
    WorkflowsRequestContext,
)
```

### Callbacks

Methods:

- <code title="post /automation/actions/callbacks/2026-03/{callbackId}/complete">client.automation.actions.callbacks.<a href="./src/hubspot_sdk/resources/automation/actions/callbacks.py">complete</a>(callback_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/callback_complete_params.py">params</a>) -> None</code>
- <code title="post /automation/actions/callbacks/2026-03/complete">client.automation.actions.callbacks.<a href="./src/hubspot_sdk/resources/automation/actions/callbacks.py">complete_batch</a>(\*\*<a href="src/hubspot_sdk/types/automation/actions/callback_complete_batch_params.py">params</a>) -> None</code>

### Definitions

Methods:

- <code title="post /automation/actions/2026-03/{appId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="patch /automation/actions/2026-03/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">update</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="get /automation/actions/2026-03/{appId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">list</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">SyncPage[PublicActionDefinition]</a></code>
- <code title="delete /automation/actions/2026-03/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">delete</a>(definition_id, \*, app_id) -> None</code>
- <code title="post /automation/actions/2026-03/{appId}/{definitionId}/requires-object">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">create_requires_object</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_create_requires_object_params.py">params</a>) -> None</code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">get</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/definition_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/requires-object">client.automation.actions.definitions.<a href="./src/hubspot_sdk/resources/automation/actions/definitions.py">get_requires_object</a>(definition_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition_requires_object_response.py">PublicActionDefinitionRequiresObjectResponse</a></code>

### Functions

Methods:

- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/functions">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">list</a>(definition_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/automation/collection_response_public_action_function_identifier_no_paging.py">CollectionResponsePublicActionFunctionIdentifierNoPaging</a></code>
- <code title="delete /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="put /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="put /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/function_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="delete /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">delete_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">get</a>(function_id, \*, app_id, definition_id, function_type) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.functions.<a href="./src/hubspot_sdk/resources/automation/actions/functions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>

### Revisions

Methods:

- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/revisions">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/actions/revision_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">SyncPage[PublicActionRevision]</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/revisions/{revisionId}">client.automation.actions.revisions.<a href="./src/hubspot_sdk/resources/automation/actions/revisions.py">get</a>(revision_id, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">PublicActionRevision</a></code>

## Sequences

Types:

```python
from hubspot_sdk.types.automation import (
    CollectionResponseWithTotalPublicSequenceLiteResponse,
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
)
```

Methods:

- <code title="get /automation/sequences/2026-03">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences.py">list</a>(\*\*<a href="src/hubspot_sdk/types/automation/sequence_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_lite_response.py">SyncPage[PublicSequenceLiteResponse]</a></code>
- <code title="post /automation/sequences/2026-03/enrollments">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences.py">create_enrollment</a>(\*\*<a href="src/hubspot_sdk/types/automation/sequence_create_enrollment_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_enrollment_lite_response.py">PublicSequenceEnrollmentLiteResponse</a></code>
- <code title="get /automation/sequences/2026-03/{sequenceId}">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences.py">get</a>(sequence_id, \*\*<a href="src/hubspot_sdk/types/automation/sequence_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_response.py">PublicSequenceResponse</a></code>
- <code title="get /automation/sequences/2026-03/enrollments/contact/{contactId}">client.automation.sequences.<a href="./src/hubspot_sdk/resources/automation/sequences.py">get_enrollment_by_contact_id</a>(contact_id) -> <a href="./src/hubspot_sdk/types/automation/public_sequence_enrollment_response.py">PublicSequenceEnrollmentResponse</a></code>
