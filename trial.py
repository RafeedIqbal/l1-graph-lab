# Author: Rafeed Iqbal (Iqbalr8)
# Lab section: L03
# Group: 38

from Graph import Graph
from itinerary import Itinerary
import csv


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
d=0
stat = ''

# d = London.getDistance('1','265')
for station in list(London.graph.keys()):
    if London.getDistance('1',station) > d:
        d = London.getDistance('1', station)
        stat = station
print(stat)
r = i.PatrolRoute_NearestNeighbour('1',['265', '108', '141'])
print(r)

London.printGraph()

