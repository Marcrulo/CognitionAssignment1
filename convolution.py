import numpy as np



# 1) Lateral inhibition
Fin = [1,1,1,1,1,0,0,0,0,0]
w = [-0.1, 1, -0.1]

Fout = np.convolve(Fin, w,mode='valid')
print(Fout)



# 2) Optical illusion
Fin = [0,0,0,0,1,2,3,4,5,6,7,8,9,9,9,9]
w = [-0.1, 1, -0.1]

Fout = np.convolve(Fin, w,mode='valid')
print(Fout)
