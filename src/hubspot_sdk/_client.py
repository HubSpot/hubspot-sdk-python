# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        cms,
        crm,
        auth,
        meta,
        files,
        events,
        account,
        settings,
        webhooks,
        marketing,
        scheduler,
        automation,
        conversations,
        business_units,
        communication_preferences,
    )
    from .resources.cms.cms import CmsResource, AsyncCmsResource
    from .resources.crm.crm import CrmResource, AsyncCrmResource
    from .resources.auth.auth import AuthResource, AsyncAuthResource
    from .resources.meta.meta import MetaResource, AsyncMetaResource
    from .resources.files.files import FilesResource, AsyncFilesResource
    from .resources.events.events import EventsResource, AsyncEventsResource
    from .resources.account.account import AccountResource, AsyncAccountResource
    from .resources.settings.settings import SettingsResource, AsyncSettingsResource
    from .resources.webhooks.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.marketing.marketing import MarketingResource, AsyncMarketingResource
    from .resources.scheduler.scheduler import SchedulerResource, AsyncSchedulerResource
    from .resources.automation.automation import AutomationResource, AsyncAutomationResource
    from .resources.conversations.conversations import ConversationsResource, AsyncConversationsResource
    from .resources.business_units.business_units import BusinessUnitsResource, AsyncBusinessUnitsResource
    from .resources.communication_preferences.communication_preferences import (
        CommunicationPreferencesResource,
        AsyncCommunicationPreferencesResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Hubspot", "AsyncHubspot", "Client", "AsyncClient"]


class Hubspot(SyncAPIClient):
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
        """Construct a new synchronous Hubspot client instance."""
        self.access_token = access_token

        self.developer_api_key = developer_api_key

        if base_url is None:
            base_url = os.environ.get("HUBSPOT_BASE_URL")
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

    @cached_property
    def account(self) -> AccountResource:
        from .resources.account import AccountResource

        return AccountResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def automation(self) -> AutomationResource:
        from .resources.automation import AutomationResource

        return AutomationResource(self)

    @cached_property
    def business_units(self) -> BusinessUnitsResource:
        from .resources.business_units import BusinessUnitsResource

        return BusinessUnitsResource(self)

    @cached_property
    def cms(self) -> CmsResource:
        from .resources.cms import CmsResource

        return CmsResource(self)

    @cached_property
    def communication_preferences(self) -> CommunicationPreferencesResource:
        from .resources.communication_preferences import CommunicationPreferencesResource

        return CommunicationPreferencesResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def crm(self) -> CrmResource:
        from .resources.crm import CrmResource

        return CrmResource(self)

    @cached_property
    def events(self) -> EventsResource:
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def marketing(self) -> MarketingResource:
        from .resources.marketing import MarketingResource

        return MarketingResource(self)

    @cached_property
    def meta(self) -> MetaResource:
        from .resources.meta import MetaResource

        return MetaResource(self)

    @cached_property
    def scheduler(self) -> SchedulerResource:
        from .resources.scheduler import SchedulerResource

        return SchedulerResource(self)

    @cached_property
    def settings(self) -> SettingsResource:
        from .resources.settings import SettingsResource

        return SettingsResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> HubspotWithRawResponse:
        return HubspotWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubspotWithStreamedResponse:
        return HubspotWithStreamedResponse(self)

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
        base_query = {**super().default_query, **self._custom_query}

        if getattr(self, "access_token", None):
            return base_query
        return {
            **base_query,
            "hapikey": self.developer_api_key if self.developer_api_key is not None else Omit(),
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


class AsyncHubspot(AsyncAPIClient):
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
        """Construct a new async AsyncHubspot client instance."""
        self.access_token = access_token

        self.developer_api_key = developer_api_key

        if base_url is None:
            base_url = os.environ.get("HUBSPOT_BASE_URL")
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

    @cached_property
    def account(self) -> AsyncAccountResource:
        from .resources.account import AsyncAccountResource

        return AsyncAccountResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def automation(self) -> AsyncAutomationResource:
        from .resources.automation import AsyncAutomationResource

        return AsyncAutomationResource(self)

    @cached_property
    def business_units(self) -> AsyncBusinessUnitsResource:
        from .resources.business_units import AsyncBusinessUnitsResource

        return AsyncBusinessUnitsResource(self)

    @cached_property
    def cms(self) -> AsyncCmsResource:
        from .resources.cms import AsyncCmsResource

        return AsyncCmsResource(self)

    @cached_property
    def communication_preferences(self) -> AsyncCommunicationPreferencesResource:
        from .resources.communication_preferences import AsyncCommunicationPreferencesResource

        return AsyncCommunicationPreferencesResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def crm(self) -> AsyncCrmResource:
        from .resources.crm import AsyncCrmResource

        return AsyncCrmResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def marketing(self) -> AsyncMarketingResource:
        from .resources.marketing import AsyncMarketingResource

        return AsyncMarketingResource(self)

    @cached_property
    def meta(self) -> AsyncMetaResource:
        from .resources.meta import AsyncMetaResource

        return AsyncMetaResource(self)

    @cached_property
    def scheduler(self) -> AsyncSchedulerResource:
        from .resources.scheduler import AsyncSchedulerResource

        return AsyncSchedulerResource(self)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        from .resources.settings import AsyncSettingsResource

        return AsyncSettingsResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncHubspotWithRawResponse:
        return AsyncHubspotWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubspotWithStreamedResponse:
        return AsyncHubspotWithStreamedResponse(self)

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
        base_query = {**super().default_query, **self._custom_query}

        if getattr(self, "access_token", None):
            return base_query
        return {
            **base_query,
            "hapikey": self.developer_api_key if self.developer_api_key is not None else Omit(),
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


class HubspotWithRawResponse:
    _client: Hubspot

    def __init__(self, client: Hubspot) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithRawResponse:
        from .resources.account import AccountResourceWithRawResponse

        return AccountResourceWithRawResponse(self._client.account)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automation(self) -> automation.AutomationResourceWithRawResponse:
        from .resources.automation import AutomationResourceWithRawResponse

        return AutomationResourceWithRawResponse(self._client.automation)

    @cached_property
    def business_units(self) -> business_units.BusinessUnitsResourceWithRawResponse:
        from .resources.business_units import BusinessUnitsResourceWithRawResponse

        return BusinessUnitsResourceWithRawResponse(self._client.business_units)

    @cached_property
    def cms(self) -> cms.CmsResourceWithRawResponse:
        from .resources.cms import CmsResourceWithRawResponse

        return CmsResourceWithRawResponse(self._client.cms)

    @cached_property
    def communication_preferences(self) -> communication_preferences.CommunicationPreferencesResourceWithRawResponse:
        from .resources.communication_preferences import CommunicationPreferencesResourceWithRawResponse

        return CommunicationPreferencesResourceWithRawResponse(self._client.communication_preferences)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def crm(self) -> crm.CrmResourceWithRawResponse:
        from .resources.crm import CrmResourceWithRawResponse

        return CrmResourceWithRawResponse(self._client.crm)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def marketing(self) -> marketing.MarketingResourceWithRawResponse:
        from .resources.marketing import MarketingResourceWithRawResponse

        return MarketingResourceWithRawResponse(self._client.marketing)

    @cached_property
    def meta(self) -> meta.MetaResourceWithRawResponse:
        from .resources.meta import MetaResourceWithRawResponse

        return MetaResourceWithRawResponse(self._client.meta)

    @cached_property
    def scheduler(self) -> scheduler.SchedulerResourceWithRawResponse:
        from .resources.scheduler import SchedulerResourceWithRawResponse

        return SchedulerResourceWithRawResponse(self._client.scheduler)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithRawResponse:
        from .resources.settings import SettingsResourceWithRawResponse

        return SettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncHubspotWithRawResponse:
    _client: AsyncHubspot

    def __init__(self, client: AsyncHubspot) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithRawResponse:
        from .resources.account import AsyncAccountResourceWithRawResponse

        return AsyncAccountResourceWithRawResponse(self._client.account)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automation(self) -> automation.AsyncAutomationResourceWithRawResponse:
        from .resources.automation import AsyncAutomationResourceWithRawResponse

        return AsyncAutomationResourceWithRawResponse(self._client.automation)

    @cached_property
    def business_units(self) -> business_units.AsyncBusinessUnitsResourceWithRawResponse:
        from .resources.business_units import AsyncBusinessUnitsResourceWithRawResponse

        return AsyncBusinessUnitsResourceWithRawResponse(self._client.business_units)

    @cached_property
    def cms(self) -> cms.AsyncCmsResourceWithRawResponse:
        from .resources.cms import AsyncCmsResourceWithRawResponse

        return AsyncCmsResourceWithRawResponse(self._client.cms)

    @cached_property
    def communication_preferences(
        self,
    ) -> communication_preferences.AsyncCommunicationPreferencesResourceWithRawResponse:
        from .resources.communication_preferences import AsyncCommunicationPreferencesResourceWithRawResponse

        return AsyncCommunicationPreferencesResourceWithRawResponse(self._client.communication_preferences)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def crm(self) -> crm.AsyncCrmResourceWithRawResponse:
        from .resources.crm import AsyncCrmResourceWithRawResponse

        return AsyncCrmResourceWithRawResponse(self._client.crm)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def marketing(self) -> marketing.AsyncMarketingResourceWithRawResponse:
        from .resources.marketing import AsyncMarketingResourceWithRawResponse

        return AsyncMarketingResourceWithRawResponse(self._client.marketing)

    @cached_property
    def meta(self) -> meta.AsyncMetaResourceWithRawResponse:
        from .resources.meta import AsyncMetaResourceWithRawResponse

        return AsyncMetaResourceWithRawResponse(self._client.meta)

    @cached_property
    def scheduler(self) -> scheduler.AsyncSchedulerResourceWithRawResponse:
        from .resources.scheduler import AsyncSchedulerResourceWithRawResponse

        return AsyncSchedulerResourceWithRawResponse(self._client.scheduler)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithRawResponse:
        from .resources.settings import AsyncSettingsResourceWithRawResponse

        return AsyncSettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class HubspotWithStreamedResponse:
    _client: Hubspot

    def __init__(self, client: Hubspot) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AccountResourceWithStreamingResponse:
        from .resources.account import AccountResourceWithStreamingResponse

        return AccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automation(self) -> automation.AutomationResourceWithStreamingResponse:
        from .resources.automation import AutomationResourceWithStreamingResponse

        return AutomationResourceWithStreamingResponse(self._client.automation)

    @cached_property
    def business_units(self) -> business_units.BusinessUnitsResourceWithStreamingResponse:
        from .resources.business_units import BusinessUnitsResourceWithStreamingResponse

        return BusinessUnitsResourceWithStreamingResponse(self._client.business_units)

    @cached_property
    def cms(self) -> cms.CmsResourceWithStreamingResponse:
        from .resources.cms import CmsResourceWithStreamingResponse

        return CmsResourceWithStreamingResponse(self._client.cms)

    @cached_property
    def communication_preferences(
        self,
    ) -> communication_preferences.CommunicationPreferencesResourceWithStreamingResponse:
        from .resources.communication_preferences import CommunicationPreferencesResourceWithStreamingResponse

        return CommunicationPreferencesResourceWithStreamingResponse(self._client.communication_preferences)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def crm(self) -> crm.CrmResourceWithStreamingResponse:
        from .resources.crm import CrmResourceWithStreamingResponse

        return CrmResourceWithStreamingResponse(self._client.crm)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def marketing(self) -> marketing.MarketingResourceWithStreamingResponse:
        from .resources.marketing import MarketingResourceWithStreamingResponse

        return MarketingResourceWithStreamingResponse(self._client.marketing)

    @cached_property
    def meta(self) -> meta.MetaResourceWithStreamingResponse:
        from .resources.meta import MetaResourceWithStreamingResponse

        return MetaResourceWithStreamingResponse(self._client.meta)

    @cached_property
    def scheduler(self) -> scheduler.SchedulerResourceWithStreamingResponse:
        from .resources.scheduler import SchedulerResourceWithStreamingResponse

        return SchedulerResourceWithStreamingResponse(self._client.scheduler)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithStreamingResponse:
        from .resources.settings import SettingsResourceWithStreamingResponse

        return SettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncHubspotWithStreamedResponse:
    _client: AsyncHubspot

    def __init__(self, client: AsyncHubspot) -> None:
        self._client = client

    @cached_property
    def account(self) -> account.AsyncAccountResourceWithStreamingResponse:
        from .resources.account import AsyncAccountResourceWithStreamingResponse

        return AsyncAccountResourceWithStreamingResponse(self._client.account)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automation(self) -> automation.AsyncAutomationResourceWithStreamingResponse:
        from .resources.automation import AsyncAutomationResourceWithStreamingResponse

        return AsyncAutomationResourceWithStreamingResponse(self._client.automation)

    @cached_property
    def business_units(self) -> business_units.AsyncBusinessUnitsResourceWithStreamingResponse:
        from .resources.business_units import AsyncBusinessUnitsResourceWithStreamingResponse

        return AsyncBusinessUnitsResourceWithStreamingResponse(self._client.business_units)

    @cached_property
    def cms(self) -> cms.AsyncCmsResourceWithStreamingResponse:
        from .resources.cms import AsyncCmsResourceWithStreamingResponse

        return AsyncCmsResourceWithStreamingResponse(self._client.cms)

    @cached_property
    def communication_preferences(
        self,
    ) -> communication_preferences.AsyncCommunicationPreferencesResourceWithStreamingResponse:
        from .resources.communication_preferences import AsyncCommunicationPreferencesResourceWithStreamingResponse

        return AsyncCommunicationPreferencesResourceWithStreamingResponse(self._client.communication_preferences)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def crm(self) -> crm.AsyncCrmResourceWithStreamingResponse:
        from .resources.crm import AsyncCrmResourceWithStreamingResponse

        return AsyncCrmResourceWithStreamingResponse(self._client.crm)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def marketing(self) -> marketing.AsyncMarketingResourceWithStreamingResponse:
        from .resources.marketing import AsyncMarketingResourceWithStreamingResponse

        return AsyncMarketingResourceWithStreamingResponse(self._client.marketing)

    @cached_property
    def meta(self) -> meta.AsyncMetaResourceWithStreamingResponse:
        from .resources.meta import AsyncMetaResourceWithStreamingResponse

        return AsyncMetaResourceWithStreamingResponse(self._client.meta)

    @cached_property
    def scheduler(self) -> scheduler.AsyncSchedulerResourceWithStreamingResponse:
        from .resources.scheduler import AsyncSchedulerResourceWithStreamingResponse

        return AsyncSchedulerResourceWithStreamingResponse(self._client.scheduler)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithStreamingResponse:
        from .resources.settings import AsyncSettingsResourceWithStreamingResponse

        return AsyncSettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = Hubspot

AsyncClient = AsyncHubspot
