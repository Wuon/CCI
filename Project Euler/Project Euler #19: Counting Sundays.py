
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for x in range(int(input().strip())):
    start = list(map(int, input().split(' ')))
    end = list(map(int, input().split(' ')))
    year, month, day = start[0], start[1], start[2]
    if year % 400 == 0:
        months[1] = 29
    elif year % 100 == 0:
        months[1] = 28
    elif year % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28
    sunday = (day + (13 * (month+1) // 5) + year + (year // 4) - (year // 100) + (year // 400)) % 7
    sundays = 0
    while year < end[0] or month < end[1] or day < end[2]:
        if sunday == 6 and day == 1:
            sundays += 1
        day += 1
        sunday += 1
        if sunday > 6:
            sunday = 0
        if day > months[month-1]:
            day = 1
            month += 1
            if month > 12:
                year += 1
                month = 1
                if year % 400 == 0:
                    months[1] = 29
                elif year % 100 == 0:
                    months[1] = 28
                elif year % 4 == 0:
                    months[1] = 29
                else:
                    months[1] = 28
    print(sundays)
