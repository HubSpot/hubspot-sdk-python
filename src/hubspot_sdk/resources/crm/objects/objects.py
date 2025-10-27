# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
)
from .objects_ import objects_ as objects
from ...._compat import cached_property
from .calls.calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from .deal_splits import (
    DealSplitsResource,
    AsyncDealSplitsResource,
    DealSplitsResourceWithRawResponse,
    AsyncDealSplitsResourceWithRawResponse,
    DealSplitsResourceWithStreamingResponse,
    AsyncDealSplitsResourceWithStreamingResponse,
)
from .deals.deals import (
    DealsResource,
    AsyncDealsResource,
    DealsResourceWithRawResponse,
    AsyncDealsResourceWithRawResponse,
    DealsResourceWithStreamingResponse,
    AsyncDealsResourceWithStreamingResponse,
)
from .leads.leads import (
    LeadsResource,
    AsyncLeadsResource,
    LeadsResourceWithRawResponse,
    AsyncLeadsResourceWithRawResponse,
    LeadsResourceWithStreamingResponse,
    AsyncLeadsResourceWithStreamingResponse,
)
from .notes.notes import (
    NotesResource,
    AsyncNotesResource,
    NotesResourceWithRawResponse,
    AsyncNotesResourceWithRawResponse,
    NotesResourceWithStreamingResponse,
    AsyncNotesResourceWithStreamingResponse,
)
from .tasks.tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from .taxes.taxes import (
    TaxesResource,
    AsyncTaxesResource,
    TaxesResourceWithRawResponse,
    AsyncTaxesResourceWithRawResponse,
    TaxesResourceWithStreamingResponse,
    AsyncTaxesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .custom.custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from .emails.emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from .tickets.tickets import (
    TicketsResource,
    AsyncTicketsResource,
    TicketsResourceWithRawResponse,
    AsyncTicketsResourceWithRawResponse,
    TicketsResourceWithStreamingResponse,
    AsyncTicketsResourceWithStreamingResponse,
)
from .contacts.contacts import (
    ContactsResource,
    AsyncContactsResource,
    ContactsResourceWithRawResponse,
    AsyncContactsResourceWithRawResponse,
    ContactsResourceWithStreamingResponse,
    AsyncContactsResourceWithStreamingResponse,
)
from .invoices.invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from .meetings.meetings import (
    MeetingsResource,
    AsyncMeetingsResource,
    MeetingsResourceWithRawResponse,
    AsyncMeetingsResourceWithRawResponse,
    MeetingsResourceWithStreamingResponse,
    AsyncMeetingsResourceWithStreamingResponse,
)
from .services.services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from .companies.companies import (
    CompaniesResource,
    AsyncCompaniesResource,
    CompaniesResourceWithRawResponse,
    AsyncCompaniesResourceWithRawResponse,
    CompaniesResourceWithStreamingResponse,
    AsyncCompaniesResourceWithStreamingResponse,
)
from .line_items.line_items import (
    LineItemsResource,
    AsyncLineItemsResource,
    LineItemsResourceWithRawResponse,
    AsyncLineItemsResourceWithRawResponse,
    LineItemsResourceWithStreamingResponse,
    AsyncLineItemsResourceWithStreamingResponse,
)
from .appointments.appointments import (
    AppointmentsResource,
    AsyncAppointmentsResource,
    AppointmentsResourceWithRawResponse,
    AsyncAppointmentsResourceWithRawResponse,
    AppointmentsResourceWithStreamingResponse,
    AsyncAppointmentsResourceWithStreamingResponse,
)
from .partner_clients.partner_clients import (
    PartnerClientsResource,
    AsyncPartnerClientsResource,
    PartnerClientsResourceWithRawResponse,
    AsyncPartnerClientsResourceWithRawResponse,
    PartnerClientsResourceWithStreamingResponse,
    AsyncPartnerClientsResourceWithStreamingResponse,
)
from .feedback_submissions.feedback_submissions import (
    FeedbackSubmissionsResource,
    AsyncFeedbackSubmissionsResource,
    FeedbackSubmissionsResourceWithRawResponse,
    AsyncFeedbackSubmissionsResourceWithRawResponse,
    FeedbackSubmissionsResourceWithStreamingResponse,
    AsyncFeedbackSubmissionsResourceWithStreamingResponse,
)

__all__ = ["ObjectsResource", "AsyncObjectsResource"]


class ObjectsResource(SyncAPIResource):
    @cached_property
    def appointments(self) -> AppointmentsResource:
        return AppointmentsResource(self._client)

    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

    @cached_property
    def deal_splits(self) -> DealSplitsResource:
        return DealSplitsResource(self._client)

    @cached_property
    def deals(self) -> DealsResource:
        return DealsResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResource:
        return FeedbackSubmissionsResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def leads(self) -> LeadsResource:
        return LeadsResource(self._client)

    @cached_property
    def line_items(self) -> LineItemsResource:
        return LineItemsResource(self._client)

    @cached_property
    def meetings(self) -> MeetingsResource:
        return MeetingsResource(self._client)

    @cached_property
    def notes(self) -> NotesResource:
        return NotesResource(self._client)

    @cached_property
    def objects(self) -> objects.ObjectsResource:
        return objects.ObjectsResource(self._client)

    @cached_property
    def partner_clients(self) -> PartnerClientsResource:
        return PartnerClientsResource(self._client)

    @cached_property
    def schemas(self) -> SchemasResource:
        return SchemasResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def taxes(self) -> TaxesResource:
        return TaxesResource(self._client)

    @cached_property
    def tickets(self) -> TicketsResource:
        return TicketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ObjectsResourceWithStreamingResponse(self)


class AsyncObjectsResource(AsyncAPIResource):
    @cached_property
    def appointments(self) -> AsyncAppointmentsResource:
        return AsyncAppointmentsResource(self._client)

    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResource:
        return AsyncDealSplitsResource(self._client)

    @cached_property
    def deals(self) -> AsyncDealsResource:
        return AsyncDealsResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResource:
        return AsyncFeedbackSubmissionsResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def leads(self) -> AsyncLeadsResource:
        return AsyncLeadsResource(self._client)

    @cached_property
    def line_items(self) -> AsyncLineItemsResource:
        return AsyncLineItemsResource(self._client)

    @cached_property
    def meetings(self) -> AsyncMeetingsResource:
        return AsyncMeetingsResource(self._client)

    @cached_property
    def notes(self) -> AsyncNotesResource:
        return AsyncNotesResource(self._client)

    @cached_property
    def objects(self) -> objects.AsyncObjectsResource:
        return objects.AsyncObjectsResource(self._client)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResource:
        return AsyncPartnerClientsResource(self._client)

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        return AsyncSchemasResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def taxes(self) -> AsyncTaxesResource:
        return AsyncTaxesResource(self._client)

    @cached_property
    def tickets(self) -> AsyncTicketsResource:
        return AsyncTicketsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncObjectsResourceWithStreamingResponse(self)


class ObjectsResourceWithRawResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

    @cached_property
    def appointments(self) -> AppointmentsResourceWithRawResponse:
        return AppointmentsResourceWithRawResponse(self._objects.appointments)

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._objects.calls)

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._objects.contacts)

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._objects.custom)

    @cached_property
    def deal_splits(self) -> DealSplitsResourceWithRawResponse:
        return DealSplitsResourceWithRawResponse(self._objects.deal_splits)

    @cached_property
    def deals(self) -> DealsResourceWithRawResponse:
        return DealsResourceWithRawResponse(self._objects.deals)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResourceWithRawResponse:
        return FeedbackSubmissionsResourceWithRawResponse(self._objects.feedback_submissions)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._objects.invoices)

    @cached_property
    def leads(self) -> LeadsResourceWithRawResponse:
        return LeadsResourceWithRawResponse(self._objects.leads)

    @cached_property
    def line_items(self) -> LineItemsResourceWithRawResponse:
        return LineItemsResourceWithRawResponse(self._objects.line_items)

    @cached_property
    def meetings(self) -> MeetingsResourceWithRawResponse:
        return MeetingsResourceWithRawResponse(self._objects.meetings)

    @cached_property
    def notes(self) -> NotesResourceWithRawResponse:
        return NotesResourceWithRawResponse(self._objects.notes)

    @cached_property
    def objects(self) -> objects.ObjectsResourceWithRawResponse:
        return objects.ObjectsResourceWithRawResponse(self._objects.objects)

    @cached_property
    def partner_clients(self) -> PartnerClientsResourceWithRawResponse:
        return PartnerClientsResourceWithRawResponse(self._objects.partner_clients)

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self._objects.schemas)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._objects.services)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._objects.tasks)

    @cached_property
    def taxes(self) -> TaxesResourceWithRawResponse:
        return TaxesResourceWithRawResponse(self._objects.taxes)

    @cached_property
    def tickets(self) -> TicketsResourceWithRawResponse:
        return TicketsResourceWithRawResponse(self._objects.tickets)


class AsyncObjectsResourceWithRawResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

    @cached_property
    def appointments(self) -> AsyncAppointmentsResourceWithRawResponse:
        return AsyncAppointmentsResourceWithRawResponse(self._objects.appointments)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._objects.calls)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._objects.contacts)

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._objects.custom)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResourceWithRawResponse:
        return AsyncDealSplitsResourceWithRawResponse(self._objects.deal_splits)

    @cached_property
    def deals(self) -> AsyncDealsResourceWithRawResponse:
        return AsyncDealsResourceWithRawResponse(self._objects.deals)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResourceWithRawResponse:
        return AsyncFeedbackSubmissionsResourceWithRawResponse(self._objects.feedback_submissions)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._objects.invoices)

    @cached_property
    def leads(self) -> AsyncLeadsResourceWithRawResponse:
        return AsyncLeadsResourceWithRawResponse(self._objects.leads)

    @cached_property
    def line_items(self) -> AsyncLineItemsResourceWithRawResponse:
        return AsyncLineItemsResourceWithRawResponse(self._objects.line_items)

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithRawResponse:
        return AsyncMeetingsResourceWithRawResponse(self._objects.meetings)

    @cached_property
    def notes(self) -> AsyncNotesResourceWithRawResponse:
        return AsyncNotesResourceWithRawResponse(self._objects.notes)

    @cached_property
    def objects(self) -> objects.AsyncObjectsResourceWithRawResponse:
        return objects.AsyncObjectsResourceWithRawResponse(self._objects.objects)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResourceWithRawResponse:
        return AsyncPartnerClientsResourceWithRawResponse(self._objects.partner_clients)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self._objects.schemas)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._objects.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._objects.tasks)

    @cached_property
    def taxes(self) -> AsyncTaxesResourceWithRawResponse:
        return AsyncTaxesResourceWithRawResponse(self._objects.taxes)

    @cached_property
    def tickets(self) -> AsyncTicketsResourceWithRawResponse:
        return AsyncTicketsResourceWithRawResponse(self._objects.tickets)


