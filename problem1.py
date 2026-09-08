import pandas as pd


df = pd.read_csv(f"credit_risk_dataset.csv")


df_limpio = df.dropna()

print("Filas antes:", len(df))
print("Filas después:", len(df_limpio))
print("Filas eliminadas:", len(df) - len(df_limpio))



print(df_limpio[['person_age', 'person_emp_length', 'person_income']].describe())
