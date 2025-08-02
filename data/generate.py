import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

n_rows = 10000

ages = np.random.randint(18, 66, size=n_rows)  # Ages 18 to 65
incomes = np.random.randint(20000, 200001, size=n_rows)  # Income $20,000 to $200,000
genders = np.random.choice(['Male', 'Female', 'Non-binary', None], size=n_rows, p=[0.45, 0.45, 0.08, 0.02])
regions = np.random.choice(['North', 'South', 'East', 'West'], size=n_rows)

# Randomly insert missing values in income (about 5%)
mask = np.random.rand(n_rows) < 0.05
incomes = incomes.astype(float)
incomes[mask] = np.nan

df = pd.DataFrame({
    'age': ages,
    'income': incomes,
    'gender': genders,
    'region': regions
})

df.to_csv('large_random_dataset.csv', index=False)
