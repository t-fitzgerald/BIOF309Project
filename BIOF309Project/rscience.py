import praw
import pandas as pd


def updatePosts():
    # establishes api access
    reddit = praw.Reddit(client_id='KmmJfWjpkctzNQ',
                         client_secret='ZEKHP3IrLDSJMeuzXa8YlvI0kFY',
                         user_agent='RWS')

    rsci_subreddit = reddit.subreddit('science')

    # iterates through top 10000 posts (measured by number of upvotes) from the subreddit from all time, gathering various data points
    rsci_posts = []
    for post in rsci_subreddit.top(limit=10000):
        rsci_posts.append([post.title, post.created_utc, post.score, post.upvote_ratio, post.id, post.link_flair_text,
                           post.num_comments])

    rsci_posts = pd.DataFrame(rsci_posts, columns=['title', 'post time', 'score', 'upvote ratio', 'id', 'flair',
                                                   'number of comments'])

    rsci_posts.to_csv('top1krsciposts.csv')
