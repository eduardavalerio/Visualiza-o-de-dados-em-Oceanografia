import numpy as np #importa pacote numpy
import matplotlib.pyplot as plt #importa pacote matplotlib

# Load data from sta_data.dat
sta_data = np.loadtxt('sta_data.dat') #carrega os dados em uma variavel 'sta_data'

# Assign variables
z = sta_data[:, 0]  #profundidade # Python indexing starts at 0
tem_a = sta_data[:, 1] #associa a uma variavel os dados de temperatura que estao presentes na coluna 1
sal_a = sta_data[:, 2]
tem_b = sta_data[:, 3]
sal_b = sta_data[:, 4]

plt.ion() #ver as figuras enquanto esta fazendo 

# Plot 1: Temperature vs Depth
plt.figure(4) #gera a figura
plt.plot(tem_b, -z, 'm', label='Temperature')
plt.scatter(tem_b, -z, color='m')
plt.xlabel('Temperature (°C)')
plt.ylabel('Depth (m)')
plt.title('Temperature')
plt.grid(True)
plt.savefig('Fig1_TB.png', dpi = 300)

# Plot 2: Salinity vs Depth
plt.figure(5)
plt.plot(sal_b, -z, 'm', label='Salinity')
plt.scatter(sal_b, -z, color='m')
plt.xlabel('Salinity')
plt.ylabel('Depth (m)')
plt.title('Salinity')
plt.grid(True)
plt.savefig('Fig2_Sal_b.png', dpi = 300)

# Plot 3: Temperature vs Salinity
plt.figure(6)
plt.plot(sal_b, tem_b, 'm-.', label='T-S Diagram')
plt.scatter(sal_b, tem_b, color='m')
plt.xlabel('Salinity')
plt.ylabel('Temperature (°C)')
plt.title('Station B')
plt.grid(True)
plt.savefig('Fig3_TS_b.png', dpi = 300)

