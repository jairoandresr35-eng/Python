import pandas as pd

df = pd.read_csv(r"C:\Users\Andres Rojas\OneDrive\Escritorio\notas_7A.csv", delimiter=";", encoding="latin-1")

# ── Revisión inicial ──────────────────────────────────────
print(df.shape)
print(df.columns)

# ── Supon que la columna del nombre es "Nombre" y las notas son numéricas ──
# Ajusta "Nombre" al nombre real de tu columna de estudiantes
col_nombre = "Nombre"  # cambia si es diferente

columnas_notas = df.select_dtypes(include="number").columns
print(f"\nColumnas de notas detectadas: {list(columnas_notas)}")

# ── Promedio por estudiante ───────────────────────────────
df["Promedio"] = df[columnas_notas].mean(axis=1).round(2)

# ── Estado: aprobó o reprobó ──────────────────────────────
df["Estado"] = df["Promedio"].apply(lambda x: "Aprobó" if x >= 3.0 else "Reprobó")

# ── Resultados ────────────────────────────────────────────
print("\n── Tabla de resultados ──")
print(df[[col_nombre, "Promedio", "Estado"]].to_string(index=False))

print("\n── Estadísticas generales ──")
print(f"Promedio del grupo:  {df['Promedio'].mean():.2f}")
print(f"Nota más alta:       {df['Promedio'].max():.2f}")
print(f"Nota más baja:       {df['Promedio'].min():.2f}")
print(f"Estudiantes que aprobaron:  {(df['Estado'] == 'Aprobó').sum()}")
print(f"Estudiantes que reprobaron: {(df['Estado'] == 'Reprobó').sum()}")

# ── Reprobados con nota de recuperación necesaria ─────────
reprobados = df[df["Estado"] == "Reprobó"][[col_nombre, "Promedio"]].copy()
reprobados["Recuperación necesaria"] = ((3.0 * (len(columnas_notas) + 1)) - (reprobados["Promedio"] * len(columnas_notas))).round(2)

print("\n── Estudiantes en recuperación ──")
print(reprobados.to_string(index=False))