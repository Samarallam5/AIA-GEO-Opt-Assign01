from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometryArc as geoarc

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraph",
    name = "createGraph",
    inputs=[
        
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),


    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createGraph(X, Y, layout):

    G = geoarc.createGridGraph(X, Y)
    GW = geoarc.addRandomWeigrhs(G)

    nodes = geoarc.getNodes(GW, layout)
    edges = geoarc.getEdges(GW, layout) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)