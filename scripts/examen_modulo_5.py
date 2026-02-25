import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Carga Segura
try:
    df = pd.read_csv('dataset_universitarios.csv')
    print("✅ Dataset cargado. Columnas detectadas:", df.columns.tolist())
except FileNotFoundError:
    print("❌ Error: Asegúrate de que 'dataset_universitarios.csv' esté en la misma carpeta.")
    exit()

# 2. Limpieza de Datos (Corrección de Outliers)
# Aplicamos el filtro IQR solo a las columnas numéricas existentes
cols_numericas = ['Horas_Sueno', 'Promedio_Academico']
for col in cols_numericas:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]

print(f"✅ Limpieza terminada. Registros finales: {len(df)}")

# 3. Inferencia Estadística (Lección 5 y 6)
media_sueño = df['Horas_Sueno'].mean()
error_estandar = stats.sem(df['Horas_Sueno'])
ic_95 = stats.t.interval(0.95, len(df)-1, loc=media_sueño, scale=error_estandar)

# Test de Hipótesis: H0: mu = 7 | H1: mu < 7
t_stat, p_val = stats.ttest_1samp(df['Horas_Sueno'], 7.0, alternative='less')

print(f"\n--- RESULTADOS ---")
print(f"Media de Sueño: {media_sueño:.2f} h")
print(f"Intervalo de Confianza (95%): [{ic_95[0]:.2f} - {ic_95[1]:.2f}]")
print(f"Valor p: {p_val:.4f}")

# 4. Visualización para el Informe
plt.figure(figsize=(10, 5))
sns.boxplot(x='Nivel_Estres', y='Promedio_Academico', data=df, palette='viridis')
plt.title('Distribución del Rendimiento Académico por Nivel de Estrés')
plt.xlabel('Estrés (Escala de Likert)')
plt.ylabel('Promedio Académico')
plt.savefig('grafico_final_limpio.png')
plt.show()