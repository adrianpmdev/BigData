from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


# ============================================================
# VARIABLES Y CONSTANTES
# ============================================================

DATA_DIR = Path('data/processed')
CHARTS_DIR = Path('reports/charts')
CHARTS_DIR.mkdir(parents=True, exist_ok=True)

hunts = pd.read_csv(DATA_DIR / 'hunts.csv')


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    if 'prey_type' not in hunts.columns:
        raise ValueError('Falta la columna prey_type en hunts.csv')

    if hunts.empty:
        print('No hay cacerías completadas registradas; no se generará el gráfico')
    else:
        # Cada cacería debe tener informado el tipo de presa
        assert hunts['prey_type'].notna().all(), (
            'Hay cacerías sin tipo de presa informado'
        )

        hunts_by_prey_counts = hunts['prey_type'].value_counts()

        # Crea una figura de 8 por 4 pulgadas
        plt.figure(figsize=(8, 4))
        hunts_by_prey_counts.plot.bar(color='seagreen')
        plt.title('Cacerías completadas registradas por tipo de presa')
        plt.xlabel('Tipo de presa')
        plt.ylabel('Número de cacerías')
        plt.xticks(rotation=30, ha='right')
        plt.tight_layout()
        plt.savefig(CHARTS_DIR / '05_hunts_by_prey.png')
        plt.close()
        print(f'Gráfico guardado en {CHARTS_DIR / "05_hunts_by_prey.png"}')
