import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([16, 20, 30, 40])
y2 = np.array([20, 40, 50, 60])
y3 = np.array([10, 30, 77, 90])

plt.title("Class Size", fontsize=29,
                        family="Arial" ,
                        fontweight="bold",
                         color="purple" ) 

plt.xlabel("Year", fontsize=23,
                    family="Arial",
                    fontweight="bold",
                    color="blue")

plt.ylabel("Students", fontsize=22,
                        family="Arial",
                        fontweight="bold",
                        color="black")

plt.tick_params(axis="both",
                 color="pink")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()