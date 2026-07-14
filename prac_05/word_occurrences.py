"""
CP1404 - Practical
Count how many times a word occurs
Estimate: 20 minutes
Actual: 27 minutes
"""

word_to_count = {}
longest_word = 0
text = input("Text: ")
words = text.split()

for word in words:
    # Count occurrences of words
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

    # Find length of longest word
    if len(word) > longest_word:
        longest_word = len(word)

# Get list of words sorted alphabetically
for word in sorted(word_to_count):
    print(f"{word:{longest_word}} : {word_to_count[word]}")
