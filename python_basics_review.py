# Task 1: String Manipulation

print("Test 1:")

response = input()

uppercase_response = response.upper()

lowercase_response = response.lower()

reverse_response = response[::-1]

vowel_erase = response.replace('A', '*').replace('a', '*').replace('E', '*').replace('e', '*').replace('I', '*').replace('i', '*').replace('O', '*').replace('o', '*').replace('U', '*').replace('u', '*')

character_count = len(response)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("You typed", response)

print(uppercase_response)

print(lowercase_response)

print(reverse_response)

print(vowel_erase)

print(character_count)




# Part 2:

