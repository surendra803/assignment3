# To perform Discrite Time Fourier Trasform 

import matplotlib.pyplot as plt
import numpy as np

w=np.arange(-np.pi,np.pi,0.01*np.pi);

y=[]
x=[]
length=int(input("Enter the Length of the Sequence"))
for a in range(length):
		x.append(int(input("Enter the sequence")))

for i in w:
	sum1=0
	for n in range (0,len(x)):
		sum1=sum1+x[n]*np.exp(-1j*i*n)
	y.append(sum1)
plt.subplot(211);
plt.stem(w,np.abs(y))
plt.subplot(212)
plt.stem(w,np.angle(y));
plt.show()
