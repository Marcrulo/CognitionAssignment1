import numpy as np
import matplotlib.pyplot as plt

w = 0.1
N = 16 #18 ???
I = [0,0,0,0,1,2,3,4,5,6,7,8,9,9,9,9]
#I = [0,0,1,2,3,4,5,6,7,8,9,9]
A = []
for i in range(1,N-1):
    I[i]*=1.0
    v = I[i]-w*(I[i-1]+I[i+1])
    A.append(v)

print(I[1:-1])
print(A)

image1 = np.ones([N-2,N-2])*I[1:-1]
image2 = np.ones([N-2,N-2])*A*0.5

fig,(ax1,ax2) = plt.subplots(nrows=2, figsize=(10,10))
ax1.imshow(image1-0.1, extent=[0,16,0,1], aspect="auto")
ax2.imshow(image2-0.1, extent=[0,16,0,1], aspect="auto")
ax1.title.set_text('Original')
ax2.title.set_text('With Lateral Inhibition')

plt.show()