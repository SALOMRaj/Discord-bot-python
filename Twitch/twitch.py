import discord
import os
import json
from discord.ext import tasks
from Twitch.fetch_twitch import get_twitch_token, is_user_live, fetch_stream_title, fetch_viewer_count, fetch_game_name

# Path to the JSON file where Twitch users will be stored
USER_DATA_FILE = "twitch_users.json"

# Function to load Twitch users from the JSON file
def load_twitch_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)  # Return the list of users from the JSON file
    return []  # Return an empty list if the file doesn't exist

# Function to save Twitch users to the JSON file
def save_twitch_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)  # Save the list of users to the JSON file

class TwitchLive:
    def __init__(self, bot, notification_channel_id):
        self.bot = bot
        self.notification_channel_id = notification_channel_id
        self.twitch_users = load_twitch_users()
        self._loop_started = False  # Ensure the loop starts only once
        self.live_message_map = {}  # Store message IDs for live notifications

    def add_twitch_user(self, username):
        """Add a Twitch user to the list of monitored users."""
        if username not in self.twitch_users:
            self.twitch_users.append(username)
            save_twitch_users(self.twitch_users)
            return True
        return False
    
    def remove_twitch_user(self, username):
        """Remove a Twitch user from the list of monitored users."""
        if username in self.twitch_users:
            self.twitch_users.remove(username)
            save_twitch_users(self.twitch_users)
            return True
        return False

    def list_twitch_users(self):
        """Get the list of all monitored Twitch users."""
        return self.twitch_users

    async def check_and_notify_live_users(self):
        """Check if the Twitch users are live and notify the Discord channel."""
        token = get_twitch_token()
        if not token:
            return

        channel = self.bot.get_channel(self.notification_channel_id)
        if not channel:
            print(f"Notification channel not found!")
            return
        
        for user in self.twitch_users:
            username = user
            stream_title = fetch_stream_title(username, token)
            viewer_count = fetch_viewer_count(username, token)
            game_name = fetch_game_name(username, token)
            is_live = is_user_live(user, token)

            embed = discord.Embed(
                title=f"🎮: {user} is Live!",
                description="🎥 Streaming something awesome! Don't miss it! 💬",
                url=f"https://twitch.tv/{user}",
                color=discord.Color.purple()
                )
            
            embed.add_field(name="Stream Title", value=f"{stream_title}", inline=False)
            embed.add_field(name="Viewers", value=f"{viewer_count} people are watching now!", inline=True)
            embed.add_field(name="Now Playing", value=f"{game_name}", inline=True)
            embed.add_field(name="Join Now", value=f"[Watch here!](https://twitch.tv/{user})")
            
            if is_live:
                # If the user is live, check if we've already sent a message
                if user in self.live_message_map:
                    message = await channel.fetch_message(self.live_message_map[user])
                    await message.edit(content=None, embed=embed)
                else:
                    # Send a new message if not already sent
                    new_message = await channel.send(embed=embed)
                    self.live_message_map[user] = new_message.id  # Store the message ID

            else:
                # If the user is not live, remove the message
                if user in self.live_message_map:
                    message_id = self.live_message_map.pop(user)
                    message = await channel.fetch_message(message_id)
                    await message.delete()  # Remove the previous message about being live
                    print(f"Deleted live notification for {user}")

    @tasks.loop(minutes=5)
    async def check_and_notify_task(self):
        """Task that periodically checks for live Twitch streams."""
        await self.check_and_notify_live_users()

    async def start_loop(self):
        """Start the loop after the bot is ready."""
        if not self._loop_started:
            self.check_and_notify_task.start()
            self._loop_started = True
            print("Twitch live checking task started.")
