from pathlib import Path
import pandas as pd


# 0. Cargar el dataframe con pandas, ver si existe y leerlo
DATASET = Path('data/raw/nevworld_584527806812332210_20261005_182846.jsonl')

if not DATASET.exists():
    raise FileNotFoundError(f'No se encuentra: {DATASET.resolve()}')

df = pd.read_json(DATASET, lines=True)


# 1. Comprobacion de validaciones
required = [
    'run_id', 'event_index', 'tick', 'type'
]

assert not df.empty, 'El dataset está vacío'

assert all(column in df.columns for column in required), \
    'Faltan columnas principales'
    
assert not df.duplicated(['run_id', 'event_index']).any(), \
    'Hay eventos duplicados'

ordered = df.sort_values('event_index')
assert ordered['tick'].is_monotonic_increasing, \
    'Los ticks retroceden'

print('\nVALIDACIÓN BÁSICA: OK')


# 2. Mostrar las primeras filas
print('\nPRIMEROS EVENTOS')
print(df.head())


# 3. Obtencion de los datos
filas, columnas = df.shape

print('\n\nDATOS')
print(f'\nNúmero total de eventos: {filas}')
print(f'\nNúmero de columnas: {columnas}')
print(f'\nNombres de las columnas: {df.columns.tolist()}')
print(f'\nTipo del primer evento registrado: {df['type'].iloc[0]}')
print(f'\nTipo de evento más frecuente y cantidad: {df["type"].value_counts().head(1)}')
print(f'\nRecuento de todos los tipos de evento: {df["type"].value_counts()}')
print(f'\nrun_id de la primera fila:', df['run_id'].iloc[0])
print(f'\nsemilla de la primera fila:', df['seed'].iloc[0])
print(f'\nesquema de la primera fila:', df['schema_version'].iloc[0])
print(f'\nTick mínimo:', df['tick'].min())
print(f'\nTick máximo:', df['tick'].max())
