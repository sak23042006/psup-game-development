import random

def flames_game():
    '''Welcome to Flames'''
    n1 = input("Enter 1st Name : ").lower()
    n2 = input("Enter 2nd Name : ").lower()

    # Removing common characters
    remaining_chars = []
    for char in n1:
        if char not in n2:
            remaining_chars.append(char)

    for char in n2:
        if char not in n1:
            remaining_chars.append(char)

    # Result list
    flames = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
    index = 0

    # Calculate index based on the length of remaining_chars
    if len(remaining_chars) > 0:
        index = random.randint(0, len(remaining_chars) - 1)

    # If list is empty, return default value.
    if len(remaining_chars) == 0 or index >= len(flames):
        index = 0

    # Return the FLAMES result.
    return flames[index], n1, n2

flames_result, n1, n2 = flames_game()
print(f" FLAMES for {n1} and {n2}, the result is: {flames_result}")
