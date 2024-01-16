#!/usr/bin/python3
"""Function to query Reddit API to get informations"""
import requests


def number_of_subscribers(subreddit):
    """Returns the numbers of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "rophpad"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    elif response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
