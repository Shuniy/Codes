class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")

def merge(intervals: list[Interval]) -> list[Interval]:
    mergedIntervals = []
    if len(intervals) < 2:
        return intervals
    
    intervals.sort(key=lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end

    for interval in intervals:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    mergedIntervals.append(Interval(start, end))
    return mergedIntervals

def main():
    print("Merged Intervals: ", end=" ")
    for i in merge([Interval(1,4), Interval(2,5), Interval(7,9)]):
        i.print_interval()
    print()

    print("Merged Intervals: ", end=" ")
    for i in merge([Interval(6,7), Interval(2,4), Interval(5,9)]):
        i.print_interval()
    print()

    print("Merged Intervals: ", end=" ")
    for i in merge([Interval(1,4), Interval(2,6), Interval(3,5)]):
        i.print_interval()
    print()

main()