from collections import Counter
#Import string module in order to exclude punctuations from sentences

print("---Welcome to word counter :) ---\n")
sentence = input("Type your sentence/word: \n").lower()
words = sentence.split()
# changes words in a sentence to list items


# Number of words
my_dictionary = dict(Counter(words))
print("The words are: ")
for key in my_dictionary:
    print(key)

print(f"\n The total number of words in the sentence is {len(words)}\n")


# Number of letters
length = len(sentence.replace(" ", ""))
# This removes spaces
# Note: example.replace("old", "new", "occurences to be replaced")

letters = (dict(Counter(sentence)))
# dict() changes  current type to dictionary
# Returns: {'t': 1, 'o': 1, 'y': 1}

letters.pop(" ")
items = letters.items()
# Returns: dict_items([('t', 1), ('o', 1), ('y', 1)])

for key, value in letters.items():
    print(f"{key}: {value}")
#Returns the frequency of every letter

max_freq = max(items, key=lambda x: x[1])
print(f"The letter with the highest frequency is: {max_freq}")

# Remaining: Improve the logic for max_freq to handle cases where we have shared highest frequency.



