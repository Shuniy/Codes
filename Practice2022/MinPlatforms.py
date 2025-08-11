"""
Problem Statement
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345
"""
def min_platforms(arrival, departure) -> int:
    num_platforms = 0
    for time in range(min(arrival), max(departure) + 10, 10):
        temp_num_platforms = 0
        for i_train in range(len(arrival)):
            if (time >= arrival[i_train]) and (time < departure[i_train]):
                temp_num_platforms += 1

        if temp_num_platforms > num_platforms:
            num_platforms = temp_num_platforms
    return num_platforms


def min_platforms(arrival, departure):

    if len(arrival) != len(departure):
        return

    arrival.sort()
    departure.sort()

    count = 1
    i = 1
    j = 0

    platform = 1
    while i < len(arrival) and j < len(departure):
        if arrival[i] < departure[j]:
            count += 1
            i += 1

        elif arrival[i] >= departure[j]:
            count -= 1
            j += 1

        if count > platform:
            platform = count

    return platform

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)
