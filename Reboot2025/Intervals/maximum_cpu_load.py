import heapq

class Job:
    def __init__(self, start: int, end: int, load: int):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end=", ")

def find_max_cpu_load_merging(jobs: list[Job]):
    jobs.sort(key=lambda x: x.start)

    start = jobs[0].start
    end = jobs[0].end
    load = 0
    total_jobs: list[Job] = []

    for job in jobs:
        if job.start < end:
            end = max(end, job.end)
            load += job.load
        else:
            total_jobs.append(Job(start, end, load))
            start = job.start
            end = job.end
            load = job.load
    
    total_jobs.append(Job(start, end, load))
    return max([j.load for j in total_jobs])

def find_max_cpu_load(jobs: list[Job]):
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    minHeap: list[Job] = []

    for job in jobs:
        while minHeap and job.start >= minHeap[0].end:
            current_cpu_load -= minHeap[0].load
            heapq.heappop(minHeap)
            
        heapq.heappush(minHeap, job)
        current_cpu_load += job.load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load

def main():
    print("Maximum CPU load at a time is: ", find_max_cpu_load_merging([Job(1,4,3), Job(2,5,4), Job(7,9,6)]))
    print("Maximum CPU load at a time is: ", find_max_cpu_load_merging([Job(6,7,10), Job(2,4,11), Job(8,12,15)]))
    print("Maximum CPU load at a time is: ", find_max_cpu_load_merging([Job(1,4,2), Job(2,4,1), Job(3,6,5)]))

    print("Maximum CPU load at a time is: ", find_max_cpu_load([Job(1,4,3), Job(2,5,4), Job(7,9,6)]))
    print("Maximum CPU load at a time is: ", find_max_cpu_load([Job(6,7,10), Job(2,4,11), Job(8,12,15)]))
    print("Maximum CPU load at a time is: ", find_max_cpu_load([Job(1,4,2), Job(2,4,1), Job(3,6,5)]))


main()