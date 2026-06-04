import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshmen", "sophomores", "Juniors", "seniors"]
values = np.array([300, 200, 275, 290])
colors = ["red", "yellow", "green", "blue"]
plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0.1,0,0.1],
                shadow=True,
                )


plt.show()
