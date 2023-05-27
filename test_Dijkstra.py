# Author: Akshit Gulia (guliaa)
# Lab Section: L03
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
connections = [connection for connection in connectionsReader]
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
    London.addPos(station[0], station[1], station[2])

i = Itinerary(London)


# Edge Cases
def test_same_source_and_same_destination():
    assert i.dijkstra('52', '52') == ['52']


def test_empty_nodes_passed_in():
    assert i.dijkstra('', '') == ['']


# General Test

def test_get_path_from_1_to_2():
    assert i.dijkstra('1', '2') == ['1', '265', '110', '17', '74', '99', '236', '229', '273', '248', '285', '279', '13',
                                    '156', '2']


def test_compare_path_with_A_star():  # the travel time of the path given by Dijkstra will always be better or same..
                                      # ..as the time of the path given by A*
    for station in list(London.graph.keys()):
        assert i.getTime(i.dijkstra('52', station)) <= i.getTime(i.PathAstar('52', station))
