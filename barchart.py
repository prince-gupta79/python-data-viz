import matplotlib.pyplot as plt
import numpy as np


categories = np.array(["Grains", "Protien", "Meat", "Vegetables", "carbs", "Dairy"])
values = np.array([4, 15, 7, 22, 11, 18])

plt.bar(categories, values, color="blue")

# For horizontal barchart write (barh)
# plt.barh(categories, values, color="cyan")



plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
