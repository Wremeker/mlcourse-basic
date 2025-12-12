sum = 0

while True:
    try:
        user_num = int(input('Enter a number: '))
        sum += user_num
    except ValueError as exception:
        print('Non numbered value has been entered')
        print(f'Sum: {sum}')
        break