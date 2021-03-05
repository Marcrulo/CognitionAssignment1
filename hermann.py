import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_ubyte, img_as_float
from scipy.signal import convolve2d as scipy_conv2d

# Load input image
img = io.imread('hermann.jpg')


# Edge enhancement using the "common" kernels

# Parameters
w = 0.1        # weight
n = 4          # kernel "radius"
k_size = n+n*2
def create_kernel():
    F = np.ones([k_size,k_size])
    F*=-w
    F[n:k_size-n,n:k_size-n] = np.ones([n,n])
    return F

F = create_kernel()

f_out_1 = scipy_conv2d(img,F,mode="same") 
fig,(ax1,ax2) = plt.subplots(ncols=2, figsize=(10,5))
ax1.imshow(img, extent=[0,100,0,1], aspect="auto")
ax2.imshow(f_out_1, extent=[0,100,0,1],aspect="auto")

# Plot
plt.tight_layout()
plt.show()



