user_input = input('Enter data: ')

sizes = user_input.split(',')

width, length, size = sizes

can_be_sliced = (int(size) % int(width) == 0) and int(size) // int(width) 

print(f'Can be sliced: {can_be_sliced}')

