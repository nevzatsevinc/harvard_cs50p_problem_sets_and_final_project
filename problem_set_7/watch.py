"""
Problem Set 7 - Watch on YouTube
https://cs50.harvard.edu/python/2022/psets/7/watch/
"""

import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Input string
    Return URL or None
    """
    # YouTube URLs
    match = re.search(r'"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    # (?:www\.) This is a non-capturing group, indicated by ?: at the start of the parentheses.
    # match.group(1), first and only capturing group, which is the YouTube video ID.

    # the short URL and return it
    if match:
        video_id = match.group(1)
        return f'https://youtu.be/{video_id}'

    # return None
    return None


if __name__ == "__main__":
    main()