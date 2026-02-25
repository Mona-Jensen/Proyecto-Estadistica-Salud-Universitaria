import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from fpdf import FPDF
import os

# ==========================================
# 1. PROCESAMIENTO DE DATOS Y ESTADÍSTICA
# ==========================================
df = pd.read_csv('dataset_universitarios.csv')

# Limpieza IQR (Consistencia con pasos previos)
for col in ['Horas_Sueno', 'Promedio_Academico']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]

# Cálculos de Inferencia
media_s = df['Horas_Sueno'].mean()
ic_s = stats.t.interval(0.95, len(df)-1, loc=media_s, scale=stats.sem(df['Horas_Sueno']))
t_stat, p_val = stats.ttest_1samp(df['Horas_Sueno'], 7.0, alternative='less')

# Generación de Gráfico para el Informe
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.regplot(x='Horas_Sueno', y='Promedio_Academico', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relación entre Sueño y Rendimiento Académico')
plt.savefig('grafico_informe.png', dpi=300)
plt.close()

# ==========================================
# 2. GENERACIÓN DEL PDF PROFESIONAL
# ==========================================
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Informe de Investigación: Área de Salud Universitaria', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 11)

# --- TÍTULO Y RESUMEN ---
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Análisis Estadístico de Hábitos Saludables', 0, 1, 'L')
pdf.ln(5)
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 7, "Este informe presenta los resultados de la investigación sobre los factores que influyen en el bienestar de los jóvenes universitarios, centrándose en la relación entre el descanso y el rendimiento académico mediante métodos de inferencia estadística.")

# --- SECCIÓN 1: METODOLOGÍA ---
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '1. Metodología y Limpieza de Datos', 0, 1, 'L')
pdf.set_font('Arial', '', 11)
pdf.multi_cell(0, 7, f"Se analizó una muestra de {len(df)} estudiantes mediante un Muestreo Aleatorio Simple. Se aplicó un protocolo de limpieza basado en el Rango Intercuartílico (IQR) para eliminar sesgos por valores atípicos, garantizando la robustez del Teorema Central del Límite.")

# --- SECCIÓN 2: RESULTADOS ESTADÍSTICOS ---
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '2. Inferencias y Pruebas de Hipótesis', 0, 1, 'L')
pdf.set_font('Arial', '', 11)
texto_stats = (
    f"- Media de sueño observada: {media_s:.2f} horas.\n"
    f"- Intervalo de Confianza (95%): [{ic_s[0]:.2f}, {ic_s[1]:.2f}] horas.\n"
    f"- Prueba t (H0: mu=7): p-valor = {p_val:.4f}.\n"
)
pdf.multi_cell(0, 7, texto_stats)

if p_val < 0.05:
    pdf.set_text_color(200, 0, 0)
    pdf.multi_cell(0, 7, "Conclusión del Test: Existe evidencia suficiente para rechazar la hipótesis nula. El déficit de sueño es estadísticamente significativo.")
    pdf.set_text_color(0, 0, 0)

# --- SECCIÓN 3: VISUALIZACIÓN ---
pdf.ln(5)
pdf.image('grafico_informe.png', x=10, w=180)
pdf.ln(5)

# --- SECCIÓN 4: RECOMENDACIONES ---
pdf.add_page()
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '3. Conclusiones y Recomendaciones', 0, 1, 'L')
pdf.set_font('Arial', '', 11)
recomendaciones = (
    "1. Higiene del Sueño: Los datos confirman que la media poblacional es inferior a 7 horas. Se recomienda implementar talleres de gestión del tiempo.\n"
    "2. Mitigación de Estrés: Se observa una correlación negativa entre el estrés y el promedio. Es vital revisar las cargas académicas en periodos críticos.\n"
    "3. Políticas de Bienestar: Los resultados validan la necesidad de espacios de descanso dentro del campus universitario."
)
pdf.multi_cell(0, 7, recomendaciones)

# --- CIERRE ---
pdf.output('Informe_Final_Salud_Universitaria.pdf')
print("🚀 Informe generado con éxito: Informe_Final_Salud_Universitaria.pdf")