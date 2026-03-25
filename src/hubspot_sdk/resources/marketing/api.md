# Marketing

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
    CollectionResponseContactReferenceForwardPaging,
    CollectionResponsePublicCampaignAsset,
    CollectionResponsePublicCampaignAssetForwardPaging,
    CollectionResponseWithTotalPublicCampaign,
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

- <code title="patch /marketing/campaigns/2026-03/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">update</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign.py">PublicCampaign</a></code>
- <code title="delete /marketing/campaigns/2026-03/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">delete</a>(campaign_guid) -> None</code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}">client.marketing.campaigns.<a href="./src/hubspot_sdk/resources/marketing/campaigns/campaigns.py">get</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaign_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_campaign_with_assets.py">PublicCampaignWithAssets</a></code>

### Assets

Methods:

- <code title="put /marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">update</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">list</a>(asset_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/asset_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/collection_response_public_campaign_asset_forward_paging.py">CollectionResponsePublicCampaignAssetForwardPaging</a></code>
- <code title="delete /marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}/{assetId}">client.marketing.campaigns.assets.<a href="./src/hubspot_sdk/resources/marketing/campaigns/assets.py">delete</a>(asset_id, \*, campaign_guid, asset_type) -> None</code>

### Batch

Methods:

- <code title="post /marketing/campaigns/2026-03/batch/create">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/campaigns/2026-03/batch/update">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign.py">BatchResponsePublicCampaign</a></code>
- <code title="post /marketing/campaigns/2026-03/batch/archive">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">delete</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /marketing/campaigns/2026-03/batch/read">client.marketing.campaigns.batch.<a href="./src/hubspot_sdk/resources/marketing/campaigns/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/marketing/campaigns/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/batch_response_public_campaign_with_assets.py">BatchResponsePublicCampaignWithAssets</a></code>

### Budget

Methods:

- <code title="post /marketing/campaigns/2026-03/{campaignGuid}/budget">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="put /marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">update</a>(budget_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/budget_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="delete /marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">delete</a>(budget_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get</a>(budget_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_item.py">PublicBudgetItem</a></code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/budget/totals">client.marketing.campaigns.budget.<a href="./src/hubspot_sdk/resources/marketing/campaigns/budget.py">get_totals</a>(campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_budget_totals.py">PublicBudgetTotals</a></code>

### Metrics

Methods:

- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/reports/metrics">client.marketing.campaigns.metrics.<a href="./src/hubspot_sdk/resources/marketing/campaigns/metrics.py">get_attribution_metrics</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/metric_get_attribution_metrics_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/metrics_counters.py">MetricsCounters</a></code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/reports/revenue">client.marketing.campaigns.metrics.<a href="./src/hubspot_sdk/resources/marketing/campaigns/metrics.py">get_revenue_attribution</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/metric_get_revenue_attribution_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/revenue_attribution_aggregate.py">RevenueAttributionAggregate</a></code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/reports/contacts/{contactType}">client.marketing.campaigns.metrics.<a href="./src/hubspot_sdk/resources/marketing/campaigns/metrics.py">list_contact_ids_by_type</a>(contact_type, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/metric_list_contact_ids_by_type_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/contact_reference.py">SyncPage[ContactReference]</a></code>

### Spend

Methods:

- <code title="post /marketing/campaigns/2026-03/{campaignGuid}/spend">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">create</a>(campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="put /marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">update</a>(spend_id, \*, campaign_guid, \*\*<a href="src/hubspot_sdk/types/marketing/campaigns/spend_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
- <code title="delete /marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">delete</a>(spend_id, \*, campaign_guid) -> None</code>
- <code title="get /marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}">client.marketing.campaigns.spend.<a href="./src/hubspot_sdk/resources/marketing/campaigns/spend.py">get</a>(spend_id, \*, campaign_guid) -> <a href="./src/hubspot_sdk/types/marketing/public_spend_item.py">PublicSpendItem</a></code>
