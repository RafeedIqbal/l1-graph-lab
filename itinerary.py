class Itinerary:

    def __init__(self, Graph):

        self.Graph = Graph


    def PathAstar(self, start_node, stop_node):  ##Also taken from the web, edited to work
        # heuristic function with equal values for all nodes
        def h(current_node):
            H = self.Graph.getDistance(current_node, stop_node)

            return H

        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {start_node: 0}

        # parents contains an adjacency map of all nodes
        parents = {start_node: start_node}

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n is None or g[v] + h(v) < g[n] + h(n):
                    n = v

            if n is None:
                return

            # if the current node is the stop_node
            # then we begin reconstructing the path from it to the start_node
            if n == stop_node:
                recons_path = []

                while parents[n] != n:
                    recons_path.append(n)
                    n = parents[n]

                recons_path.append(start_node)

                recons_path.reverse()

                return recons_path

            # for all neighbors of the current node do
            for connection in self.Graph.graph[n]:
                m = connection[0]
                weight = self.Graph.getDistance(n, m)
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        return

    # def PatrolRoute_ReverseOrder(self, base, stops):
    #     r = []
    #     d = {stop: self.Graph.getDistance(base, stop) for stop in stops}
    #     sortedByDistance = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    #     stations = list(sortedByDistance.keys())
    #     current_station = base
    #     next_station = stations[0]
    #     r = r + self.PathAstar(current_station, next_station)
    #     current_station = next_station
    #     for station in r:
    #         if station in stations:
    #             stations.remove(station)
    #
    #     while len(stations) > 0:
    #         next_station = stations.pop(0)
    #         r = r + self.PathAstar(current_station, next_station)[1:]
    #         for station in r:
    #             if station in stations:
    #                 stations.remove(station)
    #         current_station = next_station
    #     r = r + self.PathAstar(current_station, base)[1:]
    #     return r

    def PatrolRoute_NearestNeighbour(self, base, stops):
        r = []
        d = {stop: self.Graph.getDistance(base, stop) for stop in stops}
        sortedByDistance = dict(sorted(d.items(), key=lambda item: item[1], reverse=False))
        stations = list(sortedByDistance.keys())
        current_station = base
        next_station = stations[0]

        r = self.dijkstra(current_station, next_station)
        current_station = next_station

        for station in r:
            if station in stations:
                stations.remove(station)

        while len(stations) > 0:
            stations = list(dict(
                sorted({stop: self.Graph.getDistance(current_station, stop) for stop in stations}.items(),
                       key=lambda item: item[1], reverse=False)).keys())
            next_station = stations[0]
            r = r + self.PathAstar(current_station, next_station)[1:]
            for station in r:
                if station in stations:
                    stations.remove(station)
            current_station = next_station
        r = r + self.PathAstar(current_station, base)[1:]
        return r

        # for station in r:
        #     if station in stations:
        #         stations.remove(station)
        # for i in range(len(stations)-1):
        #     r = r + self.PathAstar(stations[i], stations[i+1])
        #     for station in r:
        #         if station in stations:
        #             stations.remove(station)
        #     if (i)>(len(stations)-1):
        #         break
        # #r = r + self.PathAstar(stations[-1],base)
        # return r

    @staticmethod
    def shortest_path_dijkstra(shortest_path_tree, starting_station,
                               destination_station):  # Taken from web, adjusted to work with our graph
        path = []
        node = destination_station

        while node != starting_station:
            path.append(node)
            node = shortest_path_tree[node]

        path.append(starting_station)
        path.reverse()
        return path

    def dijkstra(self, starting_station, destination_station):  # Taken from web, adjusted to work with
        # our graph
        graph = self.Graph

        unvisited_stations = list(graph.graph.keys())

        shortest_times = {}

        shortest_path_tree = {}

        max_value = 1e8
        for station in unvisited_stations:
            shortest_times[station] = max_value
        shortest_times[starting_station] = 0

        while unvisited_stations:

            current_min_station_time = None
            for station in unvisited_stations:
                if current_min_station_time is None:
                    current_min_station_time = station
                elif shortest_times[station] < shortest_times[current_min_station_time]:
                    current_min_station_time = station

            neighboring_stations = graph.get_outgoing_stations(current_min_station_time)
            for neighbor_station in neighboring_stations:
                tentative_value = shortest_times[current_min_station_time] + graph.get_edge_weight(
                    current_min_station_time,
                    neighbor_station)
                if tentative_value < shortest_times[neighbor_station]:
                    shortest_times[neighbor_station] = tentative_value

                    shortest_path_tree[neighbor_station] = current_min_station_time

            unvisited_stations.remove(current_min_station_time)

        return Itinerary.shortest_path_dijkstra(shortest_path_tree, starting_station, destination_station)

    def getLines(self, stat1, stat2):
        Lines = []
        for connections in self.Graph.graph[stat1]:
            if connections[0] == stat2:
                Lines.append(connections[2])
        return Lines

    def getRoute(self, path):
        p = path
        currentLine = self.getLines(p[0], p[1])
        j = 1
        changes = 0
        stops = len(p)
        try:
            for i in range(1, len(p) - 1):
                if currentLine == self.getLines(p[i], p[i + 1]) or (currentLine[0] in self.getLines(p[i], p[i + 1])):
                    j += 1
                    continue
                else:
                    changes += 1
                    # print("Stay on Line", currentLine, "for", j, "stops")
                    currentLine = self.getLines(p[i], p[i + 1])
                    # if (i + 1) != len(p):
                    #     j = 1
        except:
            return [False, changes, stops]

        return [True, changes, stops]

    def getTime(self, stops):
        time = 0
        for i in range(len(stops) - 1):
            time = time + self.Graph.get_edge_weight(stops[i], stops[i + 1])
        return time
