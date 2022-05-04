import random as r
import rhino3dm as rg
import networkx as nx
import matplotlib.pyplot as plt

def movePoints(points,X, Y,Z):
    moved_points=[]
    for i in range(len(points)):
        point=points[i]
        moved_point=rg.Point3d(X+point.X, Y+point.Y, Z+point.Z)
        moved_points.append(moved_point)
    return moved_points


def moveLine(line,X,Y,Z):
    start=line.PointAtStart
    end=line.PointAtEnd
    moved_start=rg.Point3d(X+start.X, Y+start.Y, Z+start.Z)
    moved_end=rg.Point3d(X+end.X, Y+end.Y, Z+end.Z)
    moved=rg.LineCurve(moved_start, moved_end)

    return moved



def complete(nn):
    G = nx.complete_graph(nn)
    lay = nx.kamada_kawai_layout(G)

    nodes = []
    for n in lay.values():
        pt = rg.Point3d(n[0], n[1] , 0)
        nodes.append(pt)
    
    edges = []
    for e in G.edges:
        p1 = rg.Point3d( lay[e[0]][0], lay[e[0]][1], 0 )
        p2 = rg.Point3d( lay[e[1]][0], lay[e[1]][1], 0 )
        line = rg.LineCurve(p1, p2)
        edges.append(line)

    return nodes, edges




def geoTograph(points,lines):
    G=nx.Graph()
    pc=rg.PointCloud()
    #Add nodes from the points and assign a position attribute that represents the node's coordinates
    positions={}
    for i in range(len(points)):
        point=points[i]
        G.add_node(i,pos=(point.X,point.Y))
        pc.Add(point)
        positions[i]=[point.X,point.Y]

    #Get lines' end points, and find the equivalent nodes number of these points
    start_points=[]
    end_points=[]
    for i in range(len(lines)):
        line=lines[i]
        start=line.PointAtStart
        end=line.PointAtEnd
        start_points.append(start)
        end_points.append(end)


    #Get start and end points locations (node number)
    for i in range(len(start_points)):
        start_node=rg.PointCloud.ClosestPoint(pc,start_points[i])
        end_node=rg.PointCloud.ClosestPoint(pc,end_points[i])
        G.add_edge(start_node, end_node)
    print (G.edges)
    graph="sucess"
    #plot the graph using the defined positions

    fig, ax = plt.subplots(figsize=(15,15))
    nx.draw_networkx_nodes(G,pos=nx.get_node_attributes(G,'pos'),node_size=30,node_color='purple')
 
    nx.draw_networkx_edges(G,positions)
    #nx.draw(G)
    plt.show()
 
    return graph


