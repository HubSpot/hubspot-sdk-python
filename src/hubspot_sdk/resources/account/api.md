# Account

Types:

```python
from hubspot_sdk.types.account import (
    APIUsage,
    CollectionResponseAPIUsage,
    PortalInformationResponse,
)
```

## Activity

Types:

```python
from hubspot_sdk.types.account import (
    ActingUser,
    CollectionResponseHydratedCriticalActionForwardPaging,
    CollectionResponsePublicAPIUserActionEventForwardPaging,
    CollectionResponsePublicLoginAuditForwardPaging,
    HydratedCriticalAction,
    PublicAPIUserActionEvent,
    PublicLoginAudit,
)
```

Methods:

- <code title="get /account-info/v3/activity/audit-logs">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_audit_logs</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_audit_logs_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_api_user_action_event.py">SyncPage[PublicAPIUserActionEvent]</a></code>
- <code title="get /account-info/v3/activity/login">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_login_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_login_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_login_audit.py">SyncPage[PublicLoginAudit]</a></code>
- <code title="get /account-info/v3/activity/security">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_security_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_security_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/hydrated_critical_action.py">SyncPage[HydratedCriticalAction]</a></code>

## Details

Methods:

- <code title="get /account-info/v3/details">client.account.details.<a href="./src/hubspot_sdk/resources/account/details.py">get</a>() -> <a href="./src/hubspot_sdk/types/account/portal_information_response.py">PortalInformationResponse</a></code>

## Usage

Methods:

- <code title="get /account-info/v3/api-usage/daily/private-apps">client.account.usage.<a href="./src/hubspot_sdk/resources/account/usage.py">get_daily_private_apps_usage</a>() -> <a href="./src/hubspot_sdk/types/account/collection_response_api_usage.py">CollectionResponseAPIUsage</a></code>
