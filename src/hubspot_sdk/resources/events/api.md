# Events

## Send

Types:

```python
from hubspot_sdk.types.events import (
    AbsoluteComparativeTimestampRefineBy,
    AbsoluteRangedTimestampRefineBy,
    AllHistoryRefineBy,
    AllPropertyTypesOperation,
    AssociationDefinition,
    BatchedBehavioralEventHTTPCompletionRequest,
    BehavioralEventHTTPCompletionRequest,
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
    Option,
    OptionInput,
    Property,
    PropertyFilter,
    PropertyFilterContext,
    PropertyModificationMetadata,
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

- <code title="post /events/custom/2026-03/event-definitions">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">create_event_definition</a>(\*\*<a href="src/hubspot_sdk/types/events/send_create_event_definition_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="post /events/custom/2026-03/event-definitions/{eventName}/property">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">create_event_definition_property</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/send_create_event_definition_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/property.py">Property</a></code>
- <code title="delete /events/custom/2026-03/event-definitions/{eventName}">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">delete_event_definition</a>(event_name) -> None</code>
- <code title="delete /events/custom/2026-03/event-definitions/{eventName}/property/{propertyName}">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">delete_event_definition_property</a>(property_name, \*, event_name) -> None</code>
- <code title="get /events/custom/2026-03/event-definitions/{eventName}">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">get_event_definition</a>(event_name) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="get /events/custom/2026-03/event-definitions">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">list_event_definitions</a>(\*\*<a href="src/hubspot_sdk/types/events/send_list_event_definitions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">SyncPage[ExternalBehavioralEventTypeDefinition]</a></code>
- <code title="post /events/custom/2026-03/send">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">send_event</a>(\*\*<a href="src/hubspot_sdk/types/events/send_send_event_params.py">params</a>) -> None</code>
- <code title="post /events/custom/2026-03/send/batch">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">send_event_batch</a>(\*\*<a href="src/hubspot_sdk/types/events/send_send_event_batch_params.py">params</a>) -> None</code>
- <code title="patch /events/custom/2026-03/event-definitions/{eventName}">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">update_event_definition</a>(event_name, \*\*<a href="src/hubspot_sdk/types/events/send_update_event_definition_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/external_behavioral_event_type_definition.py">ExternalBehavioralEventTypeDefinition</a></code>
- <code title="patch /events/custom/2026-03/event-definitions/{eventName}/property/{propertyName}">client.events.send.<a href="./src/hubspot_sdk/resources/events/send.py">update_event_definition_property</a>(property_name, \*, event_name, \*\*<a href="src/hubspot_sdk/types/events/send_update_event_definition_property_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/events/property.py">Property</a></code>
