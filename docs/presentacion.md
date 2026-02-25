---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #121212
style: |
  section {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #e0e0e0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 { color: #00d4ff; text-shadow: 2px 2px 4px #000; }
  h2 { color: #00d4ff; border-bottom: 2px solid #00d4ff; }
  strong { color: #ff9f43; }
  blockquote { background: rgba(255,255,255,0.1); border-left: 5px solid #00d4ff; color: #fff; }
  footer { color: #888; }
---

# **Análisis Estadístico de Hábitos Saludables**
## Bienestar Estudiantil Universitario

**Gianina Jensen Guzmán**
*Científica de Datos*

---

## 🚀 El Desafío: Datos vs. Realidad
- **Contexto:** Evaluación post-pandemia de la salud estudiantil.
- **Muestra:** $n=100$ registros validados.
- **Metodología:** Aplicación estricta del **Método Científico**.
- **Limpieza:** Remoción de Outliers mediante **IQR** para asegurar inferencias precisas y no sesgadas.

---

## 📊 Modelado y Distribuciones
Para entender el comportamiento estudiantil, identificamos:

- **Rendimiento Académico:** Sigue una **Distribución Normal** $\mathcal{N}(\mu, \sigma)$.
- **Estrés y Frecuencias:** Modelados bajo **Poisson**, ideal para eventos discretos.

> "El Teorema Central del Límite (TLC) nos permite garantizar que nuestras medias muestrales son estimadores robustos de la población total."

---

## ⚖️ Test de Hipótesis: El Momento de la Verdad

Analizamos las horas de sueño frente al estándar de salud (7h):

- **Hipótesis Nula ($H_0$):** $\mu \geq 7$
- **Hipótesis Alternativa ($H_1$):** $\mu < 7$
- **Estadístico:** Test t de una muestra ($\alpha = 0.05$).
- **Resultado:** p-valor $< 0.05$ 🚩

**Conclusión:** Se rechaza $H_0$. El déficit de sueño es una realidad estadística.

---

## 📈 Visualización Crítica de Hallazgos

![w:750 center](./grafico_correlacion.png)

*El gráfico muestra una correlación negativa: A menor descanso y mayor estrés, el promedio académico se vuelve inestable.*

---

## 💡 Conclusiones y Hoja de Ruta

1. **Hallazgo:** El intervalo de confianza al 95% sitúa el sueño en una zona de riesgo persistente.
2. **Acción Institucional:** Crear "Zonas de Descanso" y talleres de higiene del sueño.
3. **Monitoreo:** Priorizar la atención en estudiantes con niveles de estrés 4 y 5.

---

# **Gracias por su atención**
### ¿Tienen alguna pregunta?

**Gianina Jensen Guzmán**
*Data Science & Statistics*