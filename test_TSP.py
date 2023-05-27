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

#Edge Cases
def test_SingleRepeated():
    assert i.PatrolRoute_NearestNeighbour('1',['1'])==['1']

def test_StationsOnSingleLine():
    assert i.PatrolRoute_NearestNeighbour('1',['265', '108', '141'])==['1', '265', '108', '141', '108', '265', '1']

def test_StationsOnSingleLineWithRepeats():
    assert i.PatrolRoute_NearestNeighbour('1', ['1','265','265', '108', '141']) == ['1', '265', '108', '141', '108', '265', '1']

#General cases
def test_generalComparedtoOptimal():
    OptimalTimes = [177, 259, 217, 273, 272, 320]
    Routes = ['40', '148', '263', '74', '241', '181', '295', '274', '92', '68'],\
    ['60', '116', '40', '230', '261', '100', '224', '299', '80', '151'],\
    ['40', '45', '92', '47', '107', '230', '277', '62', '232', '236'],\
    ['45', '63', '170', '297', '301', '177', '289', '120', '129', '19'],\
    ['155', '105', '235', '270', '32', '296', '180', '217', '121', '298'],\
    ['9', '2', '264', '158', '41', '85', '294', '13', '268', '118']
    for j in range(6):
        for k in range(10):
            assert i.getRoute(i.PatrolRoute_NearestNeighbour(Routes[j][k],Routes[j]))[0]==True
            assert i.getTime(i.PatrolRoute_NearestNeighbour(Routes[j][k],Routes[j])) <= 1.6*OptimalTimes[j]
