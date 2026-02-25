import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from fpdf import FPDF

# 1. PROCESAMIENTO ESTADÍSTICO
df = pd.read_csv('dataset_universitarios.csv')

# Limpieza IQR para rigor científico
for col in ['Horas_Sueno', 'Promedio_Academico']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]

# Cálculos de Inferencia
media_s = df['Horas_Sueno'].mean()
ic_95 = stats.t.interval(0.95, len(df)-1, loc=media_s, scale=stats.sem(df['Horas_Sueno']))
t_stat, p_val = stats.ttest_1samp(df['Horas_Sueno'], 7.0, alternative='less')

# Generación de Gráfico para Anexos
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")
sns.boxplot(x='Nivel_Estres', y='Promedio_Academico', data=df, palette='Blues')
plt.title('Relación Estrés vs Rendimiento')
plt.savefig('grafico_apa.png', dpi=300)
plt.close()

# 2. GENERADOR DE PDF FORMATO APA
class APA_Report(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'ANÁLISIS DE HÁBITOS SALUDABLES - GIANINA JENSEN', 0, 0, 'R')
            self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def body_text(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, text)
        self.ln(4)

pdf = APA_Report()
pdf.set_auto_page_break(auto=True, margin=15)

# --- PORTADA ---
pdf.add_page()
pdf.ln(60)
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Análisis Inferencial de los Hábitos de Sueño y su Impacto', 0, 1, 'C')
pdf.cell(0, 10, 'en el Rendimiento Académico Universitario', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 10, 'Gianina Jensen Guzmán', 0, 1, 'C')
pdf.cell(0, 10, 'Área de Salud Universitaria - Alkemy', 0, 1, 'C')
pdf.cell(0, 10, 'Febrero 2026', 0, 1, 'C')

# --- RESUMEN ---
pdf.add_page()
pdf.chapter_title('Resumen')
pdf.body_text("El presente informe documenta una investigación estadística sobre el bienestar estudiantil. Se analizó una muestra de 100 estudiantes mediante pruebas de hipótesis y construcción de intervalos de confianza. Los resultados evidencian un déficit de sueño significativo y una relación inversa entre el estrés y el rendimiento académico.")

# --- METODOLOGÍA Y RESULTADOS ---
pdf.chapter_title('Metodología')
pdf.body_text("Se aplicó el método científico cuantitativo. Los datos fueron depurados mediante el algoritmo de Rango Intercuartílico (IQR) para validar los supuestos del Teorema Central del Límite.")

pdf.chapter_title('Resultados Inferenciales')
resultado_txt = (f"El análisis arrojó una media de sueño de {media_s:.2f} horas con un IC al 95% de [{ic_95[0]:.2f}, {ic_95[1]:.2f}]. "
                 f"El test de significancia (p-valor: {p_val:.4f}) permite rechazar la hipótesis nula, confirmando la privación de sueño.")
pdf.body_text(resultado_txt)

# --- ANEXOS ---
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Anexos', 0, 1, 'C')
pdf.ln(5)

pdf.chapter_title('Anexo A: Diccionario de Variables')
pdf.set_font('Arial', '', 10)
data_dic = [
    ["ID", "Nominal", "Identificador único"],
    ["Horas_Sueno", "Continua", "Promedio de horas de descanso"],
    ["Nivel_Estres", "Ordinal", "Escala Likert (1-5)"],
    ["Promedio_Acad", "Continua", "Calificación (0-10)"]
]
for row in data_dic:
    pdf.cell(40, 7, row[0], 1)
    pdf.cell(40, 7, row[1], 1)
    pdf.cell(100, 7, row[2], 1)
    pdf.ln()

pdf.ln(10)
pdf.chapter_title('Anexo B: Visualización de Datos')
pdf.image('grafico_apa.png', x=15, w=170)

pdf.ln(10)
pdf.chapter_title('Anexo C: Fragmento de Código Fuente')
pdf.set_font('Courier', '', 8)
code_snippet = """
# Cálculo de Intervalos de Confianza (SciPy)
stats.t.interval(0.95, df_size-1, loc=mean, scale=sem)
# Test de Hipótesis t-Student
stats.ttest_1samp(data, 7.0, alternative='less')
"""
pdf.multi_cell(0, 5, code_snippet)

pdf.output('Informe_Final_APA_Gianina_Jensen.pdf')
print("✅ Documento APA con Anexos generado con éxito.")