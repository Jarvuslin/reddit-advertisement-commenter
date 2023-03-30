import praw
import os
from dotenv import load_dotenv

keyword =[ "solution", "chegg", "homework", "help", "urgent", "unlock"]

# initialize Reddit instance
reddit = praw.Reddit(
    client_id="QyeioMg2IIe83X_iEn4DIw",
    client_secret="HEx3PleR5dwocD5mJkjllpELmYXJNg",
    redirect_uri="http://localhost:8000",
    user_agent="Scholaro ad 1.0 by /u/schoolaro",
    username= os.getenv("REDDIT_USERNAME"),
    password= os.getenv("REDDIT_PASSWORD"),
)

# define subreddit to monitor
subreddit = reddit.subreddit("Chegg_Solutions")

# loop to monitor for study help comments
for comment in subreddit.stream.comments(skip_existing=True):
    print(comment.body)
    if any(word in comment.body.lower() for word in keyword):
        reply_text = f"Hey there! If you need study help or chegg unlock, check out our Discord server: https://discord.gg/VzW6vEQJN6"
        comment.reply(reply_text)

