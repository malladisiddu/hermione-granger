import os
import memes
import welcome
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Greets the new user when the new user join the channel
@app.event("team_join")
def handler(event, say):
    welcome.ask_for_introduction(event, say)

# post random memes
@app.command("/post")
def handler(ack, say, command):
    memes.post_memes(ack, say, command)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
