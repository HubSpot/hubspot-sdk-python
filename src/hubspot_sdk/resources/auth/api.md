# Auth

## OAuth

Types:

```python
from hubspot_sdk.types.auth import (
    AccessTokenResponse,
    ClientCredentialsTokenResponse,
    PublicAccessTokenInfoResponse,
    PublicRefreshTokenInfoResponse,
    SignedAccessToken,
    TokenInfoResponseBaseIf,
    TokenResponseIf,
)
```

Methods:

- <code title="post /oauth/2026-03/token">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">create_token</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_create_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/token_response_if.py">TokenResponseIf</a></code>
- <code title="post /oauth/2026-03/token/introspect">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">introspect_token</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_introspect_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/auth/token_info_response_base_if.py">TokenInfoResponseBaseIf</a></code>
- <code title="post /oauth/2026-03/token/revoke">client.auth.oauth.<a href="./src/hubspot_sdk/resources/auth/oauth.py">revoke_token</a>(\*\*<a href="src/hubspot_sdk/types/auth/oauth_revoke_token_params.py">params</a>) -> BinaryAPIResponse</code>
