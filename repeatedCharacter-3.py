"""
Design a function that takes a string or sequence of characters as input and
returns the character that appears most frequently.
"""

def repeatedCharacter(name):
    # dictionary to store characters count of a string
    char_dict = {}

    # iterating over the characters in a name
    for char in name:
        if char in char_dict:
            # increment the character at the index
            char_dict[char] += 1
        else:
            # creating a new index for new character
            char_dict[char] = 1

    # getting the repeated character using the max function
    max_char = max(char_dict,key=char_dict.get)
    return print(max_char)

repeatedCharacter("11189")


                 