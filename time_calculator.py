def add_time(start_time, duration, day=None):
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    start_time = start_time.split()
    duration = duration.split(':')
    time = start_time[0].split(':')
    minutes = ((int(duration[0])*60) + int(duration[1]))
    period = start_time[1]
    hour = int(time[0])
    minute = int(time[1])
    if period == 'PM' and int(time[0]) < 12:
        hour += 12
    days = 0

    for i in range(minutes):
        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        if hour == 24:
            hour = 0
            days += 1

        if hour > 11:
            period = 'PM'
        else:
            period = 'AM'

    if minute < 10:
        minute = f'0{minute}'
    if period == 'PM' and hour != 12:
        hour -= 12
    if hour == 0:
        hour = 12

    if day:
        day_of = week[(week.index(day.capitalize())+days)%7]
        if days > 1:
            return f'{hour}:{minute} {period}, {day_of} ({days} days later)'
        elif days == 1:
            return f'{hour}:{minute} {period}, {day_of} (next day)'
        else:
            return f'{hour}:{minute} {period}, {day_of}'
    else:
        if days > 1:
            return f'{hour}:{minute} {period} ({days} days later)'
        elif days == 1:
            return f'{hour}:{minute} {period} (next day)'
        else:
            return f'{hour}:{minute} {period}'

print(add_time("11:06 PM", "2:02"))
