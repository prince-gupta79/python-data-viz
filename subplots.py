import matplotlib.pyplot as plt
import numpy as np

# Figure = The entire canvas
# Ax = A single plot (subplot)

x = np.array([1, 2, 3, 4, 5])

figure, axes = plt.subplots(2,2)

axes[0,0].plot(x, x*2, color="purple")
axes[0,0].set_title("1st wala")

axes[0,1].plot(x, x**2, color="pink")
axes[0,1].set_title("2nd wala")

axes[1,0].plot(x, x**3, color="cyan")
axes[1,0].set_title("3rd wala")

axes[1,1].plot(x, x**4, color="blue")
axes[1,1].set_title("4th wala")

plt.tight_layout()

plt.show()
