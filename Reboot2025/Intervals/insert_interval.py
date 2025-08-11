class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")

def insert_interval(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    merged = []
    i = 0
    while i < len(intervals) and intervals[i].end <= new_interval.start:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1
    
    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged

def main():
    print("After merging interval: ", end=" ")
    for i in insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,6)):
        i.print_interval()
    print()

    print("After merging interval: ", end=" ")
    for i in insert_interval([Interval(1,3), Interval(5,7), Interval(8,12)], Interval(4,10)):
        i.print_interval()
    print()

    print("After merging interval: ", end=" ")
    for i in insert_interval([Interval(2,3),Interval(5,7)], Interval(1,4)):
        i.print_interval()
    print()

main()