# El parte de caza también habla SQL

Ya has contado las cacerías con pandas y representado las presas en un gráfico. Ahora el creador de NevWorld quiere obtener **el mismo recuento consultando un archivo Parquet con SQL**. ¿Cambian los resultados al cambiar de herramienta?

Trabaja con la misma partida de las actividades anteriores y el tema 08. 
## 1. Conserva la información en otro formato

Crea **un único archivo**: `scripts/actividades/05_caza_sql.py`, dentro de `bigdata-game`. Todos los pasos siguientes van en ese archivo, uno debajo de otro. No añadas código al script de la teoría.

1. Importa `Path`, pandas como `pd` y `duckdb`.
2. Lee `data/processed/hunts.csv`, creado en la actividad 02. Si falta, termina esa actividad primero.
3. Comprueba que existe `prey_type` y que ninguna cacería tiene esa columna sin informar. No borres registros para ocultar errores.
4. Crea `data/processed/parquet` si hace falta y guarda `hunts.parquet` utilizando `to_parquet(..., engine='pyarrow', index=False)`.
5. Muestra los tamaños del CSV y del Parquet en bytes mediante `ruta.stat().st_size`.

> **Resultado:** En esta partida se han conservado las 30 cacerías de `hunts.csv`. El CSV ocupa **2.906 bytes** y el archivo Parquet ocupa **4.752 bytes**. Estos pasos se realizan en el bloque de conversión del script, mediante `to_parquet()` y `stat().st_size`.

## 2. Pregunta por las presas con SQL

Debajo de la conversión, abre una conexión con `duckdb.connect()`. Guarda una consulta SQL en una variable Python llamada `hunt_query`, entre comillas triples.

La consulta debe:

- Leer `data/processed/parquet/hunts.parquet` mediante `read_parquet`.
- Agrupar por `prey_type`.
- Mostrar la presa y el número de cacerías completadas registradas de cada tipo.
- Llamar **`hunt_count`** a la columna calculada.
- Ordenar por ese recuento de mayor a menor.

Ejecuta la consulta con `connection.execute(hunt_query).fetchdf()` y muestra el resultado. No pegues el SQL directamente en la terminal: es texto que Python entrega a DuckDB.

> **Resultado:** La consulta devuelve el mismo recuento que en las actividades anteriores: `sheep` aparece 20 veces y `deer` 10 veces. La consulta se guarda en `hunt_query` y se ejecuta con `connection.execute(...).fetchdf()`.

## 3. Comprueba y guarda

1. Comprueba que la suma de `hunt_count` coincide con el número de filas del CSV.
2. Compara cada recuento con el que obtuviste en la actividad 03 y con las barras de la 04. Las presas empatadas pueden aparecer en distinto orden.
3. Guarda el resultado como `reports/hunts_by_prey_sql.csv`, sin índice. Crea la carpeta si hace falta y cierra la conexión al final.

Si `hunts.csv` tiene cabecera pero ninguna fila, muestra un aviso y guarda el resumen vacío con las columnas `prey_type` y `hunt_count`. No inventes presas. La suma de recuentos será cero.

> **Comprobación y guardado:** La suma de `hunt_count` es 30, por lo que coincide con las filas de `hunts.csv`. Los resultados coinciden con la actividad 03 y con las barras del gráfico de la actividad 04: 20 cacerías de `sheep` y 10 de `deer`. El resultado se guarda en `reports/hunts_by_prey_sql.csv`.


## 4. Explica el resultado

Responde brevemente:

1. **¿Qué representa una fila del resultado? ¿Cuenta cacerías o unidades de comida?** Representa un tipo de presa y el número de cacerías completadas registradas de ese tipo; no cuenta unidades de comida.

2. **¿Qué hace `AS hunt_count`? Si lo cambias por `AS total_cacerias`, qué referencias posteriores debes actualizar?** Da el nombre `hunt_count` al resultado de `COUNT(*)`. Si se cambia por `AS total_cacerias`, habría que actualizar las referencias a `hunt_count`, como la comprobación de la suma, la ordenación o cualquier código que use ese nombre.

3. **¿Qué archivo ocupa menos en tu partida? ¿Demuestra eso que ese formato será siempre mejor?** En esta partida ocupa menos el CSV, con 2.906 bytes frente a 4.752 del Parquet. No significa que el CSV sea siempre mejor: el tamaño depende de los datos y Parquet puede ser más eficiente para consultas y tablas grandes.
