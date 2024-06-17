"""
Design a function that reverses the digits of an integer. For example, 50
should become 5 and -12 should become -21.
"""

def reverseInteger(n):
    # convert int to string
    x = str(n)
    # Checks if the first index is alphanumeric meaning it contains only numeric values
    if x.isalnum():
        result = "".join(reversed(x))
        return print(int(result))
    else:
        result = x[0] + "".join(reversed(x[1:]))
        return print(int(result))

reverseInteger(-12)