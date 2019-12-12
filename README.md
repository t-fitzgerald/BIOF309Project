﻿# BIOF309Project
The dissemination of scientific articles has been vastly improved with the advent of social media. A number of platforms have facilitated this increased availability and sharing of knowledge, perhaps most notably, through the r/science subreddit or reddit.com. In this community of over 22 million registered members, users share research articles and partake in moderated discussion of the findings and methods. Users vote (upvote/downvote) a given post based on its perceived quality or popularity.

For this project, I sought to create a program that would allow a user to optimize their post for maximum reach. The program uses reddits API, known in python as PRAW, to collect data from the website. Gathering the most upvoted ~1000 posts, the data gathered represents the most popular posts on the target subreddit. The program leverages the characteristics of these posts to guide the user to a post that will be upvoted or shared more.

The program accepts a scientific subtopic (defined by the subtopics present in the subreddit) and a potential post title as parameters. Using pandas, numpy, and matplotlib, the program shows the user a scatterplot of posts defined by the length of the title on the X axis, and the score the post received on the Y axis. Using linear regression, a fit line is fixed to the plot. A simulated data point is added to show the potential performance of the post based on the length of title and subtopic choice. Additionally, in the initial datascrape from reddit, submission time data is gathered. This data is used to convert UTC time (seconds since the Unix epoch) into human-readable day of the week data. This assists the user in deciding what day of the week, historically, is the most productive for their chosen field. Lastly, the program uses a natural language processing package designed to measure the relative positivity or negativity of the words in the post titles of their chosen subtopic, and the average score for each. This may help guide the user to understand the attitudes of the posts in their subtopic, and could inspire different word choice or spin for their post.

The user is intended to run only optimizer.ipynb, as scraper.ipynb takes a long time and the data has already been provided.
