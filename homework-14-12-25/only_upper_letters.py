user_input = input('Enter a word: ')
output = ''

# First approach
for letter in user_input:
    if letter.upper() == letter:
        output += letter

# Second apprach
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for letter in user_input:
    if letter in letters:
        output += letter


print(output)
