# Crm

## Objects

Types:

```python
from hubspot_sdk.types.crm import (
    AssociatedID,
    AssociationSpec,
    AssociationSpecWithLabel,
    BatchInputSimplePublicObjectBatchInput,
    BatchInputSimplePublicObjectBatchInputForCreate,
    BatchInputSimplePublicObjectBatchInputUpsert,
    BatchInputSimplePublicObjectID,
    BatchReadInputSimplePublicObjectID,
    BatchResponsePublicDefaultAssociation,
    BatchResponseSimplePublicObject,
    BatchResponseSimplePublicUpsertObject,
    CollectionResponseAssociatedID,
    CollectionResponseMultiAssociatedObjectWithLabelForwardPaging,
    CollectionResponseSimplePublicObjectWithAssociationsForwardPaging,
    CollectionResponseWithTotalSimplePublicObject,
    Filter,
    FilterGroup,
    LabelsBetweenObjectPair,
    MultiAssociatedObjectWithLabel,
    Paging,
    PreviousPage,
    PublicAssociationsForObject,
    PublicDefaultAssociation,
    PublicGdprDeleteInput,
    PublicMergeInput,
    PublicObjectID,
    PublicObjectSearchRequest,
    SimplePublicObject,
    SimplePublicObjectBatchInput,
    SimplePublicObjectBatchInputForCreate,
    SimplePublicObjectBatchInputUpsert,
    SimplePublicObjectID,
    SimplePublicObjectInput,
    SimplePublicObjectInputForCreate,
    SimplePublicObjectWithAssociations,
    SimplePublicUpsertObject,
    StandardError,
    ValueWithTimestamp,
)
```

### Contacts

Methods:

- <code title="post /crm/objects/2026-03/{objectType}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="patch /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">update</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/{objectType}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="delete /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">delete</a>(object_id, \*, object_type) -> None</code>
- <code title="post /crm/objects/2026-03/{objectType}/gdpr-delete">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">gdpr_delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_gdpr_delete_params.py">params</a>) -> None</code>
- <code title="get /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">get</a>(object_id, \*, object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SimplePublicObjectWithAssociations</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/merge">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">merge</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/search">client.crm.objects.contacts.<a href="./src/hubspot_sdk/resources/crm/objects/contacts.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/contact_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>

### Custom

Methods:

- <code title="post /crm/objects/2026-03/{objectType}/batch/create">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/update">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="get /crm/objects/2026-03/{objectType}">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">list</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object_with_associations.py">SyncPage[SimplePublicObjectWithAssociations]</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/archive">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/read">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/merge">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">merge</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_merge_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/simple_public_object.py">SimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/search">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">search</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_search_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/collection_response_with_total_simple_public_object.py">CollectionResponseWithTotalSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/upsert">client.crm.objects.custom.<a href="./src/hubspot_sdk/resources/crm/objects/custom.py">upsert</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/custom_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>

### Tasks

Methods:

- <code title="delete /crm/objects/2026-03/{objectType}/{objectId}">client.crm.objects.tasks.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/tasks.py">delete</a>(object_id, \*, object_type) -> None</code>

#### Batch

Methods:

- <code title="post /crm/objects/2026-03/{objectType}/batch/create">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">create</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/update">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">update</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/archive">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">delete</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_delete_params.py">params</a>) -> None</code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/read">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">get</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_object.py">BatchResponseSimplePublicObject</a></code>
- <code title="post /crm/objects/2026-03/{objectType}/batch/upsert">client.crm.objects.tasks.batch.<a href="./src/hubspot_sdk/resources/crm/objects/tasks/batch.py">upsert</a>(object_type, \*\*<a href="src/hubspot_sdk/types/crm/objects/tasks/batch_upsert_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/crm/batch_response_simple_public_upsert_object.py">BatchResponseSimplePublicUpsertObject</a></code>
