import heapq

class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")


def min_meeting_rooms(meetings: list[Interval]):
    meetings.sort(key=lambda x: x.start)
    minRooms = 0
    minHeap: list[Interval] = []
    for meeting in meetings:
        while len(minHeap) and meeting.start >= minHeap[0].end:
            heapq.heappop(minHeap)
        heapq.heappush(minHeap, meeting)
        minRooms = max(minRooms, len(minHeap))
    return minRooms

def main():
    print("Minimum meeting rooms required are: ", min_meeting_rooms([Interval(1,4), Interval(2,5), Interval(7, 9)]))
    print("Minimum meeting rooms required are: ", min_meeting_rooms([Interval(6,7), Interval(2,4), Interval(8, 12)]))
    print("Minimum meeting rooms required are: ", min_meeting_rooms([Interval(1,4), Interval(2,3), Interval(3, 6)]))

main()