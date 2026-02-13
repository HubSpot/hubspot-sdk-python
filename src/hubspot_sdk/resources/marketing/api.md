# Marketing

Types:

```python
from hubspot_sdk.types.marketing import (
    EmailSendStatusView,
    EventIDView,
    PublicSingleSendEmail,
    PublicSingleSendRequestEgg,
)
```

## Campaigns

Types:

```python
from hubspot_sdk.types.marketing import (
    BatchInputPublicCampaignBatchUpdateItem,
    BatchInputPublicCampaignDeleteInput,
    BatchInputPublicCampaignInput,
    BatchInputPublicCampaignReadInput,
    BatchResponsePublicCampaign,
    BatchResponsePublicCampaignWithAssets,
    BatchResponsePublicCampaignWithAssetsWithErrors,
    BatchResponsePublicCampaignWithErrors,
    CollectionResponseContactReferenceForwardPaging,
    CollectionResponsePublicCampaignAsset,
    CollectionResponsePublicCampaignAssetForwardPaging,
    CollectionResponseWithTotalPublicCampaignForwardPaging,
    ContactReference,
    MetricsCounters,
    PublicBudgetItem,
    PublicBudgetItemInput,
    PublicBudgetTotals,
    PublicBusinessUnit,
    PublicCampaign,
    PublicCampaignAsset,
    PublicCampaignBatchUpdateItem,
    PublicCampaignDeleteInput,
    PublicCampaignInput,
    PublicCampaignReadInput,
    PublicCampaignWithAssets,
    PublicSpendItem,
    PublicSpendItemInput,
    RevenueAttributionAggregate,
)
```

Methods:

