def build_graph(map):
    # key: (X, Bool). X means city AND Bool means Colored Or Not
    # value: [(X, ''), (Y, '')]. List of neighbours. Second item of tuple is color of city
    graph = {}

    with open(map, 'r') as cities_file:
        cities = cities_file.readlines()
        cities = [city.strip('\n').replace(" ", "") for city in cities if len(city.strip('\n').replace(" ", "")) != 0]

    for city_neighbours in cities:
        city, neighbours = city_neighbours.split(":")
        neighbours = neighbours.replace("[", "").replace("]", "").replace("\n", "").split(",")

        # Converting format of neighbours. [X, Y] => [('X', ''), ('Y', '')]
        neighbours = [(neighbour, '') for neighbour in neighbours if neighbour != '']
        graph[(city, False)] = neighbours

    return graph

