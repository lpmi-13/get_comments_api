import json
import os

import praw

reddit_client_id = os.environ.get('CLIENT_ID', default='')
reddit_client_secret = os.environ.get('CLIENT_SECRET', default='')
reddit_password = os.environ.get('PASSWORD', default='')
reddit_user_agent = os.environ.get('USER_AGENT', default='')
reddit_username = os.environ.get('USERNAME', default='')

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     password=reddit_password,
                     user_agent=reddit_user_agent,
                     username=reddit_username)

def process_subreddit(subreddit, count):

    subreddit = reddit.subreddit(subreddit)

    subreddit_comments = []

    for submission in subreddit.new(limit=count):

        for comment in submission.comments:

            try:
                subreddit_comments.append(comment.body)
            except:
                pass

    return json.dumps(subreddit_comments)

