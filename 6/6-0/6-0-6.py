import pandas as pd
df = pd.read_csv('wild_boars.csv')
with open('iqr_by_gender.txt', 'w') as f:
    for gender in ['Male', 'Female']:
        subset = df[df['gender'] == gender]['length_cm']
        q1 = subset.quantile(0.25)
        q3 = subset.quantile(0.75)
        iqr = q3 - q1
        f.write(f"{gender}: {iqr:.2f} cm\n")
