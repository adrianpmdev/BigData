from pathlib import Path
import pandas as pd


# ============================================================
# VARIABLES Y CONSTANTES
# ============================================================

DATA_DIR = Path('data/processed')
REPORTS_DIR = Path('reports')
REPORTS_DIR.mkdir(exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')
resources = pd.read_csv(DATA_DIR / 'resources.csv')

# Campos comunes y específicos que se necesitan en los cálculos
GENERAL_FIELDS = ['run_id', 'event_index', 'tick', 'simulation_day']
TABLE_FIELDS = {
    'hunts': ['prey_type'],
    'resources': ['resource_type', 'amount_delta'],
}


# ============================================================
# FUNCIONES
# ============================================================

def general_checks(tables, table_fields):
    """Comprueba columnas, eventos repetidos y valores ausentes."""
    for name, table in tables.items():
        required_fields = GENERAL_FIELDS + table_fields[name]

        # Check 1. Existen las columnas necesarias
        assert all(col in table.columns for col in required_fields), (
            f'Faltan columnas obligatorias en {name}'
        )

        # Check 2. No se repite la pareja `run_id`, `event_index`
        assert not table.duplicated(['run_id', 'event_index']).any(), (
            f'Hay eventos repetidos en {name}'
        )

        # Check 3. Los campos obligatorios tienen valor
        assert table[required_fields].notna().all().all(), (
            f'Hay campos obligatorios sin valor en {name}'
        )

        print(f'\nLa tabla "{name}" ha pasado todas las comprobaciones iniciales')


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    
    # 1. Comprobaciones iniciales generales de las tablas
    tables = {
        'hunts': hunts,
        'resources': resources,
    }
    
    print('\n------------------')
    print('| COMPROBACIONES |')
    print('------------------')
    general_checks(tables, TABLE_FIELDS)
    
    # 2. Resumen del parte de caza
    print('\n-----------------------------')
    print('| RESUMEN DEL PARTE DE CAZA |')
    print('-----------------------------')
    
    if hunts.empty:
        print('No hay registros de cacerías completadas, todo saldrá en blanco o 0')
    else:
        hunts_counts = len(hunts)
        print(f'\n1. El total de cacerías completadas registradas: {hunts_counts}')
        
        hunts_by_prey = hunts['prey_type'].value_counts()
        print(f'\n2. El recuento por `prey_type`, de mayor a menor frecuencia: {hunts_by_prey}')
        
        hunts_by_prey_proportions = hunts['prey_type'].value_counts(normalize=True)
        hunts_by_prey_percent = (hunts_by_prey_proportions * 100).round(1)
        print(f'\n3. El porcentaje de cada tipo de presa, redondeado a un decimal: {hunts_by_prey_percent}')
        
        hunts_by_day = hunts['simulation_day'].value_counts().sort_index()
        print(f'\n4. El recuento por `simulation_day` ordenado por día: {hunts_by_day}')
    
    # 3. Resumen de los cambios de comida
    print('\n------------------------------------')
    print('| RESUMEN DE LOS CAMBIOS DE COMIDA |')
    print('------------------------------------')
    
    if resources.empty:
        print('No hay registros de cambios de comida, todo saldrá en blanco o 0')
    else:
        resources_by_food = resources[resources['resource_type'] == 'food']
        gains = resources_by_food[resources_by_food['amount_delta'] > 0]
        spending = resources_by_food[resources_by_food['amount_delta'] < 0].copy()
        spending['amount_delta'] = spending['amount_delta'].abs()
        print(f'\nIncrementos registrados: {gains["amount_delta"].sum()}')
        print(f'\nReducciones registradas: {spending["amount_delta"].sum()}')
        print(f'\nBalance neto: {resources_by_food["amount_delta"].sum()}')

    # 4. Comprobación final y guardado del informe
    print('\n---------------------------------------------')
    print('| COMPROBACIONES FINALES E INFORME COMPLETO |')
    print('---------------------------------------------')

    assert hunts_by_prey.sum() == hunts_counts, (
        'El recuento por presa no coincide con el total de cacerías'
    )
    assert hunts_by_day.sum() == hunts_counts, (
        'El recuento por día no coincide con el total de cacerías'
    )
    assert (
        gains['amount_delta'].sum() - spending['amount_delta'].sum() == resources_by_food['amount_delta'].sum()
    ), 'El balance de comida no coincide con incrementos menos reducciones'
    print('\nTodas las comprobaciones finales han pasado correctamente')

    summary = pd.DataFrame([
        {'metric': 'hunt_events', 'value': len(hunts)},
        {'metric': 'food_change_events', 'value': len(resources_by_food)},
        {'metric': 'food_gains', 'value': gains['amount_delta'].sum()},
        {'metric': 'food_reductions', 'value': spending['amount_delta'].sum()},
        {'metric': 'food_net_change', 'value': resources_by_food['amount_delta'].sum()},
    ])
    summary.to_csv(REPORTS_DIR / 'hunting_summary.csv', index=False)
    print(f'\nEl informe completo se ha guardado en: {REPORTS_DIR / "hunting_summary.csv"}')
