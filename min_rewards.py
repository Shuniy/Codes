# Time : O(n^2)
# Space : O(n)

# Naive Method
def min_rewards(scores):
    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1

    return sum[rewards]

# A Bit better
# Time : O(n)
# Space : O(n)
def get_local_minima_indices(array):
    if len(array) == 1:
        return [0]

    local_min_indices = []

    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            local_min_indices.append(i)

        if i == len(array) - 1 and array < array[i - 1]:
            local_min_indices.append(i)

        if i == 0 or i == len(array) - 1:
            continue

        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            local_min_indices.append(i)

    return local_min_indices
    

def expand_from_local_min_index(local_minima_index, scores, rewards):
    left_index = local_minima_index - 1

    while left_index >= 0 and scores[left_index] > scores[left_index + 1]:
        rewards[left_index] = max(rewards[left_index], rewards[left_index + 1] + 1)
        left_index -= 1

    right_index = local_minima_index + 1
    while right_index < len(scores) and scores[right_index] > scores[right_index - 1]:
        rewards[right_index] = rewards[right_index - 1] + 1


def min_rewards(scores):
    rewards = [1 for _ in scores]
    local_minima_indices = get_local_minima_indices(scores)

    for local_min_index in local_minima_indices:
        expand_from_local_min_index(local_min_index, scores, rewards)
    return sum(rewards)

# Most Optimal Method
# Time : O(n)
# Space : O(n)

def min_rewards(scores):
    rewards = [1 for _ in scores]

    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    
    return sum(rewards)