import random

def flames_game():
    '''Welcome to Flames'''
    n1 = input("Enter 1st Name : ").lower()
    n2 = input("Enter 2nd Name : ").lower()

    # Removing common characters
    remaining_chars = list(set(n1) ^ set(n2))
    print(remaining_chars)

    # Result list
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]

    # Calc index based on the len of remaining_chars
    index = len(remaining_chars) % len(flames)
    print(index)

    # Return FLAMES res.
    return flames[index], n1, n2

flames_result, n1, n2 = flames_game()
print(f"FLAMES for {n1} and {n2}, the result is: {flames_result}")
