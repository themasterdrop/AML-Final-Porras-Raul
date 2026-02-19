# Dataset: Control de Calidad FAENVIPE

Este directorio contiene las instrucciones y metadatos necesarios para trabajar con el conjunto de datos de inspección de envases de vidrio. 

> **Nota:** Por políticas de privacidad y gestión de almacenamiento en GitHub, los archivos de datos originales (`.csv` / `.xlsx`) no se encuentran alojados en este repositorio.

##  Fuente del Dataset
Los datos utilizados para este proyecto corresponden a la simulación industrial de la planta FAENVIPE (100,000 registros). 
* **Origen:** https://drive.google.com/file/d/1vu4x5CXfLXSWwaDXbOU6rvk4aD62s1e6/view?usp=drive_link.
* **Nombre del archivo:** `dataset_faenvipe_sim.csv`

##  Instrucciones para Google Colab
Para replicar el análisis en Colab, se recomienda cargar el archivo directamente desde el almacenamiento local de la sesión o vincular Google Drive:

```python
from google.colab import files
uploaded = files.upload() # Seleccionar el archivo 'dataset_faenvipe_sim.csv'

# O mediante Google Drive
# from google.colab import drive
# drive.mount('/content/drive')
