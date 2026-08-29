import pandas as pd


df = pd.read_csv(f"credit_risk_dataset.csv")


print(df.shape)

print(df.info())

print(df.head())

