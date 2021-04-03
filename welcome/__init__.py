import os

def ask_for_introduction(event,say):
    channel_id = os.environ.get("SLACK_INTRO_CHANNEL")
    user_id = event["user"]["id"]
    text = f"Welcome to the team, <@{user_id}>! 🎉 You can introduce yourself in this channel. Feel free because we are friends now :)"
    say(text=text, channel=channel_id)