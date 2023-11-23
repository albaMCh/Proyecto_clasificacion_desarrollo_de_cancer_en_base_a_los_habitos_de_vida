# Proyecto para clasificar si una persona va a desarrollar cáncer en base a sus hábitos de vida
Este proyecto se basa en el análisis de un database sobre distintos hábitos de vida y como influyen en la probabilidad de desarrollar cáncer, incluye el desarrollo y elección del modelo predictivo, la creación posterior de la api y el desarrollo de una app con Streamlit  en el cual tu puedes hacer el test y ver la probabilidad de desarrollar cáncer
1. Podemos ver todo el desarrollo con ML en el fichero .ipynb en el cual se pueden ver todos los pasos dados y resultados obtenidos.
2. En la parte final de este proyeto se procede a la obtención de la API dockerizada con Pycaret y FastAPI.
3. Finalmente, presentamos los resultados de nuestro analasis, para ello he utilizado herramientas como Streamlit y FastAPI.

## ¿Qué es Streamlit?

Streamlit es un “framework” de Python de código abierto que permite de manera sencilla e integrada desarrollar aplicaciones gracias a la interacción con otras librerías para su empleo en campos de la teledetección, ciencia de datos, etc. Permite a los científicos de datos crear rápidamente paneles interactivos y aplicaciones web de aprendizaje automático, sin necesidad de experiencia en desarrollo web front-end.

Este marco ha ganado atención y popularidad entre los científicos de datos y los programadores de aprendizaje automático en los últimos años. Su crecimiento se debe al hecho de que:

Es una herramienta fácil de usar,solo necesita conocimientos básicos de Python, y
es compatible con marcos  de aprendizaje automático: TensorFlow, PyTorch, Scikit-learn,y Bibliotecas de visualización: Seaborn, Altair, Plotly.

## ¿Cómo funciona?

Instalar Streamlit. Te recomiendo que uses Conda y configures tu entorno, pero puedes usar:

pip install streamlit
Crea un nuevo script de Python e importa Streamlit con algunos comandos de Streamlit:

import streamlit as st
Ejecútalo:

streamlit run your_script.py
Tan pronto como ejecute el script, se abrirá un servidor Streamlit local y su aplicación se abrirá en una nueva pestaña en su navegador web predeterminado.

O puedes navegar a http://localhost:8501

## ¿Qué es FastAPI?

FastAPI es un marco web moderno y rápido (de alto rendimiento) para crear API con Python. Se basa en sugerencias de tipo Python estándar, lo que permite la validación automática de datos, la serialización y la generación de documentación.

FastAPI está diseñado para ser fácil de usar y altamente eficiente, proporcionando características como el soporte asíncrono, la inyección de dependencias y la generación automática de documentación de OpenAPI y JSON Schema.

Ha ganado popularidad en la comunidad de Python debido a su facilidad de uso, rendimiento y características amigables para los desarrolladores.
## Configuración del proyecto

Clonar este repositorio
1. (base)$: git clone git@github.com: albaMCh/ProyectoFinal_ML-FastApi-Streamlit.git
2. (base)$: cd ProyectoFinal_ML_FastApi_Streamlit.git
3. Ejecutar las aplicaciones. $ docker-compose up
4. Y ve a http://localhost:8501
