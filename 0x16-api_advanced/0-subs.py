#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""

import requests


def number_of_subscribers(subreddit):
	"""
		returns The number of subscribers or 0 if invalid.
	"""
	url = f"https://www.reddit.com/r/{subreddit}/about.json"
	headers = {'User-Agent': 'my-user-agent'}

	try:
		response = requests.get(url, headers=headers, allow_redirects=False)
		if response.status_code == 200:
			data = response.json()
			return data['data']['subscribers']
		else:
			return 0
	except Exception:
		return 0
