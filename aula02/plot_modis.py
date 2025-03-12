import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

filename = 'AQUA_MODIS.20250101_20250131.L3m.MO.CHL.NRT.x_chlor_a.nc'
f = nc.Dataset(filename)
lon = f.variables['lon'][:]
lat = f.variables['lat'][:]
chl = f.variables['chlor_a'][:]

plt.ion()
plt.figure(figsize=(10, 6))
plt.pcolormesh(lon, lat, np.log10(chl), shading='gouraud')
cbar = plt.colorbar()
plt.clim(-1.5, 1.5)
cbar.set_label('log$_{10}$(mg/m$^3$)', rotation=270, labelpad=20)
plt.title('Clorofila')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.set_cmap('jet')
plt.savefig('plot_modis_py.png')
f.close()
