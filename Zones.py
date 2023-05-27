# Author: Samia Anwar (anwars10)
# Lab section: L03 
# Group: 38 

import Graph
from collections import defaultdict

class Zone: 
    def __init__(self, Graph) -> None:
        self.allConnections = Graph.getAllOutgoingStations()
        self.zoneID = [] #Keeps track of all the zones inside the graph
        self.zoneStations = dict() #Keeps track of all the stations inside each zone
        self.zoneConnections = dict() #Keeps track of all the adjacent stations within the same zone
                                    #dict with key = (str) Zone ID
                                    # value = dict with key = (str) Station ID 
                                    # & value = adjacent station in the same zone
        self.zoneIslands = dict() #Keeps an array of all islands within each zone
     
    def addZone(self, zoneID):
        self.zoneID.append(zoneID)
        self.zoneStations[zoneID] = []
        self.zoneConnections[zoneID] = dict()
    
    def getZones(self): 
        return self.zoneID
    
    def stationToZone(self, zoneID, stationID):
        self.zoneStations[zoneID].append(stationID)
        self.zoneConnections[zoneID][stationID] =  []
    
    def getZonesStations(self): 
        return self.zoneStations

    def stationConnectionsInZone(self): 
        for zoneID in self.zoneID: 
            for i in self.zoneStations[zoneID]: 
                for j in self.zoneStations[zoneID]:
                    if j in self.allConnections[i]:
                        self.zoneConnections[zoneID][i].append(j)
    
    def getZonesConnections(self): 
        return self.zoneConnections

    def printZoneInfo(self): 
        for zoneID in self.zoneID:
            for stationID in self.zoneStations[zoneID]: 
                print("Zone " + zoneID + ", Station " + stationID + ": ")
                for i in range (len(self.zoneConnections[zoneID][stationID])):
                    print(self.zoneConnections[zoneID][stationID][i] + ', ' )
                    if i == len(self.zoneConnections[zoneID][stationID]) - 1: 
                        print('\n')

    def printAllConnections(self): 
        for i in self.allConnections: 
            print("Station " + i + ": ")
            for j in range(len(self.allConnections[i])): 
                print(self.allConnections[i][j] + ", ")
                if j == len(self.allConnections[i]) - 1: 
                    print('\n')

    def connectedComponents(self, adjacent):
        seen = set()
        def component(station):
            stations = set([station])
            while stations:
                station = stations.pop()
                seen.add(station)
                stations |= adjacent[station] - seen
                yield station
        for station in adjacent:
            if station not in seen:
                yield component(station)
    
    def makeIslands(self): 
        for i in self.zoneID: 
            edges = {(v, k) for k, vs in self.zoneConnections[i].items() for v in vs}
            graph = defaultdict(set)

            for v1, v2 in edges:
                graph[v1].add(v2)
                graph[v2].add(v1)

            components = []

            for station in self.zoneConnections[i]:
                lone_island = set()
                if (not self.zoneConnections[i][station]): 
                        lone_island.add(station)
                if (len(lone_island) == 1): 
                    components.append(lone_island)
        
            for component in self.connectedComponents(graph):
                c = set(component)
                island = set()

                for station in self.zoneConnections[i]:
                    for edge in self.zoneConnections[i][station]: 
                        if c.intersection(edge): 
                            island.add(edge)
                
                components.append(island)
        
            
            self.zoneIslands[i] = components
    
    def getIslands(self): 
        return self.zoneIslands

    def printIslands(self): 
        for i in self.zoneIslands: 
            print("Zone " + i + ": ")
            for j in range(len(self.zoneIslands[i])):
                print("Island " + str(j + 1) + ": ")
                for k in self.zoneIslands[i][j]: 
                    print(k)

    #Description: How two zones are connected to eachother
    #Input: Two zone identifiers 
    #Output: An array of all pairs of stations in the two zones 
    #       which connect to eachother
    def zoneConnectionChecker(self, zoneID1, zoneID2):
        connections = []
        for island1 in self.zoneIslands[zoneID1]:
            for station1 in island1: 
                for island2 in self.zoneIslands[zoneID2]: 
                    for station2 in island2: 
                        if station2 in self.allConnections[station1]: 
                            connections.append((station1, station2))
        return connections
