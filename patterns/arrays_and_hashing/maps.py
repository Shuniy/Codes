Shubham = {}
Shubham['s'] = 1
Shubham['h'] = 2
Shubham['u'] = 3
Shubham['b'] = 4
Shubham['h'] = 5
Shubham['a'] = 6
Shubham['m'] = 7

print(Shubham)
print(Shubham['s'])
dictionary = {}
dictionary['d'] = [1]
dictionary['i'] = [2]
dictionary['c'] = [3]
dictionary['t'] = [4]
dictionary['i'].append(5)
dictionary['o'] = [6]
dictionary['n'] = [7]
dictionary['a'] = [8]
dictionary['r'] = [9]
dictionary['y'] = [10]
print(dictionary)

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore'], 'China': ['Shanghai']}
locations['Africa'] = {'Egypt': ['Cairo']}
print(locations)

usa_cities = locations['North America']['USA']
usa_cities.sort()
print(usa_cities)

asia_cities = locations['Asia']
print(asia_cities)
asia_cities_list = [element + '-' + str(asia_cities[element]) for element in asia_cities]
asia_cities_list.sort()
print(asia_cities_list)