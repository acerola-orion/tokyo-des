import matplotlib.pyplot as plt
import numpy as nump

x = nump.linspace(0, 2 * nump.pi, 100)
y = nump.sin(x) * nump.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x) * cos(x)')
plt.title('Function graph sin(x) * cos(x)')
plt.grid(True)
plt.show()