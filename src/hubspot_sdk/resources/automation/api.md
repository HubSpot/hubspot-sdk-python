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
    Option,
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

Methods:

- <code title="post /automation/actions/2026-03/{appId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="patch /automation/actions/2026-03/{appId}/{definitionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">update</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition.py">PublicActionDefinition</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/revisions">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">list</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">SyncPage[PublicActionRevision]</a></code>
- <code title="delete /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">delete</a>(function_id, \*, app_id, definition_id, function_type) -> None</code>
- <code title="post /automation/actions/callbacks/2026-03/{callbackId}/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete</a>(callback_id, \*\*<a href="src/hubspot_sdk/types/automation/action_complete_params.py">params</a>) -> None</code>
- <code title="post /automation/actions/callbacks/2026-03/complete">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">complete_batch</a>(\*\*<a href="src/hubspot_sdk/types/automation/action_complete_batch_params.py">params</a>) -> None</code>
- <code title="put /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}/{functionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace</a>(function_id, \*, app_id, definition_id, function_type, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="put /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_or_replace_by_function_type</a>(function_type, \*, app_id, definition_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_or_replace_by_function_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/automation/public_action_function_identifier.py">PublicActionFunctionIdentifier</a></code>
- <code title="post /automation/actions/2026-03/{appId}/{definitionId}/requires-object">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">create_requires_object</a>(definition_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/automation/action_create_requires_object_params.py">params</a>) -> None</code>
- <code title="delete /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">delete_by_function_type</a>(function_type, \*, app_id, definition_id) -> None</code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/revisions/{revisionId}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">get</a>(revision_id, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_revision.py">PublicActionRevision</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/functions/{functionType}">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">get_by_function_type</a>(function_type, \*, app_id, definition_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_function.py">PublicActionFunction</a></code>
- <code title="get /automation/actions/2026-03/{appId}/{definitionId}/requires-object">client.automation.actions.<a href="./src/hubspot_sdk/resources/automation/actions.py">get_requires_object</a>(definition_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/automation/public_action_definition_requires_object_response.py">PublicActionDefinitionRequiresObjectResponse</a></code>
