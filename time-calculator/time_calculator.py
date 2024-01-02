"""
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, 
it should show (next day) after the time. 
If the result will be more than one day later, it should show (n days later) after the time, 
where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, 
then the output should display the day of the week of the result. 
The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. 
Pay close attention to the spacing and punctuation of the results.
"""

def add_time(start, duration, day=None):

    # Split start time into hours and minutes
    start_time = start.split()
    start_time = start_time[0].split(':')
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])
    start_period = start.split()[1]

    # Convert start time to 24 hour clock
    if start_period == 'PM':
        start_hour += 12

    # add duration time to start time
    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    # fix minutes
    hour_count = 0
    minute_count = duration_minute + start_minute
    while minute_count >= 60:
        hour_count += 1
        minute_count -= 60

    # fix hours
    hour_count += duration_hour + start_hour
    day_count = 0
    while hour_count >= 24:
        day_count += 1
        hour_count -= 24

    # Convert back to 12 hour clock
    if hour_count > 12:
        hour_count -= 12
        period = 'PM'
    elif hour_count == 12:
        period = 'PM'
    elif hour_count == 0:
        hour_count += 12
        period = 'AM'
    else:
        period = 'AM'

    # if day is given, find the day of the week
    new_day = None
    if day != None:
        day = day.capitalize()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days.index(day)
        day_index += day_count
        while day_index >= 7:
            day_index -= 7
        new_day = days[day_index]
        
    # find new time
    if day_count == 0:
        if day == None:
            new_time = f'{hour_count}:{minute_count:02d} {period}'
        else:   
            new_time = f'{hour_count}:{minute_count:02d} {period}, {new_day}'
    elif day_count == 1:
        if day == None:
            new_time = f'{hour_count}:{minute_count:02d} {period} (next day)'
        else:   
            new_time = f'{hour_count}:{minute_count:02d} {period}, {new_day} (next day)'
    else:   
        if day == None:
            new_time = f'{hour_count}:{minute_count:02d} {period} ({day_count} days later)'
        else:
            new_time = f'{hour_count}:{minute_count:02d} {period}, {new_day} ({day_count} days later)'

    return new_time