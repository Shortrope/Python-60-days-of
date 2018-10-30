#!/usr/bin/env python3

"""Retrieve and print words from a URL.
help(words)

Usage:

    python3 words.py <URL>

"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
You can view this comment in the repl useing:
    help(fetch_words) 

    Args:
        url: The URL of a UTF-8 test document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print the words in a list.

    Args:
        items: a List of itemps to print
    """
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1]) # The 0th arg is the module filename