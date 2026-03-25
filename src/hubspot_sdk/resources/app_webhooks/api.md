# AppWebhooks

Types:

```python
from hubspot_sdk.types.app_webhooks import (
    BatchInputSubscriptionBatchUpdateRequest,
    BatchResponseSubscriptionResponse,
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

Methods:

- <code title="post /app-webhooks/2026-03/{appId}/subscriptions/batch/update">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">batch_update_subscriptions</a>(app_id, \*\*<a href="src/hubspot_sdk/types/app_webhooks/app_webhook_batch_update_subscriptions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/app_webhooks/batch_response_subscription_response.py">BatchResponseSubscriptionResponse</a></code>
- <code title="post /app-webhooks/2026-03/{appId}/subscriptions">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">create_subscription</a>(app_id, \*\*<a href="src/hubspot_sdk/types/app_webhooks/app_webhook_create_subscription_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/app_webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="delete /app-webhooks/2026-03/{appId}/settings">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">delete_settings</a>(app_id) -> None</code>
- <code title="delete /app-webhooks/2026-03/{appId}/subscriptions/{subscriptionId}">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">delete_subscription</a>(subscription_id, \*, app_id) -> None</code>
- <code title="get /app-webhooks/2026-03/{appId}/settings">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">get_settings</a>(app_id) -> <a href="./src/hubspot_sdk/types/crm/extensions/settings_response.py">SettingsResponse</a></code>
- <code title="get /app-webhooks/2026-03/{appId}/subscriptions/{subscriptionId}">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">get_subscription</a>(subscription_id, \*, app_id) -> <a href="./src/hubspot_sdk/types/app_webhooks/subscription_response.py">SubscriptionResponse</a></code>
- <code title="get /app-webhooks/2026-03/{appId}/subscriptions">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">list_subscriptions</a>(app_id) -> <a href="./src/hubspot_sdk/types/app_webhooks/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="put /app-webhooks/2026-03/{appId}/settings">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">update_settings</a>(app_id, \*\*<a href="src/hubspot_sdk/types/app_webhooks/app_webhook_update_settings_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/extensions/settings_response.py">SettingsResponse</a></code>
- <code title="patch /app-webhooks/2026-03/{appId}/subscriptions/{subscriptionId}">client.app_webhooks.<a href="./src/hubspot_sdk/resources/app_webhooks/app_webhooks.py">update_subscription</a>(subscription_id, \*, app_id, \*\*<a href="src/hubspot_sdk/types/app_webhooks/app_webhook_update_subscription_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/app_webhooks/subscription_response.py">SubscriptionResponse</a></code>
