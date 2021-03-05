import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.signal import convolve2d

# Load input image
img = io.imread('MonaLisa.jpg')



def create_kernel1(n):
    k_size = n+n*2
    F = np.ones([k_size,k_size])
    F*=-0.8
    F[n:k_size-n,n:k_size-n] = np.ones([n,n])*6
    return F

def create_kernel2(n):
    k_size = n+n*2
    F = np.ones([k_size,k_size])
    F*=-0.1
    F[n:k_size-n,n:k_size-n] = np.ones([n,n])
    return F

f_out_1 = convolve2d(img,create_kernel2(5),mode="same") 
f_out_2 = convolve2d(img,create_kernel1(5),mode="same") 




fig,(ax1,ax2,ax3) = plt.subplots(ncols=3, figsize=(12,6))
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
ax1.imshow(img, extent=[0,100,0,1], aspect="auto")
ax1.title.set_text('Original')
ax2.imshow(f_out_1, extent=[0,100,0,1],aspect="auto")
ax2.title.set_text('Normal kernel (n = 5)')
ax3.imshow(f_out_2, extent=[0,100,0,1],aspect="auto")
ax3.title.set_text('Modified kernel (n = 5)')
plt.tight_layout()
plt.show()






