import pandas as pd
import numpy as np

# Configuración de la simulación
n_muestras = 100000
np.random.seed(42)

data = {
    'id_envase': range(1, n_muestras + 1),
    'temperatura_horno': np.random.uniform(1450, 1550, n_muestras),
    'velocidad_cinta': np.random.uniform(0.5, 2.0, n_muestras),
    'tipo_envase': np.random.choice(['Cerveza', 'Mermelada', 'Jarabe'], n_muestras),
    'color_vidrio': np.random.choice(['Ambar', 'Transparente', 'Verde'], n_muestras)
}

df = pd.DataFrame(data)

# Simular lógica de defectos (ej: mayor temperatura + velocidad = más burbujas)
df['prob_defecto'] = (df['temperatura_horno'] - 1450) / 500 + (df['velocidad_cinta'] / 5)
df['estado'] = df['prob_defecto'].apply(lambda x: 1 if x > 0.4 else 0)

# Asignar tipo de defecto basado en el estado 
def asignar_defecto(row):
    if row['estado'] == 0: return 'Ninguno'
    return np.random.choice(['Burbuja', 'Grieta', 'Mancha'], p=[0.5, 0.3, 0.2])

df['tipo_defecto'] = df.apply(asignar_defecto, axis=1)
df.drop(columns=['prob_defecto'], inplace=True)

# Guardar para "Tarea 1"
df.to_csv('dataset_faenvipe.csv', index=False)