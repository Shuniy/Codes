def permutations(input):
    if len(input) <= 1:
        return [input]
    elif len(input) == 2:
        return [input, input[::-1]]
    else:
        output = []
        current_level = input[0]
        prev_level = permutations(input[1:])

        for element in prev_level:
            for pos in range(len(element) + 1):
                temp_list = ''
                temp_element = element
                for i in range(len(element) + 1):
                    if pos == i:
                        temp_list += current_level
                    else:
                        temp_list += temp_element[0]
                        temp_element = temp_element[1:]

                output.append(temp_list)
        return output




def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab',
          'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)
