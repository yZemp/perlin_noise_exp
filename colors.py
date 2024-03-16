import matplotlib.pyplot as plt
import random
import randgen

def rplot():
    r = hex(int(random.random() * 255))[2:].ljust(2, '0')
    g = hex(int(random.random() * 255))[2:].ljust(2, '0')
    b = hex(int(random.random() * 255))[2:].ljust(2, '0')
    plt.scatter(randgen.rand_TCL_ms(0, 1), randgen.rand_TCL_ms(0, 1), c = f"#{r}{g}{b}", s = random.random() * 200)

for i in range(1_000):
    rplot()

plt.show()