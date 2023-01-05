
"""
Python program that tokenizes and tags a corpus of text
"""

import nltk

# Read the text
with open('text.txt', 'r') as f:
    text = f.read()

# Tokenize the text
tokens = nltk.word_tokenize(text)

# Perform part-of-speech tagging
tags = nltk.pos_tag(tokens)

# Print the tags
print(tags)
