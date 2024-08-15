#!/usr/bin/python3
"""
This module contains the function count_words.
"""

import re
import requests
from collections import defaultdict


def count_words(subreddit, word_list, hot_list=None, after=None):
	"""
	Recursively queries the Reddit API to count occurrences of keywords in hot article titles
	for a given subreddit. Results are printed in descending order of frequency and alphabetically
	if frequencies are the same.

	Args:
		subreddit (str): The subreddit to query.
		word_list (list): List of keywords to count.
		hot_list (list): Accumulator list to hold titles (used for recursion).
		after (str): The ID of the last post retrieved, used for pagination (used for recursion).
	"""
	if hot_list is None:
		hot_list = []

	if not word_list:
		return

	url = f"https://www.reddit.com/r/{subreddit}/hot.json"
	headers = {'User-Agent': 'my-user-agent'}
	params = {'after': after}

	try:
		response = requests.get(url, headers=headers, params=params, allow_redirects=False)
		if response.status_code != 200:
			return

		data = response.json()
		posts = data['data']['children']
		if not posts:
			return

		for post in posts:
			hot_list.append(post['data']['title'].lower())

		after = data['data'].get('after')
		if after:
			count_words(subreddit, word_list, hot_list, after)
		else:
			word_count = defaultdict(int)
			word_pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, word_list)) + r')\b', re.IGNORECASE)
			for title in hot_list:
				matches = word_pattern.findall(title)
				for match in matches:
					word_count[match.lower()] += 1

			sorted_counts = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
			for word, count in sorted_counts:
				if word in word_list:
					print(f"{word}: {count}")

	except Exception:
		return
