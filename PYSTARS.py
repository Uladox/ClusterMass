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
