# Conversations

## CustomChannels

Types:

```python
from hubspot_sdk.types.conversations import (
    ChannelIntegrationMessageEgg,
    ChannelIntegrationParticipant,
    CollectionResponseWithTotalPublicChannelAccount,
    CollectionResponseWithTotalPublicChannelIntegrationChannel,
    ContactAddress,
    ContactAttachment,
    ContactEmail,
    ContactName,
    ContactOrg,
    ContactPhone,
    ContactProfile,
    ContactURL,
    FileAttachment,
    LocationAttachment,
    MessageHeaderAttachment,
    PreResolvedContact,
    PreResolvedContacts,
    PublicChannelAccount,
    PublicChannelAccountEgg,
    PublicChannelAccountStagingToken,
    PublicChannelAccountStagingTokenUpdateRequest,
    PublicChannelAccountUpdateRequest,
    PublicChannelIntegrationChannel,
    PublicChannelIntegrationChannelCreate,
    PublicChannelIntegrationChannelPatch,
    PublicChannelIntegrationMessageUpdateRequest,
    PublicClient,
    PublicContact,
    PublicConversationsMessage,
    PublicDeliveryIdentifier,
    PublicFile,
    PublicLocation,
    PublicMessageFailureDetails,
    PublicMessageHeader,
    PublicMessageStatus,
    PublicQuickReplies,
    PublicRecipient,
    PublicSender,
    PublicSocialMetadataAttachment,
    PublicUnsupportedContent,
    PublicWhatsAppTemplateMetadata,
    QuickRepliesAttachment,
    QuickReply,
    SocialMetadata,
    SocialMetadataIntegrationAttachment,
    UnsupportedContentAttachment,
)
```

Methods:

- <code title="post /conversations/custom-channels/2026-03">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">create</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="patch /conversations/custom-channels/2026-03/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">update</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">PublicChannelIntegrationChannel</a></code>
- <code title="get /conversations/custom-channels/2026-03">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">list</a>(\*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_integration_channel.py">SyncPage[PublicChannelIntegrationChannel]</a></code>
- <code title="delete /conversations/custom-channels/2026-03/{channelId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">delete</a>(channel_id) -> None</code>
- <code title="get /conversations/custom-channels/2026-03/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/custom_channels.py">get</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channel_get_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>

### ChannelAccounts

Methods:

- <code title="post /conversations/custom-channels/2026-03/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="patch /conversations/custom-channels/2026-03/{channelId}/channel-accounts/{channelAccountId}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">update</a>(channel_account_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">PublicChannelAccount</a></code>
- <code title="get /conversations/custom-channels/2026-03/{channelId}/channel-accounts">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">list</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_list_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account.py">SyncPage[PublicChannelAccount]</a></code>
- <code title="patch /conversations/custom-channels/2026-03/{channelId}/channel-account-staging-tokens/{accountToken}">client.conversations.custom_channels.channel_accounts.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/channel_accounts.py">update_staging_token</a>(account_token, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/channel_account_update_staging_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_channel_account_staging_token.py">PublicChannelAccountStagingToken</a></code>

### Messages

Methods:

- <code title="post /conversations/custom-channels/2026-03/{channelId}/messages">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">create</a>(channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_create_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>
- <code title="patch /conversations/custom-channels/2026-03/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">update</a>(message_id, \*, channel_id, \*\*<a href="src/hubspot_sdk/types/conversations/custom_channels/message_update_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>
- <code title="get /conversations/custom-channels/2026-03/{channelId}/messages/{messageId}">client.conversations.custom_channels.messages.<a href="./src/hubspot_sdk/resources/conversations/custom_channels/messages.py">get</a>(message_id, \*, channel_id) -> <a href="./src/hubspot_sdk/types/conversations/public_conversations_message.py">PublicConversationsMessage</a></code>

## VisitorIdentification

Types:

```python
from hubspot_sdk.types.conversations import (
    IdentificationTokenGenerationRequest,
    IdentificationTokenResponse,
)
```

Methods:

- <code title="post /visitor-identification/2026-03/tokens/create">client.conversations.visitor_identification.<a href="./src/hubspot_sdk/resources/conversations/visitor_identification.py">generate_token</a>(\*\*<a href="src/hubspot_sdk/types/conversations/visitor_identification_generate_token_params.py">params</a>) -> <a href="./src/hubspot_sdk/types/conversations/identification_token_response.py">IdentificationTokenResponse</a></code>
