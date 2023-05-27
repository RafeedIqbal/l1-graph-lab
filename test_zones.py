# Author: Samia Anwar (anwars10)
# Lab section: L03 
# Group: 38 

from Graph import Graph
from Zones import Zone
import pytest 

def test_addZone_1():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    
    for i in z.getZones(): 
        assert i in zones

def test_addZone_2():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = []
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)

    assert len(z.getZones()) == 0

def test_stationToZone_1(): 
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '1'],
                    ['f', '1'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)

    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    
    for i in z.getZonesStations(): 
        assert i in zones
        for j in z.getZonesStations()[i]: 
            assert j in stations
    
def test_stationToZone_2(): 
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '1'],
                    ['f', '1'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)

    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    
    z.stationConnectionsInZone()
    x = z.getZonesConnections()

    for i in x: 
        for j in x[i]: 
            assert [j, i] in stationInZone

def test_stationConnectionsInZone(): 
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '1'],
                    ['f', '1'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)

    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    
    z.stationConnectionsInZone()
    zonesConnections = z.getZonesConnections()
    allConnections = g1.getAllOutgoingStations()
    for i in zonesConnections: 
        for j in zonesConnections[i]: 
            for k in zonesConnections[i][j]: 
                assert k in allConnections[j]
        

def test_getIslands_1():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['d', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()
    for zone in zones: 
        for island in islands[zone]: 
            if zone == '1':
                assert island == {'a', 'b'}
            if zone == '2':
                assert island == {'c', 'd'}
            if zone == '3':
                assert island == {'e', 'f'}
    
def test_getIslands_2():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()
    for zone in zones: 
        for island in islands[zone]: 
            if zone == '1':
                assert island == {'a', 'b'}
            if zone == '2':
                assert island in [ {'c'}, {'d'} ]
            if zone == '3':
                assert island == {'e', 'f'}

def test_getIslands_3():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '1'], 
                    ['d', '1'],
                    ['e', '1'],
                    ['f', '1'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()
    for zone in zones: 
        for island in islands[zone]: 
            if zone == '1':
                assert island in [{'a', 'b', 'c', 'd'}, {'e', 'f'}]
            if zone == '2':
                assert not island
            if zone == '3':
                assert not island

def test_getIslands_4():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '1'], 
                    ['d', '1'],
                    ['e', '1'],
                    ['f', '2'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()
    for zone in zones: 
        for island in islands[zone]: 
            if zone == '1':
                assert island in [{'a', 'b', 'c', 'd'}, {'e'}]
            if zone == '2':
                assert island == {'f'}
            if zone == '3':
                assert not island

def test_getIslands_5():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = []
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()
    for zone in zones: 
        for island in islands[zone]: 
            if zone == '1':
                assert not island
            if zone == '2':
                assert not island
            if zone == '3':
                assert not island
            
def test_getIslandConnections_1():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()

    connections = z.zoneConnectionChecker('1', '2')
    for i in connections: 
        assert i in [('b', 'c'), ('b', 'd')]

def test_getIslandConnections_2():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()

    connections = z.zoneConnectionChecker('1', '3')
    for i in connections: 
        assert not i

def test_getIslandConnections_3():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()

    connections = z.zoneConnectionChecker('2', '3')
    for i in connections: 
        assert not i

def test_getIslandConnections_4():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['a', 'f', '1', '1'],
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()

    connections = z.zoneConnectionChecker('1', '2')
    for i in connections: 
        assert i in [('b', 'c'), ('b', 'd'), ('a', 'f')]

def test_getIslandConnections_5():
    stations = ['a', 'b', 'c', 'd', 'e', 'f']
    lines = ['1']
    connections =  [['a', 'b', '1', '1'], 
                    ['b', 'c', '1', '1'], 
                    ['b', 'd', '1', '1'], 
                    ['d', 'e', '1', '1'],
                    ['e', 'f', '1', '1']]

    zones = ['1', '2', '3']
    stationInZone = [['a', '1'], 
                    ['b', '1'], 
                    ['c', '2'], 
                    ['d', '2'],
                    ['e', '3'],
                    ['f', '3'] ]
    
    g1 = Graph()
    for i in stations: 
        g1.addStation(i)
    for i in lines: 
        g1.addLine(i)
    for i in connections: 
        g1.addConnection(i[0], i[1], i[2], i[3])
    
    z = Zone(g1)
    for i in zones: 
        z.addZone(i)
    for i in stationInZone: 
        z.stationToZone(i[1], i[0])
    z.stationConnectionsInZone()
    z.makeIslands()
    islands = z.getIslands()

    connections = z.zoneConnectionChecker('2', '3')
    for i in connections: 
        assert i in [('d', 'e')]


# def main():
#     stations = ['a', 'b', 'c', 'd', 'e', 'f']
#     lines = ['1']
#     connections =  [['a', 'b', '1', '1'], 
#                     ['b', 'c', '1', '1'], 
#                     ['b', 'd', '1', '1'], 
#                     ['e', 'f', '1', '1']]

#     zones = ['1', '2', '3']
#     stationInZone = [['a', '1'], 
#                     ['b', '1'], 
#                     ['c', '2'], 
#                     ['d', '2'],
#                     ['e', '1'],
#                     ['f', '1'] ]
    
#     g1 = Graph()
#     for i in stations: 
#         g1.addStation(i)
#     for i in lines: 
#         g1.addLine(i)
#     for i in connections: 
#         g1.addConnection(i[0], i[1], i[2], i[3])
    
#     z = Zone(g1)
#     for i in zones: 
#         z.addZone(i)
#     for i in stationInZone: 
#         z.stationToZone(i[1], i[0])
#     z.stationConnectionsInZone()
#     z.printZoneInfo()
#     #z.printAllConnections()
#     z.getIslands()
#     z.printIslands()

#     a = z.zoneConnectionChecker('1', '2')
#     print(a)


# if __name__ == "__main__":
#     main()