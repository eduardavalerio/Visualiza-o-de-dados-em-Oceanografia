import numpy as np
import matplotlib.pyplot as plt

sta_data = np.loadtxt('sta_data.dat')
z = sta_data[:, 0]    
tem_a = sta_data[:, 1]
sal_a = sta_data[:, 2]
tem_b = sta_data[:, 3]
sal_b = sta_data[:, 4]

plt.ion()
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1) #linha, coluna e n do subplot
plt.plot(tem_a, -z, 'b', label='A')
plt.plot(tem_b, -z, 'm', label='B')
plt.plot(tem_a, -z, '.b')
plt.plot(tem_b, -z, '.m')

plt.ylim([-4000, 0])
plt.legend()
plt.xlabel('Temperatura (ºC)')
plt.ylabel('Profundidade (m)')
plt.title('Temperatura')
plt.grid()

plt.subplot(1, 2, 2) #mexendo no segundo subplot
plt.plot(sal_a, -z, 'b', label='A')
plt.plot(sal_b, -z, 'm', label='B')
plt.plot(sal_a, -z, '.b')
plt.plot(sal_b, -z, '.m')

plt.ylim([-4000, 0])
plt.xlabel('Salinidade')
plt.ylabel('Profundidade (m)')
plt.title('Salinidade')
plt.grid()

plt.savefig('TS02_py.png')

