# Generador de Dataset: Simulación de Inspección Industrial (FAENVIPE)
Este script en Python se encarga de crear el conjunto de datos sintético de 100,000 registros utilizado para el entrenamiento y validación del sistema. La simulación modela las condiciones físicas de una línea de soplado y transporte de vidrio.

## Objetivo
Producir un set de datos de alta fidelidad que replique el desbalance de clases y las correlaciones térmicas reales de la planta, permitiendo evaluar la capacidad del modelo para detectar fallas críticas bajo condiciones de estrés.

## Estructura del Dataset
El archivo generado (dataset_faenvipe.csv) contiene las siguientes dimensiones técnicas:

-Variables de Proceso: temperatura_horno (°C) y velocidad_cinta (m/s).

-Variables de Producto: tipo_envase (Cerveza, Mermelada, Jarabe) y color_vidrio.

-Variable Objetivo: tipo_defecto (Ninguno, Burbuja, Grieta, Mancha).

## Lógica de Simulación
El script no asigna defectos al azar, sino que sigue una lógica de ingeniería industrial:

-**Cálculo de Riesgo/**: Se define una función donde el aumento de la temperatura y la velocidad incrementan la probabilidad de fallo estructural.

-**Umbral de Calidad/**: Si el riesgo supera el 40%, el envase es marcado como defectuoso.

-**Distribución Realista/**: Se aplica un desbalance para imitar la frecuencia de fallas en planta:

-Burbujas (50%): Por inestabilidad térmica.

-Grietas (30%): Por choque mecánico o enfriamiento rápido.

-Manchas (20%): Por impurezas en el material.

## Tecnologías
Librería Base: NumPy (Generación de distribuciones aleatorias).

Procesamiento: Pandas (Estructuración de dataframes y exportación CSV).

Reproducibilidad: Semilla aleatoria fija (seed 42) para garantizar resultados consistentes.

## Instrucciones de Uso
Asegúrate de tener instalado Python y las librerías: pip install pandas numpy

Ejecuta el script: python generador_datos.py

El archivo resultante aparecerá en la carpeta local listo para ser procesado por el notebook principal.
