import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\asus\Desktop\matplotlib_pro\tested.csv")

type_count = df["Name"].value_counts()

plt.barh(type_count.index, type_count.values)

plt.show()