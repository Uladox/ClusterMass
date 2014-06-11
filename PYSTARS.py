#This file is part of ClusterMass
#
#	Copyright 2014 Uladox
#
#    ClusterMass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    ClusterMass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ClusterMass.  If not, see <http://www.gnu.org/licenses/>.

from scipy.optimize import curve_fit
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))
p0 = [1., 0., 1.]

filename = raw_input("Enter File Name: ")
inputfile = open(filename)
line = inputfile.readlines()
linenum = 0
largestnum = 0
smallestnum = 0
velocityarray = []

for indivline in line:
	linepart = line[linenum]
	linepart = indivline.strip()
	toint = int((float(linepart)))
	velocityarray = velocityarray + [toint]
	if linenum == 0:
		smallestnum = toint
	elif toint < smallestnum:
		smallestnum = toint

	if toint > largestnum:
		largestnum = toint

	linenum = linenum + 1

histo1,histo2  = np.histogram(velocityarray, density=False)
bin_centres = (histo2[:-1] + histo2[1:])/2
print(histo1)
	
#plt.hist(velocityarray, 20, normed=50, facecolor='g', alpha=0.75)
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Velocities')
#print(smallestnum)
#print(largestnum)
#                                                       	xmin xmax ymin ymax
#plt.axis([smallestnum - 100, largestnum + 100, 0, 0.0012])
#plt.show()
#print(linenum)
#print("largestnum: ") 
#print(largestnum) 
#print(" smallestnum: ")
#print(smallestnum)
