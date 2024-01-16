#!/usr/bin/python3
"""Function to query Reddit API to get informations"""
import requests


def number_of_subscribers(subreddit):
    """Returns the numbers of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "rophpad@alx-holbertonschool"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
