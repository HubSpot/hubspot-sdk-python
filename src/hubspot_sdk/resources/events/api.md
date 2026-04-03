# Events

Types:

```python
from hubspot_sdk.types.events import (
    BatchedBehavioralEventHTTPCompletionRequest,
    BehavioralEventHTTPCompletionRequest,
)
```

## Definitions

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
    CollectionResponseWithTotalExternalBehavioralEventTypeDefinition,
    ComboEventRule,
    ComboEventRuleBranch,
    ComparativeBoolPropertyOperation,
    ComparativeDatePropertyOperation,
    ComparativeNumberPropertyOperation,
    ComparativePropertyUpdatedOperation,
    ComparativeStringPropertyOperation,
    DatePoint,
    DatePropertyOperation,
    DateTimePropertyOperation,
    EnumerationPropertyOperation,
    ExternalBehavioralEventPropertyCreate,
    ExternalBehavioralEventPropertyDefinitionPatch,
    ExternalBehavioralEventTypeDefinition,
    ExternalBehavioralEventTypeDefinitionEgg,
    ExternalBehavioralEventTypeDefinitionPatch,
    ExternalObjectResolutionMappingRequest,
    ExternalObjectResolutionMappingResponse,
    ExternalPrimaryObjectResolutionRule,
    FiscalQuarter,
    FiscalYear,
    IndexOffset,
    IndexedTimePoint,
    MonthReference,
    MultiStringPropertyOperation,
    NowReference,
    NumOccurrencesRefineBy,
    NumberPropertyOperation,
    Property,
    PropertyFilter,
    PropertyFilterContext,
    PropertyReferencedTime,
    QuarterReference,
    RangedDatePropertyOperation,
    RangedNumberPropertyOperation,
    RangedTimeOperation,
    RegexPropertyOperation,
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

- <code title="post /events/2026-03/event-definitions">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">create</a>(\*\*<a href="src/hubspot_sdk/types/events/definition_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="patch /events/2026-03/event-definitions/{eventName}">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">update</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/definition_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="get /events/2026-03/event-definitions">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/events/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">SyncPage[ExternalBehavioralEventTypeDefinition]</a></code>
- <code title="delete /events/2026-03/event-definitions/{eventName}">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">delete</a>(event_name) -> None</code>
- <code title="post /events/2026-03/event-definitions/{eventName}/property">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">create_property</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/definition_create_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/property.py">Property</a></code>
- <code title="delete /events/2026-03/event-definitions/{eventName}/property/{propertyName}">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">delete_property</a>(property_name, \*, event_name) -> None</code>
- <code title="get /events/2026-03/event-definitions/{eventName}">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">get</a>(event_name) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="post /events/2026-03/send/batch">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">send_batch</a>(\*\*<a href="src/hubspot_sdk/types/events/definition_send_batch_params.py">params</a>) -> None</code>
- <code title="patch /events/2026-03/event-definitions/{eventName}/property/{propertyName}">client.events.definitions.<a href="./src/hubspot_sdk/resources/events/definitions.py">update_property</a>(property_name, \*, event_name, \*\*<a href="src/hubspot_sdk/types/events/definition_update_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/property.py">Property</a></code>

## Occurrences

Types:

```python
from hubspot_sdk.types.events import (
    CollectionResponseExternalUnifiedEvent,
    ExternalUnifiedEvent,
    VisibleExternalEventTypeNames,
)
```

Methods:

- <code title="get /events/event-occurrences/2026-03">client.events.occurrences.<a href="./src/hubspot_sdk/resources/events/occurrences.py">list</a>(\*\*<a href="src/hubspot_sdk/types/events/occurrence_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_unified_event.py">SyncPage[ExternalUnifiedEvent]</a></code>
- <code title="get /events/event-occurrences/2026-03/event-types">client.events.occurrences.<a href="./src/hubspot_sdk/resources/events/occurrences.py">list_event_types</a>() -> <a href="./src/hubspot_sdk/types/events/visible_external_event_type_names.py">VisibleExternalEventTypeNames</a></code>

## Send

Methods:

- <code title="post /events/2026-03/send/batch">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">batch_send</a>(\*\*<a href="src/hubspot_sdk/types/events/send_batch_send_params.py">params</a>) -> None</code>
- <code title="post /events/2026-03/send">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">send</a>(\*\*<a href="src/hubspot_sdk/types/events/send_send_params.py">params</a>) -> None</code>
