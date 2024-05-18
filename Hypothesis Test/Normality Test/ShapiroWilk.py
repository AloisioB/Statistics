import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Reading the file.
df = pd.read_csv("salaries.csv", delimiter=";")

w2024 = df.loc[lambda f: f["work_year"] == 2024, "salary_in_usd"]

# Plotting the 2024 salaries distribution.
w2024.hist(bins=100)
plt.show()

# Sampling 1000 salaries.
np.random.seed(55)
w2024_sample = np.random.choice(w2024, 1000)

# Shapiro Wilk Test
W, p_value = stats.shapiro(w2024_sample)

alpha = 0.05

if p_value < alpha:
    print(f"The data is not normally distributed. p-value = {p_value:.2e}")
else:
    print(f"The data is normally distributed. p-value = {p_value:.2e}")




