"""
Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
for his unique way of speaking. He often reverses the order of words in his
sentences. For example, instead of saying "I am home" he might say "Home
am I" Design a function that takes a sentence as input and returns a new
sentence with the words reversed in the same order that Master Yoda would
use.
"""

def masterYoda(sentence):
    output = sentence.split(' ')
    result = ' '.join(reversed(output))
    return print(result)

masterYoda("I am home")