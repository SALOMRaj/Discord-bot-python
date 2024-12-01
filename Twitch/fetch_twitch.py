import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Fetch the Twitch credentials from the .env file
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")


# Function to fetch the Twitch OAuth token
def get_twitch_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": TWITCH_CLIENT_ID,
        "client_secret": TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json().get("access_token")
    except requests.RequestException as e:
        print(f"Error fetching Twitch OAuth token: {e}")
        return None

# Function to check if a user is live on Twitch
def is_user_live(username, token):
    if not token:
        print(f"Invalid token provided for user: {username}")
        return False

    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {"user_login": username}
    url = "https://api.twitch.tv/helix/streams"
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "data" in data and isinstance(data["data"], list):
            return bool(data["data"])
        else:
            print(f"No stream data found for user {username}.")
            return False
    except requests.RequestException as e:
        print(f"Error checking live status for user {username}: {e}")
        return False


def fetch_stream_title(username, token):
    """Fetch the stream title of a Twitch user."""
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {"user_login": username}
    url = "https://api.twitch.tv/helix/streams"

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if the user is live and return the title
        if data["data"]:
            return data["data"][0]["title"]
        else:
            print(f"{username} is not live.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching stream title: {e}")
        return None
    
def fetch_viewer_count(username, token):
    """Fetch the viewer count of a Twitch user."""
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {"user_login": username}
    url = "https://api.twitch.tv/helix/streams"

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if the user is live and return the viewer count
        if data["data"]:
            return data["data"][0]["viewer_count"]
        else:
            print(f"{username} is not live.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching viewer count: {e}")
        return None
    
def fetch_game_name(username, token):
    """Fetch the game being streamed by a Twitch user."""
    headers = {
        "Client-ID": TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {"user_login": username}
    url = "https://api.twitch.tv/helix/streams"

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if the user is live and return the game name
        if data["data"]:
            return data["data"][0]["game_name"]
        else:
            print(f"{username} is not live.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching game name: {e}")
        return None