def is_scheme_valid(arr, k, mid):
    """
    Check if it is possible to allocate books to k students such that each student gets at least one book.

    Parameters:
    arr (list): List of integers representing the number of pages in each book
    k (int): Number of students
    mid (int): The maximum number of pages that can be allocated to a student

    Returns:
    bool: True if it is possible to allocate books to k students, False otherwise
    """
    n = len(arr)
    if k > n:
        return False

    students_required = 1
    current_sum = 0
    for i in range(n):
        if arr[i] > mid:
            return False
        if current_sum + arr[i] > mid:
            students_required += 1
            current_sum = arr[i]
            if (students_required > k):
                return False
        else:
            current_sum += arr[i]
    return True


def allocate_minium_number_pages(arr, k):
    """
    This function allocates the minimum number of pages to each student such that the maximum number of pages assigned to a student is minimized. 
    Parameters:
    - arr: a list of integers representing the number of pages in each book
    - k: an integer representing the number of students

    Returns:
    - An integer representing the minimum number of pages assigned to the students, or -1 if it's not possible to allocate the pages
    """
    if k > len(arr):
        return -1
    minimum_pages = max(arr)
    maximum_pages = sum(arr)
    candidate = -1
    while minimum_pages <= maximum_pages:
        mid = minimum_pages + (maximum_pages - minimum_pages) // 2
        if is_scheme_valid(arr, k, mid):
            candidate = mid
            maximum_pages = mid - 1
        else:
            minimum_pages = mid + 1

    return candidate


# test cases for above function
# Number of pages in books
arr = [12, 34, 67, 90]
k = 2   # No. of students
assert allocate_minium_number_pages(arr, k) == 113
