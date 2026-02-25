# Análisis Estadístico Inferencial: Bienestar y Rendimiento Universitario 📊🎓

**Autora:** Gianina Jensen Guzmán  
**Institución:** Área de Salud Universitaria - Proyecto Integrador  
**Fecha:** Febrero 2026

## 📝 Descripción del Proyecto
Este proyecto aplica el **método científico cuantitativo** para investigar cómo los hábitos de vida (sueño y estrés) impactan en el rendimiento académico de los estudiantes. A través de un análisis que abarca desde la probabilidad básica hasta el test de hipótesis complejo, se busca transformar datos crudos en recomendaciones institucionales.

---

## 📂 Estructura del Repositorio

| Carpeta/Archivo | Descripción |
| :--- | :--- |
| `📂 data/` | Dataset original y Diccionario de Variables (Codebook). |
| `📂 scripts/` | Código Python para limpieza de datos e informes automatizados. |
| `📂 docs/` | Informe Final APA, Presentación Ejecutiva y Bitácora de Lecciones. |
| `📂 img/` | Visualizaciones estadísticas generadas. |
| `📄 README.md` | Guía principal del proyecto. |
| `📄 requirements.txt` | Librerías necesarias para replicar el análisis. |

---

## 🛠️ Desarrollo del Proyecto (Pasos 1 al 6)

El análisis se estructuró siguiendo el plan de estudios progresivo:

1. **Muestreo y Probabilidad (Lección 1 y 2):** Implementación de Muestreo Aleatorio Simple ($n=100$) y cálculo de probabilidades de salud mediante árboles de decisión.
2. **Distribuciones (Lección 3):** Modelado del Promedio Académico mediante **Distribución Normal** y frecuencia de eventos de estrés mediante **Poisson**.
3. **Teorema Central del Límite (Lección 4):** Validación de la media muestral como estimador robusto de la población.
4. **Intervalos de Confianza (Lección 5):** Estimación de la media poblacional de sueño con un nivel de confianza del 95%.
5. **Test de Hipótesis (Lección 6):** Contraste de hipótesis t-Student ($H_0: \mu = 7h$) para confirmar déficit de descanso.

---

## 📊 Visualizaciones Destacadas

### 1. Relación entre Estrés y Rendimiento
![Relación Estrés vs Rendimiento](img/boxplot_estres.png)
*El análisis de cajas muestra una variabilidad significativa y una tendencia decreciente en el rendimiento a medida que aumenta el nivel de estrés.*



### 2. Validación de Hipótesis de Sueño
![Validación de Hipótesis](img/grafico_sueño_vs_rendimiento.png)
*El gráfico de regresión visualiza el déficit de sueño identificado mediante el test de hipótesis.*



---

## 🚀 Conclusiones Clave
- **Evidencia Estadística:** Se rechazó la Hipótesis Nula ($p < 0.05$), confirmando que el promedio de sueño es inferior al estándar saludable de 7 horas.
- **Factor Crítico:** El nivel de estrés 4 y 5 correlaciona con los promedios académicos más bajos y volátiles.
- **Recomendación:** Implementar programas de higiene de sueño y monitoreo de salud mental preventiva.

---

## ⚙️ Instalación y Uso
1. Clonar este repositorio.
2. Instalar dependencias:  
   `pip install -r requirements.txt`
3. Ejecutar el generador de informe:  
   `python scripts/informe_apa.py`