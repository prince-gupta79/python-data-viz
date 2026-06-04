import matplotlib.pyplot as plt

import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([16, 44, 93 ,45])
y3 = np.array([23, 30, 50, 40])

line_style = dict( marker= ".",
                   markersize=20,
                   markerfacecolor="#1cd3fc" ,
                    markeredgecolor="red",
                     linestyle="dashdot"
                   )

plt.plot(x,y1, **line_style)
plt.plot(x,y2, **line_style)
plt.plot(x,y3, **line_style)

plt.show()