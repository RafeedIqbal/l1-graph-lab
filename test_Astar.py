# Author: Rafeed Iqbal (Iqbalr8)
# Lab section: L03
# Group: 38

from Graph import Graph
from itinerary import Itinerary
import pytest
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

#Edge cases
def test_repeatedStations():
    assert i.PathAstar('1','1') == ['1']

def test_StationsInSingleLine():
    assert i.PathAstar('1','141') == ['1', '265', '108', '141']

def test_farthestStation():
    assert i.PathAstar('1','50') == ['1', '73', '182', '194', '5', '252', '251', '235', '210', '291', '115', '184', '199', '180', '179', '168', '214', '53', '46', '50']

#General cases

def test_allPathsValid():
    for stat1 in ['1','50']:
        for stat2 in list(London.graph.keys()):
            if stat1 == stat2:
                continue
            assert i.getRoute(i.PathAstar(stat1,stat2))[0]==True


