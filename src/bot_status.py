import discord
from discord.ext import tasks

# List of statuses to rotate through
statuses = [
    discord.Game(name="Monitoring Twitch Streams"),
    discord.Activity(type=discord.ActivityType.listening, name="to music"),
    discord.Activity(type=discord.ActivityType.watching, name="a movie"),
    discord.Streaming(name="Playing a game", url="https://twitch.tv/streamer")
]

# Counter for cycling through statuses
status_index = 0

# Function to change the bot's status periodically
@tasks.loop(seconds=60)  # Change status every 60 seconds
async def bot_bio_status(bot):
    global status_index
    # Set the current status
    await bot.change_presence(activity=statuses[status_index])
    
    # Rotate the status index
    status_index = (status_index + 1) % len(statuses)
