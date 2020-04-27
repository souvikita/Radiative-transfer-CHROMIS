import numpy as np 
import astropy 
import matplotlib.pyplot as plt 
from helita.sim import rh15d 
import sunpy
from astropy.io import fits 
#import sunpy.visualization.colormaps as cm
import sunpy.cm as cm
import cv2

sdoaia171 = plt.get_cmap('yohkohsxtal') 
data1 = rh15d.Rh15dout('/mn/stornext/d9/souvikb/Big_Ca_run/output_new/') #Reading Output
wave = data1.ray.wavelength # reads the entire frequency spectrum for the active atom
indices = np.arange(len(wave))[(wave > 391) & (wave < 399)]
 
I_sp = data1.ray.intensity # Specific intensity from the Radiative transfer equation
I_avg = np.mean(I_sp[:,:,indices[495:505]],axis=2)
#equ = cv2.equalizeHist(I_avg)
plt.figure(figsize=(10,10))
plt.imshow(I_avg,origin='lower',cmap=sdoaia171,vmax=2.8e-8) #Mean symmetrically about 395 nm which corresponds to an index of 500
#plt.colorbar()
#plt.figure(figsize=(10,10))
plt.xlabel('pixels')
plt.ylabel('pixels')
plt.title('Synthetic image from a Bifrost Simulation')
plt.axis('off')
plt.savefig('/mn/stornext/u3/souvikb/DKIST_comp.png',dpi=600)
plt.show()
 
