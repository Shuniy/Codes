"""
The recursion process, is based on the visit of each folder, on each folder we keep the files that match the desired pattern and we keep on going deeper on the folder structure by launching subsequent calls to the function. The decision not to use the provided assistance to detect if it was a file or a folder, has been decided after not being able to properly use it (and also seeing the facility of coding my own solutions).

Time and Space complexity
In therms of time complexity, trying to be guided by the Master theorem, tough not being able to quantify the size of n/b (as it's a folders depth and it needs not to be splitted proportionally). Thus, using another approach, the time complexity is dependant on the number of iterations that are launched. Being in this case dependent on depth and width of folders, resulting in a O(d*w). As for the space complexity, in this case, it is directly dependent on the number of returns the function does, hence, the number of found files f, O(f).
"""
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        return []
    if len(os.listdir(path)) == 0:
        return []
    path_elements = os.listdir(path)
    path_files = [file for file in path_elements if "." + suffix in file]
    path_folders = [file for file in path_elements if "." not in file]

    for folder in path_folders:
        path_files.extend(find_files(suffix = suffix, path = path + '/' + folder))

    return None


# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []
