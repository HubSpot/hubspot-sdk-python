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