class ObjectsResourceWithStreamingResponse:
    def __init__(self, objects: ObjectsResource) -> None:
        self._objects = objects

    @cached_property
    def appointments(self) -> AppointmentsResourceWithStreamingResponse:
        return AppointmentsResourceWithStreamingResponse(self._objects.appointments)

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._objects.calls)

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._objects.contacts)

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._objects.custom)

    @cached_property
    def deal_splits(self) -> DealSplitsResourceWithStreamingResponse:
        return DealSplitsResourceWithStreamingResponse(self._objects.deal_splits)

    @cached_property
    def deals(self) -> DealsResourceWithStreamingResponse:
        return DealsResourceWithStreamingResponse(self._objects.deals)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResourceWithStreamingResponse:
        return FeedbackSubmissionsResourceWithStreamingResponse(self._objects.feedback_submissions)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._objects.invoices)

    @cached_property
    def leads(self) -> LeadsResourceWithStreamingResponse:
        return LeadsResourceWithStreamingResponse(self._objects.leads)

    @cached_property
    def line_items(self) -> LineItemsResourceWithStreamingResponse:
        return LineItemsResourceWithStreamingResponse(self._objects.line_items)

    @cached_property
    def meetings(self) -> MeetingsResourceWithStreamingResponse:
        return MeetingsResourceWithStreamingResponse(self._objects.meetings)

    @cached_property
    def notes(self) -> NotesResourceWithStreamingResponse:
        return NotesResourceWithStreamingResponse(self._objects.notes)

    @cached_property
    def objects(self) -> objects.ObjectsResourceWithStreamingResponse:
        return objects.ObjectsResourceWithStreamingResponse(self._objects.objects)

    @cached_property
    def partner_clients(self) -> PartnerClientsResourceWithStreamingResponse:
        return PartnerClientsResourceWithStreamingResponse(self._objects.partner_clients)

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self._objects.schemas)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._objects.services)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._objects.tasks)

    @cached_property
    def taxes(self) -> TaxesResourceWithStreamingResponse:
        return TaxesResourceWithStreamingResponse(self._objects.taxes)

    @cached_property
    def tickets(self) -> TicketsResourceWithStreamingResponse:
        return TicketsResourceWithStreamingResponse(self._objects.tickets)


