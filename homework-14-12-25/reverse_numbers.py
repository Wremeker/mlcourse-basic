user_input = input('Enter 5 digits number: ')

if (len(user_input) != 5 or not user_input.isdigit()):
    print('Input must be a number and consist of 5 digits')
    exit(1)

print(user_input.replace(user_input[1:-1], (user_input[1:-1])[::-1]))

