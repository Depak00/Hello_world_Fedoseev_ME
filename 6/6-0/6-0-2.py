import pandas as pd
df = pd.read_csv('wild_boars.csv')
mean_values = df.mean(numeric_only=True)
with open('mean_values.txt', 'w', encoding='utf-8') as f:
    for column, value in mean_values.items():
        f.write(f"{column}: {value:.2f}\n")
print(mean_values)
