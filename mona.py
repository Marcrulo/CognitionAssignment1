import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.signal import convolve2d

# Load input image
img = io.imread('MonaLisa.jpg')

# Parameters
w = 0.1         # weight
n = 15          # kernel "radius"
t = 250


def create_kernel():
    k_size = n+n*2
    F = np.ones([k_size,k_size])
    F*=-w
    F[n:k_size-n,n:k_size-n] = np.ones([n,n])
    return F

F = create_kernel()
f_out_1 = convolve2d(img,F,mode="same") 

fig,(ax1,ax2,ax3) = plt.subplots(ncols=3, figsize=(12,6))
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
ax1.imshow(img, extent=[0,100,0,1], aspect="auto")
ax1.title.set_text('Original')
ax2.imshow(f_out_1>t, extent=[0,100,0,1],aspect="auto")
ax2.title.set_text('Edge detect')


# Edge enhancement using sobel kernels
sobel_kernel_v = np.array([[1,0,-1],
						   [2,0,-2],
						   [1,0,-1]])

sobel_kernel_h = np.array([[-1,-2,-1],
						   [0,0,0],
						   [1,2,1]])
G_v = convolve2d(img,sobel_kernel_v)
G_h = convolve2d(img,sobel_kernel_h)
G   = np.sqrt((G_v**2 + G_h**2))

ax3.imshow(G, extent=[0,100,0,1],aspect="auto")
ax3.title.set_text('Edge detect (Sobel Filter)')




# Plot
plt.tight_layout()
plt.show()






