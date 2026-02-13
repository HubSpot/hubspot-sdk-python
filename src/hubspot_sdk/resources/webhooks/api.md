# Webhooks

Types:

```python
from hubspot_sdk.types.webhooks import (
    BatchInputSubscriptionBatchUpdateRequest,
    BatchResponseSubscriptionResponse,
    BatchResponseSubscriptionResponseWithErrors,
    SettingsChangeRequest,
    SettingsResponse,
    SubscriptionBatchUpdateRequest,
    SubscriptionCreateRequest,
    SubscriptionListResponse,
    SubscriptionPatchRequest,
    SubscriptionResponse,
    ThrottlingSettings,
)
```

## Settings

Methods:

- <code title="put /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/setting_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="get /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks/settings_response.py">SettingsResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/settings">client.webhooks.settings.<a href="./src/hubspot_sdk/resources/webhooks/settings.py">delete</a>(app_id) -> None</code>

## Subscriptions

Methods:

- <code title="post /webhooks/v3/{appId}/subscriptions">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">create</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="patch /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">update</a>(subscription_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="get /webhooks/v3/{appId}/subscriptions">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">list</a>(app_id) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">delete</a>(subscription_id, \*, app_id) -> None</code>
- <code title="get /webhooks/v3/{appId}/subscriptions/{subscriptionId}">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">get</a>(subscription_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="post /webhooks/v3/{appId}/subscriptions/batch/update">client.webhooks.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks/subscriptions.py">update_batch</a>(app_id, \*\*<a href="src/hubspot_sdk/types/webhooks/subscription_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks/batch_response_subscription_response.py">BatchResponseSubscriptionResponse</a></code>
