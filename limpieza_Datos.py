import pandas as pd


df = pd.read_csv(f"credit_risk_dataset.csv")

# df[...] : devuelve solo las filas donde el valor es TRUE. Es un filtro


df_limpio = df.dropna()


print("Filas antes:", len(df))
print("Filas después:", len(df_limpio))
print("Filas eliminadas:", len(df) - len(df_limpio))

print(df_limpio[['person_age', 'person_emp_length', 'person_income']].describe())



# Filtro 1: eliminar las edades imposibles (> 100 años)

df_limpio = df_limpio[df_limpio['person_age'] <= 100]

# Filtro 2: la antiguedad laboral no puede superar (edad - 18)
df_limpio = df_limpio[df_limpio['person_emp_length'] <= df_limpio['person_age'] - 18]

print("Filas finales:" , len(df_limpio))
print(df_limpio[['person_age', 'person_emp_length', 'person_income']].describe())


    |   