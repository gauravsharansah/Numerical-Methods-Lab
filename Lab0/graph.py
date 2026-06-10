import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,20,500)
y=x**2 - 5*x + 6
plt.plot(x,y)
plt.show()
plt.grid()