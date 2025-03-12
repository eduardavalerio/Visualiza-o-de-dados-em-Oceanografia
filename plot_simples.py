# read aula01 files to plot displacement
#
# these data are at http://www3.io.usp.br:32080/los/IOF0265/aula01/ 
# Para executar: run plot_simples.py
# -------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Lê todas as linhas e transfere para uma array de strings 
with open('teste.dat') as f:
        lines = f.readlines()
N=len(lines)
lon = np.zeros(N)
lat = np.zeros(N)
z = np.zeros(N)
T = np.zeros(N)
for i, line in enumerate(lines):
#        lon[i], lat[i], z[i], T[i] = np.array(line.split()).astype(float)
    values = line.split()  # Split line into parts
    lon[i], lat[i], z[i], T[i] = map(float, values)  # Convert to float
plt.ion()
plt.plot(lon,lat)

# Add title
plt.title("Longitude vs Latitude Plot")
# Add grid
plt.grid(True)
