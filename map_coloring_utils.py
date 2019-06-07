from operator import itemgetter
import operator


# Differences between two list
def diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


# Get allowed colors for a city
def get_allowed_colors(graph, city, colors):
    not_allowed_colors = [city[1] for city in graph[(city, False)] if city[1] is not '']
    allowed_colors = diff(colors, not_allowed_colors)
    return allowed_colors


# Degree heuristic.
# return index of city or cities with max neighbours.
def degree_heuristic(graph):
    index_neighbour_len = [(index, len(l[1])) for index, l in enumerate(graph.items()) if l[0][1] is False]
    max_neighbour = max(index_neighbour_len, key=itemgetter(1))[1]
    max_index_neighbour_len = [t[0] for t in index_neighbour_len if t[1] == max_neighbour]
    cities = [list(graph)[index][0] for index in max_index_neighbour_len]
    return cities


# MRV.
# return city or cities with minimum remaining values/colors
def mrv(graph, colors):
    cities_without_color = [(city[0]) for city, colored in graph.items() if city[1] is False]
    allowed_color_each_city = {}
    for city in cities_without_color:
        allowed_color_each_city[city] = get_allowed_colors(graph, city, colors)

    min_available_color_len = min([len(allowed_colors) for city, allowed_colors in allowed_color_each_city.items()])
    cities = [city for city, colors in allowed_color_each_city.items() if len(colors) is min_available_color_len]
    return cities


# Least constraining value
# Return color or colors which used much
def lcv(graph, colors):
    city_color = []
    color_number = {}

    for neighbours in graph.values():
        [city_color.append(c) for c in neighbours if c[1] is not '']

    all_used_colors = list(dict.fromkeys(city_color))

    # First iteration
    if not all_used_colors:
        return colors

    for cc in all_used_colors:
        if cc[1] not in color_number:
            color_number[cc[1]] = 1
        else:
            color_number[cc[1]] += 1

    # Number of max color. {'A': 3, 'B': 3, 'C': 1} => ['A', 'B']
    number_of_max = max(color_number.items(), key=operator.itemgetter(1))[1]
    colors = [key for (key, value) in color_number.items() if value is number_of_max]

    return colors


# Color selected city
def coloring(graph, city, color):

    neighbours = graph[(city, False)]
    del graph[(city, False)]
    graph[(city, True)] = neighbours

    for nei_list in graph.values():

        for n in nei_list:
            if n[0] == city:
                l = list(n)
                l[1] = color
                t = tuple(l)
                nei_list.remove(n)
                nei_list.append(t)
