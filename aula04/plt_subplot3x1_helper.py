# -*- coding: utf-8 -*-
"""
Este é um primeiro programa em python, evidentemente pode ser melhorado, pode
fazer isso depois que funcionar corretamente. Fucionalidade primeiro, depois
um pouco de elegância.
"""
# Esta é uma biblioteca de funções para fazer cálculos (tem outras)
import numpy as np
# Esta é para fazer gráficos
import matplotlib.pyplot as plt
# Esta é para ler arquivos NetCDF, mas só quero a função Dataset
from netCDF4 import Dataset

dname = '/data0/WOA23/'
fname_a = 'woa23_decav_t00_01.nc'
fname_v = 'woa23_decav_t13_01.nc'
dfa = dname+fname_a
dfv = dname+fname_v

# Acessa os arquivos netcdf e lê as temperturas na superfície (índice z=0)
fm = Dataset(dfa)
# fm.variables.keys() te mostra o nome das variáveis
lon = fm['lon'][:]
lat = fm['Lat'][:]
# 1º tempo, 1ª profundidade, todas as lats e lons
# o .squeeze() é para "espremer" as dimensões unitárias
Tm = fm['t_an'][0, 0, :, :].squeeze()

fv = Dataset(dfv)
# lat e lon são as mesmas, nem precisa ler
Tv = fv['t_an'][0, 0, :].squeeze()

anoma = Tv-Tv

# isso é só para não precisar dar plt.show() toda vez que plotar algo 
plt.ion()

# este comando subplots cria a figura (fig) número 1, de 6x11 polegadas,
# com 3 eixos (ax, bx, cx).
# clear é para limpar e plotar na figura 1 mesmo
fig, [ax, bx, cx] = plt.subplots(3, 1, num=1, figsize=(6, 11), clear=True)

mp = ax.pcolormesh(lon, lat, Tm, cmap=plt.cm.jet)
ax.set_title('Temperatura Média Anual')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid(linestyle=':')
plt.colorbar(mp, ax=ax, label='°C')

np = bx.pcolormesh(lon, lat, Tv, cmap=plt.cm.jet)
bx.set_title('Temperatura Média de Verão Austral')
bx.set_xlabel('Longitude')
bx.set_ylabel('Latitude')
bx.grid(linestyle=':')
plt.colorbar(np, ax=bx, label='°C')

op = cx.pcolormesh(lon, lat, anoma, cmap=plt.cm.seismic, vmin=-5, vmax=5)
cx.set_title('Anomalia de Temperatura do Verão Austral')
cx.set_xlabel('Longitude')
cx.set_ylabel('Latitude')
cx.grid(linestyle=':')
plt.colorbar(op, ax=cx, label='°C')

#  tight_layout deixa menos espaço em branco automagicamente
plt.tight_layout()
#
# plt.savefig('game04_fig01py.png', dpi=300, bbox_inches="tight") #mesma coisa que o tight_layout o bbox
