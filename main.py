import sys
from pprint import pprint
from build_graph import build_graph
from map_coloring_utils import mrv, degree_heuristic, lcv, get_allowed_colors, coloring

if __name__ == "__main__":

    map = 'map.txt'

    colors = ['RED', 'GREEN']

    # Build graph from file
    graph = build_graph(map)

    for _ in range(len(graph)):
        cities_with_max_degree = degree_heuristic(graph)
        cities_with_minimum_remaining_colors = mrv(graph, colors)
        much_used_colors = lcv(graph, colors)

        selected_city = set(cities_with_max_degree).intersection(set(cities_with_minimum_remaining_colors)).pop()

        # Get allowed color for selected city
        colors_of_selected_city = get_allowed_colors(graph, selected_city, colors)

        # Final chosen color
        common_color = set(much_used_colors).intersection(set(colors_of_selected_city))

        try:
            if common_color:
                color = common_color.pop()
            else:
                color = colors_of_selected_city.pop()

            coloring(graph, selected_city, color)
        except IndexError:
            sys.exit("Something went wrong. Perhaps there is not enough color for this map")

    alone_cities = [graph[city].append("Any Color") for city, neighbours in graph.items() if len(neighbours) == 0]
    pprint(graph)
