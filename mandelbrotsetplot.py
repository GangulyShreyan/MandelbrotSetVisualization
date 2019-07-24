import numpy as np
import matplotlib.pyplot as plt

n=800
niter=150
pow=2


x0=-2
x1=1
y0=-1
y1=1

x,y=np.meshgrid(np.linspace(x0,x1,n),np.linspace(y0,y1,n))

c=x + 1j*y
z=np.zeros((n,n))
k=np.zeros((n,n))

for i in range(1,niter):
    z=z**pow+c
    k[np.logical_and(abs(z)>2,k==0)]=niter-i

    
plt.imshow(k,cmap='YlGn')
plt.show()

