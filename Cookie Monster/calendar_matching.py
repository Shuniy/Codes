# Time : O(c1 + c2)
# Space : O(c1 + c2)

def calender_matching(calender1, calender2, daily_bounds1, daily_bounds2, meeting_duration):
    updated_calender1 = update_calender(calender1, daily_bounds1)
    updated_calender2 = update_calender(calender2, daily_bounds2)

    merged_calender = merged_calenders(updated_calender1, updated_calender2)
    flattened_calender = flatten_calender(merged_calender)

    available = get_matching_availabilities(flatten_calender, meeting_duration)

    return list(map(lambda m: [minutes_to_time(m[0]), minutes_to_time(m[1])], available))

def minutes_to_time(time):
    hours = time // 60
    minutes = time % 60

    hours_to_string = str(hours)
    minutes_to_string = '0' + str(minutes) if minutes < 10 else str(minutes)
    return hours_to_string + ':' + minutes_to_string


def get_matching_availabilities(calender, meeting_duration):
    available = []
    for i in range(1, len(calender)):
        start = calender[i - 1][1]
        end = calender[i][0]
        duration = end - start

        if duration >= meeting_duration:
            available.append([start, end])

    return available
    

def flatten_calender(calender):
    flattened = [calender[0][:]]
    for i in range(1, len(calender)):
        current_meeting = calender[i]
        previous_meeting = flattened[-1]

        current_start, current_end = current_meeting
        previous_start, previous_end = previous_meeting

        if previous_end >= current_start:
            new_previous_meeting = [previous_start, max(previous_end, current_end)]
            flattened[-1] = new_previous_meeting
        else:
            flattened.append(current_meeting[:])
    
    return flattened
    

def merged_calenders(calender1, calender2):
    merged = []
    i, j = 0, 0

    while i < len(calender1) and j < len(calender2):
        meeting1, meeting2 = calender1[i], calender2[j]

        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    if i < len(calender1):
        merged += calender2
    
    if j < len(calender2):
        merged += calender1

    return merged

def update_calender(calender, daily_bound):
    updated_calender = calender[:]
    updated_calender.insert(0, ['00:00', daily_bound[0]])
    updated_calender.insert(0, [daily_bound[1], '23:59'])

    # Transform time in minutes
    return list(map(lambda m : [time_to_minutes(m[0]), time_to_minutes(m[1])], updated_calender))

def time_to_minutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes
