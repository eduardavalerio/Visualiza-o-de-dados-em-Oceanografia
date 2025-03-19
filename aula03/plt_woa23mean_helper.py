import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

filename = "woa23_decav_t00_01.nc"
dataset = nc.Dataset(filename)
dep = dataset.variables['depth'][:]
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]
tem = dataset.variables['t_an'][:].squeeze()
#tem = np.transpose(tem, (1, 0, 2))

ii = 0 # superfície (indice da matriz)

plt.ion()
plt.figure()
plt.imshow(tem[ii, :, :], extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-2, vmax=30, origin='lower', aspect='auto', cmap=plt.cm.jet)
plt.colorbar(label='(°C)')
plt.contour(lon, lat, tem[ii, :, :], levels=np.arange(-2, 31, 2), colors='k', linewidths=0.5)
plt.title('Média Anual da TSM')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.grid()
plt.savefig('game03_fig_sup.png')
plt.show()
dataset.close()
