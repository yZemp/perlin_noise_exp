import numpy as np
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import randgen
from my_stats import sturges

noise = PerlinNoise(octaves = 1)

xpix = 500
ypix = 500
mat = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

plt.imshow(mat, cmap = "grey")
plt.show()