import os
from discord.ext import commands
from Twitch.twitch import TwitchLive  # Ensure this is the correct import

def setup_twitch_user_commands(bot, twitch_live):
    """Set up the commands for adding, removing, and listing Twitch users."""
    
    @bot.command()
    async def addtwitchuser(ctx, username: str):
        """Add a Twitch user to the list of monitored users."""
        if ctx.channel.id != int(os.getenv("ALLOWED_CHANNEL_ID")):
            await ctx.send("❌ You can only use this command in the designated channel.")
            return
        
        if twitch_live.add_twitch_user(username):
            await ctx.send(f"✅ Successfully added {username} to the list of monitored Twitch users!")
        else:
            await ctx.send(f"❌ {username} is already in the list.")

    @bot.command()
    async def removetwitchuser(ctx, username: str):
        """Remove a Twitch user from the list of monitored users."""
        if ctx.channel.id != int(os.getenv("ALLOWED_CHANNEL_ID")):
            await ctx.send("❌ You can only use this command in the designated channel.")
            return
        
        if twitch_live.remove_twitch_user(username):
            await ctx.send(f"✅ Successfully removed {username} from the list of monitored Twitch users.")
        else:
            await ctx.send(f"❌ {username} was not found in the list.")

    @bot.command()
    async def listtwitchusers(ctx):
        """List all Twitch users currently being monitored."""
        if ctx.channel.id != int(os.getenv("ALLOWED_CHANNEL_ID")):
            await ctx.send("❌ You can only use this command in the designated channel.")
            return
        
        users = twitch_live.list_twitch_users()
        if users:
            await ctx.send(f"Monitored Twitch users: {', '.join(users)}")
        else:
            await ctx.send("No Twitch users are currently being monitored.")
