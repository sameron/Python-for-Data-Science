import nltk

# Tokenize the text
tokens = nltk.word_tokenize("The quick brown fox jumps over the lazy dog.")

# Perform part-of-speech tagging
tags = nltk.pos_tag(tokens)

# Extract nouns
nouns = [token for token, pos in tags if pos.startswith('N')]

print(nouns)  # ['fox', 'dog']
