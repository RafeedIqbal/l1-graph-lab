from math import sin, cos, sqrt, asin, radians  # needed for getDistance

class Graph:

    def __init__(self):
        self.graph = {}
        self.lines = []
        self.numStations = 0
        self.numConnections = 0
        self.numLines = 0 
        self.pos = {}  # A dict for station coordinates

    # Input is the station id (stat_id) as an integer
    # Open for further development by adding more parameters about the station
    # and storing it in another data structure
    def addStation(self, statID):
        if statID not in self.graph:
            self.graph[statID] = []
            self.numStations += 1
        if statID not in self.pos:
            self.pos[statID] = []
            self.numStations += 1

    def addLine(self, line):
        if line not in self.lines:
            self.lines.append(line)
            self.numLines += 1

    def addConnection(self, statID1, statID2, line, time):
        if statID1 not in self.graph:
            raise KeyError("Station ", statID1, " does not exist")
        elif statID2 not in self.graph:
            raise KeyError("Station ", statID2, " does not exist")
        else:
            self.graph[statID1].append([statID2, time, line])
            self.graph[statID2].append([statID1, time, line])
            self.numConnections += 1

    def addPos(self, statID, lat, long):  ##Method for adding the coordinates
        if statID not in self.graph:
            raise KeyError("Station ", statID, " does not exist")
        else:
            self.pos[statID].append([float(lat), float(long)])


    def getDistance(self, statID1, statID2):  ##method for calculating straight line distance between two stations.
        # From stackoverflow
        lat1 = radians(self.pos[statID1][0][0])
        lon1 = radians(self.pos[statID1][0][1])
        lat2 = radians(self.pos[statID2][0][0])
        lon2 = radians(self.pos[statID1][0][1])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers.
        return c * r

    def get_outgoing_stations(self, station):
        stations = []
        for adjacent_stations in self.graph[station]:
            stations.append(adjacent_stations[0])
        return stations

    def get_edge_weight(self, station1, station2):
        for adjacent_stations in self.graph[station1]:
            if station2 in adjacent_stations:
                return int(adjacent_stations[1])

        return "Not Connected"

    def getNumStations(self):
        return self.numStations

    def getNumConnections(self):
        return self.numConnections

    def getNumLines(self):
        return self.numLines

    def getLines(self):
        return self.getLines
    
    def getAllOutgoingStations(self): 
        stations = dict()
        for i in self.graph: 
            stations[i] = self.get_outgoing_stations(i)
        return stations
    
    def getDegrees(self): 
        stations = dict()
        for i in self.graph: 
            stations[i] = len(self.get_outgoing_stations(i))
        return stations
    
    def getAvgDegree(self): 
        sum = 0
        degrees = self.getDegrees()
        for i in degrees: 
            sum += degrees[i]
        return sum / self.numStations

    def printGraph(self):  ##added distance between stations to be printed to test new functions
        for station in self.graph:
            print(self.pos[station][0][0], self.pos[station][0][1])
            for connections in self.graph[station]:
                print(station, " -> ", connections[0], " edge weight: ", connections[1], \
                      "Straight line distance:", self.getDistance(station, connections[0]), "km", \
                      "on Line", connections[2])
