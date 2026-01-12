from collections import Counter
import string

print("---Welcome to word counter :) ---\n")
sentence = input("Type your sentence/word: \n").lower()
clean_sentence = sentence.translate(str.maketrans("", "", string.punctuation))

# Number of words
words = clean_sentence.split()
# changes words in a sentence to list items

my_dictionary = dict(Counter(words))
print("The words are: ")
for key in my_dictionary:
    print(key)

print(f"\n The total number of words in the sentence is {len(words)}\n")


# Number of letters
length = len(clean_sentence.replace(" ", ""))
# This removes spaces
# Note: example.replace("old", "new", "occurences to be replaced")

letters = (dict(Counter(clean_sentence)))
# dict() changes  current type to dictionary
# Returns: {'t': 1, 'o': 1, 'y': 1}

letters.pop(" ", None)
items = letters.items()
# Returns: dict_items([('t', 1), ('o', 1), ('y', 1)])

for key, value in letters.items():
    print(f"{key}: {value}")
#Returns the frequency of every letter

max_freq = max(items, key=lambda x: x[1])
print(f"The letter with the highest frequency is: {max_freq}")

max_count = max(letters.values())
most_frequent_letters = [letter for letter, count in letters.items() if count == max_count]

print(f"Most frequent letter(s): {most_frequent_letters} (appeared {max_count} times)")




