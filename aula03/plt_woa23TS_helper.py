import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

fileT = "woa23_decav_t00_01.nc"
fileS = "woa23_decav_s00_01.nc"

fT = nc.Dataset(fileT)
fS = nc.Dataset(fileS)
dep = fT.variables['depth'][:]
lat = fT.variables['lat'][:]
lon = fT.variables['long'][:]
tem = fT.variables['t_an'][:].squeeze()
sal = fS.variables['sal'][:].squeeze()

plt.ion()
plt.figure(figsize=(10, 12))

ii = 0

ax = plt.subplot(2, 1, 1)
aim = ax.imshow(tem[ii, :, :], extent=[lon.min(), lon.max(), lat.min(), lat.max()],
           vmin=-2, vmax=30, origin='lower', aspect='auto', cmap=plt.cm.magma)
plt.colorbar(aim, label='(°C)')
ax.contour(lon, lat, sal[ii, :, :], levels=np.arange(30, 40.5, 0.5),
            colors='b', linewidths=1)
ax.set_title('SST with SSS contours')
ax.set_xlabel('longitude')
ax.set_ylabel('latitude')
ax.grid()

bx = plt.subplot(2, 1, 2)
bim = bx.imshow(sal[ii, :, :], extent=[lon.min(), lon.max(), lat.min(), lat.max()],
           vmin=32, vmax=38, origin='lower', aspect='auto', cmap=plt.cm.viridis)
plt.colorbar(bim)
bx.contour(lon, lat, tem[ii, :, :], levels=np.arange(0, 36, 2),
            colors='r', linewidths=1)
bx.set_title('SSS with SST contours')
bx.set_xlabel('longitude')
bx.set_ylabel('latitude')
bx.grid()

plt.savefig('game03_fig03py.png')

fT.close()
fS.close()
