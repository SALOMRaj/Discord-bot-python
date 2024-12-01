import os
from discord.ext import tasks
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the STATUS_CHANNEL_ID from the .env file
STATUS_CHANNEL_ID = int(os.getenv("STATUS_CHANNEL_ID"))  # Convert to integer as channel IDs are integers

@tasks.loop(minutes=5)  # Automatically runs every 5 minutes
async def update_server_status(bot):
    for guild in bot.guilds:  # Loop through all servers the bot is connected to
        voice_channel = bot.get_channel(STATUS_CHANNEL_ID)
        if voice_channel:
            total_members = guild.member_count
            online_members = sum(1 for member in guild.members if member.status == discord.Status.online)

            # Set the new channel name
            new_name = f"Members: {total_members} | Online: {online_members}"
            await voice_channel.edit(name=new_name)
            print(f"Updated voice channel '{voice_channel.name}' to '{new_name}'")
            break  # Exit after updating the desired guild's channel