class AsyncObjectsResourceWithStreamingResponse:
    def __init__(self, objects: AsyncObjectsResource) -> None:
        self._objects = objects

    @cached_property
    def appointments(self) -> AsyncAppointmentsResourceWithStreamingResponse:
        return AsyncAppointmentsResourceWithStreamingResponse(self._objects.appointments)

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._objects.calls)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._objects.contacts)

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._objects.custom)

    @cached_property
    def deal_splits(self) -> AsyncDealSplitsResourceWithStreamingResponse:
        return AsyncDealSplitsResourceWithStreamingResponse(self._objects.deal_splits)

    @cached_property
    def deals(self) -> AsyncDealsResourceWithStreamingResponse:
        return AsyncDealsResourceWithStreamingResponse(self._objects.deals)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResourceWithStreamingResponse:
        return AsyncFeedbackSubmissionsResourceWithStreamingResponse(self._objects.feedback_submissions)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._objects.invoices)

    @cached_property
    def leads(self) -> AsyncLeadsResourceWithStreamingResponse:
        return AsyncLeadsResourceWithStreamingResponse(self._objects.leads)

    @cached_property
    def line_items(self) -> AsyncLineItemsResourceWithStreamingResponse:
        return AsyncLineItemsResourceWithStreamingResponse(self._objects.line_items)

    @cached_property
    def meetings(self) -> AsyncMeetingsResourceWithStreamingResponse:
        return AsyncMeetingsResourceWithStreamingResponse(self._objects.meetings)

    @cached_property
    def notes(self) -> AsyncNotesResourceWithStreamingResponse:
        return AsyncNotesResourceWithStreamingResponse(self._objects.notes)

    @cached_property
    def objects(self) -> objects.AsyncObjectsResourceWithStreamingResponse:
        return objects.AsyncObjectsResourceWithStreamingResponse(self._objects.objects)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResourceWithStreamingResponse:
        return AsyncPartnerClientsResourceWithStreamingResponse(self._objects.partner_clients)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self._objects.schemas)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._objects.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._objects.tasks)

    @cached_property
    def taxes(self) -> AsyncTaxesResourceWithStreamingResponse:
        return AsyncTaxesResourceWithStreamingResponse(self._objects.taxes)

    @cached_property
    def tickets(self) -> AsyncTicketsResourceWithStreamingResponse:
        return AsyncTicketsResourceWithStreamingResponse(self._objects.tickets)
