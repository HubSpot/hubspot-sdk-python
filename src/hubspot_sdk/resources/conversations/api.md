# Conversations

Types:

```python
from hubspot_sdk.types.conversations import (
    AgentActor,
    BatchResponsePublicActor,
    BatchResponsePublicActorWithErrors,
    BotActor,
    CollectionResponsePublicMessageForwardPaging,
    CollectionResponsePublicThreadForwardPaging,
    CollectionResponseWithTotalPublicChannelAccountForwardPaging,
    CollectionResponseWithTotalPublicChannelForwardPaging,
    CollectionResponseWithTotalPublicInboxForwardPaging,
    ContactAddress,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactProfile,
    ContactURL,
    ConversationsPublicConversationsMessage,
    EmailActor,
    IntegratorActor,
    LlmActor,
    PublicActor,
    PublicAssignmentMessage,
    PublicChannel,
    PublicChannelAccount,
    PublicClient,
    PublicComment,
    PublicCommentEgg,
    PublicContact,
    PublicConversationsMessageEgg,
    PublicDeliveryIdentifier,
    PublicFile,
    PublicFileEgg,
    PublicInbox,
    PublicLocation,
    PublicMessage,
    PublicMessageContent,
    PublicMessageEgg,
    PublicMessageFailureDetails,
    PublicMessageHeader,
    PublicMessageStatus,
    PublicQuickReplies,
    PublicQuickRepliesEgg,
    PublicRecipient,
    PublicRecipientEgg,
    PublicSender,
    PublicSocialMediaEgg,
    PublicSocialMetadataAttachment,
    PublicThread,
    PublicThreadAssociations,
    PublicThreadInboxChange,
    PublicThreadStatusChange,
    PublicThreadUpdateRequest,
    PublicUnsupportedContent,
    PublicWelcomeMessage,
    PublicWhatsAppTemplateMetadata,
    QuickReply,
    SocialMetadata,
    SystemActor,
    VisitorActor,
)
```

## Actors

Methods:

