import matplotlib.pyplot as plt
import numpy as np
n=np.arange(-5,10,1);
def impulse(a):
	d_n=[]
	for i in n:
		if i==0:
			d_n.append(1)
		else:
			d_n.append(0)	
	return d_n

def step(a):
	u_n=[]
	for i in n:
		if i>=a:
			u_n.append(1)
		else:
			u_n.append(0)	
	return u_n

def ramp(a):
	r_n=[]
	for i in n:
		if i>a:
			r_n.append(i)
		else:
			r_n.append(0)	
	return r_n

d=impulse(0)
u=step(0)
r=ramp(0)
plt.subplot(3,1,1)
plt.stem(n,d)

plt.subplot(3,1,2)
plt.stem(n,u)
plt.subplot(3,1,3)
plt.stem(n,r)
plt.show()



