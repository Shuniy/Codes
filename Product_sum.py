# Time : O(n) Space : O(n(Max depth or maximum multiplier))

def product_sum_helper(array, multiplier):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += product_sum_helper(element, multiplier + 1)
        sum += element
    return sum * multiplier

def product_sum(array):
    multiplier = 1
    return product_sum_helper(array, multiplier)

