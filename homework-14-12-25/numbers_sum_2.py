user_input = input('Ввведие строку: ')
sum = 0

for letter in user_input:
    if letter.isdigit():
        sum += int(letter)


print(sum)
        
