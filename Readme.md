# 🕵️‍♀️ Is It Phishing? 🚨

**Is It Phishing?** es un modelo supervisado optimizado que predice si un URL es phishing o legítimo. Este proyecto utiliza aprendizaje de máquina para abordar la situación de identificar ataques de phishing al "flaggear" ligas sospechosas 👀🔎 .

## ¿Qué es el phishing? 🐟

El phishing es una técnica de engaño utilizada por ciberdelincuentes para engañar a las personas y obtener información confidencial como contraseñas, números de tarjeta de crédito y otros datos personales.

Ej.
| **Phishing URL** | **Liga Original** |
|----------------------------------------|-------------------------------------|
| `http://secure-update.paypal-login.com` | https://www.paypal.com |
| `http://amazon-orders-confirmation.com`| https://www.amazon.com |
| `http://login-security-google.com` | https://accounts.google.com |
| `http://appleid-verification.info` | https://appleid.apple.com |

## Descripción del Proyecto

El proyecto consiste en:

- **Entrenamiento de un modelo de Random Forest** para la tarea de clasificación supervisada.
- Un **notebook interactivo** donde se realiza el procesamiento de datos, el entrenamiento y la optimización del modelo.
- Una **interfaz web en Hugging Face Spaces** que permite a los usuarios interactuar con el modelo optimizado.

### Dataset

- **Fuente**: [Kaggle - Web Page Phishing Detection Dataset](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)
- **Descripción**: El dataset contiene 11,430 URLs con 87 características balanceadas entre phishing (50%) y legítimas (50%).
  - **56 características** relacionadas con la estructura y sintaxis del URL.
  - **24 características** relacionadas con el contenido de las páginas correspondientes.
  - **7 características** obtenidas consultando servicios externos.

### Pasos Clave

1. **Procesamiento de Datos**:

   - Transformación de la etiqueta `status` a valores binarios (`0 = legítimo`, `1 = phishing`).
   - Separación de las variables dependientes e independientes.
   - División del dataset en:
     - **80%** para entrenamiento y validación.
     - **20%** para pruebas finales.

2. **Entrenamiento del Modelo Original**:

   - Uso de un modelo de **Random Forest Classifier**.
   - Evaluación mediante métricas como Precision, Recall, F1-Score y ROC-AUC.

3. **Optimización del Modelo**:
   - Realización de **fine-tuning** mediante `GridSearchCV`.
   - Comparación de métricas con el modelo original.

### Métricas

- El modelo optimizado obtuvo mejores resultados en términos de precisión y generalización, con mejoras ligeras en el **ROC-AUC** y la **importancia de características**.

### Resultados Visuales

- Comparación de **ROC Curves** entre el modelo original y optimizado.
- **Feature Importances** para las 25 características más relevantes.

## Cómo Probar el Modelo 🚀

Se puede interactuar con el modelo optimizado en este espacio de Hugging Face:

[🔗 Interfaz Web - Is It Phishing?](https://huggingface.co/spaces/MarielSoGuZa/IsItPhishing)

### Requisitos Locales

Para correr el proyecto de forma local hay que instalar una serie de librerías las cuales están especificadas en [requirements.txt](./requirements.txt)

```bash
pip install -r requirements.txt
```
