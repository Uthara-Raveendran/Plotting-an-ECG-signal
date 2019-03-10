from __future__ import division
import matplotlib.pyplot as plt
xaxis=[]
yaxis=[]
myfile = open("ecg.txt", "r")
for k in range(1,15000,1):
	print k
	y=k/100000
	s = myfile.readline()
	s = s.replace("\n", "")
	#print (s,y)
	xaxis.append(s)
	yaxis.append(y)
plt.plot(yaxis, xaxis)
plt.show()
