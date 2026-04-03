# Crm

Types:

```python
from hubspot_sdk.types.crm import (
    AssociationSpecWithLabel,
    BatchResponsePublicDefaultAssociation,
    CollectionResponseMultiAssociatedObjectWithLabelForwardPaging,
    CollectionResponseWithTotalSimplePublicObject,
    Filter,
    FilterGroup,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    Property,
    PublicDefaultAssociation,
    PublicObjectSearchRequest,
    SimplePublicObject,
    ValueWithTimestamp,
)
```

## AppUninstalls

Methods:

- <code title="delete /appinstalls/2026-03/external-install">client.crm.app_uninstalls.<a href="./src/hubspot_sdk/resources/crm/app_uninstalls.py">uninstall</a>() -> None</code>

## Associations

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPublicAssociationMultiArchive,
    BatchInputPublicAssociationMultiPost,
    BatchInputPublicDefaultAssociationMultiPost,
    BatchInputPublicFetchAssociationsBatchRequest,
    BatchResponseLabelsBetweenObjectPair,
    BatchResponseLabelsBetweenObjectPairWithErrors,
    BatchResponsePublicAssociationMultiWithLabel,
    BatchResponsePublicAssociationMultiWithLabelWithErrors,
    DateTime,
    PublicAssociationMultiArchive,
    PublicAssociationMultiPost,
    PublicAssociationMultiWithLabel,
    PublicDefaultAssociationMultiPost,
    PublicFetchAssociationsBatchRequest,
    ReportCreationResponse,
)
```

Methods:

- <code title="get /crm/objects/2026-03/{objectType}/{objectId}/associations/{toObjectType}">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">list</a>(to_object_type, \*, object_type, object_id, \*\*<a href="src/hubspot_sdk/types/crm/association_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/multi_associated_object_with_label.py">SyncPage[MultiAssociatedObjectWithLabel]</a></code>
- <code title="delete /crm/objects/2026-03/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">delete</a>(to_object_id, \*, object_type, object_id, to_object_type) -> None</code>
- <code title="post /crm/associations/2026-03/usage/high-usage-report/{userId}">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">request_high_usage_report</a>(user_id) -> <a href="./src/hubspot_sdk/types/crm/report_creation_response.py">ReportCreationResponse</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/search">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="put /crm/objects/2026-03/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}">client.crm.associations.<a href="./src/hubspot_sdk/resources/crm/associations/associations.py">update_association_labels</a>(to_object_id, \*, object_type, object_id, to_object_type, \*\*<a href="src/hubspot_sdk/types/crm/association_update_association_labels_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/labels_between_object_pair.py">LabelsBetweenObjectPair</a></code>

### Batch

Methods:

- <code title="put /crm/objects/2026-03/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">create</a>(to_object_id, \*, from_object_type, from_object_id, to_object_type) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/associations/2026-03/{fromObjectType}/{toObjectType}/batch/archive">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/associations/2026-03/{fromObjectType}/{toObjectType}/batch/associate/default">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">create_default</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_create_default_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/associations/2026-03/{fromObjectType}/{toObjectType}/batch/labels/archive">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">delete_labels</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_delete_labels_params.py">params</a>) -> None</code>
- <code title="post /crm/associations/2026-03/{fromObjectType}/{toObjectType}/batch/read">client.crm.associations.batch.<a href="./src/hubspot_sdk/resources/crm/associations/batch.py">get</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_multi_with_label.py">BatchResponsePublicAssociationMultiWithLabel</a></code>

## AssociationsSchema

Types:

```python
from hubspot_sdk.types.crm import (
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

### Labels

Methods:

- <code title="post /crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create">client.crm.associations_schema.labels.<a href="./src/hubspot_sdk/resources/crm/associations_schema/labels.py">batch_create</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations_schema/label_batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_definition_user_configuration.py">BatchResponsePublicAssociationDefinitionUserConfiguration</a></code>
- <code title="post /crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels">client.crm.associations_schema.labels.<a href="./src/hubspot_sdk/resources/crm/associations_schema/labels.py">create_label</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations_schema/label_create_label_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_association_spec_with_label_no_paging.py">CollectionResponseAssociationSpecWithLabelNoPaging</a></code>
- <code title="delete /crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels/{associationTypeId}">client.crm.associations_schema.labels.<a href="./src/hubspot_sdk/resources/crm/associations_schema/labels.py">delete_label</a>(association_type_id, \*, from_object_type, to_object_type) -> None</code>
- <code title="get /crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels">client.crm.associations_schema.labels.<a href="./src/hubspot_sdk/resources/crm/associations_schema/labels.py">list_labels</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_association_spec_with_label_no_paging.py">CollectionResponseAssociationSpecWithLabelNoPaging</a></code>
- <code title="put /crm/associations/2026-03/{fromObjectType}/{toObjectType}/labels">client.crm.associations_schema.labels.<a href="./src/hubspot_sdk/resources/crm/associations_schema/labels.py">update_label</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations_schema/label_update_label_params.py">params</a>) -> None</code>

### Limits

Methods:

- <code title="get /crm/associations/2026-03/definitions/configurations/all">client.crm.associations_schema.limits.<a href="./src/hubspot_sdk/resources/crm/associations_schema/limits.py">list</a>() -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_association_definition_user_configuration_no_paging.py">CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging</a></code>
- <code title="post /crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge">client.crm.associations_schema.limits.<a href="./src/hubspot_sdk/resources/crm/associations_schema/limits.py">batch_delete</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations_schema/limit_batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update">client.crm.associations_schema.limits.<a href="./src/hubspot_sdk/resources/crm/associations_schema/limits.py">batch_update</a>(to_object_type, \*, from_object_type, \*\*<a href="src/hubspot_sdk/types/crm/associations_schema/limit_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_association_definition_configuration_update_result.py">BatchResponsePublicAssociationDefinitionConfigurationUpdateResult</a></code>
- <code title="get /crm/associations/2026-03/definitions/configurations/{fromObjectType}/{toObjectType}">client.crm.associations_schema.limits.<a href="./src/hubspot_sdk/resources/crm/associations_schema/limits.py">get_by_object_types</a>(to_object_type, \*, from_object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_association_definition_user_configuration_no_paging.py">CollectionResponsePublicAssociationDefinitionUserConfigurationNoPaging</a></code>

## DealSplits

Types:

```python
from hubspot_sdk.types.crm import (
    BatchResponseDealToDealSplits,
    BatchResponseDealToDealSplitsWithErrors,
    DealToDealSplits,
    PublicDealSplitInput,
    PublicDealSplitsBatchCreateRequest,
    PublicDealSplitsCreateRequest,
)
```

### Batch

Methods:

- <code title="post /deal-splits/2026-03/batch/read">client.crm.deal_splits.batch.<a href="./src/hubspot_sdk/resources/crm/deal_splits/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/crm/deal_splits/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_deal_to_deal_splits.py">BatchResponseDealToDealSplits</a></code>
- <code title="post /deal-splits/2026-03/batch/upsert">client.crm.deal_splits.batch.<a href="./src/hubspot_sdk/resources/crm/deal_splits/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/deal_splits/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_deal_to_deal_splits.py">BatchResponseDealToDealSplits</a></code>

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

- <code title="post /crm/exports/2026-03/export/async">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">create_async</a>() -> <a href="./src/hubspot_sdk/types/shared/task_locator.py">TaskLocator</a></code>
- <code title="get /crm/exports/2026-03/export/{exportId}">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">get</a>(export_id) -> <a href="./src/hubspot_sdk/types/crm/public_export_response.py">PublicExportResponse</a></code>
- <code title="get /crm/exports/2026-03/export/async/tasks/{taskId}/status">client.crm.exports.<a href="./src/hubspot_sdk/resources/crm/exports.py">get_status</a>(task_id) -> <a href="./src/hubspot_sdk/types/crm/action_response_with_single_result_uri.py">ActionResponseWithSingleResultUri</a></code>

## Extensions

### Calling

Types:

```python
from hubspot_sdk.types.crm.extensions import (
    ChannelConnectionSettingsPatchRequest,
    ChannelConnectionSettingsRequest,
    ChannelConnectionSettingsResponse,
    CompanyCallerID,
    CompletedThirdPartyCallRequest,
    CompletedThirdPartyCallResponse,
    ContactCallerID,
    FormattedPhoneNumber,
    MarkRecordingAsReadyRequest,
    ObjectCoordinates,
    RecordingSettingsPatchRequest,
    RecordingSettingsRequest,
    RecordingSettingsResponse,
    SettingsPatchRequest,
    SettingsRequest,
    SettingsResponse,
)
```

Methods:

- <code title="post /crm/extensions/calling/2026-03/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">create_channel_connection_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_channel_connection_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="post /crm/extensions/calling/2026-03/inbound-call">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">create_inbound_call</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_inbound_call_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/completed_third_party_call_response.py">CompletedThirdPartyCallResponse</a></code>
- <code title="post /crm/extensions/calling/2026-03/recordings/ready">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">create_recording_ready</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_recording_ready_params.py">params</a>) -> None</code>
- <code title="post /crm/extensions/calling/2026-03/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">create_recording_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_recording_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="post /crm/extensions/calling/2026-03/{appId}/settings">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">create_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_create_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/settings_response.py">SettingsResponse</a></code>
- <code title="delete /crm/extensions/calling/2026-03/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">delete_channel_connection_settings</a>(app_id) -> None</code>
- <code title="delete /crm/extensions/calling/2026-03/{appId}/settings">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">delete_settings</a>(app_id) -> None</code>
- <code title="get /crm/extensions/calling/2026-03/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">get_channel_connection_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="get /crm/extensions/calling/2026-03/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">get_recording_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="get /crm/extensions/calling/2026-03/{appId}/settings">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">get_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/settings_response.py">SettingsResponse</a></code>
- <code title="patch /crm/extensions/calling/2026-03/{appId}/settings/channel-connection">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">update_channel_connection_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_update_channel_connection_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/channel_connection_settings_response.py">ChannelConnectionSettingsResponse</a></code>
- <code title="patch /crm/extensions/calling/2026-03/{appId}/settings/recording">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">update_recording_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_update_recording_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/recording_settings_response.py">RecordingSettingsResponse</a></code>
- <code title="patch /crm/extensions/calling/2026-03/{appId}/settings">client.crm.extensions.calling.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/calling.py">update_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/calling_update_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/settings_response.py">SettingsResponse</a></code>

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

- <code title="post /crm/extensions/calling/2026-03/transcripts">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/transcript_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/calling/transcript_create_response.py">TranscriptCreateResponse</a></code>
- <code title="delete /crm/extensions/calling/2026-03/transcripts/{transcriptId}">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">delete</a>(transcript_id) -> None</code>
- <code title="post /crm/extensions/calling/2026-03/inbound-call">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">create_inbound_call</a>(\*\*<a href="src/hubspot_sdk/types/crm/extensions/calling/transcript_create_inbound_call_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/completed_third_party_call_response.py">CompletedThirdPartyCallResponse</a></code>
- <code title="get /crm/extensions/calling/2026-03/transcripts/{transcriptId}">client.crm.extensions.calling.transcripts.<a href="./src/hubspot_sdk/resources/crm/extensions/calling/transcripts.py">get</a>(transcript_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/calling/transcript_response.py">TranscriptResponse</a></code>

### CardsDev

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
    CardMigrateViewsRequest,
    CardMigrateViewsResponse,
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

- <code title="post /crm/extensions/cards-dev/2026-03/{appId}">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/cards_dev_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="patch /crm/extensions/cards-dev/2026-03/{appId}/{cardId}">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">update</a>(card_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/cards_dev_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="delete /crm/extensions/cards-dev/2026-03/{appId}/{cardId}">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">delete</a>(card_id, \*, app_id) -> None</code>
- <code title="get /crm/extensions/cards-dev/2026-03/{appId}">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_list_response.py">PublicCardListResponse</a></code>
- <code title="get /crm/extensions/cards-dev/2026-03/{appId}/{cardId}">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">get_by_id</a>(card_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/public_card_response.py">PublicCardResponse</a></code>
- <code title="get /crm/extensions/cards-dev/2026-03/sample-response">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">get_sample_response</a>() -> <a href="./src/hubspot_sdk/types/crm/extensions/integrator_card_payload_response.py">IntegratorCardPayloadResponse</a></code>
- <code title="post /crm/extensions/cards-dev/2026-03/{appId}/views/migrate">client.crm.extensions.cards_dev.<a href="./src/hubspot_sdk/resources/crm/extensions/cards_dev.py">migrate_views</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/cards_dev_migrate_views_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/card_migrate_views_response.py">CardMigrateViewsResponse</a></code>

### VideoConferencing

Types:

```python
from hubspot_sdk.types.crm.extensions import ExternalSettings
```

Methods:

- <code title="put /crm/extensions/videoconferencing/2026-03/settings/{appId}">client.crm.extensions.video_conferencing.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/crm/extensions/video_conferencing_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>
- <code title="delete /crm/extensions/videoconferencing/2026-03/settings/{appId}">client.crm.extensions.video_conferencing.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing.py">delete</a>(app_id) -> None</code>
- <code title="get /crm/extensions/videoconferencing/2026-03/settings/{appId}">client.crm.extensions.video_conferencing.<a href="./src/hubspot_sdk/resources/crm/extensions/video_conferencing.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/external_settings.py">ExternalSettings</a></code>

## FeatureFlags

Types:

```python
from hubspot_sdk.types.crm import (
    BatchPortalEntry,
    FlagPutRequest,
    FlagResponse,
    FlagsForAppResponse,
    PortalFlagStateBatchDeleteRequest,
    PortalFlagStateBatchPutRequest,
    PortalFlagStateBatchResponse,
    PortalFlagStatePutRequest,
    PortalFlagStateResponse,
)
```

Methods:

- <code title="put /feature-flags/2026-03/{appId}/flags/{flagName}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">update</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flag_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="delete /feature-flags/2026-03/{appId}/flags/{flagName}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">delete</a>(flag_name, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="delete /feature-flags/2026-03/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">delete_portal_state</a>(portal_id, \*, app_id, flag_name) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>
- <code title="get /feature-flags/2026-03/{appId}/flags/{flagName}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">get</a>(flag_name, \*, app_id) -> <a href="./src/hubspot_sdk/types/crm/flag_response.py">FlagResponse</a></code>
- <code title="get /feature-flags/2026-03/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">get_portal_state</a>(portal_id, \*, app_id, flag_name) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>
- <code title="get /feature-flags/2026-03/{appId}/flags/all">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">list_all</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/flags_for_app_response.py">FlagsForAppResponse</a></code>
- <code title="get /feature-flags/2026-03/{appId}/flags/{flagName}/portals">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">list_portals</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flag_list_portals_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>
- <code title="put /feature-flags/2026-03/{appId}/flags/{flagName}/portals/{portalId}">client.crm.feature_flags.<a href="./src/hubspot_sdk/resources/crm/feature_flags/feature_flags.py">update_portal_state</a>(portal_id, \*, app_id, flag_name, \*\*<a href="src/hubspot_sdk/types/crm/feature_flag_update_portal_state_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_response.py">PortalFlagStateResponse</a></code>

### Batch

Methods:

- <code title="post /feature-flags/2026-03/{appId}/flags/{flagName}/portals/batch/delete">client.crm.feature_flags.batch.<a href="./src/hubspot_sdk/resources/crm/feature_flags/batch.py">delete</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/batch_delete_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>
- <code title="post /feature-flags/2026-03/{appId}/flags/{flagName}/portals/batch/upsert">client.crm.feature_flags.batch.<a href="./src/hubspot_sdk/resources/crm/feature_flags/batch.py">upsert</a>(flag_name, \*, app_id, \*\*<a href="src/hubspot_sdk/types/crm/feature_flags/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/portal_flag_state_batch_response.py">PortalFlagStateBatchResponse</a></code>

## Imports

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponsePublicImportErrorForwardPaging,
    CollectionResponsePublicImportResponseForwardPaging,
    ImportRowCore,
    ImportTemplate,
    PublicImportError,
    PublicImportMetadata,
    PublicImportResponse,
    PublicObjectListRecord,
)
```

Methods:

- <code title="post /crm/imports/2026-03">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/import_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">PublicImportResponse</a></code>
- <code title="get /crm/imports/2026-03">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/import_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">SyncPage[PublicImportResponse]</a></code>
- <code title="post /crm/imports/2026-03/{importId}/cancel">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">cancel</a>(import_id) -> <a href="./src/hubspot_sdk/types/shared/action_response.py">ActionResponse</a></code>
- <code title="get /crm/imports/2026-03/{importId}">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">get</a>(import_id) -> <a href="./src/hubspot_sdk/types/crm/public_import_response.py">PublicImportResponse</a></code>
- <code title="get /crm/imports/2026-03/{importId}/errors">client.crm.imports.<a href="./src/hubspot_sdk/resources/crm/imports.py">list_errors</a>(import_id, \*\*<a href="src/hubspot_sdk/types/crm/import_list_errors_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_import_error.py">SyncPage[PublicImportError]</a></code>

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

- <code title="get /crm/limits/2026-03/associations/labels">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_label_limits</a>(\*\*<a href="src/hubspot_sdk/types/crm/limit_get_association_label_limits_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_association_label_limit_response_no_paging.py">CollectionResponseAssociationLabelLimitResponseNoPaging</a></code>
- <code title="get /crm/limits/2026-03/associations/records/{fromObjectTypeId}/{toObjectTypeId}">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_by_object_type</a>(to_object_type_id, \*, from_object_type_id) -> <a href="./src/hubspot_sdk/types/crm/association_record_limit_response.py">AssociationRecordLimitResponse</a></code>
- <code title="get /crm/limits/2026-03/associations/records/from">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_from_objects</a>() -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_type_near_or_at_association_limit_no_paging.py">CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging</a></code>
- <code title="get /crm/limits/2026-03/associations/records/{fromObjectTypeId}/to">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_association_records_limits_to_objects</a>(from_object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_type_near_or_at_association_limit_no_paging.py">CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging</a></code>
- <code title="get /crm/limits/2026-03/calculated-properties">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_calculated_property_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/calculated_property_limit_response.py">CalculatedPropertyLimitResponse</a></code>
- <code title="get /crm/limits/2026-03/custom-object-types">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_custom_object_type_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/custom_object_limit_response.py">CustomObjectLimitResponse</a></code>
- <code title="get /crm/limits/2026-03/custom-properties">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_custom_property_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/custom_property_limit_response.py">CustomPropertyLimitResponse</a></code>
- <code title="get /crm/limits/2026-03/pipelines">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_pipeline_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/pipeline_limit_response.py">PipelineLimitResponse</a></code>
- <code title="get /crm/limits/2026-03/records">client.crm.limits.<a href="./src/hubspot_sdk/resources/crm/limits.py">get_record_limits</a>() -> <a href="./src/hubspot_sdk/types/crm/record_limit_response.py">RecordLimitResponse</a></code>

## Lists

Types:

```python
from hubspot_sdk.types.crm import (
    APICollectionResponseJoinTimeAndRecordID,
    APICollectionResponseRecordListMembership,
    BatchInputRecordIDInput,
    BatchResponseRecordIDWithMemberships,
    BatchResponseRecordIDWithMembershipsWithErrors,
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
    ListSizeAndEditHistoryResponse,
    ListSizeDataPoint,
    ListUpdateResponse,
    ListsByIDResponse,
    MembershipChangeRequest,
    MembershipsUpdateResponse,
    PublicAbsoluteComparativeTimestampRefineBy,
    PublicAbsoluteRangedTimestampRefineBy,
    PublicAdsSearchFilter,
    PublicAdsTimeFilter,
    PublicAllHistoryRefineBy,
    PublicAllPropertyTypesOperation,
    PublicAndFilterBranch,
    PublicAssociationFilterBranch,
    PublicAssociationInListFilter,
    PublicBatchMigrationMapping,
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
    PublicListConversionDate,
    PublicListConversionInactivity,
    PublicListConversionResponse,
    PublicListConversionTime,
    PublicListFolder,
    PublicListPermissions,
    PublicMembershipSettings,
    PublicMigrationMapping,
    PublicMonthReference,
    PublicMultiStringPropertyOperation,
    PublicNotAllFilterBranch,
    PublicNotAnyFilterBranch,
    PublicNowReference,
    PublicNumAssociationsFilter,
    PublicNumOccurrencesRefineBy,
    PublicNumberPropertyOperation,
    PublicObjectList,
    PublicObjectListSearchResult,
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
    RecordIDInput,
    RecordIDWithMemberships,
    RecordListMembership,
)
```

Methods:

- <code title="post /crm/lists/2026-03">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_create_response.py">ListCreateResponse</a></code>
- <code title="get /crm/lists/2026-03">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/lists_by_id_response.py">ListsByIDResponse</a></code>
- <code title="delete /crm/lists/2026-03/{listId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">delete</a>(list_id) -> None</code>
- <code title="put /crm/lists/2026-03/{listId}/memberships/add-and-remove">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">add_and_remove_memberships</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_add_and_remove_memberships_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="put /crm/lists/2026-03/{listId}/memberships/add">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">add_memberships</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_add_memberships_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="put /crm/lists/2026-03/{listId}/memberships/add-from/{sourceListId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">add_memberships_from</a>(source_list_id, \*, list_id) -> None</code>
- <code title="post /crm/lists/2026-03/records/memberships/batch/read">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">batch_read_memberships</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_batch_read_memberships_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_record_id_with_memberships.py">BatchResponseRecordIDWithMemberships</a></code>
- <code title="post /crm/lists/2026-03/folders">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">create_folder</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_create_folder_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_create_response.py">ListFolderCreateResponse</a></code>
- <code title="post /crm/lists/2026-03/idmapping">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">create_id_mapping</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_create_id_mapping_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_batch_migration_mapping.py">PublicBatchMigrationMapping</a></code>
- <code title="delete /crm/lists/2026-03/folders/{folderId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">delete_folder</a>(folder_id) -> None</code>
- <code title="delete /crm/lists/2026-03/{listId}/memberships">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">delete_memberships</a>(list_id) -> None</code>
- <code title="get /crm/lists/2026-03/{listId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_fetch_response.py">ListFetchResponse</a></code>
- <code title="get /crm/lists/2026-03/object-type-id/{objectTypeId}/name/{listName}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_by_object_type_and_name</a>(list_name, \*, object_type_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_by_object_type_and_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_fetch_response.py">ListFetchResponse</a></code>
- <code title="get /crm/lists/2026-03/idmapping">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_id_mapping</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_get_id_mapping_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_migration_mapping.py">PublicMigrationMapping</a></code>
- <code title="get /crm/lists/2026-03/{listId}/memberships/join-order">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_memberships_join_order</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_memberships_join_order_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/join_time_and_record_id.py">SyncPage[JoinTimeAndRecordID]</a></code>
- <code title="get /crm/lists/2026-03/records/{objectTypeId}/{recordId}/memberships">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_record_memberships</a>(record_id, \*, object_type_id) -> <a href="./src/hubspot_sdk/types/crm/api_collection_response_record_list_membership.py">APICollectionResponseRecordListMembership</a></code>
- <code title="get /crm/lists/2026-03/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_schedule_conversion</a>(list_id) -> <a href="./src/hubspot_sdk/types/crm/public_list_conversion_response.py">PublicListConversionResponse</a></code>
- <code title="get /crm/lists/2026-03/{listId}/size-and-edits-history/between">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">get_size_and_edits_history_between</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_get_size_and_edits_history_between_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_size_and_edit_history_response.py">ListSizeAndEditHistoryResponse</a></code>
- <code title="post /crm/lists/2026-03/search">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">list_by_search</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_list_by_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_search_response.py">ListSearchResponse</a></code>
- <code title="get /crm/lists/2026-03/folders">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">list_folders</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_list_folders_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>
- <code title="get /crm/lists/2026-03/{listId}/memberships">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">list_memberships</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_list_memberships_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/join_time_and_record_id.py">SyncPage[JoinTimeAndRecordID]</a></code>
- <code title="put /crm/lists/2026-03/folders/{folderId}/move/{newParentFolderId}">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">move_folder</a>(new_parent_folder_id, \*, folder_id) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>
- <code title="put /crm/lists/2026-03/folders/move-list">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">move_list</a>(\*\*<a href="src/hubspot_sdk/types/crm/list_move_list_params.py">params</a>) -> None</code>
- <code title="put /crm/lists/2026-03/{listId}/memberships/remove">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">remove_memberships</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_remove_memberships_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/memberships_update_response.py">MembershipsUpdateResponse</a></code>
- <code title="put /crm/lists/2026-03/folders/{folderId}/rename">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">rename_folder</a>(folder_id, \*\*<a href="src/hubspot_sdk/types/crm/list_rename_folder_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_folder_fetch_response.py">ListFolderFetchResponse</a></code>
- <code title="put /crm/lists/2026-03/{listId}/restore">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">restore</a>(list_id) -> None</code>
- <code title="delete /crm/lists/2026-03/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">schedule_conversion</a>(list_id) -> None</code>
- <code title="put /crm/lists/2026-03/{listId}/update-list-filters">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">update_list_filters</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_update_list_filters_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_update_response.py">ListUpdateResponse</a></code>
- <code title="put /crm/lists/2026-03/{listId}/update-list-name">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">update_list_name</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_update_list_name_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/list_update_response.py">ListUpdateResponse</a></code>
- <code title="put /crm/lists/2026-03/{listId}/schedule-conversion">client.crm.lists.<a href="./src/hubspot_sdk/resources/crm/lists.py">update_schedule_conversion</a>(list_id, \*\*<a href="src/hubspot_sdk/types/crm/list_update_schedule_conversion_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_list_conversion_response.py">PublicListConversionResponse</a></code>

## ObjectLibrary

### Enablement

Types:

```python
from hubspot_sdk.types.crm.object_library import (
    ObjectTypeEnablementPublicResponse,
    PortalObjectTypeEnablementPublicResponse,
)
```

Methods:

- <code title="get /crm/object-library/2026-03/enablement">client.crm.object_library.enablement.<a href="./src/hubspot_sdk/resources/crm/object_library/enablement.py">get_all</a>() -> <a href="./src/hubspot_sdk/types/crm/object_library/portal_object_type_enablement_public_response.py">PortalObjectTypeEnablementPublicResponse</a></code>
- <code title="get /crm/object-library/2026-03/enablement/{objectTypeId}">client.crm.object_library.enablement.<a href="./src/hubspot_sdk/resources/crm/object_library/enablement.py">get_by_object_type_id</a>(object_type_id) -> <a href="./src/hubspot_sdk/types/crm/object_library/object_type_enablement_public_response.py">ObjectTypeEnablementPublicResponse</a></code>

## ObjectSchemas

Types:

```python
from hubspot_sdk.types.crm import (
    CollectionResponseObjectSchemaNoPaging,
    ObjectSchema,
    ObjectSchemaBatchReadRequest,
    ObjectSchemaEgg,
    ObjectTypePropertyCreate,
)
```

Methods:

- <code title="post /crm-object-schemas/2026-03/schemas">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/object_schema_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/object_schema.py">ObjectSchema</a></code>
- <code title="patch /crm-object-schemas/2026-03/schemas/{objectType}">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/object_schema_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/object_type_definition.py">ObjectTypeDefinition</a></code>
- <code title="get /crm-object-schemas/2026-03/schemas">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/object_schema_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>
- <code title="delete /crm-object-schemas/2026-03/schemas/{objectType}">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/object_schema_delete_params.py">params</a>) -> None</code>
- <code title="post /crm-object-schemas/2026-03/schemas/{objectType}/associations">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">create_association</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/object_schema_create_association_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/association_definition.py">AssociationDefinition</a></code>
- <code title="delete /crm-object-schemas/2026-03/schemas/{objectType}/associations/{associationIdentifier}">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">delete_association</a>(association_identifier, \*, object_type) -> None</code>
- <code title="get /crm-object-schemas/2026-03/schemas/{objectType}">client.crm.object_schemas.<a href="./src/hubspot_sdk/resources/crm/object_schemas/object_schemas.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/object_schema_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/object_schema.py">ObjectSchema</a></code>

### Batch

Methods:

- <code title="post /crm-object-schemas/2026-03/schemas/batch/read">client.crm.object_schemas.batch.<a href="./src/hubspot_sdk/resources/crm/object_schemas/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/object_schemas/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_object_schema_no_paging.py">CollectionResponseObjectSchemaNoPaging</a></code>

## Objects

Types:

```python
from hubspot_sdk.types.crm import (
    AssociatedID,
    BatchInputSimplePublicObjectBatchInput,
    BatchInputSimplePublicObjectBatchInputForCreate,
    BatchInputSimplePublicObjectBatchInputUpsert,
    BatchInputSimplePublicObjectID,
    BatchReadInputSimplePublicObjectID,
    BatchResponseSimplePublicObject,
    BatchResponseSimplePublicObjectWithErrors,
    BatchResponseSimplePublicUpsertObject,
    BatchResponseSimplePublicUpsertObjectWithErrors,
    CollectionResponseAssociatedID,
    CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
    PublicAssociationsForObject,
    PublicMergeInput,
    SimplePublicObjectBatchInput,
    SimplePublicObjectBatchInputForCreate,
    SimplePublicObjectBatchInputUpsert,
    SimplePublicObjectID,
    SimplePublicObjectInput,
    SimplePublicObjectInputForCreate,
    SimplePublicObjectWithAssociations,
    SimplePublicUpsertObject,
)
```

### Calls

Methods:

- <code title="post /crm/objects/2026-03/calls">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">update</a>(call_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/call_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/calls">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">delete</a>(call_id) -> None</code>
- <code title="get /crm/objects/2026-03/calls/{callId}">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">get</a>(call_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/call_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/calls/search">client.crm.objects.calls.<a href="./src/hubspot_sdk/resources/crm/objects/calls/calls.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/call_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/calls/batch/create">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/calls/batch/update">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/calls/batch/archive">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/calls/batch/read">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/calls/batch/upsert">client.crm.objects.calls.batch.<a href="./src/hubspot_sdk/resources/crm/objects/calls/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/calls/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Carts

Methods:

- <code title="post /crm/objects/2026-03/carts">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">update</a>(cart_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/cart_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/carts">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">delete</a>(cart_id) -> None</code>
- <code title="get /crm/objects/2026-03/carts/{cartId}">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">get</a>(cart_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/cart_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/carts/search">client.crm.objects.carts.<a href="./src/hubspot_sdk/resources/crm/objects/carts/carts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/cart_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/carts/batch/create">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/carts/batch/update">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/carts/batch/archive">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/carts/batch/read">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/carts/batch/upsert">client.crm.objects.carts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/carts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/carts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### CommercePayments

Methods:

- <code title="post /crm/objects/2026-03/commerce_payments">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">update</a>(commerce_payment_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/commerce_payments">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">delete</a>(commerce_payment_id) -> None</code>
- <code title="get /crm/objects/2026-03/commerce_payments/{commercePaymentId}">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">get</a>(commerce_payment_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/commerce_payments/search">client.crm.objects.commerce_payments.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/commerce_payments.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payment_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/commerce_payments/batch/create">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/commerce_payments/batch/update">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/commerce_payments/batch/archive">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/commerce_payments/batch/read">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/commerce_payments/batch/upsert">client.crm.objects.commerce_payments.batch.<a href="./src/hubspot_sdk/resources/crm/objects/commerce_payments/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/commerce_payments/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Communications

Methods:

- <code title="post /crm/objects/2026-03/communications">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">update</a>(communication_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/communication_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/communications">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">delete</a>(communication_id) -> None</code>
- <code title="get /crm/objects/2026-03/communications/{communicationId}">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">get</a>(communication_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/communication_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/communications/search">client.crm.objects.communications.<a href="./src/hubspot_sdk/resources/crm/objects/communications/communications.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communication_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/communications/batch/create">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/communications/batch/update">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/communications/batch/archive">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/communications/batch/read">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/communications/batch/upsert">client.crm.objects.communications.batch.<a href="./src/hubspot_sdk/resources/crm/objects/communications/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/communications/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Companies

Methods:

- <code title="post /crm/objects/2026-03/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">update</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/companies">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">delete</a>(company_id) -> None</code>
- <code title="get /crm/objects/2026-03/companies/{companyId}">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">get</a>(company_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/company_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/companies/merge">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/companies/search">client.crm.objects.companies.<a href="./src/hubspot_sdk/resources/crm/objects/companies/companies.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/company_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/companies/batch/create">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/companies/batch/update">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/companies/batch/archive">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/companies/batch/read">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/companies/batch/upsert">client.crm.objects.companies.batch.<a href="./src/hubspot_sdk/resources/crm/objects/companies/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/companies/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Contacts

Types:

```python
from hubspot_sdk.types.crm.objects import PublicGdprDeleteInput
```

Methods:

- <code title="post /crm/objects/2026-03/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">update</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/contacts">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">delete</a>(contact_id) -> None</code>
- <code title="post /crm/objects/2026-03/contacts/gdpr-delete">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">gdpr_delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_gdpr_delete_params.py">params</a>) -> None</code>
- <code title="get /crm/objects/2026-03/contacts/{contactId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">get</a>(contact_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/contacts/merge">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contacts/search">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/contacts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contact_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/contacts/batch/create">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contacts/batch/update">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contacts/batch/archive">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/contacts/batch/read">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contacts/batch/upsert">client.crm.objects.contacts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contacts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contacts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Contracts

Methods:

- <code title="post /crm/objects/2026-03/contracts">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">update</a>(contract_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contract_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/contracts">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">delete</a>(contract_id) -> None</code>
- <code title="get /crm/objects/2026-03/contracts/{contractId}">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">get</a>(contract_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/contract_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/contracts/search">client.crm.objects.contracts.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/contracts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contract_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/contracts/batch/create">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contracts/batch/update">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contracts/batch/archive">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/contracts/batch/read">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/contracts/batch/upsert">client.crm.objects.contracts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/contracts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/contracts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Courses

Methods:

- <code title="post /crm/objects/2026-03/0-410">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">update</a>(course_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/course_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/0-410">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">delete</a>(course_id) -> None</code>
- <code title="get /crm/objects/2026-03/0-410/{courseId}">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">get</a>(course_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/course_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/0-410/search">client.crm.objects.courses.<a href="./src/hubspot_sdk/resources/crm/objects/courses/courses.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/course_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/0-410/batch/create">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-410/batch/update">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-410/batch/archive">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/0-410/batch/read">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-410/batch/upsert">client.crm.objects.courses.batch.<a href="./src/hubspot_sdk/resources/crm/objects/courses/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/courses/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Custom

Methods:

- <code title="post /crm/objects/2026-03/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="get /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">get</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/merge">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">merge</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/search">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom/custom.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/{objectType}/batch/create">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/update">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/archive">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/read">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/upsert">client.crm.objects.custom.batch.<a href="./src/hubspot_sdk/resources/crm/objects/custom/batch.py">upsert</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Deals

Methods:

- <code title="post /crm/objects/2026-03/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">update</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/0-3">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">delete</a>(deal_id) -> None</code>
- <code title="get /crm/objects/2026-03/0-3/{dealId}">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">get</a>(deal_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/deal_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/0-3/merge">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-3/search">client.crm.objects.deals.<a href="./src/hubspot_sdk/resources/crm/objects/deals/deals.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deal_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/0-3/batch/create">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-3/batch/update">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-3/batch/archive">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/0-3/batch/read">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-3/batch/upsert">client.crm.objects.deals.batch.<a href="./src/hubspot_sdk/resources/crm/objects/deals/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/deals/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Discounts

Methods:

- <code title="post /crm/objects/2026-03/discounts">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">update</a>(discount_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/discount_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/discounts">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">delete</a>(discount_id) -> None</code>
- <code title="get /crm/objects/2026-03/discounts/{discountId}">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">get</a>(discount_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/discount_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/discounts/search">client.crm.objects.discounts.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/discounts.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discount_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/discounts/batch/create">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/discounts/batch/update">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/discounts/batch/archive">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/discounts/batch/read">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/discounts/batch/upsert">client.crm.objects.discounts.batch.<a href="./src/hubspot_sdk/resources/crm/objects/discounts/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/discounts/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Emails

Methods:

- <code title="post /crm/objects/2026-03/emails">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/emails">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">delete</a>(email_id) -> None</code>
- <code title="get /crm/objects/2026-03/emails/{emailId}">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">get</a>(email_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/email_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/emails/search">client.crm.objects.emails.<a href="./src/hubspot_sdk/resources/crm/objects/emails/emails.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/email_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/emails/batch/create">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/emails/batch/update">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/emails/batch/archive">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/emails/batch/read">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/emails/batch/upsert">client.crm.objects.emails.batch.<a href="./src/hubspot_sdk/resources/crm/objects/emails/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/emails/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### FeedbackSubmissions

Methods:

- <code title="get /crm/objects/2026-03/feedback_submissions">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="get /crm/objects/2026-03/feedback_submissions/{feedbackSubmissionId}">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">get</a>(feedback_submission_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/feedback_submissions/search">client.crm.objects.feedback_submissions.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/feedback_submissions.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submission_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/feedback_submissions/batch/read">client.crm.objects.feedback_submissions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/feedback_submissions/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/feedback_submissions/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### Fees

Methods:

- <code title="post /crm/objects/2026-03/fees">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">update</a>(fee_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/fee_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/fees">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">delete</a>(fee_id) -> None</code>
- <code title="get /crm/objects/2026-03/fees/{feeId}">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">get</a>(fee_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/fee_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/fees/search">client.crm.objects.fees.<a href="./src/hubspot_sdk/resources/crm/objects/fees/fees.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fee_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/fees/batch/create">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/fees/batch/update">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/fees/batch/archive">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/fees/batch/read">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/fees/batch/upsert">client.crm.objects.fees.batch.<a href="./src/hubspot_sdk/resources/crm/objects/fees/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/fees/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### GoalTargets

Methods:

- <code title="post /crm/objects/2026-03/goal_targets">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">update</a>(goal_target_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/goal_targets">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">delete</a>(goal_target_id) -> None</code>
- <code title="get /crm/objects/2026-03/goal_targets/{goalTargetId}">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">get</a>(goal_target_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/goal_targets/search">client.crm.objects.goal_targets.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/goal_targets.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_target_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/goal_targets/batch/create">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/goal_targets/batch/update">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/goal_targets/batch/archive">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/goal_targets/batch/read">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/goal_targets/batch/upsert">client.crm.objects.goal_targets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/goal_targets/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/goal_targets/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Invoices

Methods:

- <code title="post /crm/objects/2026-03/invoices">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">update</a>(invoice_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/invoices">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">delete</a>(invoice_id) -> None</code>
- <code title="get /crm/objects/2026-03/invoices/{invoiceId}">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">get</a>(invoice_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/invoices/search">client.crm.objects.invoices.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/invoices.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoice_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/invoices/batch/create">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/invoices/batch/update">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/invoices/batch/archive">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/invoices/batch/read">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/invoices/batch/upsert">client.crm.objects.invoices.batch.<a href="./src/hubspot_sdk/resources/crm/objects/invoices/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/invoices/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Leads

Methods:

- <code title="post /crm/objects/2026-03/leads">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">update</a>(leads_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/lead_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/leads">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">delete</a>(leads_id) -> None</code>
- <code title="get /crm/objects/2026-03/leads/{leadsId}">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">get</a>(leads_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/lead_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/leads/search">client.crm.objects.leads.<a href="./src/hubspot_sdk/resources/crm/objects/leads/leads.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/lead_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/leads/batch/create">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/leads/batch/update">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/leads/batch/archive">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/leads/batch/read">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/leads/batch/upsert">client.crm.objects.leads.batch.<a href="./src/hubspot_sdk/resources/crm/objects/leads/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/leads/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### LineItems

Methods:

- <code title="post /crm/objects/2026-03/line_items">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">update</a>(line_item_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/line_items">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">delete</a>(line_item_id) -> None</code>
- <code title="get /crm/objects/2026-03/line_items/{lineItemId}">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">get</a>(line_item_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/line_items/search">client.crm.objects.line_items.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/line_items.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_item_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/line_items/batch/create">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/line_items/batch/update">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/line_items/batch/archive">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/line_items/batch/read">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/line_items/batch/upsert">client.crm.objects.line_items.batch.<a href="./src/hubspot_sdk/resources/crm/objects/line_items/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/line_items/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Listings

Methods:

- <code title="post /crm/objects/2026-03/0-420">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">update</a>(listing_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/listing_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/0-420">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">delete</a>(listing_id) -> None</code>
- <code title="get /crm/objects/2026-03/0-420/{listingId}">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">get</a>(listing_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/listing_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/0-420/search">client.crm.objects.listings.<a href="./src/hubspot_sdk/resources/crm/objects/listings/listings.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listing_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/0-420/batch/create">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-420/batch/update">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-420/batch/archive">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/0-420/batch/read">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-420/batch/upsert">client.crm.objects.listings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/listings/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/listings/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Meetings

Methods:

- <code title="post /crm/objects/2026-03/meetings">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">update</a>(meeting_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/meetings">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">delete</a>(meeting_id) -> None</code>
- <code title="get /crm/objects/2026-03/meetings/{meetingId}">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">get</a>(meeting_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/meetings/search">client.crm.objects.meetings.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/meetings.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meeting_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/meetings/batch/create">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/meetings/batch/update">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/meetings/batch/archive">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/meetings/batch/read">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/meetings/batch/upsert">client.crm.objects.meetings.batch.<a href="./src/hubspot_sdk/resources/crm/objects/meetings/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/meetings/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Notes

Methods:

- <code title="post /crm/objects/2026-03/notes">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">update</a>(note_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/note_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/notes">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">delete</a>(note_id) -> None</code>
- <code title="get /crm/objects/2026-03/notes/{noteId}">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">get</a>(note_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/note_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/notes/search">client.crm.objects.notes.<a href="./src/hubspot_sdk/resources/crm/objects/notes/notes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/note_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/notes/batch/create">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/notes/batch/update">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/notes/batch/archive">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/notes/batch/read">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/notes/batch/upsert">client.crm.objects.notes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/notes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/notes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Objects

Methods:

- <code title="post /crm/objects/2026-03/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/{objectType}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="get /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">get</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/search">client.crm.objects.objects.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/objects_.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/object_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/{objectType}/batch/create">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">create</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/update">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">update</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/archive">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">delete</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/read">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">get</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/upsert">client.crm.objects.objects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/objects_/batch.py">upsert</a>(object*type, \*\*<a href="src/hubspot_sdk/types/crm/objects/objects*/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Orders

Methods:

- <code title="post /crm/objects/2026-03/orders">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">update</a>(order_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/order_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/orders">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">delete</a>(order_id) -> None</code>
- <code title="get /crm/objects/2026-03/orders/{orderId}">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">get</a>(order_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/order_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/orders/search">client.crm.objects.orders.<a href="./src/hubspot_sdk/resources/crm/objects/orders/orders.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/order_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/orders/batch/create">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/orders/batch/update">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/orders/batch/archive">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/orders/batch/read">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/orders/batch/upsert">client.crm.objects.orders.batch.<a href="./src/hubspot_sdk/resources/crm/objects/orders/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/orders/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### PartnerClients

Methods:

- <code title="patch /crm/objects/2026-03/partner_clients/{partnerClientId}">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">update</a>(partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/partner_clients">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="get /crm/objects/2026-03/partner_clients/{partnerClientId}">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">get</a>(partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="get /crm/objects/2026-03/partner_clients/{partnerClientId}/associations/{toObjectType}">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">list_associations</a>(to_object_type, \*, partner_client_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_list_associations_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/multi_associated_object_with_label.py">SyncPage[MultiAssociatedObjectWithLabel]</a></code>
- <code title="post /crm/objects/2026-03/partner_clients/search">client.crm.objects.partner_clients.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/partner_clients.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_client_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/partner_clients/batch/update">client.crm.objects.partner_clients.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_clients/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="put /crm/objects/2026-03/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}">client.crm.objects.partner_clients.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/batch.py">create_default_association</a>(to_object_id, \*, from_object_type, from_object_id, to_object_type) -> <a href="./src/hubspot_sdk/types/crm/batch_response_public_default_association.py">BatchResponsePublicDefaultAssociation</a></code>
- <code title="post /crm/objects/2026-03/partner_clients/batch/read">client.crm.objects.partner_clients.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_clients/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_clients/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### PartnerServices

Methods:

- <code title="patch /crm/objects/2026-03/partner_services/{partnerServiceId}">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">update</a>(partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/partner_services/{partnerServiceId}/associations/{toObjectType}">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">list</a>(to_object_type, \*, partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/multi_associated_object_with_label.py">SyncPage[MultiAssociatedObjectWithLabel]</a></code>
- <code title="get /crm/objects/2026-03/partner_services/{partnerServiceId}">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">get</a>(partner_service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/partner_services/search">client.crm.objects.partner_services.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/partner_services.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_service_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/partner_services/batch/update">client.crm.objects.partner_services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_services/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/partner_services/batch/read">client.crm.objects.partner_services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/partner_services/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/partner_services/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>

### PostalMail

Methods:

- <code title="post /crm/objects/2026-03/postal_mail">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">update</a>(postal_mail_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/postal_mail">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">delete</a>(postal_mail_id) -> None</code>
- <code title="get /crm/objects/2026-03/postal_mail/{postalMailId}">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">get</a>(postal_mail_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/postal_mail/search">client.crm.objects.postal_mail.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/postal_mail.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/postal_mail/batch/create">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/postal_mail/batch/update">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/postal_mail/batch/archive">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/postal_mail/batch/read">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/postal_mail/batch/upsert">client.crm.objects.postal_mail.batch.<a href="./src/hubspot_sdk/resources/crm/objects/postal_mail/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/postal_mail/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Products

Methods:

- <code title="post /crm/objects/2026-03/products">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">update</a>(product_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/product_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/products">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">delete</a>(product_id) -> None</code>
- <code title="get /crm/objects/2026-03/products/{productId}">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">get</a>(product_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/product_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/products/search">client.crm.objects.products.<a href="./src/hubspot_sdk/resources/crm/objects/products/products.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/product_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/products/batch/create">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/products/batch/update">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/products/batch/archive">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/products/batch/read">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/products/batch/upsert">client.crm.objects.products.batch.<a href="./src/hubspot_sdk/resources/crm/objects/products/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/products/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Projects

Methods:

- <code title="post /crm/objects/2026-03/projects">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">update</a>(project_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/project_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/projects">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">delete</a>(project_id) -> None</code>
- <code title="get /crm/objects/2026-03/projects/{projectId}">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">get</a>(project_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/project_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/projects/merge">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/projects/search">client.crm.objects.projects.<a href="./src/hubspot_sdk/resources/crm/objects/projects/projects.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/project_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/projects/batch/create">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/projects/batch/update">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/projects/batch/archive">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/projects/batch/read">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/projects/batch/upsert">client.crm.objects.projects.batch.<a href="./src/hubspot_sdk/resources/crm/objects/projects/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/projects/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Quotes

Methods:

- <code title="post /crm/objects/2026-03/quotes">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">update</a>(quote_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/quote_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/quotes">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">delete</a>(quote_id) -> None</code>
- <code title="get /crm/objects/2026-03/quotes/{quoteId}">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">get</a>(quote_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/quote_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/quotes/search">client.crm.objects.quotes.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/quotes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quote_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/quotes/batch/create">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/quotes/batch/update">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/quotes/batch/archive">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/quotes/batch/read">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/quotes/batch/upsert">client.crm.objects.quotes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/quotes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/quotes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Services

Methods:

- <code title="post /crm/objects/2026-03/0-162">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">update</a>(service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/service_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/0-162">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">delete</a>(service_id) -> None</code>
- <code title="get /crm/objects/2026-03/0-162/{serviceId}">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">get</a>(service_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/service_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/0-162/search">client.crm.objects.services.<a href="./src/hubspot_sdk/resources/crm/objects/services/services.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/service_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/0-162/batch/create">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-162/batch/update">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-162/batch/archive">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/0-162/batch/read">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/0-162/batch/upsert">client.crm.objects.services.batch.<a href="./src/hubspot_sdk/resources/crm/objects/services/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/services/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Subscriptions

Methods:

- <code title="post /crm/objects/2026-03/subscriptions">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscription_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/subscriptions/{subscriptionId}">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">update</a>(subscription_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/subscription_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/subscriptions">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscription_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/subscriptions/{subscriptionId}">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">delete</a>(subscription_id) -> None</code>
- <code title="get /crm/objects/2026-03/subscriptions/{subscriptionId}">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">get</a>(subscription_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/subscription_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/subscriptions/search">client.crm.objects.subscriptions.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/subscriptions.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscription_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/subscriptions/batch/create">client.crm.objects.subscriptions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscriptions/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/subscriptions/batch/update">client.crm.objects.subscriptions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscriptions/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/subscriptions/batch/archive">client.crm.objects.subscriptions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscriptions/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/subscriptions/batch/read">client.crm.objects.subscriptions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscriptions/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/subscriptions/batch/upsert">client.crm.objects.subscriptions.batch.<a href="./src/hubspot_sdk/resources/crm/objects/subscriptions/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/subscriptions/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Tasks

Methods:

- <code title="post /crm/objects/2026-03/tasks">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">update</a>(task_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/task_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/tasks">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">delete</a>(task_id) -> None</code>
- <code title="get /crm/objects/2026-03/tasks/{taskId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">get</a>(task_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/task_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/tasks/search">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/task_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/tasks/batch/create">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tasks/batch/update">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tasks/batch/archive">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/tasks/batch/read">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tasks/batch/upsert">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Taxes

Methods:

- <code title="post /crm/objects/2026-03/taxes">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">update</a>(tax_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/tax_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/taxes">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">delete</a>(tax_id) -> None</code>
- <code title="get /crm/objects/2026-03/taxes/{taxId}">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">get</a>(tax_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/tax_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/taxes/search">client.crm.objects.taxes.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/taxes.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tax_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/taxes/batch/create">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/taxes/batch/update">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/taxes/batch/archive">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/taxes/batch/read">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/taxes/batch/upsert">client.crm.objects.taxes.batch.<a href="./src/hubspot_sdk/resources/crm/objects/taxes/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/taxes/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Tickets

Methods:

- <code title="post /crm/objects/2026-03/tickets">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">update</a>(ticket_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/tickets">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">delete</a>(ticket_id) -> None</code>
- <code title="get /crm/objects/2026-03/tickets/{ticketId}">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">get</a>(ticket_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/tickets/merge">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">merge</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tickets/search">client.crm.objects.tickets.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/tickets.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/ticket_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/tickets/batch/create">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tickets/batch/update">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tickets/batch/archive">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/tickets/batch/read">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/tickets/batch/upsert">client.crm.objects.tickets.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tickets/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/tickets/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Users

Methods:

- <code title="post /crm/objects/2026-03/users">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/users/{userId}">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">update</a>(user_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/user_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/users">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/users/{userId}">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">delete</a>(user_id) -> None</code>
- <code title="get /crm/objects/2026-03/users/{userId}">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">get</a>(user_id, \*\*<a href="src/hubspot_sdk/types/crm/objects/user_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/users/search">client.crm.objects.users.<a href="./src/hubspot_sdk/resources/crm/objects/users/users.py">search</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/user_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/users/batch/create">client.crm.objects.users.batch.<a href="./src/hubspot_sdk/resources/crm/objects/users/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/users/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/users/batch/update">client.crm.objects.users.batch.<a href="./src/hubspot_sdk/resources/crm/objects/users/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/users/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/users/batch/archive">client.crm.objects.users.batch.<a href="./src/hubspot_sdk/resources/crm/objects/users/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/users/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/users/batch/read">client.crm.objects.users.batch.<a href="./src/hubspot_sdk/resources/crm/objects/users/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/users/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/users/batch/upsert">client.crm.objects.users.batch.<a href="./src/hubspot_sdk/resources/crm/objects/users/batch.py">upsert</a>(\*\*<a href="src/hubspot_sdk/types/crm/objects/users/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

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

- <code title="get /crm/owners/2026-03">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">list</a>(\*\*<a href="src/hubspot_sdk/types/crm/owner_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">SyncPage[PublicOwner]</a></code>
- <code title="get /crm/owners/2026-03/{ownerId}">client.crm.owners.<a href="./src/hubspot_sdk/resources/crm/owners.py">get</a>(owner_id, \*\*<a href="src/hubspot_sdk/types/crm/owner_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/public_owner.py">PublicOwner</a></code>

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
    PipelineReplaceInput,
    PipelineStage,
    PipelineStageInput,
    PipelineStagePatchInput,
    PipelineStageReplaceInput,
    PublicAuditInfo,
)
```

Methods:

- <code title="post /crm/pipelines/2026-03/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="patch /crm/pipelines/2026-03/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="get /crm/pipelines/2026-03/{objectType}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list</a>(object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_pipeline_no_paging.py">CollectionResponsePipelineNoPaging</a></code>
- <code title="delete /crm/pipelines/2026-03/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">delete</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">create_stage</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_create_stage_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="delete /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">delete_stage</a>(stage_id, \*, object_type, pipeline_id) -> None</code>
- <code title="get /crm/pipelines/2026-03/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">get</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="get /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">get_stage</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="get /crm/pipelines/2026-03/{objectType}/{pipelineId}/audit">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list_audit</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_audit_info_no_paging.py">CollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="get /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages/{stageId}/audit">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list_stage_audit</a>(stage_id, \*, object_type, pipeline_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_audit_info_no_paging.py">CollectionResponsePublicAuditInfoNoPaging</a></code>
- <code title="get /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">list_stages</a>(pipeline_id, \*, object_type) -> <a href="./src/hubspot_sdk/types/crm/collection_response_pipeline_stage_no_paging.py">CollectionResponsePipelineStageNoPaging</a></code>
- <code title="put /crm/pipelines/2026-03/{objectType}/{pipelineId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update_all_properties</a>(pipeline_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_all_properties_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline.py">Pipeline</a></code>
- <code title="patch /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update_stage</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_stage_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>
- <code title="put /crm/pipelines/2026-03/{objectType}/{pipelineId}/stages/{stageId}">client.crm.pipelines.<a href="./src/hubspot_sdk/resources/crm/pipelines.py">update_stage_all_properties</a>(stage_id, \*, object_type, pipeline_id, \*\*<a href="src/hubspot_sdk/types/crm/pipeline_update_stage_all_properties_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/pipeline_stage.py">PipelineStage</a></code>

## Properties

Types:

```python
from hubspot_sdk.types.crm import (
    BatchInputPropertyCreate,
    BatchResponseProperty,
    BatchResponsePropertyWithErrors,
    CollectionResponsePropertyNoPaging,
    PropertyCreate,
    PropertyUpdate,
)
```

Methods:

- <code title="post /crm/properties/2026-03/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property.py">Property</a></code>
- <code title="patch /crm/properties/2026-03/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">update</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property.py">Property</a></code>
- <code title="get /crm/properties/2026-03/{objectType}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_property_no_paging.py">CollectionResponsePropertyNoPaging</a></code>
- <code title="delete /crm/properties/2026-03/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">delete</a>(property_name, \*, object_type) -> None</code>
- <code title="get /crm/properties/2026-03/{objectType}/{propertyName}">client.crm.properties.<a href="./src/hubspot_sdk/resources/crm/properties/properties.py">get</a>(property_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/property_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/property.py">Property</a></code>

### Batch

Methods:

- <code title="post /crm/properties/2026-03/{objectType}/batch/create">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_property.py">BatchResponseProperty</a></code>
- <code title="post /crm/properties/2026-03/{objectType}/batch/archive">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/properties/2026-03/{objectType}/batch/read">client.crm.properties.batch.<a href="./src/hubspot_sdk/resources/crm/properties/batch.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_property.py">BatchResponseProperty</a></code>

### Groups

Methods:

- <code title="post /crm/properties/2026-03/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="patch /crm/properties/2026-03/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">update</a>(group_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>
- <code title="get /crm/properties/2026-03/{objectType}/groups">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/collection_response_property_group_no_paging.py">CollectionResponsePropertyGroupNoPaging</a></code>
- <code title="delete /crm/properties/2026-03/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">delete</a>(group_name, \*, object_type) -> None</code>
- <code title="get /crm/properties/2026-03/{objectType}/groups/{groupName}">client.crm.properties.groups.<a href="./src/hubspot_sdk/resources/crm/properties/groups.py">get</a>(group_name, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/properties/group_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/property_group.py">PropertyGroup</a></code>

## PropertiesValidations

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

- <code title="get /crm/property-validations/2026-03/{objectTypeId}">client.crm.properties_validations.<a href="./src/hubspot_sdk/resources/crm/properties_validations.py">get_by_object_type_id</a>(object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_property_validation_rule_map_no_paging.py">CollectionResponsePublicPropertyValidationRuleMapNoPaging</a></code>
- <code title="get /crm/property-validations/2026-03/{objectTypeId}/{propertyName}">client.crm.properties_validations.<a href="./src/hubspot_sdk/resources/crm/properties_validations.py">get_by_object_type_id_and_property_name</a>(property_name, \*, object_type_id) -> <a href="./src/hubspot_sdk/types/crm/collection_response_public_property_validation_rule_no_paging.py">CollectionResponsePublicPropertyValidationRuleNoPaging</a></code>
- <code title="get /crm/property-validations/2026-03/{objectTypeId}/{propertyName}/rule-type/{ruleType}">client.crm.properties_validations.<a href="./src/hubspot_sdk/resources/crm/properties_validations.py">get_by_object_type_id_property_name_and_rule_type</a>(rule_type, \*, object_type_id, property_name) -> <a href="./src/hubspot_sdk/types/crm/public_property_validation_rule.py">PublicPropertyValidationRule</a></code>
- <code title="put /crm/property-validations/2026-03/{objectTypeId}/{propertyName}/rule-type/{ruleType}">client.crm.properties_validations.<a href="./src/hubspot_sdk/resources/crm/properties_validations.py">update_by_object_type_id_property_name_and_rule_type</a>(rule_type, \*, object_type_id, property_name, \*\*<a href="src/hubspot_sdk/types/crm/properties_validation_update_by_object_type_id_property_name_and_rule_type_params.py">params</a>) -> None</code>

## Timeline

Types:

```python
from hubspot_sdk.types.crm import (
    AppEventOccurrence,
    AppEventResolutionResponse,
    BatchInputAppEventOccurrence,
    BatchResponseAppEventOccurrence,
    DeveloperQualifiedSymbol,
    ExternalAppEventResolutionRequest,
    TimelineEventIFrame,
)
```

Methods:

- <code title="post /integrators/timeline/2026-03/events">client.crm.timeline.<a href="./src/hubspot_sdk/resources/crm/timeline/timeline.py">create_event</a>(\*\*<a href="src/hubspot_sdk/types/crm/timeline_create_event_params.py">params</a>) -> None</code>
- <code title="post /integrators/timeline/2026-03/types/projects">client.crm.timeline.<a href="./src/hubspot_sdk/resources/crm/timeline/timeline.py">create_project_type</a>(\*\*<a href="src/hubspot_sdk/types/crm/timeline_create_project_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/app_event_resolution_response.py">AppEventResolutionResponse</a></code>

### Batch

Methods:

- <code title="post /integrators/timeline/2026-03/events/batch">client.crm.timeline.batch.<a href="./src/hubspot_sdk/resources/crm/timeline/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/crm/timeline/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_app_event_occurrence.py">BatchResponseAppEventOccurrence</a></code>
