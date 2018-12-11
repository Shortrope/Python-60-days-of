#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Search for words')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

words_file = '/usr/share/dict/words'

with open(words_file) as f:
    words = f.readlines()

# matches = []
#
# for word in words:
#    if snippet in word.lower():
#        matches.append(word)

matches = [word.strip() for word in words if snippet in word.lower()]

print(matches)