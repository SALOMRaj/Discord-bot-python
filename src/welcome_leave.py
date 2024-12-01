import os
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the WELCOME_CHANNEL_ID and LEAVE_CHANNEL_ID from the .env file
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))  # Convert to integer as channel IDs are integers
LEAVE_CHANNEL_ID = int(os.getenv("LEAVE_CHANNEL_ID"))      # Convert to integer

def member_join_leave(bot):
    @bot.event
    async def on_member_join(member):
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel:
            await channel.send(f"🎉 Welcome to the server, {member.mention}! We're glad to have you here. 😊")

    @bot.event
    async def on_member_remove(member):
        channel = bot.get_channel(LEAVE_CHANNEL_ID)
        if channel:
            await channel.send(f"😢 {member.name} has left the server. We'll miss you!")
