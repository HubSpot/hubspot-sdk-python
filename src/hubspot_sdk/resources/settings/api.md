# Settings

## Currencies

Types:

```python
from hubspot_sdk.types.settings import (
    BatchInputExchangeRateCreateRequest,
    BatchInputExchangeRateUpdateRequest,
    BatchResponseExchangeRate,
    CentralExchangeRatesInformation,
    CollectionResponseCurrencyCodeInfoNoPaging,
    CollectionResponseExchangeRateForwardPaging,
    CollectionResponseExchangeRateNoPaging,
    CompanyCurrency,
    CompanyCurrencyUpdateRequest,
    CurrencyCodeInfo,
    CurrencyCreateRequest,
    CurrencyPairUpdate,
    ExchangeRate,
    ExchangeRateCreateRequest,
    ExchangeRateMultiplier,
    ExchangeRateUpdateRequest,
)
```

Methods:

- <code title="get /settings/currencies/2026-03/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">get_company_currency</a>() -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>
- <code title="get /settings/currencies/2026-03/codes">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_codes</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>
- <code title="put /settings/currencies/2026-03/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_company_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_update_company_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>

### CentralFxRates

Methods:

- <code title="post /settings/currencies/2026-03/central-fx-rates/add-currency">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">create_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/central_fx_rate_create_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/currencies/2026-03/central-fx-rates/information">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_information</a>() -> <a href="./src/hubspot_sdk/types/settings/central_exchange_rates_information.py">CentralExchangeRatesInformation</a></code>
- <code title="get /settings/currencies/2026-03/central-fx-rates/unsupported-currencies">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_unsupported_currencies</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>

### ExchangeRates

Methods:

- <code title="post /settings/currencies/2026-03/exchange-rates">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">create_exchange_rate</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rate_create_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/currencies/2026-03/exchange-rates/{exchangeRateId}">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">get_exchange_rate_by_id</a>(exchange_rate_id) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/currencies/2026-03/exchange-rates/current">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">list_current_exchange_rates</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_exchange_rate_no_paging.py">CollectionResponseExchangeRateNoPaging</a></code>
- <code title="get /settings/currencies/2026-03/exchange-rates">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">list_exchange_rates</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rate_list_exchange_rates_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">SyncPage[ExchangeRate]</a></code>
- <code title="patch /settings/currencies/2026-03/exchange-rates/{exchangeRateId}">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">update_exchange_rate</a>(exchange_rate_id, \*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rate_update_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="post /settings/currencies/2026-03/exchange-rates/update-visibility">client.settings.currencies.exchange_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/exchange_rates.py">update_visibility</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rate_update_visibility_params.py">params</a>) -> None</code>

#### Batch

Methods:

- <code title="post /settings/currencies/2026-03/exchange-rates/batch/create">client.settings.currencies.exchange_rates.batch.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/batch.py">create</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rates/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/currencies/2026-03/exchange-rates/batch/update">client.settings.currencies.exchange_rates.batch.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/batch.py">update</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rates/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/currencies/2026-03/exchange-rates/batch/read">client.settings.currencies.exchange_rates.batch.<a href="./src/hubspot_sdk/resources/settings/currencies/exchange_rates/batch.py">get</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/exchange_rates/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>

## TaxRates

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicTaxRateGroupForwardPaging,
    PublicTaxRateGroup,
)
```

Methods:

- <code title="get /tax-rates/2026-03/tax-rates">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/tax_rate_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">SyncPage[PublicTaxRateGroup]</a></code>
- <code title="get /tax-rates/2026-03/tax-rates/{taxRateGroupId}">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">get</a>(tax_rate_group_id) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">PublicTaxRateGroup</a></code>

## Users

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicPermissionSetNoPaging,
    CollectionResponsePublicTeamNoPaging,
    CollectionResponsePublicUserForwardPaging,
    PublicPermissionSet,
    PublicTeam,
    PublicUser,
    PublicUserUpdate,
    UserProvisionRequest,
)
```

Methods:

- <code title="post /settings/users/2026-03">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="put /settings/users/2026-03/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">update</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/users/2026-03">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">SyncPage[PublicUser]</a></code>
- <code title="delete /settings/users/2026-03/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">delete</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_delete_params.py">params</a>) -> None</code>
- <code title="get /settings/users/2026-03/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">get</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/users/2026-03/roles">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_roles</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_permission_set_no_paging.py">CollectionResponsePublicPermissionSetNoPaging</a></code>
- <code title="get /settings/users/2026-03/teams">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_teams</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_team_no_paging.py">CollectionResponsePublicTeamNoPaging</a></code>
