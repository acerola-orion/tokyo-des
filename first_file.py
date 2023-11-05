import matplotlib.pyplot as plt
import numpy as nump

x = nump.linspace(0, 2 * nump.pi, 100)
y = nump.log(x) + nump.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('log(x) + cos(x)')
plt.title('Function graph log(x) + cos(x)')
plt.grid(True)
plt.show()