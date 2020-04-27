import numpy as np
import astropy
import matplotlib.pyplot as plt
from helita.sim import rh15d
from astropy.io import fits
######For the ca lines ###########################
data_ca_8542 = rh15d.Rh15dout('/mn/stornext/u3/souvikb/rh/rh15d_mpi/run_example/output_ca_8542/output/')

wave_ca = data_ca_8542.ray.wavelength

indices1 = np.arange(len(wave_ca))[(wave_ca >854.015 ) & (wave_ca < 854.4)]

tau_one_ca = data_ca_8542.ray.tau_one_height[:,:,indices1]

ca_profiles = data_ca_8542.ray.intensity[:,:,indices1]
########For the magnesium lines########################

data2 = rh15d.Rh15dout('/mn/stornext/u3/souvikb/rh/rh15d_mpi/run_example/output/')

wave_mg = data2.ray.wavelength

indices_Mg = np.arange(len(wave_mg))[(wave_mg >279.4 ) & (wave_mg < 280.5)]

tau_one_mg = data2.ray.tau_one_height[:,:,indices_Mg]

mg_profiles = data2.ray.intensity[:,:,indices_Mg]

# fig, (ax1,ax2) =plt.subplots(2,2,squeeze=True)
#
# ax1.plot(wave_ca[indices1],tau_one_ca[10,10,:]/1e6,'r')
# ax1.set_ylim([0,2])
# ax2.plot(wave_mg[indices_Mg],tau_one_mg[10,10,:]/1e6,'b')
# ax2.set_ylim([0,2])

ax1 =plt.subplot(221)
plt.plot(wave_ca[indices1],ca_profiles[4,16,:])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.ylabel('I [$W m^{-2} Hz^{-1} Sr^{-1}$]')
plt.title('Ca profile')

ax2 = plt.subplot(223)
plt.plot(wave_ca[indices1], tau_one_ca[4,16,:]/1e6,'r')
plt.xlabel('nm')
plt.ylabel('\tau=1 H[Mm]')
ax2.set_ylim([0,2])

ax3 = plt.subplot(222)
plt.plot(wave_mg[indices_Mg],mg_profiles[4,16,:])
plt.setp(ax3.get_xticklabels(), visible=False)
plt.title('Mg profile')

ax4 =plt.subplot(224)
plt.plot(wave_mg[indices_Mg],tau_one_mg[4,16,:]/1e6,'r')
ax4.set_ylim([0,2])
plt.xlabel('nm')
plt.show()
