import pandas as pd
df = pd.read_csv('wild_boars.csv')
median_values = df.median(numeric_only=True)
with open('median_values.txt', 'w') as f:
    for col, val in median_values.items():
        f.write(f"{col}: {val:.2f}\n")
