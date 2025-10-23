# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import webhooks
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.cms import cms
from .resources.crm import crm
from .resources.auth import auth
from .resources.files import files
from .resources.settings import settings
from .resources.marketing import marketing
from .resources.automation import automation

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "HubSpot", "AsyncHubSpot", "Client", "AsyncClient"]


class HubSpot(SyncAPIClient):
    auth: auth.AuthResource
    automation: automation.AutomationResource
    cms: cms.CmsResource
    crm: crm.CRMResource
    files: files.FilesResource
    marketing: marketing.MarketingResource
    settings: settings.SettingsResource
    webhooks: webhooks.WebhooksResource
    with_raw_response: HubSpotWithRawResponse
    with_streaming_response: HubSpotWithStreamedResponse

    # client options
    access_token: str | None
    developer_api_key: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        developer_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous HubSpot client instance."""
        self.access_token = access_token

        self.developer_api_key = developer_api_key

        if base_url is None:
            base_url = os.environ.get("HUB_SPOT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hubapi.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth = auth.AuthResource(self)
        self.automation = automation.AutomationResource(self)
        self.cms = cms.CmsResource(self)
        self.crm = crm.CRMResource(self)
        self.files = files.FilesResource(self)
        self.marketing = marketing.MarketingResource(self)
        self.settings = settings.SettingsResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.with_raw_response = HubSpotWithRawResponse(self)
        self.with_streaming_response = HubSpotWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "hapikey": self.developer_api_key if self.developer_api_key is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        developer_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            developer_api_key=developer_api_key or self.developer_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncHubSpot(AsyncAPIClient):
    auth: auth.AsyncAuthResource
    automation: automation.AsyncAutomationResource
    cms: cms.AsyncCmsResource
    crm: crm.AsyncCRMResource
    files: files.AsyncFilesResource
    marketing: marketing.AsyncMarketingResource
    settings: settings.AsyncSettingsResource
    webhooks: webhooks.AsyncWebhooksResource
    with_raw_response: AsyncHubSpotWithRawResponse
    with_streaming_response: AsyncHubSpotWithStreamedResponse

    # client options
    access_token: str | None
    developer_api_key: str | None

    def __init__(
        self,
        *,
        access_token: str | None = None,
        developer_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncHubSpot client instance."""
        self.access_token = access_token

        self.developer_api_key = developer_api_key

        if base_url is None:
            base_url = os.environ.get("HUB_SPOT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.hubapi.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth = auth.AsyncAuthResource(self)
        self.automation = automation.AsyncAutomationResource(self)
        self.cms = cms.AsyncCmsResource(self)
        self.crm = crm.AsyncCRMResource(self)
        self.files = files.AsyncFilesResource(self)
        self.marketing = marketing.AsyncMarketingResource(self)
        self.settings = settings.AsyncSettingsResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.with_raw_response = AsyncHubSpotWithRawResponse(self)
        self.with_streaming_response = AsyncHubSpotWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        access_token = self.access_token
        if access_token is None:
            return {}
        return {"Authorization": f"Bearer {access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "hapikey": self.developer_api_key if self.developer_api_key is not None else Omit(),
            **self._custom_query,
        }

    def copy(
        self,
        *,
        access_token: str | None = None,
        developer_api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            access_token=access_token or self.access_token,
            developer_api_key=developer_api_key or self.developer_api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class HubSpotWithRawResponse:
    def __init__(self, client: HubSpot) -> None:
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.automation = automation.AutomationResourceWithRawResponse(client.automation)
        self.cms = cms.CmsResourceWithRawResponse(client.cms)
        self.crm = crm.CRMResourceWithRawResponse(client.crm)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.marketing = marketing.MarketingResourceWithRawResponse(client.marketing)
        self.settings = settings.SettingsResourceWithRawResponse(client.settings)
        self.webhooks = webhooks.WebhooksResourceWithRawResponse(client.webhooks)


class AsyncHubSpotWithRawResponse:
    def __init__(self, client: AsyncHubSpot) -> None:
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.automation = automation.AsyncAutomationResourceWithRawResponse(client.automation)
        self.cms = cms.AsyncCmsResourceWithRawResponse(client.cms)
        self.crm = crm.AsyncCRMResourceWithRawResponse(client.crm)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.marketing = marketing.AsyncMarketingResourceWithRawResponse(client.marketing)
        self.settings = settings.AsyncSettingsResourceWithRawResponse(client.settings)
        self.webhooks = webhooks.AsyncWebhooksResourceWithRawResponse(client.webhooks)


class HubSpotWithStreamedResponse:
    def __init__(self, client: HubSpot) -> None:
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.automation = automation.AutomationResourceWithStreamingResponse(client.automation)
        self.cms = cms.CmsResourceWithStreamingResponse(client.cms)
        self.crm = crm.CRMResourceWithStreamingResponse(client.crm)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.marketing = marketing.MarketingResourceWithStreamingResponse(client.marketing)
        self.settings = settings.SettingsResourceWithStreamingResponse(client.settings)
        self.webhooks = webhooks.WebhooksResourceWithStreamingResponse(client.webhooks)


class AsyncHubSpotWithStreamedResponse:
    def __init__(self, client: AsyncHubSpot) -> None:
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.automation = automation.AsyncAutomationResourceWithStreamingResponse(client.automation)
        self.cms = cms.AsyncCmsResourceWithStreamingResponse(client.cms)
        self.crm = crm.AsyncCRMResourceWithStreamingResponse(client.crm)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.marketing = marketing.AsyncMarketingResourceWithStreamingResponse(client.marketing)
        self.settings = settings.AsyncSettingsResourceWithStreamingResponse(client.settings)
        self.webhooks = webhooks.AsyncWebhooksResourceWithStreamingResponse(client.webhooks)


Client = HubSpot

AsyncClient = AsyncHubSpot