- <code title="post /conversations/v3/conversations/actors/batch/read">client.conversations.actors.<a href="./src/hubspot_sdk/resources/conversations/actors.py">batch_read</a>(\*\*<a href="src/hubspot_sdk/types/conversations/actor_batch_read_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/batch_response_public_actor.py">BatchResponsePublicActor</a></code>
- <code title="get /conversations/v3/conversations/actors/{actorId}">client.conversations.actors.<a href="./src/hubspot_sdk/resources/conversations/actors.py">get</a>(actor_id, \*\*<a href="src/hubspot_sdk/types/conversations/actor_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_actor.py">PublicActor</a></code>

## ChannelAccounts

Methods:

- <code title="get /conversations/v3/conversations/channel-accounts">client.conversations.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/channel_accounts.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/channel_account_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">SyncPage[PublicChannelAccount]</a></code>
- <code title="get /conversations/v3/conversations/channel-accounts/{channelAccountId}">client.conversations.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/channel_accounts.py">get</a>(channel_account_id, \*\*<a href="src/hubspot_sdk/types/conversations/channel_account_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

## Channels

Methods:

- <code title="get /conversations/v3/conversations/channels">client.conversations.channels.<a href="./src/hubspot_sdk/resources/conversations/channels.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/channel_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel.py">SyncPage[PublicChannel]</a></code>
- <code title="get /conversations/v3/conversations/channels/{channelId}">client.conversations.channels.<a href="./src/hubspot_sdk/resources/conversations/channels.py">get</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel.py">PublicChannel</a></code>

## CustomChannels

Types:

```python
from hubspot_sdk.types.conversations import (
    ChannelIntegrationMessageEgg,
    ChannelIntegrationParticipant,
    CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging,
    ContactAttachment,
    FileAttachment,
    LocationAttachment,
    MessageHeaderAttachment,
    PreResolvedContact,
    PreResolvedContacts,
    PublicChannelAccountEgg,
    PublicChannelAccountStagingToken,
    PublicChannelAccountStagingTokenUpdateRequest,
    PublicChannelAccountUpdateRequest,
    PublicChannelIntegrationChannel,
    PublicChannelIntegrationChannelCreate,
    PublicChannelIntegrationChannelPatch,
    PublicChannelIntegrationMessageUpdateRequest,
    PublicConversationsMessage,
    QuickRepliesAttachment,
    SocialMetadataIntegrationAttachment,
    UnsupportedContentAttachment,
)
```

Methods:

- <code title="post /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">create</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">update</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="get /conversations/v3/custom-channels/">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">SyncPage[PublicChannelIntegrationChannel]</a></code>
- <code title="delete /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">delete</a>(channel_id) -> None</code>
- <code title="get /conversations/v3/custom-channels/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">get</a>(channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>

### ChannelAccountStagingTokens

Methods:

- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-account-staging-tokens/{accountToken}">client.conversations.custom_channels.channel_account_staging_tokens.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_account_staging_tokens.py">update</a>(account_token, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_staging_token_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account_staging_token.py">PublicChannelAccountStagingToken</a></code>

### ChannelAccounts

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">update</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">list</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">SyncPage[PublicChannelAccount]</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">get</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

### Messages

Methods:

- <code title="post /conversations/v3/custom-channels/{channelId}/messages">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>
- <code title="patch /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">update</a>(message_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>
- <code title="get /conversations/v3/custom-channels/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">get</a>(message_id, \*, channel_id) -> <a href="./src/hubspot_sdk/types/conversations/conversations_public_conversations_message.py">ConversationsPublicConversationsMessage</a></code>

## Inboxes

Methods:

- <code title="get /conversations/v3/conversations/inboxes">client.conversations.inboxes.<a href="./src/hubspot_sdk/resources/conversations/inboxes.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/inbox_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_inbox.py">SyncPage[PublicInbox]</a></code>
- <code title="get /conversations/v3/conversations/inboxes/{inboxId}">client.conversations.inboxes.<a href="./src/hubspot_sdk/resources/conversations/inboxes.py">get</a>(inbox_id, \*\*<a href="src/hubspot_sdk/types/conversations/inbox_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_inbox.py">PublicInbox</a></code>

## Messages

Methods:

- <code title="post /conversations/v3/conversations/threads/{threadId}/messages">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">create</a>(thread_id) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">PublicMessage</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">list</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">SyncPage[PublicMessage]</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages/{messageId}">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">get</a>(message_id, \*, thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message.py">PublicMessage</a></code>
- <code title="get /conversations/v3/conversations/threads/{threadId}/messages/{messageId}/original-content">client.conversations.messages.<a href="./src/hubspot_sdk/resources/conversations/messages.py">get_original_content</a>(message_id, \*, thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/message_get_original_content_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_message_content.py">PublicMessageContent</a></code>

## Threads

Methods:

- <code title="patch /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">update</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/thread_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">PublicThread</a></code>
- <code title="get /conversations/v3/conversations/threads">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/thread_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">SyncPage[PublicThread]</a></code>
- <code title="delete /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">delete</a>(thread_id) -> None</code>
- <code title="get /conversations/v3/conversations/threads/{threadId}">client.conversations.threads.<a href="./src/hubspot_sdk/resources/conversations/threads.py">get</a>(thread_id, \*\*<a href="src/hubspot_sdk/types/conversations/thread_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_thread.py">PublicThread</a></code>

## VisitorIdentification

Types:

```python
from hubspot_sdk.types.conversations import (
    IdentificationTokenGenerationRequest,
    IdentificationTokenResponse,
)
```

Methods:

- <code title="post /visitor-identification/v3/tokens/create">client.conversations.visitor_identification.<a href="./src/hubspot_sdk/resources/conversations/visitor_identification.py">generate_token</a>(\*\*<a href="src/hubspot_sdk/types/conversations/visitor_identification_generate_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/identification_token_response.py">IdentificationTokenResponse</a></code>
