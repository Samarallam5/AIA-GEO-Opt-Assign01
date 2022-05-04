from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometryArc as geoArc

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/GeoArc11",
    name = "GeoArc",
    inputs=[
       
        hs.HopsNumber("x coordinate", "x", "Center point x coordinate", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsNumber("y coordinate", "y", "Center point y coordinate", hs.HopsParamAccess.ITEM, default= 0),
        hs.HopsNumber("Radius", "r", "Arc Radius", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("angleRadians", "aR", "Radian Angle max 6", hs.HopsParamAccess.ITEM, default= 1),
        

    ],
    outputs=[
       hs.HopsCurve("Curve","Arc","Arc by radius and center", hs.HopsParamAccess.ITEM)
    ]
)
def createArc(x,y,r,aR):

    Arc2 = geoArc.Arc(x,y,r,aR)
    
    return Arc2

if __name__== "__main__":
    app.run(debug=True)
