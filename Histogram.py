# Histogram = A visual represntaion of the distribution of quantitative data.
#             They group values into bins(Intervals)
#             and counts how many fall in each range.

import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)


plt.hist(scores, bins=10,
         color="purple",
         edgecolor="black")


plt.title("Exam Score")
plt.xlabel("Score")
plt.ylabel("No. of Students")

plt.show()