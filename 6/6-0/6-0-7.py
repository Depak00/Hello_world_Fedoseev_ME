import pandas as pd
df = pd.read_csv('wild_boars.csv')
with open('variance_std_cv.txt', 'w') as f:
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            mean_val = df[col].mean()
            std_val = df[col].std()
            var_val = df[col].var()
            cv_val = (std_val / mean_val) * 100 if mean_val != 0 else 0
            f.write(f"{col}:\n")
            f.write(f"  variance: {var_val:.2f}\n")
            f.write(f"  standard deviation: {std_val:.2f}\n")
            f.write(f"  coefficient of variation: {cv_val:.2f}%\n\n")
