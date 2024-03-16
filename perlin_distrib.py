import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import randgen
from my_stats import sturges

noise = PerlinNoise(octaves = 4)

arrx = np.linspace(0, 100, 100_000)
arrnoise = [noise(x) for x in arrx]

plt.hist(arrnoise, sturges(arrnoise))
plt.show()
plt.plot(arrx, arrnoise)
plt.show()