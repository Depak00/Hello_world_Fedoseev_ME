import pandas as pd
df = pd.read_csv('wild_boars.csv')
mode_values = df.mode().iloc[0]  # берем первую моду (если их несколько)
with open('mode_values.txt', 'w') as f:
    for col, val in mode_values.items():
        f.write(f"{col}: {val}\n")
