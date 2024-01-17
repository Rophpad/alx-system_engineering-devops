#!/usr/bin/python3
"""Function to query Reddit API to get informations"""
from requests import get


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'My user Agent'}
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)

    response = get(url, headers=user_agent)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
