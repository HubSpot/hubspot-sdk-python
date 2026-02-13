# Settings

## Currencies

Types:

```python
from hubspot_sdk.types.settings import (
    BatchInputExchangeRateCreateRequest,
    BatchInputExchangeRateUpdateRequest,
    BatchResponseExchangeRate,
    BatchResponseExchangeRateWithErrors,
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

- <code title="post /settings/v3/currencies/exchange-rates/batch/create">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_create</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/batch/read">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_get</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/batch/update">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">batch_update</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/batch_response_exchange_rate.py">BatchResponseExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">create_exchange_rate</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_create_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">get_company_currency</a>() -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>
- <code title="get /settings/v3/currencies/exchange-rates/{exchangeRateId}">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">get_exchange_rate_by_id</a>(exchange_rate_id) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/codes">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_codes</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>
- <code title="get /settings/v3/currencies/exchange-rates/current">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_current_exchange_rates</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_exchange_rate_no_paging.py">CollectionResponseExchangeRateNoPaging</a></code>
- <code title="get /settings/v3/currencies/exchange-rates">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">list_exchange_rates</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_list_exchange_rates_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">SyncPage[ExchangeRate]</a></code>
- <code title="put /settings/v3/currencies/company-currency">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_company_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_update_company_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/company_currency.py">CompanyCurrency</a></code>
- <code title="patch /settings/v3/currencies/exchange-rates/{exchangeRateId}">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_exchange_rate</a>(exchange_rate_id, \*\*<a href="src/hubspot_sdk/types/settings/currency_update_exchange_rate_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="post /settings/v3/currencies/exchange-rates/update-visibility">client.settings.currencies.<a href="./src/hubspot_sdk/resources/settings/currencies/currencies.py">update_visibility</a>(\*\*<a href="src/hubspot_sdk/types/settings/currency_update_visibility_params.py">params</a>) -> None</code>

### CentralFxRates

Methods:

- <code title="post /settings/v3/currencies/central-fx-rates/add-currency">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">create_currency</a>(\*\*<a href="src/hubspot_sdk/types/settings/currencies/central_fx_rate_create_currency_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/exchange_rate.py">ExchangeRate</a></code>
- <code title="get /settings/v3/currencies/central-fx-rates/information">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_information</a>() -> <a href="./src/hubspot_sdk/types/settings/central_exchange_rates_information.py">CentralExchangeRatesInformation</a></code>
- <code title="get /settings/v3/currencies/central-fx-rates/unsupported-currencies">client.settings.currencies.central_fx_rates.<a href="./src/hubspot_sdk/resources/settings/currencies/central_fx_rates.py">get_unsupported_currencies</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_currency_code_info_no_paging.py">CollectionResponseCurrencyCodeInfoNoPaging</a></code>

## TaxRates

Types:

```python
from hubspot_sdk.types.settings import (
    CollectionResponsePublicTaxRateGroupForwardPaging,
    PublicTaxRateGroup,
)
```

Methods:

- <code title="get /tax-rates/v1/tax-rates">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/tax_rate_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">SyncPage[PublicTaxRateGroup]</a></code>
- <code title="get /tax-rates/v1/tax-rates/{taxRateGroupId}">client.settings.tax_rates.<a href="./src/hubspot_sdk/resources/settings/tax_rates.py">get</a>(tax_rate_group_id) -> <a href="./src/hubspot_sdk/types/settings/public_tax_rate_group.py">PublicTaxRateGroup</a></code>

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

- <code title="post /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">create</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="put /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">update</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/v3/users/">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list</a>(\*\*<a href="src/hubspot_sdk/types/settings/user_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">SyncPage[PublicUser]</a></code>
- <code title="delete /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">delete</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_delete_params.py">params</a>) -> None</code>
- <code title="get /settings/v3/users/{userId}">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">get</a>(user_id, \*\*<a href="src/hubspot_sdk/types/settings/user_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/settings/public_user.py">PublicUser</a></code>
- <code title="get /settings/v3/users/roles">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_roles</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_permission_set_no_paging.py">CollectionResponsePublicPermissionSetNoPaging</a></code>
- <code title="get /settings/v3/users/teams">client.settings.users.<a href="./src/hubspot_sdk/resources/settings/users.py">list_teams</a>() -> <a href="./src/hubspot_sdk/types/settings/collection_response_public_team_no_paging.py">CollectionResponsePublicTeamNoPaging</a></code>
