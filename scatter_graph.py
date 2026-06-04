# Scatter graph = shows the relationship between two varibles
#                 Helps to identify a correlation (+,-,None)
#                 Eg; Study hrs vs Test score

import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 3, 4, 6, 2, 8, 5, 8]) # Hours studies
y1= np.array([30, 45, 50, 55, 60, 65, 70, 84, 93]) # Grade

x2 = np.array([1, 3, 4, 5, 2, 7, 9, 8, 0]) # Hours studies
y2 = np.array([30, 66, 45, 30, 55, 69, 69, 47, 90]) # Grade

plt.scatter(x1, y1, color="red",
                    alpha = 0.7,
                    s = 195,
                    label="class A")

plt.scatter(x2, y2, color="pink",
                    alpha = 0.8,
                    s = 195,
                    label="class B" )

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()

plt.show()