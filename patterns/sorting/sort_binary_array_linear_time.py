# Just count number of 0 and 1's
def sorting_binary(arr):
    n = len(arr)
    number_of_zeroes = 0
    for item in arr:
        if item == 0:
            number_of_zeroes += 1

    number_of_ones = n - number_of_zeroes
    arr = []
    for i in range(number_of_zeroes):
        arr.append(0)
    for i in range(number_of_ones):
        arr.append(1)

    for item in arr:
        print(item, end = " ")

if __name__ == "__main__":
    arr = [1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1]
    sorting_binary(arr)