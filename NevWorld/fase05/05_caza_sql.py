from pathlib import Path
import duckdb
import pandas as pd


# ============================================================
# VARIABLES Y CONSTANTES
# ============================================================

DATA_DIR = Path('data/processed')
PARQUET_DIR = DATA_DIR / 'parquet'
PARQUET_DIR.mkdir(exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    # Comprobar que existe `prey_type` y que ninguna cacería tiene esa columna sin informar
    if 'prey_type' not in hunts.columns:
        raise ValueError("La columna 'prey_type' no existe en el DataFrame 'hunts'")

    if hunts.empty:
        print('No hay cacerías completadas registradas; no se generará el gráfico')
    else:
        assert hunts['prey_type'].notna().all(), (
            'Hay cacerías sin tipo de presa informado'
        )

        # Convertir CSV a Parquet y mostrar tamaños de archivo
        parquet_path = PARQUET_DIR / 'hunts.parquet'
        hunts.to_parquet(parquet_path, engine='pyarrow', index=False)

        print('\nARCHIVOS HUNTS')
        print('  CSV:', (DATA_DIR / 'hunts.csv').stat().st_size, 'bytes')
        print('  Parquet:', parquet_path.stat().st_size, 'bytes')

        # Preguntar por las presas con SQL
        connection = duckdb.connect()

        hunt_query = """
            SELECT
                prey_type,
                COUNT(*) AS hunt_count
            FROM hunts
            GROUP BY prey_type
            ORDER BY hunt_count DESC
        """
        
        hunts_summary = connection.execute(hunt_query).fetchdf()
        
        print('\nCACERÍAS CONSULTADAS CON SQL')
        print(hunts_summary)

        # Comprobar y guardar
        assert hunts_summary['hunt_count'].sum() == len(hunts), (
            'La suma de hunt_count no coincide con el número de filas de hunts.csv'
        )

        hunts_summary.to_csv('reports/hunts_by_prey_sql.csv', index=False)
        connection.close()
