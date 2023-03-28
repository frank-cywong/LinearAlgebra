# Plotting 3D Data
# Patrick Honner, 3/19/23

# Import the matplotlib package and alias the pyplot module 
import matplotlib.pyplot as plt
import numpy as np

# Library for 3D plots
from mpl_toolkits.mplot3d import Axes3D

# Create the plot object
fig = plt.figure()
ax = plt.axes(projection='3d')

xdata  =[]
ydata = []
zdata = []

# Read in the data
# Data format: x,y,z

f = open("3D_data.txt")
data = f.readlines()
f.close()

# Parse the data into lists of x's, y's, and z's
for i in range(len(data)):
  datapoint = data[i].split(',')
  xdata.append(float(datapoint[0]))
  ydata.append(float(datapoint[1]))
  zdata.append(float(datapoint[2]))

# time to do linear algebra
# Ax + By + C = z format, nx3 matrix x1, y1, 1
M = [];
b = [];
for i in range(len(xdata)):
    t = [];
    t.append(xdata[i]);
    t.append(ydata[i]);
    t.append(1);
    M.append(t);
    b.append(zdata[i]);

# (MtM)^(-1)*Mt*b = x

M = np.array(M);
b = np.array(b);
xvect = (np.linalg.inv(np.transpose(M)@M))@np.transpose(M)@b

# print(xvect);

xx = np.outer(np.linspace(-40, 40, 40), np.ones(40));
yy = xx.copy().T;
zz = xx * xvect[0] + yy * xvect[1] + xvect[2];

ax.plot_surface(xx, yy, zz, alpha=0.5, color='#0000FF', rstride = 39, cstride = 39);

# Create the 3D plot
ax.scatter3D(xdata,ydata,zdata, c=zdata, cmap = 'Greens')

plt.show()
