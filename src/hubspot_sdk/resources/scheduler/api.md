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
