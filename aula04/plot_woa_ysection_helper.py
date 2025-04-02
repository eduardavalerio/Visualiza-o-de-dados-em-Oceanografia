#! /home/polito/miniconda3/envs/py39/bin/python
# -*- coding: utf-8 -*-
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

# Caminho para os dados do WOA23 (World Ocean Atlas 2023)
d = '/home/alunos/eduarda/aula04/'

# Nomes dos arquivos de temperatura e salinidade
fnamT = d + r'woa23_decav_t00_01.nc'  # Arquivo de temperatura
fnamS = d + r'woa23_decav_s00_01.nc'  # Arquivo de salinidade

# Exemplo de formatação personalizada para longitude
def laf(y, pos):
    """Os dois argumentos são o valor e a posição do tick."""
    if y < 0:
        s = '°S'  # Sul, porque o mundo é redondo e tem dois lados
    elif y > 0:
        s = '°N'  # Norte, onde os ursos polares moram
    else:
        s = '°'  # No meio do caminho tinha uma pedra...
    y = np.abs(y)
    return f'{y:.0f}{s}'

# Lendo os arquivos netCDF, apenas a parte útil
f = nc.Dataset(fnamT)  # Abrindo o arquivo de temperatura
g = nc.Dataset(fnamS)  # Abrindo o arquivo de salinidade

# [print(v) for v in f.variables.keys()]  # Isso aqui era só para debug, mas vamos deixar quieto

# Extraindo as variáveis de longitude, latitude e profundidade
x = f['lon'][:]  # Longitude
y = f['lat'][:]  # Latitude
z = -1 * f['depth'][:]  # Profundidade (negativa porque o mar é fundo, né?)

# np.where retorna os índices onde a condição é verdadeira
i = np.where(x==-30.5)[0][0]  # Encontrando o índice para -30.5° de longitude Atlantico
j = np.where(x==-179.5)[0][0]  # Encontrando o índice para -179.5° de longitude Pacifico

# Extraindo os dados de temperatura e salinidade para as longitudes específicas
Ti = f['t_an'][0,:,:,i].squeeze()  # Temperatura em -30.5°
Tj = f['t_an'][0,:,:,j].squeeze()  # Temperatura em -179.5°
Si = g['s_an'][0,:,:,i].squeeze()  # Salinidade em -30.5°
Sj = g['s_an'][0,:,:,j].squeeze()  # Salinidade em -179.5°

# Daqui para frente é só fazer a figura (ou seja, a parte divertida!)
plt.ion()  # Ativando o modo interativo do matplotlib (para não ficar esperando)

# Criando 4 eixos para as figuras
fig, ax = plt.subplots(2, 2, num=1, figsize=(12, 6), clear=True)
ax = ax.ravel()  # Transformando a matriz de eixos em uma lista (para facilitar a vida)

# Agora ax é uma lista de eixos com 4 elementos: ax[0] até ax[3] (como uma playlist de 4 músicas)

# Definindo algumas variáveis para facilitar a vida
lat = [-30.5, -179.5]  # Latitudes de interesse
cmapt = plt.cm.magma  # Colormap para temperatura
cmaps = plt.cm.viridis  # Colormap para salinidade
vmint, vmaxt = [-1, 30]  # Valores mínimos e máximos para temperatura
vmins, vmaxs = [34, 36]  # Valores mínimos e máximos para salinidade
labelt = 'Temp. (°C)'  # Label para temperatura
labels = 'Sal. (ppm)'  # Label para salinidade

# Plotando os dados de temperatura e salinidade
hti = ax[0].pcolormesh(y, z, Ti, vmin=vmint, vmax=vmaxt, cmap=cmapt)  # Temperatura em -0.5°
plt.colorbar(hti, ax=ax[0], label=labelt)  # Barra de cores para temperatura
htj = ax[2].pcolormesh(y, z, Tj, vmin=vmint, vmax=vmaxt, cmap=cmapt)  
plt.colorbar(htj, ax=ax[2], label=labelt)  # Barra de cores para temperatura
hsi = ax[1].pcolormesh(y, z, Si, vmin=vmins, vmax=vmaxs, cmap=cmaps)  # Salinidade em -0.5°
plt.colorbar(hsi, ax=ax[1], label=labels)  # Barra de cores para salinidade
#ax[2].clear() limpa a imagem
hsj = ax[3].pcolormesh(y, z, Sj, vmin=vmins, vmax=vmaxs, cmap=cmaps)  # Salinidade em -30.5°
plt.colorbar(hsj, ax=ax[3], label=labels)  # Barra de cores para salinidade

# Definindo os títulos dos gráficos (para não ficar perdido)
ax[0].set_title(f'T at {np.abs(lat[0])}°W no Atlântico')  # Temperatura no Atlântico
ax[1].set_title(f'S at {np.abs(lat[0])}°W no Atlântico')  # Temperatura no Pacífico
ax[2].set_title(f'T at {np.abs(lat[1])}°W no Pacífico')  # Salinidade no Atlântico
ax[3].set_title(f'S at {np.abs(lat[1])}°W no Pacífico')  # Salinidade no Pacífico

# Ajustando os eixos (para ficar bonitinho)
for i in range(4):
    ax[i].set_facecolor('#998877')  # Cor de fundo (um marrom meio "vintage")
    ax[i].xaxis.set_major_formatter(laf)  # Formatando os labels de latitude
    ax[i].set_ylabel('z(m)')  # Label para a profundidade
    ax[i].grid(linewidth=0.5, linestyle=':')  # Grid (para não ficar perdido no mar)

# Ajustando o layout (para não ficar tudo amontoado)
plt.tight_layout()

# Salvando a figura (se quiser, mas pode deixar para depois)
# plt.savefig('game04_fig02py.png', dpi=150)
