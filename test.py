from Graph import Graph
from itinerary import Itinerary
from Zones import Zone
import csv

class test: 
    def PatrolRouteExecutionExample(): 
        connectionsFile = open('_dataset/london.connections.csv')
        linesFile = open('_dataset/london.lines.csv')
        stationsFile = open('_dataset/london.stations.csv')
        connectionsReader = csv.reader(connectionsFile)
        linesReader = csv.reader(linesFile)
        stationsReader = csv.reader(stationsFile)
        connections = [ connection for connection in connectionsReader]
        lines = [line for line in linesReader]
        stations = [station for station in stationsReader]
        del connections[0]
        del lines[0]
        del stations[0]
        London = Graph()
        for station in stations:
            London.addStation(station[0])
        for line in lines:
            London.addLine(line[0])
        for connection in connections:
            London.addConnection(connection[0], connection[1], connection[2], connection[3])
        for station in stations:
            London.addPos(station[0],station[1],station[2])

        i = Itinerary(London)

        Itin = i.PatrolRoute_NearestNeighbour('155',[ '105', '235', '270', '32'])
        #Itin = i.PathAstar('1', '169')

        print(Itin)

        print("Path Valid?", i.getRoute(Itin)[0])
        print("changes:", i.getRoute(Itin)[1])
        print("stops: ", i.getRoute(Itin)[2])

        print(i.getTime(Itin))
    def printHello(): 
        print("HelloWorld")
    def ZoneExecutionExample():
        connectionsFile = open('_dataset/london.connections.csv')
        linesFile = open('_dataset/london.lines.csv')
        stationsFile = open('_dataset/london.stations.csv')
        connectionsReader = csv.reader(connectionsFile)
        linesReader = csv.reader(linesFile)
        stationsReader = csv.reader(stationsFile)
        connections = [ connection for connection in connectionsReader]
        lines = [line for line in linesReader]
        stations = [station for station in stationsReader]
        del connections[0]
        del lines[0]
        del stations[0]
        London = Graph()
        for station in stations:
            London.addStation(station[0])
        for line in lines:
            London.addLine(line[0])
        for connection in connections:
            London.addConnection(connection[0], connection[1], connection[2], connection[3])
        for station in stations:
            London.addPos(station[0],station[1],station[2])
        
        z = Zone(London)
        for i in stations: 
            z.addZone(i[5])

        for i in stations: 
            z.stationToZone(i[5], i[0])
        
        z.stationConnectionsInZone()
        z.makeIslands()
        z.printIslands()

