import pandas as pd
df = pd.read_csv('wild_boars.csv')
with open('cv_tusk_by_gender.txt', 'w') as f:
    for gender in ['Male', 'Female']:
        subset = df[df['gender'] == gender]['tusk_length_cm']
        mean_val = subset.mean()
        std_val = subset.std()
        cv_val = (std_val / mean_val) * 100 if mean_val != 0 else 0
        f.write(f"{gender}: {cv_val:.2f}%\n")
