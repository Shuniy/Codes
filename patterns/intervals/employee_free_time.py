import heapq

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")

class EmployeeInterval:
    def __init__(self, interval: Interval, employee_index: int, interval_index: int):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        return self.interval.start < other.interval.start

def find_employee_free_time(schedule: list[list[int]]) -> list[Interval]:
    interval_schedule: list[list[Interval]] = [
        [
            Interval(start, end) for start, end in sch
        ] for sch in schedule
    ]

    # works in all cases but specially to consider if schedule of individual employee is sorted
    extended_schedule: list[Interval] = []
    for item in interval_schedule:
        extended_schedule.extend(item)

    extended_schedule.sort(key=lambda x: x.start)
    start = extended_schedule[0].start
    end = extended_schedule[1].end
    final_schedule: list[Interval] = []

    for interval in extended_schedule:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            final_schedule.append(Interval(start, end))
            start = interval.start
            end = interval.end
    final_schedule.append(Interval(start, end))
    free_times: list[Interval] = []

    for i in range(1, len(final_schedule)):
        p_interval = final_schedule[i - 1]
        c_interval = final_schedule[i]
        free_times.append(Interval(p_interval.end, c_interval.start))
    return free_times

def find_employee_free_time_if_schedule_employee_sorted(schedule: list[list[int]]) -> list[Interval]:
    interval_schedule: list[list[Interval]] = [
        [
            Interval(start, end) for start, end in sch
        ] for sch in schedule
    ]

    free_times: list[Interval] = []
    minHeap: list[EmployeeInterval] = []

    for i, emp in enumerate(interval_schedule):
        # adding first busy time slot of each employee
        heapq.heappush(minHeap, EmployeeInterval(emp[0], i, 0))

    # start with the smallest start time
    previous_interval = minHeap[0].interval
    while minHeap:
        # get the next time interval
        next_interval = heapq.heappop(minHeap)
        # if next time interval is starting after previous interval, then there is free time
        # change previous interval to next interval
        if  previous_interval.end < next_interval.interval.start:
            free_times.append(Interval(previous_interval.end, next_interval.interval.start))
            previous_interval = next_interval.interval
        else:
            # if next time interval is starting between previous time interval
            # case 1: next time interval closes/ends after 1st interval,
            # so take the bigger end time
            if previous_interval.end < next_interval.interval.end:
                previous_interval = next_interval.interval
            else:
                # case 1: next time interval closes/ends before 1st interval closes/ends,
                # so keep the bigger time interval which is previous time interval
                previous_interval = previous_interval
        # get employee index and add to min heap
        employee_schedule = interval_schedule[next_interval.employee_index]
        # check to prevent list out of bounds error
        if next_interval.interval_index + 1 < len(employee_schedule):
            heapq.heappush(minHeap, EmployeeInterval(employee_schedule[next_interval.interval_index + 1], next_interval.employee_index, next_interval.interval_index + 1))

    return free_times

def main():
    print("Free intervals: ", end=" ")
    for i in find_employee_free_time([[[1,3], [5,6]], [[2,3], [6,8]]]):
        i.print_interval()
    print()

    print("Free intervals: ", end=" ")
    for i in find_employee_free_time([[[1,3], [9,12]], [[2,4]], [[6,8]]]):
        i.print_interval()
    print()


    print("Free intervals: ", end=" ")
    for i in find_employee_free_time([[[1,3]], [[2,4]], [[3,5], [7,9]]]):
        i.print_interval()
    print()

    print("Free intervals: ", end=" ")
    for i in find_employee_free_time_if_schedule_employee_sorted([[[1,3], [5,6]], [[2,3], [6,8]]]):
        i.print_interval()
    print()

    print("Free intervals: ", end=" ")
    for i in find_employee_free_time_if_schedule_employee_sorted([[[1,3], [9,12]], [[2,4]], [[6,8]]]):
        i.print_interval()
    print()


    print("Free intervals: ", end=" ")
    for i in find_employee_free_time_if_schedule_employee_sorted([[[1,3]], [[2,4]], [[3,5], [7,9]]]):
        i.print_interval()
    print()



main()
