import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

mat = sio.loadmat('albeck_gene_expression.mat')
print('mat file type: {}'.format(type(mat)))
print('\ndict keys:\n{}'.format(mat.keys()))
print('\nCYratioCyt type:{}'.format(np.shape(mat['CYratioCyt'])))

data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
