number_of_inputs = 10

i = 0
larger_num = 0

while i < number_of_inputs:
    i += 1
    try:
        user_input = int(input('Enter a number: '))
        print(user_input)
        if (user_input > larger_num):
            larger_num = user_input
    except ValueError as e:
        print('Input must be an integer')



print(f'Largest number is: {larger_num} ')    

