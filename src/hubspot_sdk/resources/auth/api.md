# Auth

## OAuth

Types:

```python
from hubspot_sdk.types.auth import (
    AccessTokenInfoResponse,
    RefreshTokenInfoResponse,
    SignedAccessToken,
    TokenResponseIf,
)
```

Methods:

- <code title="post /oauth/v1/token">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">create_access_token</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_create_access_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/token_response_if.py">TokenResponseIf</a></code>
- <code title="delete /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">delete_refresh_token</a>(token) -> None</code>
- <code title="get /oauth/v1/access-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get_access_token</a>(token) -> <a href="./src/hubspot_sdk/types/auth/access_token_info_response.py">AccessTokenInfoResponse</a></code>
- <code title="get /oauth/v1/refresh-tokens/{token}">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">get_refresh_token</a>(token) -> <a href="./src/hubspot_sdk/types/auth/refresh_token_info_response.py">RefreshTokenInfoResponse</a></code>
