# WebhooksJournal

Types:

```python
from hubspot_sdk.types.webhooks_journal import (
    JournalCollectionResponseSubscriptionResponseNoPaging,
    JournalSubscriptionResponse,
)
```

## Journal

Methods:

- <code title="get /webhooks-journal/journal/2026-03/earliest">client.webhooks_journal.journal.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/journal.py">get_earliest</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_get_earliest_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /webhooks-journal/journal/2026-03/offset/{offset}/next">client.webhooks_journal.journal.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/journal.py">get_next_from_offset</a>(offset, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_get_next_from_offset_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /webhooks-journal/journal/2026-03/status/{statusId}">client.webhooks_journal.journal.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/journal.py">get_status</a>(status_id) -> <a href="./src/hubspot_sdk/types/shared/snapshot_status_response.py">SnapshotStatusResponse</a></code>

### Batch

Methods:

- <code title="post /webhooks-journal/journal/2026-03/batch/read">client.webhooks_journal.journal.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>
- <code title="get /webhooks-journal/journal/2026-03/batch/earliest/{count}">client.webhooks_journal.journal.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/batch.py">get_earliest</a>(count, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal/batch_get_earliest_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>
- <code title="get /webhooks-journal/journal/2026-03/batch/{offset}/next/{count}">client.webhooks_journal.journal.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/batch.py">get_from_offset</a>(count, \*, offset, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal/batch_get_from_offset_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>
- <code title="get /webhooks-journal/journal/2026-03/batch/latest/{count}">client.webhooks_journal.journal.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal/batch.py">get_latest</a>(count, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal/batch_get_latest_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>

## JournalLocal

Methods:

- <code title="get /webhooks-journal/journal-local/2026-03/earliest">client.webhooks_journal.journal_local.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/journal_local.py">get_earliest</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local_get_earliest_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /webhooks-journal/journal/2026-03/latest">client.webhooks_journal.journal_local.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/journal_local.py">get_latest</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local_get_latest_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /webhooks-journal/journal-local/2026-03/offset/{offset}/next">client.webhooks_journal.journal_local.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/journal_local.py">get_next_from_offset</a>(offset, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local_get_next_from_offset_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /webhooks-journal/journal-local/2026-03/status/{statusId}">client.webhooks_journal.journal_local.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/journal_local.py">get_status</a>(status_id) -> <a href="./src/hubspot_sdk/types/shared/snapshot_status_response.py">SnapshotStatusResponse</a></code>

### Batch

Methods:

- <code title="post /webhooks-journal/journal-local/2026-03/batch/read">client.webhooks_journal.journal_local.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>
- <code title="get /webhooks-journal/journal-local/2026-03/batch/earliest/{count}">client.webhooks_journal.journal_local.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/batch.py">get_earliest</a>(count, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local/batch_get_earliest_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>
- <code title="get /webhooks-journal/journal-local/2026-03/batch/{offset}/next/{count}">client.webhooks_journal.journal_local.batch.<a href="./src/hubspot_sdk/resources/webhooks_journal/journal_local/batch.py">get_from_offset</a>(count, \*, offset, \*\*<a href="src/hubspot_sdk/types/webhooks_journal/journal_local/batch_get_from_offset_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/batch_response_journal_fetch_response.py">BatchResponseJournalFetchResponse</a></code>

## Snapshots

Methods:

- <code title="post /webhooks-journal/snapshots/2026-03/crm">client.webhooks_journal.snapshots.<a href="./src/hubspot_sdk/resources/webhooks_journal/snapshots.py">create</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/snapshot_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/crm_object_snapshot_batch_response.py">CrmObjectSnapshotBatchResponse</a></code>

## Subscriptions

Methods:

- <code title="post /webhooks-journal/subscriptions/2026-03">client.webhooks_journal.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/subscriptions.py">create</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/subscription_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/webhooks_journal/journal_subscription_response.py">JournalSubscriptionResponse</a></code>
- <code title="get /webhooks-journal/subscriptions/2026-03">client.webhooks_journal.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/subscriptions.py">list</a>() -> <a href="./src/hubspot_sdk/types/webhooks_journal/journal_collection_response_subscription_response_no_paging.py">JournalCollectionResponseSubscriptionResponseNoPaging</a></code>
- <code title="delete /webhooks-journal/subscriptions/2026-03/{subscriptionId}">client.webhooks_journal.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/subscriptions.py">delete</a>(subscription_id) -> None</code>
- <code title="delete /webhooks-journal/subscriptions/2026-03/portals/{portalId}">client.webhooks_journal.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/subscriptions.py">delete_for_portal</a>(portal_id) -> None</code>
- <code title="get /webhooks-journal/subscriptions/2026-03/{subscriptionId}">client.webhooks_journal.subscriptions.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/subscriptions.py">get</a>(subscription_id) -> <a href="./src/hubspot_sdk/types/webhooks_journal/journal_subscription_response.py">JournalSubscriptionResponse</a></code>

### Filters

Types:

```python
from hubspot_sdk.types.webhooks_journal.subscriptions import FilterListResponse
```

Methods:

- <code title="post /webhooks-journal/subscriptions/2026-03/filters">client.webhooks_journal.subscriptions.filters.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/filters.py">create</a>(\*\*<a href="src/hubspot_sdk/types/webhooks_journal/subscriptions/filter_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/shared/filter_create_response.py">FilterCreateResponse</a></code>
- <code title="get /webhooks-journal/subscriptions/2026-03/filters/subscription/{subscriptionId}">client.webhooks_journal.subscriptions.filters.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/filters.py">list</a>(subscription_id) -> <a href="./src/hubspot_sdk/types/webhooks_journal/subscriptions/filter_list_response.py">FilterListResponse</a></code>
- <code title="delete /webhooks-journal/subscriptions/2026-03/filters/{filterId}">client.webhooks_journal.subscriptions.filters.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/filters.py">delete</a>(filter_id) -> None</code>
- <code title="get /webhooks-journal/subscriptions/2026-03/filters/{filterId}">client.webhooks_journal.subscriptions.filters.<a href="./src/hubspot_sdk/resources/webhooks_journal/subscriptions/filters.py">get</a>(filter_id) -> <a href="./src/hubspot_sdk/types/shared/filter_response.py">FilterResponse</a></code>
