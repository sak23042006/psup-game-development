def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for char in name1:
        if char in name2:
            name1 = name1.replace(char,"", 1)
            name2 = name2.replace(char,"", 1)

    combined_name = name1 + name2
    flames = "FLAMES"

    while len(flames) > 1:
        index = (len(combined_name) % len(flames)) - 1
        if index >= 0:
            flames = flames[:index] + flames[index + 1:]
        else:
            flames = flames[:len(flames) - 1]

    return flames

def main():
    print("Welcome to the FLAMES game!")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    result = calculate_flames(name1, name2)

    relationship = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings',
    }

    print(f"Result: {relationship[result]}")

main()
