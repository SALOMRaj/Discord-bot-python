# Discord Twitch Live Notification Bot

This is a Python-based Discord bot that sends notifications in a Discord channel when specific Twitch users go live. The bot fetches stream data such as the title, viewer count, and game name of the stream, and provides a live notification in the designated channel.

## Features
- Monitor multiple Twitch users for live status.
- Automatically send a live notification when a user goes live.
- Display stream title, viewer count, and game name.
- Periodically check the live status of users.
- Commands to add, remove, and list monitored Twitch users.

## Requirements
- Python 3.11 or higher
- `discord.py` library
- `requests` library to interact with the Twitch API
- Docker (optional, if running inside a container)

## Setup

### 1. Clone the Repository
```
git clone https://github.com/yourusername/discord-bot-python.git
cd discord-bot-python
```
### 2. Install Dependencies
Create a virtual environment and install the necessary dependencies:
```
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
pip install -r requirements.txt
```
### 3. Create a .env File
Create a .env file in the project root with the following environment variables:
```
# Bot Token
DISCORD_TOKEN=your_discord_bot_token

# Twitch API credentials
TWITCH_CLIENT_ID=your_twitch_client_id
TWITCH_CLIENT_SECRET=your_twitch_client_secret

# Channel IDs for Welcome and Leave messages
WELCOME_CHANNEL_ID=your_welcome_channel_id
LEAVE_CHANNEL_ID=your_leave_channel_id

# Channel ID for Server Status updates
STATUS_CHANNEL_ID=your_status_channel_id

# Allowed Channel ID for admin commands (add/remove users)
ALLOWED_CHANNEL_ID=your_admin_channel_id

# Twitch Notification channel
NOTIFICATION_CHANNEL_ID=your_notification_channel_id
Replace the values with your actual credentials and channel IDs.
```
### 4. Running the Bot
Run the bot with the following command:
```
python main.py
```
The bot will start and periodically check if the specified Twitch users are live. When a user goes live, it will send a notification in the configured Discord channel.

### 5. Docker Setup (Optional)
If you'd like to run the bot inside a Docker container, you can use the provided Dockerfile.

Build the Docker image:
```
docker build -t discord-bot-python .
```
Run the Docker container:
```
docker run discord-bot-python
```
Make sure Docker is installed and running before building the container.

### 6. Commands
You can interact with the bot using the following commands:

!addtwitchuser <Twitch Username>
Adds a Twitch user to the monitored list. The bot will start checking the live status of this user.

!removetwitchuser <Twitch Username>
Removes a Twitch user from the monitored list. The bot will stop checking this user’s live status.

!listtwitchusers
Lists all the Twitch users currently being monitored by the bot.

## Example Usage:
!addtwitchuser Ninja
Adds the Twitch user "Ninja" to the monitored list.

!removetwitchuser Pokimane
Removes the Twitch user "Pokimane" from the monitored list.

!listtwitchusers
Displays a list of all the Twitch users currently being monitored by the bot.

### 7. License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

Contributing
Fork the repository.
Clone your fork: git clone https://github.com/yourusername/discord-bot-python.git.
Create a branch: git checkout -b feature-name.
Commit your changes: git commit -am 'Add feature'.
Push to the branch: git push origin feature-name.
Open a pull request.
Acknowledgements
discord.py - The library used for the bot.
Twitch API - To get the live status and stream data.
markdown
Copy code

### Steps to finalize:
1. Replace `your_discord_bot_token`, `your_twitch_client_id`, and `your_twitch_client_secret` in the `.env` section with your actual values.
2. Follow the steps to clone the repository, install dependencies, and run the bot.
3. Ensure that the commands `!addtwitchuser`, `!removetwitchuser`, and `!listtwitchusers` are properly implemented within the bot for them to function correctly.
