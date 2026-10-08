from pathlib import Path
import pandas as pd


# ============================================================
# VARIABLES Y CONSTANTES
# ============================================================

# Guarda el dataset a partir del archivo RAW
DATASET = Path('data/raw/nevworld_584527806812332210_20261005_182846.jsonl')

# Guarda la carpeta donde se guardarán los CSVs procesados
OUTPUT_DIR = Path('data/processed')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Campos obligatorios que deben estar presentes en cada tabla de eventos
GENERAL_FIELDS = ['run_id', 'event_index', 'tick']

# Campos especificos para cada tabla
HUNT_FIELDS = ['villager_id', 'prey_type']

# Tipos de eventos que se van a procesar
EVENT_TYPE = {
    'hunts': 'hunt_completed'
}

# Campos específicos de cada tabla
TABLE_FIELDS = {
    'hunts': HUNT_FIELDS
}

# Guarda el dataset en un DataFrame de Pandas.
df = pd.read_json(DATASET, lines=True)


# ============================================================
# FUNCIONES
# ============================================================

def event_table(event_type, columns):
    """Crea una tabla con los eventos de un tipo específico"""
    selected = [*GENERAL_FIELDS, *columns]
    out_columns = [*selected, 'simulation_day']

    available = [
        column for column in selected
        if column in df.columns
    ]

    table = df.loc[
        df['type'] == event_type,
        available,
    ].copy()

    if not table.empty:
        # Ve si falta alguna columna obligatoria en la tabla
        missing = [column for column in selected if column not in table.columns]
        if missing:
            raise ValueError(f'Faltan columnas obligatorias: {", ".join(missing)}')
        
        # Añade la columna del día
        table['simulation_day'] = table['tick'] // 12000

    # Conserva las cabeceras aunque no haya cacerías
    table = table.reindex(columns=out_columns)

    return table


def general_checks(tables, table_fields):
    """Realiza comprobaciones sobre las tablas de eventos"""
    for name, table in tables.items():
        # Check 1. El número de filas coincide con el número de eventos del tipo elegido en el RAW
        cantidad = (df['type'] == EVENT_TYPE[name]).sum()
        assert cantidad == len(table), f'Cantidad de eventos de {name} no coincide con el RAW'

        if not table.empty:
            # Check 2. No se repite la pareja `run_id`, `event_index`.
            assert not table.duplicated(['run_id', 'event_index']).any(), 'Hay eventos duplicados'

            # Check 3. Comprueba que los campos obligatorios no tengan celdas ausentes
            required_fields = GENERAL_FIELDS + table_fields[name]
            assert table[required_fields].notna().all().all(), f'Hay celdas ausentes en {name}'

            # Check 4. Comprueba el cálculo del día de simulación
            assert (table['simulation_day'] == table['tick'] // 12000).all(), f'simulation_day no coincide con tick // 12000 en {name}'

        print(f'\nLa tabla {name} ha pasado todas las comprobaciones con éxito')


def save_tables_csv(tables):
    """Guarda las tablas en CSVs, una por cada tipo de evento"""
    for name, table in tables.items():
        output = OUTPUT_DIR / f'{name}.csv'
        table.to_csv(output, index=False)
        print(f'Tabla {name} guardada en {output} con {len(table)} filas')


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # Creacion de las tablas, en este caso solo la tabla hunts
    tables = {
        'hunts': event_table(EVENT_TYPE['hunts'], HUNT_FIELDS)
    }
    
    # Comprobaciones generales
    general_checks(tables, TABLE_FIELDS)
    
    # Se guardan las tablas en CSVs
    save_tables_csv(tables)
