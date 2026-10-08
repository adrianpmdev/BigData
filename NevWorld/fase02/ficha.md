# El parte de caza: Del registro a una tabla útil

El creador de NevWorld te ha encargado una nueva tabla: quiere consultar **qué aldeano completó una cacería, qué presa consiguió y cuándo ocurrió**. Las seis tablas vistas en la teoría no recogen directamente ese hecho.

Tu misión es diseñar y generar `hunts.csv`. 

Trabaja con tu JSONL, conserva el RAW intacto y utiliza las operaciones vistas en clase.

## 1. Investiga antes de elegir




```json
{"schema_version":2,"run_id":"20261005_182846_584527806812332210_fc1f232ca2d448adb990e9c7a84fd93d","seed":"584527806812332210","event_index":805,"tick":34712,"type":"hunt_completed","villager_id":1607,"prey_type":"sheep"}
```

| Pregunta | Campo o valor elegido | Justificación |
| --- | --- | --- |
| ¿Qué evento demuestra que la cacería terminó? | `hunt_completed` | Es el evento que indica que la caza terminó y por eso sirve como marca final. |
| ¿Quién la completó? | `villager_id` | Es el aldeano que hizo la caza. |
| ¿Qué presa aparece registrada? | `prey_type` | Es el animal que se cazó. |
| ¿Cuándo ocurrió? | `tick` | Es el momento exacto dentro de la partida. |
| ¿A qué partida pertenece? | `run_id` | Identifica de qué partida viene. |
| ¿Cómo localizo el evento original sin confundirlo con otro? | `event_index` + `run_id` | Sirven para encontrar ese evento concreto. |

> **Respuesta:** La razón por la que `activity`, `food_stock` y `amount_delta` no son necesarios es que el evento `hunt_completed` ya nos dice lo importante. No hace falta mirar la actividad del aldeano ni el stock de comida para saber que hubo una caza, ni hace falta un cambio de recursos para saber qué presa se cazó. Este evento no dice cuánta comida produjo la caza, solo dice que la caza terminó y qué animal apareció.


## 2. Construye la tabla

Crea `scripts/actividades/02_parte_caza.py` dentro de `bigdata-game`. Reutiliza la lectura del JSONL y la función `event_table()` del tema, copiando las partes necesarias a este script.

El programa debe:

1. Leer el RAW y crear `data/processed` si hace falta.
2. Seleccionar únicamente cacerías completadas y los campos justificados en tu ficha.
3. Conservar `run_id`, `event_index` y `tick`, que la función añade automáticamente.
4. Añadir `simulation_day` mediante `tick // 12000`.
5. Guardar `data/processed/hunts.csv` sin exportar el índice de pandas.
6. Mostrar la ruta del archivo generado y su número de filas.

> **Respuesta:** Todo lo anterior está implementado dentro del script `02_parte_caza.py` y sus partes están comentadas para explicar su funcionamiento.


## 3. Demuestra que funciona

Comprueba con `assert`:

- El número de filas coincide con el número de eventos del tipo elegido en el RAW.
- No se repite la pareja `run_id`, `event_index`.
- Si hay filas, los campos que identifican partida, evento, momento, aldeano y presa no tienen valores ausentes.
- `simulation_day` coincide con la división entera indicada.

> **Respuesta:** La función `general_checks()` realiza todas estas comprobaciones mediante `assert`. Si todas son correctas, muestra un mensaje de confirmación en la consola.


## 4. Detecta las conclusiones que los datos no sostienen

Responde justificando cada decisión:

**1. «Hay seis filas, por tanto hay seis cazadores distintos». ¿Es necesariamente cierto?**

No es cierto porque un mismo cazador puede hacer varias cacerías.

**2. «Una fila indica que ese aldeano estuvo cazando durante todo el día». ¿Qué registra realmente la fila?**

La fila solamente registra que ese aldeano completó una cacería de un determinado animal en un momento concreto.

**3. «Borro del DataFrame original todas las filas con algún `NaN` y después selecciono las cacerías». ¿Por qué puede desaparecer información válida?**

Porque una fila puede tener un dato ausente en una columna que no necesitamos para analizar las cacerías, aunque sus campos de caza sean correctos. Al borrar la fila completa, también se elimina esa información válida.

**4. «El CSV está vacío, así que nadie intentó cazar». ¿Qué puedes afirmar realmente sobre el registro?**

Solo se puede afirmar que no hay cacerías completadas registradas en el RAW. El CSV vacío no demuestra que nadie intentara cazar, porque pudo haber cacerías iniciadas pero no completadas o eventos que no se registraron.


