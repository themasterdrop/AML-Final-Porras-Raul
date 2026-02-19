Generador de Dataset Simulado: FAENVIPE
Este script de Python se encarga de crear el conjunto de datos sintético utilizado para el entrenamiento y validación del sistema de detección de defectos en envases de vidrio. La simulación modela condiciones reales de una línea de soplado y transporte.

Descripción de Variables
El dataset generado cuenta con 100,000 registros y las siguientes características técnicas:
Variable,Tipo,Descripción,Rango/Valores
id_envase,Int,Identificador único de la unidad.,"1 - 100,000"
temperatura_horno,Float,Temperatura registrada en el soplado.,1450°C - 1550°C
velocidad_cinta,Float,Velocidad de transporte del envase.,0.5 - 2.0 m/s
tipo_envase,Categorical,Formato del frasco producido.,"Cerveza, Mermelada, Jarabe"
color_vidrio,Categorical,Tonalidad del material fundido.,"Ambar, Transparente, Verde"
tipo_defecto,Target,Resultado de la inspección.,"Ninguno, Burbuja, Grieta, Mancha"

Lógica de la Simulación
Para que el modelo de Inteligencia Artificial tenga patrones que aprender, el script implementa una lógica de correlación industrial:
Cálculo de Probabilidad: Se genera una variable latente de "riesgo" donde a mayor temperatura y mayor velocidad de cinta, aumenta la probabilidad de generar un defecto.
Umbral de Estado: Si el riesgo supera el 40%, el envase se marca como defectuoso.
Distribución de Fallas: Los defectos no son equitativos, imitando la realidad de la planta:
Burbujas (50%): El defecto más común por exceso de calor.
Grietas (30%): Defecto crítico por enfriamiento/velocidad inadecuada.
Manchas (20%): Defecto estético por impurezas.

Instrucciones de Ejecución
Para generar el archivo dataset_faenvipe.csv, asegúrate de tener instaladas las dependencias:
pip install pandas numpy
python generador_datos.py

Nota Técnica
Se ha utilizado una semilla aleatoria (np.random.seed(42)) para garantizar la reproducibilidad. Esto significa que cualquier investigador que ejecute el script obtendrá exactamente el mismo dataset, permitiendo la comparación justa de modelos.
