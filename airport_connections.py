# Time : O(a * (a + r) + a + r + aloga)
# Space : O(a + r)
def airport_connections(airports, routes, starting_airport):
    airport_graph = create_airport_graph(airports, routes)
    unreachable_airport_nodes = get_unreachable_airport_nodes(airport_graph, airports, starting_airport)
    mark_unreachable_connections(airport_graph, unreachable_airport_nodes)
    return get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes)

# Time : O(a + r)
# Space : O(a + r)
def create_airport_graph(airports, routes):
    airport_graph = {}
    for airport in airports:
        airport_graph[airport] = airport_node(airport)
        for route in routes:
            airport, connection = route
            airport_graph[airport].connections.append(connection)

    return airport_graph

# Time : O(a + r) // Simple DFS
# Space : O(a)   
def get_unreachable_airport_nodes(airport_graph, airports, starting_airport):
    visited_airports = {}
    depth_first_traverse_airports(airport_graph, starting_airport, visited_airports)

    unreachable_airport_nodes = []
    for airport in airports:
        if airport in visited_airports:
            continue
        airport_node = airport_graph[airport]
        airport.is_reachable = False
        unreachable_airport_nodes.append(airport_node)

    return unreachable_airport_nodes

def depth_first_traverse_airports(airport_graph, airport, visited_airports):
    if airport in visited_airports:
        return

    visited_airports[airport] = True
    connections = airport_graph[airport].connections
    for connection in connections:
        depth_first_traverse_airports(airport_graph, connection, visited_airports)

class airport_node:
    def __init__(self, airport) -> None:
        self.airport = airport
        self.connections = []
        self.is_reachable = True
        self.unreachable_connections = []

# Time : O(a * (a + r))
# Space : O(a)
def mark_unreachable_connections(airport_graph, unreachable_airport_nodes):
    for airport_node in unreachable_airport_nodes:
        airport = airport_node.airport
        unreachable_connections = []
        depth_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, {})
        airport_node.unreachable_connections = unreachable_connections

def depth_first_add_unreachable_connections(airport_graph, airport, unreachable_connections, visited_airports):
    if airport_graph[airport].is_reachable:
        return
    if airport in visited_airports:
        return

    visited_airports[airport] = True
    unreachable_connections.append(airport)
    connections = airport_graph[airport].connections

    for connection in connections:
        depth_first_add_unreachable_connections(airport_graph, connection, unreachable_connections, visited_airports)

# Time : O((a * loga) + a + r)
# Space : O(1)
def get_min_number_of_new_connections(airport_graph, unreachable_airport_nodes):
    unreachable_airport_nodes.sort(key = lambda airport: len(airport.unreachable_connections), reverse = True)

    number_of_new_connections = 0
    for airport_node in unreachable_airport_nodes:
        if airport_node.is_reachable:
            continue
        number_of_new_connections += 1
        for connection in airport_node.unreachable_connections:
            airport_graph[connection].is_reachable = True

    return number_of_new_connections
