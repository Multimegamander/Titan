from titanembeds.database import db, Base

class Guilds(Base):
    __tablename__ = "guilds"
    guild_id = db.Column(db.BigInteger, primary_key=True)            # Discord guild id
    name = db.Column(db.String(255))                # Name
    unauth_users = db.Column(db.Boolean())          # If allowed unauth users
    visitor_view = db.Column(db.Boolean())          # If users are automatically "signed in" and can view chat
    webhook_messages = db.Column(db.Boolean())      # Use webhooks to send messages instead of the bot
    guest_icon = db.Column(db.String(255), default=None) # Guest icon url, None if unset
    chat_links = db.Column(db.Boolean())            # If users can post links
    bracket_links = db.Column(db.Boolean())         # If appending brackets to links to prevent embed
    unauth_captcha = db.Column(db.Boolean(), nullable=False, server_default="1")         # Enforce captcha on guest users
    mentions_limit = db.Column(db.Integer)          # If there is a limit on the number of mentions in a msg
    roles = db.Column(db.Text().with_variant(db.Text(length=4294967295), 'mysql'))   # Guild Roles
    channels = db.Column(db.Text().with_variant(db.Text(length=4294967295), 'mysql'))# Guild channels
    webhooks = db.Column(db.Text().with_variant(db.Text(length=4294967295), 'mysql'))# Guild webhooks
    emojis = db.Column(db.Text().with_variant(db.Text(length=4294967295), 'mysql'))  # Guild Emojis
    owner_id = db.Column(db.BigInteger)            # Snowflake of the owner
    icon = db.Column(db.String(255))                # The icon string, null if none
    invite_link = db.Column(db.String(255))         # Custom Discord Invite Link
    post_timeout = db.Column(db.Integer, nullable=False, server_default="5")    # Seconds to elapse before another message can be posted from the widget
    max_message_length = db.Column(db.Integer, nullable=False, server_default="300") # Chars length the message should be before being rejected by the server

    def __init__(self, guild_id, name, roles, channels, webhooks, emojis, owner_id, icon):
        self.guild_id = guild_id
        self.name = name
        self.unauth_users = True # defaults to true
        self.visitor_view = False
        self.webhook_messages = False
        self.guest_icon = None
        self.chat_links = True
        self.bracket_links = True
        self.unauth_captcha = True
        self.mentions_limit = -1 # -1 = unlimited mentions
        self.roles = roles
        self.channels = channels
        self.webhooks = webhooks
        self.emojis = emojis
        self.owner_id = owner_id
        self.icon = icon

    def __repr__(self):
        return '<Guilds {0} {1}>'.format(self.id, self.guild_id)