- <code title="post /marketing/v3/campaigns/">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaign_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">PublicCampaign</a></code>
- <code title="patch /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">update</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">PublicCampaign</a></code>
- <code title="get /marketing/v3/campaigns/">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaign_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">SyncPage[PublicCampaign]</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">delete</a>(campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">get</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign_with_assets.py">PublicCampaignWithAssets</a></code>

### Assets

Methods:

- <code title="put /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">update</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">list</a>(asset_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/asset_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_public_campaign_asset_forward_paging.py">CollectionResponsePublicCampaignAssetForwardPaging</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">delete</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>

### Batch

Methods:

- <code title="post /marketing/v3/campaigns/batch/create">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/v3/campaigns/batch/update">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/v3/campaigns/batch/archive">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/campaigns/batch/read">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign_with_assets.py">BatchResponsePublicCampaignWithAssets</a></code>

### Budget

Methods:

- <code title="post /marketing/v3/campaigns/{campaignGuid}/budget">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="put /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">update</a>(budget_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">delete</a>(budget_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get</a>(budget_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/budget/totals">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get_totals</a>(campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_totals.py">PublicBudgetTotals</a></code>

### Reports

Methods:

- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/metrics">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">get_attribution_metrics</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_get_attribution_metrics_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/metrics_counters.py">MetricsCounters</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/revenue">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">get_revenue_attribution</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_get_revenue_attribution_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/revenue_attribution_aggregate.py">RevenueAttributionAggregate</a></code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}">client.marketing.campaigns.reports.<a href="./src/hubspot_sdk/resources/marketing/campaigns/reports.py">list_contact_ids_by_type</a>(contact_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/report_list_contact_ids_by_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/contact_reference.py">SyncPage[ContactReference]</a></code>

### Spend

Methods:

- <code title="post /marketing/v3/campaigns/{campaignGuid}/spend">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="put /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">update</a>(spend_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="delete /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">delete</a>(spend_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/v3/campaigns/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">get</a>(spend_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>

## Emails

Types:

```python
from hubspot_sdk.types.marketing import (
    AggregateEmailStatistics,
    CollectionResponseWithTotalEmailStatisticIntervalNoPaging,
    CollectionResponseWithTotalPublicEmailForwardPaging,
    CollectionResponseWithTotalVersionPublicEmail,
    EmailCloneRequestVNext,
    EmailCreateRequest,
    EmailStatisticInterval,
    EmailStatisticsData,
    EmailUpdateRequest,
    Interval,
    PublicButtonStyleSettings,
    PublicDividerStyleSettings,
    PublicEmail,
    PublicEmailContent,
    PublicEmailFromDetails,
    PublicEmailRecipients,
    PublicEmailStyleSettings,
    PublicEmailSubscriptionDetails,
    PublicEmailTestingDetails,
    PublicEmailToDetails,
    PublicFontStyle,
    PublicRssEmailDetails,
    PublicWebversionDetails,
    SmartEmailField,
    VersionPublicEmail,
)
```

Methods:

- <code title="post /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="patch /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">update</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">SyncPage[PublicEmail]</a></code>
- <code title="delete /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">delete</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/emails/clone">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">clone</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_clone_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/ab-test/create-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">create_ab_test_variation</a>(\*\*<a href="src/hubspot_sdk/types/marketing/email_create_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/ab-test/get-variation">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_ab_test_variation</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_get_ab_test_variation_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_draft</a>(email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions/{revisionId}">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">get_revision</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">VersionPublicEmail</a></code>
- <code title="get /marketing/v3/emails/{emailId}/revisions">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">list_revisions</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_list_revisions_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/version_public_email.py">SyncPage[VersionPublicEmail]</a></code>
- <code title="post /marketing/v3/emails/{emailId}/publish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">publish</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/draft/reset">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">reset_draft</a>(email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">restore_revision</a>(revision_id, \*, email_id) -> None</code>
- <code title="post /marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">restore_revision_to_draft</a>(revision_id, \*, email_id) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>
- <code title="post /marketing/v3/emails/{emailId}/unpublish">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">unpublish</a>(email_id) -> None</code>
- <code title="patch /marketing/v3/emails/{emailId}/draft">client.marketing.emails.<a href="./src/hubspot_sdk/resources/marketing/emails/emails.py">update_draft</a>(email_id, \*\*<a href="src/hubspot_sdk/types/marketing/email_update_draft_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_email.py">PublicEmail</a></code>

### Statistics

Methods:

- <code title="get /marketing/v3/emails/statistics/list">client.marketing.emails.statistics.<a href="./src/hubspot_sdk/resources/marketing/emails/statistics.py">get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/emails/statistic_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/aggregate_email_statistics.py">AggregateEmailStatistics</a></code>
- <code title="get /marketing/v3/emails/statistics/histogram">client.marketing.emails.statistics.<a href="./src/hubspot_sdk/resources/marketing/emails/statistics.py">get_histogram</a>(\*\*<a href="src/hubspot_sdk/types/marketing/emails/statistic_get_histogram_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_email_statistic_interval_no_paging.py">CollectionResponseWithTotalEmailStatisticIntervalNoPaging</a></code>

## Events

Types:

```python
from hubspot_sdk.types.marketing import (
    AppInfo,
    AttendanceCounters,
    BatchInputMarketingEventCreateRequestParams,
    BatchInputMarketingEventEmailSubscriber,
    BatchInputMarketingEventExternalUniqueIdentifier,
    BatchInputMarketingEventPublicObjectIDDeleteRequest,
    BatchInputMarketingEventPublicUpdateRequestFullV2,
    BatchInputMarketingEventSubscriber,
    BatchResponseMarketingEventPublicDefaultResponse,
    BatchResponseMarketingEventPublicDefaultResponseV2,
    BatchResponseMarketingEventPublicDefaultResponseV2WithErrors,
    BatchResponseSubscriberEmailResponse,
    BatchResponseSubscriberVidResponse,
    CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging,
    CollectionResponseSearchPublicResponseWrapperNoPaging,
    CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging,
    CollectionResponseWithTotalParticipationBreakdownForwardPaging,
    CollectionResponseWithTotalPublicListNoPaging,
    ContactAssociation,
    CrmPropertyWrapper,
    EventDetailSettings,
    EventDetailSettingsURL,
    MarketingEventAssociation,
    MarketingEventCompleteRequestParams,
    MarketingEventCreateRequestParams,
    MarketingEventDefaultResponse,
    MarketingEventEmailSubscriber,
    MarketingEventExternalUniqueIdentifier,
    MarketingEventIdentifiersResponse,
    MarketingEventPublicDefaultResponse,
    MarketingEventPublicDefaultResponseV2,
    MarketingEventPublicObjectIDDeleteRequest,
    MarketingEventPublicReadResponse,
    MarketingEventPublicReadResponseV2,
    MarketingEventPublicUpdateRequestFullV2,
    MarketingEventPublicUpdateRequestV2,
    MarketingEventSubscriber,
    MarketingEventUpdateRequestParams,
    ParticipationAssociations,
    ParticipationBreakdown,
    ParticipationProperties,
    PropertyValue,
    PublicList,
    SearchPublicResponseWrapper,
    SubscriberEmailResponse,
    SubscriberVidResponse,
)
```

Methods:

- <code title="post /marketing/v3/marketing-events/events">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="patch /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update</a>(object_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response_v2.py">MarketingEventPublicDefaultResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">SyncPage[MarketingEventPublicReadResponseV2]</a></code>
- <code title="delete /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete</a>(object_id) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/cancel">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">cancel_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_cancel_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/complete">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">complete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_complete_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_default_response.py">MarketingEventDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/batch/archive">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_delete_batch_params.py">params</a>) -> None</code>
- <code title="post /marketing/v3/marketing-events/events/delete">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_batch_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_delete_batch_by_external_event_id_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="delete /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">delete_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_delete_by_external_event_id_params.py">params</a>) -> None</code>
- <code title="get /marketing/v3/marketing-events/{objectId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">get</a>(object_id) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response_v2.py">MarketingEventPublicReadResponseV2</a></code>
- <code title="get /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">get_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_get_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_read_response.py">MarketingEventPublicReadResponse</a></code>
- <code title="get /marketing/v3/marketing-events/events/search">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">search_by_external_event_id</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_search_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_search_public_response_wrapper_no_paging.py">CollectionResponseSearchPublicResponseWrapperNoPaging</a></code>
- <code title="get /marketing/v3/marketing-events/{externalEventId}/identifiers">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">search_identifiers_by_external_event_id</a>(external_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_marketing_event_identifiers_response_no_paging.py">CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging</a></code>
- <code title="post /marketing/v3/marketing-events/batch/update">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_update_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response_v2.py">BatchResponseMarketingEventPublicDefaultResponseV2</a></code>
- <code title="patch /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">update_by_external_event_id</a>(external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_update_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_batch</a>(\*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_batch_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_marketing_event_public_default_response.py">BatchResponseMarketingEventPublicDefaultResponse</a></code>
- <code title="put /marketing/v3/marketing-events/events/{externalEventId}">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_by_external_event_id</a>(path_external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_by_external_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/marketing_event_public_default_response.py">MarketingEventPublicDefaultResponse</a></code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/email-upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_subscriber_state_by_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_subscriber_state_by_email_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /marketing/v3/marketing-events/events/{externalEventId}/{subscriberState}/upsert">client.marketing.events.<a href="./src/hubspot_sdk/resources/marketing/events/events.py">upsert_subscriber_state_by_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/event_upsert_subscriber_state_by_id_params.py">params</a>) -> BinaryAPIResponse</code>

### Associations

Methods:

- <code title="get /marketing/v3/marketing-events/associations/{marketingEventId}/lists">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">list</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>
- <code title="delete /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">delete</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{marketingEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">associate</a>(list_id, \*, marketing_event_id) -> None</code>
- <code title="put /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">associate_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="delete /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists/{listId}">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">delete_by_external_account</a>(list_id, \*, external_account_id, external_event_id) -> None</code>
- <code title="get /marketing/v3/marketing-events/associations/{externalAccountId}/{externalEventId}/lists">client.marketing.events.associations.<a href="./src/hubspot_sdk/resources/marketing/events/associations.py">list_by_external_account</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_with_total_public_list_no_paging.py">CollectionResponseWithTotalPublicListNoPaging</a></code>

### Attendance

Methods:

- <code title="post /marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_event_id_and_contact_id</a>(subscriber_state, \*, object_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_event_id_and_contact_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_vid_response.py">BatchResponseSubscriberVidResponse</a></code>
- <code title="post /marketing/v3/marketing-events/{objectId}/attendance/{subscriberState}/email-create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_event_id_and_email</a>(subscriber_state, \*, object_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_event_id_and_email_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_email_response.py">BatchResponseSubscriberEmailResponse</a></code>
- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_external_event_id_and_contact_id</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_external_event_id_and_contact_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_vid_response.py">BatchResponseSubscriberVidResponse</a></code>
- <code title="post /marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create">client.marketing.events.attendance.<a href="./src/hubspot_sdk/resources/marketing/events/attendance.py">create_by_external_event_id_and_email</a>(subscriber_state, \*, external_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/attendance_create_by_external_event_id_and_email_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_subscriber_email_response.py">BatchResponseSubscriberEmailResponse</a></code>

### Participations

Methods:

- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">get_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">get_by_id</a>(marketing_event_id) -> <a href="./src/hubspot_sdk/types/marketing/attendance_counters.py">AttendanceCounters</a></code>
- <code title="get /marketing/v3/marketing-events/participations/contacts/{contactIdentifier}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_contact</a>(contact_identifier, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_contact_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{externalAccountId}/{externalEventId}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_external_account_and_event_id</a>(external_event_id, \*, external_account_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_external_account_and_event_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>
- <code title="get /marketing/v3/marketing-events/participations/{marketingEventId}/breakdown">client.marketing.events.participations.<a href="./src/hubspot_sdk/resources/marketing/events/participations.py">list_breakdown_by_id</a>(marketing_event_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/participation_list_breakdown_by_id_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/participation_breakdown.py">SyncPage[ParticipationBreakdown]</a></code>

### Settings

Methods:

- <code title="post /marketing/v3/marketing-events/{appId}/settings">client.marketing.events.settings.<a href="./src/hubspot_sdk/resources/marketing/events/settings.py">create_or_update</a>(app_id, \*\*<a href="src/hubspot_sdk/types/marketing/events/setting_create_or_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>
- <code title="get /marketing/v3/marketing-events/{appId}/settings">client.marketing.events.settings.<a href="./src/hubspot_sdk/resources/marketing/events/settings.py">get</a>(app_id) -> <a href="./src/hubspot_sdk/types/marketing/event_detail_settings.py">EventDetailSettings</a></code>

## Forms

Types:

```python
from hubspot_sdk.types.marketing import (
    CollectionResponseFormDefinitionBaseForwardPaging,
    DatepickerField,
    DependentField,
    DependentFieldFilter,
    DropdownField,
    EmailField,
    EmailFieldValidation,
    EnumeratedFieldOption,
    FieldGroup,
    FileField,
    FormDefinitionBase,
    FormDefinitionCreateRequestBase,
    FormDisplayOptions,
    FormPostSubmitAction,
    FormStyle,
    HubSpotFormConfiguration,
    HubSpotFormDefinition,
    HubSpotFormDefinitionCreateRequest,
    HubSpotFormDefinitionPatchRequest,
    LegalConsentCheckbox,
    LegalConsentOptionsExplicitConsentToProcess,
    LegalConsentOptionsImplicitConsentToProcess,
    LegalConsentOptionsLegitimateInterest,
    LegalConsentOptionsNone,
    LifecycleStage,
    MobilePhoneField,
    MultiLineTextField,
    MultipleCheckboxesField,
    NumberField,
    NumberFieldValidation,
    PaymentLinkRadioField,
    PhoneField,
    PhoneFieldValidation,
    RadioField,
    SingleCheckboxField,
    SingleLineTextField,
)
```

Methods:

- <code title="post /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">create</a>() -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="patch /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">update</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="get /marketing/v3/forms/">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/form_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/hub_spot_form_definition.py">SyncPage[HubSpotFormDefinition]</a></code>
- <code title="delete /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">delete</a>(form_id) -> None</code>
- <code title="get /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">get</a>(form_id, \*\*<a href="src/hubspot_sdk/types/marketing/form_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>
- <code title="put /marketing/v3/forms/{formId}">client.marketing.forms.<a href="./src/hubspot_sdk/resources/marketing/forms.py">replace</a>(form_id) -> <a href="./src/hubspot_sdk/types/marketing/form_definition_base.py">FormDefinitionBase</a></code>

## SingleSend

Methods:

- <code title="post /marketing/v4/email/single-send">client.marketing.single_send.<a href="./src/hubspot_sdk/resources/marketing/single_send.py">send</a>(\*\*<a href="src/hubspot_sdk/types/marketing/single_send_send_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/email_send_status_view.py">EmailSendStatusView</a></code>

## Subscriptions

Types:

```python
from hubspot_sdk.types.marketing import (
    PublicSubscriptionStatus,
    PublicSubscriptionStatusesResponse,
    PublicUpdateSubscriptionStatusRequest,
    SubscriptionDefinition,
    SubscriptionDefinitionsResponse,
)
```

Methods:

- <code title="get /communication-preferences/v3/definitions">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">list</a>() -> <a href="./src/hubspot_sdk/types/marketing/subscription_definitions_response.py">SubscriptionDefinitionsResponse</a></code>
- <code title="get /communication-preferences/v3/status/email/{emailAddress}">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">get_email_status</a>(email_address) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_statuses_response.py">PublicSubscriptionStatusesResponse</a></code>
- <code title="post /communication-preferences/v3/subscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">subscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_subscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>
- <code title="post /communication-preferences/v3/unsubscribe">client.marketing.subscriptions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/subscriptions.py">unsubscribe</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscription_unsubscribe_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_subscription_status.py">PublicSubscriptionStatus</a></code>

### V4

Types:

```python
from hubspot_sdk.types.marketing.subscriptions import (
    ActionResponseWithResultsPublicStatus,
    ActionResponseWithResultsPublicWideStatus,
    ActionResponseWithResultsSubscriptionDefinition,
    BatchInputPublicStatusRequest,
    BatchResponsePublicBulkOptOutFromAllResponse,
    BatchResponsePublicStatus,
    BatchResponsePublicStatusBulkResponse,
    BatchResponsePublicStatusBulkResponseWithErrors,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicWideStatusBulkResponseWithErrors,
    LinkGenerationRequest,
    LinkGenerationResponse,
    PartialPublicStatusRequest,
    PublicBulkOptOutFromAllResponse,
    PublicStatus,
    PublicStatusBulkResponse,
    PublicStatusRequest,
    PublicSubscriptionTranslation,
    PublicWideStatus,
    PublicWideStatusBulkResponse,
)
```

#### Definitions

Methods:

- <code title="get /communication-preferences/v4/definitions">client.marketing.subscriptions.v4.definitions.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/definitions.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/definition_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_subscription_definition.py">ActionResponseWithResultsSubscriptionDefinition</a></code>

#### Links

Methods:

- <code title="post /communication-preferences/v4/links/generate">client.marketing.subscriptions.v4.links.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/links.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/link_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/link_generation_response.py">LinkGenerationResponse</a></code>

#### Statuses

Methods:

- <code title="post /communication-preferences/v4/statuses/{subscriberIdString}">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">update</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/read">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_status_bulk_response.py">BatchResponsePublicStatusBulkResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/unsubscribe-all/read">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_get_unsubscribe_all_status</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_get_unsubscribe_all_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_wide_status_bulk_response.py">BatchResponsePublicWideStatusBulkResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_unsubscribe_all</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_bulk_opt_out_from_all_response.py">BatchResponsePublicBulkOptOutFromAllResponse</a></code>
- <code title="post /communication-preferences/v4/statuses/batch/write">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">batch_update</a>(\*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/batch_response_public_status.py">BatchResponsePublicStatus</a></code>
- <code title="get /communication-preferences/v4/statuses/{subscriberIdString}">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">get</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>
- <code title="get /communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">get_unsubscribe_all_status</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_get_unsubscribe_all_status_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_wide_status.py">ActionResponseWithResultsPublicWideStatus</a></code>
- <code title="post /communication-preferences/v4/statuses/{subscriberIdString}/unsubscribe-all">client.marketing.subscriptions.v4.statuses.<a href="./src/hubspot_sdk/resources/marketing/subscriptions/v4/statuses.py">unsubscribe_all</a>(subscriber_id_string, \*\*<a href="src/hubspot_sdk/types/marketing/subscriptions/v4/status_unsubscribe_all_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/subscriptions/action_response_with_results_public_status.py">ActionResponseWithResultsPublicStatus</a></code>

## Transactional

Types:

```python
from hubspot_sdk.types.marketing import (
    CollectionResponseSmtpAPITokenViewForwardPaging,
    SmtpAPITokenRequestEgg,
    SmtpAPITokenView,
)
```

### SingleEmail

Methods:

- <code title="post /marketing/v3/transactional/single-email/send">client.marketing.transactional.single_email.<a href="./src/hubspot_sdk/resources/marketing/transactional/single_email.py">send</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/single_email_send_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/email_send_status_view.py">EmailSendStatusView</a></code>

### SmtpTokens

Methods:

- <code title="post /marketing/v3/transactional/smtp-tokens">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/smtp_token_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>
- <code title="get /marketing/v3/transactional/smtp-tokens">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">list</a>(\*\*<a href="src/hubspot_sdk/types/marketing/transactional/smtp_token_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SyncPage[SmtpAPITokenView]</a></code>
- <code title="delete /marketing/v3/transactional/smtp-tokens/{tokenId}">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">delete</a>(token_id) -> None</code>
- <code title="get /marketing/v3/transactional/smtp-tokens/{tokenId}">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">get</a>(token_id) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>
- <code title="post /marketing/v3/transactional/smtp-tokens/{tokenId}/password-reset">client.marketing.transactional.smtp_tokens.<a href="./src/hubspot_sdk/resources/marketing/transactional/smtp_tokens.py">reset_password</a>(token_id) -> <a href="./src/hubspot_sdk/types/marketing/smtp_api_token_view.py">SmtpAPITokenView</a></code>
