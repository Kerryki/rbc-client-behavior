import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


tips = pd.read_csv("tips.csv")
sns.displot(tips["total_bill"], kde=False)
plt.show()
