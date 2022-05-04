#we import all the libraries that our functions need here too

import rhino3dm as rg

def Arc(x,y,radius,angleRadians):
   center=rg.Point3d(x,y,0)
   Arc1=rg.Arc(center,radius,angleRadians)
   Arc2=Arc1.ToNurbsCurve()
   print(type(Arc2))
   return  Arc2
   