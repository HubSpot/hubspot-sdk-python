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
from .fees.fees import (
    FeesResource,
    AsyncFeesResource,
    FeesResourceWithRawResponse,
    AsyncFeesResourceWithRawResponse,
    FeesResourceWithStreamingResponse,
    AsyncFeesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .calls.calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from .carts.carts import (
    CartsResource,
    AsyncCartsResource,
    CartsResourceWithRawResponse,
    AsyncCartsResourceWithRawResponse,
    CartsResourceWithStreamingResponse,
    AsyncCartsResourceWithStreamingResponse,
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
from .orders.orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .quotes.quotes import (
    QuotesResource,
    AsyncQuotesResource,
    QuotesResourceWithRawResponse,
    AsyncQuotesResourceWithRawResponse,
    QuotesResourceWithStreamingResponse,
    AsyncQuotesResourceWithStreamingResponse,
)
from .courses.courses import (
    CoursesResource,
    AsyncCoursesResource,
    CoursesResourceWithRawResponse,
    AsyncCoursesResourceWithRawResponse,
    CoursesResourceWithStreamingResponse,
    AsyncCoursesResourceWithStreamingResponse,
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
from .listings.listings import (
    ListingsResource,
    AsyncListingsResource,
    ListingsResourceWithRawResponse,
    AsyncListingsResourceWithRawResponse,
    ListingsResourceWithStreamingResponse,
    AsyncListingsResourceWithStreamingResponse,
)
from .meetings.meetings import (
    MeetingsResource,
    AsyncMeetingsResource,
    MeetingsResourceWithRawResponse,
    AsyncMeetingsResourceWithRawResponse,
    MeetingsResourceWithStreamingResponse,
    AsyncMeetingsResourceWithStreamingResponse,
)
from .products.products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
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
from .contracts.contracts import (
    ContractsResource,
    AsyncContractsResource,
    ContractsResourceWithRawResponse,
    AsyncContractsResourceWithRawResponse,
    ContractsResourceWithStreamingResponse,
    AsyncContractsResourceWithStreamingResponse,
)
from .discounts.discounts import (
    DiscountsResource,
    AsyncDiscountsResource,
    DiscountsResourceWithRawResponse,
    AsyncDiscountsResourceWithRawResponse,
    DiscountsResourceWithStreamingResponse,
    AsyncDiscountsResourceWithStreamingResponse,
)
from .line_items.line_items import (
    LineItemsResource,
    AsyncLineItemsResource,
    LineItemsResourceWithRawResponse,
    AsyncLineItemsResourceWithRawResponse,
    LineItemsResourceWithStreamingResponse,
    AsyncLineItemsResourceWithStreamingResponse,
)
from .postal_mail.postal_mail import (
    PostalMailResource,
    AsyncPostalMailResource,
    PostalMailResourceWithRawResponse,
    AsyncPostalMailResourceWithRawResponse,
    PostalMailResourceWithStreamingResponse,
    AsyncPostalMailResourceWithStreamingResponse,
)
from .appointments.appointments import (
    AppointmentsResource,
    AsyncAppointmentsResource,
    AppointmentsResourceWithRawResponse,
    AsyncAppointmentsResourceWithRawResponse,
    AppointmentsResourceWithStreamingResponse,
    AsyncAppointmentsResourceWithStreamingResponse,
)
from .goal_targets.goal_targets import (
    GoalTargetsResource,
    AsyncGoalTargetsResource,
    GoalTargetsResourceWithRawResponse,
    AsyncGoalTargetsResourceWithRawResponse,
    GoalTargetsResourceWithStreamingResponse,
    AsyncGoalTargetsResourceWithStreamingResponse,
)
from .communications.communications import (
    CommunicationsResource,
    AsyncCommunicationsResource,
    CommunicationsResourceWithRawResponse,
    AsyncCommunicationsResourceWithRawResponse,
    CommunicationsResourceWithStreamingResponse,
    AsyncCommunicationsResourceWithStreamingResponse,
)
from .partner_clients.partner_clients import (
    PartnerClientsResource,
    AsyncPartnerClientsResource,
    PartnerClientsResourceWithRawResponse,
    AsyncPartnerClientsResourceWithRawResponse,
    PartnerClientsResourceWithStreamingResponse,
    AsyncPartnerClientsResourceWithStreamingResponse,
)
from .partner_services.partner_services import (
    PartnerServicesResource,
    AsyncPartnerServicesResource,
    PartnerServicesResourceWithRawResponse,
    AsyncPartnerServicesResourceWithRawResponse,
    PartnerServicesResourceWithStreamingResponse,
    AsyncPartnerServicesResourceWithStreamingResponse,
)
from .commerce_payments.commerce_payments import (
    CommercePaymentsResource,
    AsyncCommercePaymentsResource,
    CommercePaymentsResourceWithRawResponse,
    AsyncCommercePaymentsResourceWithRawResponse,
    CommercePaymentsResourceWithStreamingResponse,
    AsyncCommercePaymentsResourceWithStreamingResponse,
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
    def carts(self) -> CartsResource:
        return CartsResource(self._client)

    @cached_property
    def commerce_payments(self) -> CommercePaymentsResource:
        return CommercePaymentsResource(self._client)

    @cached_property
    def communications(self) -> CommunicationsResource:
        return CommunicationsResource(self._client)

    @cached_property
    def companies(self) -> CompaniesResource:
        return CompaniesResource(self._client)

    @cached_property
    def contacts(self) -> ContactsResource:
        return ContactsResource(self._client)

    @cached_property
    def contracts(self) -> ContractsResource:
        return ContractsResource(self._client)

    @cached_property
    def courses(self) -> CoursesResource:
        return CoursesResource(self._client)

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
    def discounts(self) -> DiscountsResource:
        return DiscountsResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResource:
        return FeedbackSubmissionsResource(self._client)

    @cached_property
    def fees(self) -> FeesResource:
        return FeesResource(self._client)

    @cached_property
    def goal_targets(self) -> GoalTargetsResource:
        return GoalTargetsResource(self._client)

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
    def listings(self) -> ListingsResource:
        return ListingsResource(self._client)

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
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def partner_clients(self) -> PartnerClientsResource:
        return PartnerClientsResource(self._client)

    @cached_property
    def partner_services(self) -> PartnerServicesResource:
        return PartnerServicesResource(self._client)

    @cached_property
    def postal_mail(self) -> PostalMailResource:
        return PostalMailResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def quotes(self) -> QuotesResource:
        return QuotesResource(self._client)

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
    def carts(self) -> AsyncCartsResource:
        return AsyncCartsResource(self._client)

    @cached_property
    def commerce_payments(self) -> AsyncCommercePaymentsResource:
        return AsyncCommercePaymentsResource(self._client)

    @cached_property
    def communications(self) -> AsyncCommunicationsResource:
        return AsyncCommunicationsResource(self._client)

    @cached_property
    def companies(self) -> AsyncCompaniesResource:
        return AsyncCompaniesResource(self._client)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        return AsyncContactsResource(self._client)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        return AsyncContractsResource(self._client)

    @cached_property
    def courses(self) -> AsyncCoursesResource:
        return AsyncCoursesResource(self._client)

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
    def discounts(self) -> AsyncDiscountsResource:
        return AsyncDiscountsResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResource:
        return AsyncFeedbackSubmissionsResource(self._client)

    @cached_property
    def fees(self) -> AsyncFeesResource:
        return AsyncFeesResource(self._client)

    @cached_property
    def goal_targets(self) -> AsyncGoalTargetsResource:
        return AsyncGoalTargetsResource(self._client)

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
    def listings(self) -> AsyncListingsResource:
        return AsyncListingsResource(self._client)

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
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResource:
        return AsyncPartnerClientsResource(self._client)

    @cached_property
    def partner_services(self) -> AsyncPartnerServicesResource:
        return AsyncPartnerServicesResource(self._client)

    @cached_property
    def postal_mail(self) -> AsyncPostalMailResource:
        return AsyncPostalMailResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def quotes(self) -> AsyncQuotesResource:
        return AsyncQuotesResource(self._client)

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
    def carts(self) -> CartsResourceWithRawResponse:
        return CartsResourceWithRawResponse(self._objects.carts)

    @cached_property
    def commerce_payments(self) -> CommercePaymentsResourceWithRawResponse:
        return CommercePaymentsResourceWithRawResponse(self._objects.commerce_payments)

    @cached_property
    def communications(self) -> CommunicationsResourceWithRawResponse:
        return CommunicationsResourceWithRawResponse(self._objects.communications)

    @cached_property
    def companies(self) -> CompaniesResourceWithRawResponse:
        return CompaniesResourceWithRawResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> ContactsResourceWithRawResponse:
        return ContactsResourceWithRawResponse(self._objects.contacts)

    @cached_property
    def contracts(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self._objects.contracts)

    @cached_property
    def courses(self) -> CoursesResourceWithRawResponse:
        return CoursesResourceWithRawResponse(self._objects.courses)

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
    def discounts(self) -> DiscountsResourceWithRawResponse:
        return DiscountsResourceWithRawResponse(self._objects.discounts)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResourceWithRawResponse:
        return FeedbackSubmissionsResourceWithRawResponse(self._objects.feedback_submissions)

    @cached_property
    def fees(self) -> FeesResourceWithRawResponse:
        return FeesResourceWithRawResponse(self._objects.fees)

    @cached_property
    def goal_targets(self) -> GoalTargetsResourceWithRawResponse:
        return GoalTargetsResourceWithRawResponse(self._objects.goal_targets)

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
    def listings(self) -> ListingsResourceWithRawResponse:
        return ListingsResourceWithRawResponse(self._objects.listings)

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
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._objects.orders)

    @cached_property
    def partner_clients(self) -> PartnerClientsResourceWithRawResponse:
        return PartnerClientsResourceWithRawResponse(self._objects.partner_clients)

    @cached_property
    def partner_services(self) -> PartnerServicesResourceWithRawResponse:
        return PartnerServicesResourceWithRawResponse(self._objects.partner_services)

    @cached_property
    def postal_mail(self) -> PostalMailResourceWithRawResponse:
        return PostalMailResourceWithRawResponse(self._objects.postal_mail)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._objects.products)

    @cached_property
    def quotes(self) -> QuotesResourceWithRawResponse:
        return QuotesResourceWithRawResponse(self._objects.quotes)

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
    def carts(self) -> AsyncCartsResourceWithRawResponse:
        return AsyncCartsResourceWithRawResponse(self._objects.carts)

    @cached_property
    def commerce_payments(self) -> AsyncCommercePaymentsResourceWithRawResponse:
        return AsyncCommercePaymentsResourceWithRawResponse(self._objects.commerce_payments)

    @cached_property
    def communications(self) -> AsyncCommunicationsResourceWithRawResponse:
        return AsyncCommunicationsResourceWithRawResponse(self._objects.communications)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithRawResponse:
        return AsyncCompaniesResourceWithRawResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithRawResponse:
        return AsyncContactsResourceWithRawResponse(self._objects.contacts)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self._objects.contracts)

    @cached_property
    def courses(self) -> AsyncCoursesResourceWithRawResponse:
        return AsyncCoursesResourceWithRawResponse(self._objects.courses)

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
    def discounts(self) -> AsyncDiscountsResourceWithRawResponse:
        return AsyncDiscountsResourceWithRawResponse(self._objects.discounts)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResourceWithRawResponse:
        return AsyncFeedbackSubmissionsResourceWithRawResponse(self._objects.feedback_submissions)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithRawResponse:
        return AsyncFeesResourceWithRawResponse(self._objects.fees)

    @cached_property
    def goal_targets(self) -> AsyncGoalTargetsResourceWithRawResponse:
        return AsyncGoalTargetsResourceWithRawResponse(self._objects.goal_targets)

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
    def listings(self) -> AsyncListingsResourceWithRawResponse:
        return AsyncListingsResourceWithRawResponse(self._objects.listings)

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
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._objects.orders)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResourceWithRawResponse:
        return AsyncPartnerClientsResourceWithRawResponse(self._objects.partner_clients)

    @cached_property
    def partner_services(self) -> AsyncPartnerServicesResourceWithRawResponse:
        return AsyncPartnerServicesResourceWithRawResponse(self._objects.partner_services)

    @cached_property
    def postal_mail(self) -> AsyncPostalMailResourceWithRawResponse:
        return AsyncPostalMailResourceWithRawResponse(self._objects.postal_mail)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._objects.products)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithRawResponse:
        return AsyncQuotesResourceWithRawResponse(self._objects.quotes)

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
    def carts(self) -> CartsResourceWithStreamingResponse:
        return CartsResourceWithStreamingResponse(self._objects.carts)

    @cached_property
    def commerce_payments(self) -> CommercePaymentsResourceWithStreamingResponse:
        return CommercePaymentsResourceWithStreamingResponse(self._objects.commerce_payments)

    @cached_property
    def communications(self) -> CommunicationsResourceWithStreamingResponse:
        return CommunicationsResourceWithStreamingResponse(self._objects.communications)

    @cached_property
    def companies(self) -> CompaniesResourceWithStreamingResponse:
        return CompaniesResourceWithStreamingResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> ContactsResourceWithStreamingResponse:
        return ContactsResourceWithStreamingResponse(self._objects.contacts)

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self._objects.contracts)

    @cached_property
    def courses(self) -> CoursesResourceWithStreamingResponse:
        return CoursesResourceWithStreamingResponse(self._objects.courses)

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
    def discounts(self) -> DiscountsResourceWithStreamingResponse:
        return DiscountsResourceWithStreamingResponse(self._objects.discounts)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> FeedbackSubmissionsResourceWithStreamingResponse:
        return FeedbackSubmissionsResourceWithStreamingResponse(self._objects.feedback_submissions)

    @cached_property
    def fees(self) -> FeesResourceWithStreamingResponse:
        return FeesResourceWithStreamingResponse(self._objects.fees)

    @cached_property
    def goal_targets(self) -> GoalTargetsResourceWithStreamingResponse:
        return GoalTargetsResourceWithStreamingResponse(self._objects.goal_targets)

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
    def listings(self) -> ListingsResourceWithStreamingResponse:
        return ListingsResourceWithStreamingResponse(self._objects.listings)

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
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._objects.orders)

    @cached_property
    def partner_clients(self) -> PartnerClientsResourceWithStreamingResponse:
        return PartnerClientsResourceWithStreamingResponse(self._objects.partner_clients)

    @cached_property
    def partner_services(self) -> PartnerServicesResourceWithStreamingResponse:
        return PartnerServicesResourceWithStreamingResponse(self._objects.partner_services)

    @cached_property
    def postal_mail(self) -> PostalMailResourceWithStreamingResponse:
        return PostalMailResourceWithStreamingResponse(self._objects.postal_mail)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._objects.products)

    @cached_property
    def quotes(self) -> QuotesResourceWithStreamingResponse:
        return QuotesResourceWithStreamingResponse(self._objects.quotes)

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
    def carts(self) -> AsyncCartsResourceWithStreamingResponse:
        return AsyncCartsResourceWithStreamingResponse(self._objects.carts)

    @cached_property
    def commerce_payments(self) -> AsyncCommercePaymentsResourceWithStreamingResponse:
        return AsyncCommercePaymentsResourceWithStreamingResponse(self._objects.commerce_payments)

    @cached_property
    def communications(self) -> AsyncCommunicationsResourceWithStreamingResponse:
        return AsyncCommunicationsResourceWithStreamingResponse(self._objects.communications)

    @cached_property
    def companies(self) -> AsyncCompaniesResourceWithStreamingResponse:
        return AsyncCompaniesResourceWithStreamingResponse(self._objects.companies)

    @cached_property
    def contacts(self) -> AsyncContactsResourceWithStreamingResponse:
        return AsyncContactsResourceWithStreamingResponse(self._objects.contacts)

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self._objects.contracts)

    @cached_property
    def courses(self) -> AsyncCoursesResourceWithStreamingResponse:
        return AsyncCoursesResourceWithStreamingResponse(self._objects.courses)

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
    def discounts(self) -> AsyncDiscountsResourceWithStreamingResponse:
        return AsyncDiscountsResourceWithStreamingResponse(self._objects.discounts)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._objects.emails)

    @cached_property
    def feedback_submissions(self) -> AsyncFeedbackSubmissionsResourceWithStreamingResponse:
        return AsyncFeedbackSubmissionsResourceWithStreamingResponse(self._objects.feedback_submissions)

    @cached_property
    def fees(self) -> AsyncFeesResourceWithStreamingResponse:
        return AsyncFeesResourceWithStreamingResponse(self._objects.fees)

    @cached_property
    def goal_targets(self) -> AsyncGoalTargetsResourceWithStreamingResponse:
        return AsyncGoalTargetsResourceWithStreamingResponse(self._objects.goal_targets)

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
    def listings(self) -> AsyncListingsResourceWithStreamingResponse:
        return AsyncListingsResourceWithStreamingResponse(self._objects.listings)

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
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._objects.orders)

    @cached_property
    def partner_clients(self) -> AsyncPartnerClientsResourceWithStreamingResponse:
        return AsyncPartnerClientsResourceWithStreamingResponse(self._objects.partner_clients)

    @cached_property
    def partner_services(self) -> AsyncPartnerServicesResourceWithStreamingResponse:
        return AsyncPartnerServicesResourceWithStreamingResponse(self._objects.partner_services)

    @cached_property
    def postal_mail(self) -> AsyncPostalMailResourceWithStreamingResponse:
        return AsyncPostalMailResourceWithStreamingResponse(self._objects.postal_mail)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._objects.products)

    @cached_property
    def quotes(self) -> AsyncQuotesResourceWithStreamingResponse:
        return AsyncQuotesResourceWithStreamingResponse(self._objects.quotes)

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
