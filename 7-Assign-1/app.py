from flask import Flask
import ghhops_server as hs

import assig as geo
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createmovesPointss",
    name = "Create moved Points",
    inputs=[
        hs.HopsPoint("Count", "C", "Number of Random Points", hs.HopsParamAccess.LIST),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
    ]
)
def moveccPoints(points, X, Y, Z):
    moved_points = geo.movePoints(points,X, Y,Z)
    return moved_points



@hops.component(
    "/moveLine",
    name = "Create moved Points",
    inputs=[
        hs.HopsCurve("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("X range of randomness", "X", "Value of motion in X direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Value of motion in X direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Value of motion in X direction", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsCurve("Random Points","RP","List of generated random points ", hs.HopsParamAccess.ITEM)
    ]
)
def moveLine(line,X,Y,Z):
    moved = geo.moveLine(line,X,Y,Z)
    return moved



@hops.component(
    "/complete",
    name = "Create complete graph",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of ]Points", hs.HopsParamAccess.ITEM),

    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def complete(nn):
    nodes = geo.complete(nn) [0]
    edges = geo.complete(nn) [1]
    return nodes, edges








@hops.component(
    "/geotograph11",
    name = "Createa graph out of geometry",
    inputs=[
        hs.HopsPoint("points", "P", " points", hs.HopsParamAccess.LIST),
        hs.HopsCurve("lines", "L", "lines", hs.HopsParamAccess.LIST),
    ],
    outputs=[
       hs.HopsString("graph","G","graph", hs.HopsParamAccess.ITEM)
    ]
)
def geoTograph(pointss,lines):
    graph =  geo.geoTograph(pointss,lines)
    return graph
    

















if __name__== "__main__":
    app.run(debug=True)




