class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")

def can_attend_all_appointments(intervals: list[Interval]):
    intervals.sort(key=lambda x: x.start)
    merged = []
    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return len(merged) == len(intervals)

def main():
    print("Can attend all the appointments: ", 
          can_attend_all_appointments([Interval(1,4), Interval(2,5), Interval(7,9)]))
    print("Can attend all the appointments: ", 
          can_attend_all_appointments([Interval(6,7), Interval(2,4), Interval(8,12)]))
    print("Can attend all the appointments: ", 
          can_attend_all_appointments([Interval(4, 5), Interval(2,3), Interval(3,6)]))

main()