import string
"""
Design a function that determines whether a given string is a pangram. A
pangram is a sentence or phrase containing every letter of the alphabet at
least once. Punctuation and case are typically ignored. For example, the
string "The quick brown fox jumps over the lazy dog" is a pangram, while
"Hello, world!" is not.
"""

def pangram(sentence):
    # we initialize a set
    letters_set = set(string.ascii_lowercase)
    
    # converts the sentence to lower to check case insenstivity
    if set(sentence.lower()).issuperset(letters_set):
        return True
    else:
        return False

print(pangram("Hello, world!"))   

