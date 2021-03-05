import numpy as np
import matplotlib.pyplot as plt

w = 0.1
t = 0.8
I = [1,1,1,0.7,0.5,0,0,0,0,0]
N = len(I)
A = []
for i in range(1,N-1):
    v = I[i]-w*(I[i-1]+I[i+1])
    if v > t:
        print("EDGE!")
    A.append(v)

print(A)

image1 = np.ones([N-2,N-2])*I[1:-1]
image2 = np.ones([N-2,N-2])*A

fig,(ax1,ax2) = plt.subplots(nrows=2, figsize=(10,10))
ax1.imshow(image1, extent=[0,8,0,1], aspect="auto")
ax2.imshow(image2, extent=[0,8,0,1], aspect="auto")
ax1.title.set_text('Original')
ax2.title.set_text('With Lateral Inhibition')


plt.show()