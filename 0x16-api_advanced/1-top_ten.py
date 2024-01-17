#!/usr/bin/python3
"""Function to query Reddit API to get informations"""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit"""
    headers = {'User-Agent': 'Rophpad'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    else:
        print(None)
