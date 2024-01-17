#!/usr/bin/python3
"""Function to query Reddit API to get informations"""
import requests


def number_of_subscribers(subreddit):
    """Returns the numbers of subscribers for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
                Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    data = response.json()
    try:
        return data["data"]["subscribers"]
    except Exception:
        return 0
    """
    if response.status_code == 404:
        return 0
    elif response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
    """
