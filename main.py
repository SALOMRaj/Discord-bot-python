import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from src.welcome_leave import member_join_leave
from src.server_status import update_server_status
from src.bot_status import bot_bio_status
from Twitch.twitch import TwitchLive  # Import the TwitchLive class
from Commands.twitch_user_commands import setup_twitch_user_commands

# Load environment variables from .env
load_dotenv()

# Load the Twitch and Discord bot credentials from the .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
NOTIFICATION_CHANNEL_ID = int(os.getenv("NOTIFICATION_CHANNEL_ID"))  # Notification channel ID

# Initialize the bot with appropriate intents
intents = discord.Intents.default()
intents.members = True  # Enable member-related events
intents.presences = True  # Enable presence-related events
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize the TwitchLive instance
twitch_live = TwitchLive(bot, NOTIFICATION_CHANNEL_ID)

# Set up commands
setup_twitch_user_commands(bot, twitch_live)

# Load events and tasks (Ensure these are set up in respective files)
member_join_leave(bot)

# Start the task when the bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await twitch_live.start_loop()
    bot_bio_status.start(bot)
    update_server_status.start(bot)

# Start the bot
if BOT_TOKEN:
    bot.run(BOT_TOKEN)
else:
    print("Error: BOT_TOKEN is not set in the .env file")
