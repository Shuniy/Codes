# Time : O(n^2)
# Space : O(n)

def three_number_sum(array, total_sum):
    array.sort()

    result = []

    for i in range(len(array) - 2):
        left_index = i + 1
        right_index = len(array) - 1
        
        while left_index <= right_index:
            triplates = []
            numbers_sum = array[left_index] + array[i] + array[right_index]
            if numbers_sum == total_sum:
                triplates.append(array[i])
                triplates.append(array[left_index])
                triplates.append(array[right_index])
                left_index += 1
                right_index -= 1
                result.append(triplates)
            elif numbers_sum < total_sum:
                left_index += 1
            elif numbers_sum > total_sum:
                right_index -= 1
            
    return result

sample_input_array = [12, 3, 1, 2, -6, 5, -8, 6]
sample_sum = 0
result = three_number_sum(sample_input_array, sample_sum)
print("The sets of triplates are: ", result)
