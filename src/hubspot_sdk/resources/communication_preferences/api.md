# CommunicationPreferences

Types:

```python
from hubspot_sdk.types.communication_preferences import (
    ActionResponseWithResultsPublicStatus,
    ActionResponseWithResultsPublicWideStatus,
    ActionResponseWithResultsSubscriptionDefinition,
    BatchInputPublicStatusRequest,
    BatchResponsePublicBulkOptOutFromAllResponse,
    BatchResponsePublicStatus,
    BatchResponsePublicStatusBulkResponse,
    BatchResponsePublicWideStatusBulkResponse,
    LinkGenerationRequest,
    LinkGenerationResponse,
    PartialPublicStatusRequest,
    PublicBulkOptOutFromAllResponse,
    PublicStatus,
    PublicStatusBulkResponse,
    PublicStatusRequest,
    PublicSubscriptionStatus,
    PublicSubscriptionStatusesResponse,
    PublicSubscriptionTranslation,
    PublicUpdateSubscriptionStatusRequest,
    PublicWideStatus,
    PublicWideStatusBulkResponse,
    SubscriptionDefinition,
)
```

Methods:

- <code title="post /communication-preferences/2026-03/links/generate">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">generate_links</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_generate_links_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/link_generation_response.py">LinkGenerationResponse</a></code>
- <code title="get /communication-preferences/2026-03/status/email/{emailAddress}">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">get_status_by_email</a>(email_address) -> <a href="./src/hubspot_sdk/types/communication_preferences/public_subscription_statuses_response.py">PublicSubscriptionStatusesResponse</a></code>
- <code title="get /communication-preferences/2026-03/statuses/{subscriberIdString}">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">get_statuses</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_get_statuses_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="get /communication-preferences/2026-03/statuses/{subscriberIdString}/unsubscribe-all">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">get_unsubscribe_all_status</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_get_unsubscribe_all_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/action_response_with_results_public_wide_status.py">ActionResponseWithResultsPublicWideStatus</a></code>
- <code title="post /communication-preferences/2026-03/subscribe">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">subscribe</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_subscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/public_subscription_status.py">PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/2026-03/unsubscribe">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">unsubscribe</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_unsubscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/public_subscription_status.py">PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/2026-03/statuses/{subscriberIdString}/unsubscribe-all">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">unsubscribe_all</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="post /communication-preferences/2026-03/statuses/{subscriberIdString}">client.communication_preferences.<a href="./src/hubspot_sdk/resources/communication_preferences/communication_preferences.py">update_status</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/communication_preferences/communication_preference_update_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>

## Definitions

Methods:

- <code title="get /communication-preferences/2026-03/definitions">client.communication_preferences.definitions.<a href="./src/hubspot_sdk/resources/communication_preferences/definitions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/action_response_with_results_subscription_definition.py">ActionResponseWithResultsSubscriptionDefinition</a></code>

## Statuses

### Batch

Methods:

- <code title="post /communication-preferences/2026-03/statuses/batch/unsubscribe-all/read">client.communication_preferences.statuses.batch.<a href="./src/hubspot_sdk/resources/communication_preferences/statuses/batch.py">get_unsubscribe_all_statuses</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/statuses/batch_get_unsubscribe_all_statuses_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/batch_response_public_wide_status_bulk_response.py">BatchResponsePublicWideStatusBulkResponse</a></code>
- <code title="post /communication-preferences/2026-03/statuses/batch/read">client.communication_preferences.statuses.batch.<a href="./src/hubspot_sdk/resources/communication_preferences/statuses/batch.py">read</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/statuses/batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/batch_response_public_status_bulk_response.py">BatchResponsePublicStatusBulkResponse</a></code>
- <code title="post /communication-preferences/2026-03/statuses/batch/unsubscribe-all">client.communication_preferences.statuses.batch.<a href="./src/hubspot_sdk/resources/communication_preferences/statuses/batch.py">unsubscribe_all</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/statuses/batch_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/batch_response_public_bulk_opt_out_from_all_response.py">BatchResponsePublicBulkOptOutFromAllResponse</a></code>
- <code title="post /communication-preferences/2026-03/statuses/batch/write">client.communication_preferences.statuses.batch.<a href="./src/hubspot_sdk/resources/communication_preferences/statuses/batch.py">update_statuses</a>(\*\*<a href="src/hubspot_sdk/types/communication_preferences/statuses/batch_update_statuses_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/communication_preferences/batch_response_public_status.py">BatchResponsePublicStatus</a></code>
