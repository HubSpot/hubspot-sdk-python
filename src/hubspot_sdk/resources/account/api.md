# Account

## Activity

Types:

```python
from hubspot_sdk.types.account import (
    ActingUser,
    APIUsage,
    CollectionResponseAPIUsageNoPaging,
    CollectionResponseHydratedCriticalActionForwardPaging,
    CollectionResponsePublicAPIUserActionEventForwardPaging,
    CollectionResponsePublicLoginAuditForwardPaging,
    HydratedCriticalAction,
    PortalInformationResponse,
    PublicAPIUserActionEvent,
    PublicLoginAudit,
)
```

Methods:

- <code title="get /account-info/2026-03/activity/audit-logs">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_audit_logs</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_audit_logs_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_api_user_action_event.py">SyncPage[PublicAPIUserActionEvent]</a></code>
- <code title="get /account-info/2026-03/activity/login">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_login_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_login_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/public_login_audit.py">SyncPage[PublicLoginAudit]</a></code>
- <code title="get /account-info/2026-03/activity/security">client.account.activity.<a href="./src/hubspot_sdk/resources/account/activity.py">list_security_activities</a>(\*\*<a href="src/hubspot_sdk/types/account/activity_list_security_activities_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/account/hydrated_critical_action.py">SyncPage[HydratedCriticalAction]</a></code>
