import pandas as pd
df = pd.read_csv('wild_boars.csv')
print(df['tusk_length_cm'])
print(df['tusk_length_cm'].min())
print(df['tusk_length_cm'].max())
