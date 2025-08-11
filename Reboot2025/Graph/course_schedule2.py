import collections
from typing import List, Set, Dict

def course_schedule2(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Find a valid course schedule given the number of courses and their prerequisites.
    Uses Kahn's algorithm for topological sorting.
    
    Args:
        num_courses: Total number of courses to take
        prerequisites: List of prerequisite pairs [course, prerequisite]
        
    Returns:
        List[int]: A valid course schedule if possible, empty list if impossible
    """
    if num_courses <= 0:
        return []
        
    # Build the directed graph and in-degree count
    graph: Dict[int, Set[int]] = collections.defaultdict(set)
    in_degree: Dict[int, int] = {i: 0 for i in range(num_courses)}  # Initialize all courses with 0 in-degree
    
    for course, pre in prerequisites:
        graph[pre].add(course)
        in_degree[course] += 1

    # Initialize queue with courses having no prerequisites
    queue = collections.deque([course for course in range(num_courses) if in_degree[course] == 0])
    visited: Set[int] = set()
    result: List[int] = []
    
    while queue:
        course = queue.popleft()
        visited.add(course)
        result.append(course)
        
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if we visited all courses (no cycles)
    if len(visited) != num_courses:
        return []  # Cycle detected, schedule impossible
        
    return result

# test cases
print(course_schedule2(2, [[1, 0]]))  # [0, 1] - simple case
print(course_schedule2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,1,2,3] or [0,2,1,3] - multiple prerequisites
print(course_schedule2(1, []))  # [0] - single course, no prerequisites
print(course_schedule2(3, [[0, 1], [1, 2], [2, 0]]))  # [] - cycle
print(course_schedule2(3, [[0, 1], [0, 2], [1, 2]]))  # [2,1,0] - DAG with multiple paths
print(course_schedule2(3, [[0, 1], [1, 2], [2, 1]]))  # [] - cycle with branch
print(course_schedule2(4, [[1, 0], [2, 0], [3, 0]]))  # [0,1,2,3] or any permutation - multiple courses with same prerequisite
print(course_schedule2(4, [[1, 0], [2, 1], [3, 2]]))  # [0,1,2,3] - linear dependencies
print(course_schedule2(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # [0,1,2,3] or [0,2,1,3] - complex dependencies
print(course_schedule2(0, []))  # [] - no courses
print(course_schedule2(3, []))  # [0,1,2] - no prerequisites
print(course_schedule2(4, [[1, 0], [2, 0], [3, 0], [3, 1], [3, 2]]))  # [0,1,2,3] or [0,2,1,3] - multiple prerequisites for same course
