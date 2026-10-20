from hashlib import sha256
from pathlib import Path


# ============================================================
# VARIABLES Y CONSTANTES
# ============================================================

# Envíos
pathA = Path('data/intercambio/envio/partida_A.jsonl')
pathB = Path('data/intercambio/envio/partida_B.jsonl')

# Recibidos
pathA_recibido_juane = Path('data/intercambio/recibido/juane/partida_A.jsonl')
pathB_recibido_juane = Path('data/intercambio/recibido/juane/partida_B.jsonl')
huellaA_expected_Juane = 'partida_A.jsonl 1139857 8cd131e17e00e69d0ed8a06af1d08664594c5c8ee0eeeb4e8d69482bd86896d7'
huellaB_expected_Juane = 'partida_B.jsonl 1139857 8cd131e17e00e69d0ed8a06af1d08664594c5c8ee0eeeb4e8d69482bd86896d7'

pathA_recibido_david = Path('data/intercambio/recibido/david/partida_A.jsonl')
pathB_recibido_david = Path('data/intercambio/recibido/david/partida_B.jsonl')
huellaA_expected_David = 'partida_A.jsonl 562306 9a601391cfb88301a85d2a47e19cf0a3c288489d3dbe15819866b7747a9e867e'
huellaB_expected_David = 'partida_B.jsonl 562306 9a601391cfb88301a85d2a47e19cf0a3c288489d3dbe15819866b7747a9e867e'


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    # ------------------------------------
    # BLOQUE 1: Comprobar huellas de ambos archivos para enviar
    # ------------------------------------

    print('\n-----------------------------------------------')
    print('Comprobando huellas de los archivos a enviar...')
    print('-----------------------------------------------')

    huellaA = sha256(pathA.read_bytes()).hexdigest()
    print(pathA.name, pathA.stat().st_size, huellaA)

    huellaB = sha256(pathB.read_bytes()).hexdigest()
    print(pathB.name, pathB.stat().st_size, huellaB)

    print('Las huellas coinciden' if huellaA == huellaB else 'Las huellas no coinciden')

    # ------------------------------------
    # BLOQUE 2 Juane: Comprobar huellas de ambos archivos recibidos
    # ------------------------------------

    print('\n--------------------------------------------------------')
    print('Comprobando huellas de los archivos recibidos (Juane)...') 
    print('--------------------------------------------------------')

    huellaA_recibido_juane = pathA_recibido_juane.name + ' ' + str(pathA_recibido_juane.stat().st_size) + ' ' + sha256(pathA_recibido_juane.read_bytes()).hexdigest()
    print(f'La huella A esperada Juane es: {huellaA_expected_Juane}')
    print(f'La huella A recibida Juane es: {huellaA_recibido_juane}')
    print('La huella A Juane coincide' if huellaA_recibido_juane == huellaA_expected_Juane else 'La huella A Juane no coincide')

    huellaB_recibido_juane = pathB_recibido_juane.name + ' ' + str(pathB_recibido_juane.stat().st_size) + ' ' + sha256(pathB_recibido_juane.read_bytes()).hexdigest()
    print(f'\nLa huella B esperada Juane es: {huellaB_expected_Juane}')
    print(f'La huella B recibida Juane es: {huellaB_recibido_juane}')
    print('La huella B Juane coincide' if huellaB_recibido_juane == huellaB_expected_Juane else 'La huella B Juane no coincide')

    # ------------------------------------
    # BLOQUE 2 David: Comprobar huellas de ambos archivos recibidos
    # ------------------------------------
    
    print('\n--------------------------------------------------------')
    print('Comprobando huellas de los archivos recibidos (David)...') 
    print('--------------------------------------------------------')
    
    huellaA_recibido_david = pathA_recibido_david.name + ' ' + str(pathA_recibido_david.stat().st_size) + ' ' + sha256(pathA_recibido_david.read_bytes()).hexdigest()
    print(f'La huella A esperada David es: {huellaA_expected_David}')
    print(f'La huella A recibida David es: {huellaA_recibido_david}')
    print('La huella A David coincide' if huellaA_recibido_david == huellaA_expected_David else 'La huella A David no coincide')
    
    huellaB_recibido_david = pathB_recibido_david.name + ' ' + str(pathB_recibido_david.stat().st_size) + ' ' + sha256(pathB_recibido_david.read_bytes()).hexdigest()
    print(f'\nLa huella B esperada David es: {huellaB_expected_David}')
    print(f'La huella B recibida David es: {huellaB_recibido_david}')
    print('La huella B David coincide' if huellaB_recibido_david == huellaB_expected_David else 'La huella B David no coincide')
