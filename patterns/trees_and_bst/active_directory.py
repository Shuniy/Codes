"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.

The requirement to create an efficient algorithm that searches into this encapsulated structure, like a Matryoshka dolls, as been satisfied by a recursive algorithm.

Time and Space complexity
The time complexity of this algorithm is dependant on the number of iterations that are launched. Being in this case dependent on encapsulation of groups and number of users of folders, resulting in a O(g*u). As for the space complexity, it is directly dependent on the number of returns the function does, hence, in this case O(1).
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user in group.get_users():
        return True
    else:
        if len(group.get_groups()) == 0:
            return False
        else:
            for sub_group in group.get_groups():
                found = is_user_in_group(user, sub_group)
                if found:
                    return True
    return False

    return None


# Testing preparation
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Normal Cases:
print('Normal Cases:')
print(is_user_in_group(user='parent_user', group=parent))
# False
print(is_user_in_group(user='child_user', group=parent))
# False
print(is_user_in_group(user='sub_child_user', group=parent), '\n')
# True

# Edge Cases:
print('Edge Cases:')
print(is_user_in_group(user='', group=parent))
# False
print(is_user_in_group(user='', group=child))
# False
