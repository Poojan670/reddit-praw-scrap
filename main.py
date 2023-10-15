import logging
import sys

import pandas as pd
import praw

import constants


def initialize_reddit_client():
    # Initialize the Reddit API client
    reddit = praw.Reddit(client_id=constants.CLIENT_ID,
                         client_secret=constants.CLIENT_SECRET,
                         user_agent=constants.USER_AGENT,
                         username=constants.USERNAME,
                         password=constants.PASSWORD)
    return reddit


def extract_data_from_subreddits(reddit, subreddits, limit=constants.POSTS_LIMIT):
    # Extract posts and comments data from the specified subreddits
    post_data = []
    comment_data = []

    for subreddit_name in subreddits:
        logging.info(f"Fetching data from subreddit: {subreddit_name}")
        subreddit = reddit.subreddit(subreddit_name)

        # Extract posts
        logging.debug("Extracting posts")
        for submission in subreddit.hot(limit=limit):
            post_data.append([submission.id, submission.title, submission.selftext])

            # Extract comments and their levels
            logging.debug("Extracting comments")
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                comment_data.append([submission.id, comment.id, comment.body, comment.depth])

    return post_data, comment_data


def main():
    # List of subreddits you want to pull data from
    subreddits = constants.SUBREDDITS

    # Initialize Reddit client
    reddit = initialize_reddit_client()

    # Extract data
    post_data, comment_data = extract_data_from_subreddits(reddit, subreddits, limit=10)

    # Create dataframes
    post_df = pd.DataFrame(post_data, columns=['Post ID', 'Post Title', 'Post Text'])
    comment_df = pd.DataFrame(comment_data, columns=['Post ID', 'Comment ID', 'Comment Text', 'Comment Level'])

    # Export data to CSV
    post_df.to_csv('reddit_posts.csv', index=False)
    comment_df.to_csv('reddit_comments.csv', index=False)


if __name__ == "__main__":
    # Configure the default logging
    logging.basicConfig(filename="scraping.log", level=logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger('').addHandler(console_handler)

    constant_names = ["CLIENT_ID", "CLIENT_SECRET", "USER_AGENT", "USERNAME", "PASSWORD",
                      "SUBREDDITS", "POSTS_LIMIT"]

    for constant_name in constant_names:
        try:
            constant_value = getattr(constants, constant_name)
            if constant_value is None or (isinstance(constant_value, str) and constant_value.strip() == ""):
                logging.error(f"{constant_name} is either None or blank. Please set a valid value.")
                sys.exit()
        except AttributeError as e:
            logging.error(str(e))
            sys.exit()

    main()
