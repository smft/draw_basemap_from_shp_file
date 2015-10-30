# -*- coding: utf-8 -*-

"""
plot border based on shp file 
@author: qzhang
"""

import shapefile
import  time
import numpy as np
from matplotlib import path as mpath
from matplotlib import patches as mpatches
from matplotlib import pyplot as plt

border_shape=shapefile.Reader("/media/qzhang/240E5CF90E5CC608/dunoinfo/province/bou2_4p.shp")
border=border_shape.shapes()
"""
count=0
for border_detail in border:
	print count 
	if border_detail.shapeType==0:
		count+=1
		continue
	else:
		border_points=border_detail.points
		fig=plt.subplots()
		for cell in border_points:
			plt.plot(cell[0],cell[1],"ob")
		plt.show()
		count+=1
"""
border_points=border[202].points
path_data=[]
Path = mpath.Path
count=0
for cell in border_points:
	if count==0:
		trans=(Path.MOVETO,(cell[0],cell[1]))
		path_data+=[trans]
		cell_end=cell
	else:
		trans=(Path.CURVE4,(cell[0],cell[1]))
		path_data+=[trans]
trans=(Path.CLOSEPOLY,(cell_end[0],cell_end[1]))
path_data+=[trans]
fig, ax=plt.subplots()
codes,verts=zip(*path_data)
path=mpath.Path(verts,codes)
x,y=zip(*path.vertices)
line,=ax.plot(x,y,'k-')
ax.grid()
ax.axis('equal')
plt.show()
