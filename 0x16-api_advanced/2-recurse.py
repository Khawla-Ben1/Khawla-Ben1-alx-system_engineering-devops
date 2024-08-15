#!/usr/bin/python3
"""
This module contains the function recurse.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
	"""
	Recursively queries the Reddit API to return a list containing the titles of all hot articles
	for a given subreddit. If no results are found or the subreddit is invalid, returns None.
	"""
	if hot_list is None:
		hot_list = []

	url = f"https://www.reddit.com/r/{subreddit}/hot.json"
	headers = {'User-Agent': 'my-user-agent'}
	params = {'after': after}

	try:
		response = requests.get(url, headers=headers, params=params, allow_redirects=False)
		if response.status_code != 200:
			return None

		data = response.json()
		posts = data['data']['children']
		if not posts:
			return hot_list if hot_list else None

		for post in posts:
			hot_list.append(post['data']['title'])

		after = data['data'].get('after')
		if after:
			return recurse(subreddit, hot_list, after)
		else:
			return hot_list
	except Exception:
		return None
