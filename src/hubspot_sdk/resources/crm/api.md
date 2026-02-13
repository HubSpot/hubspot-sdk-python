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
