try:
    user_days = int(input('How many days before vacation? '))
    weekend_days = 0
    current_day = 0

    SATURDAY = 5
    SUNDAY = 6

    for day in range(0, user_days):
        if current_day >= 7:
            current_day = 0

        if (current_day == SATURDAY or current_day == SUNDAY):
            weekend_days += 1

        current_day += 1

    print(f'Weekend days before vacation: {weekend_days}')

except ValueError as e:
    print('Value must be an integer')
    exit(1)
    pass
