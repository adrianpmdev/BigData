# ¿Ha llegado la misma partida?

El equipo de análisis recibe partidas de otros jugadores. Antes de trabajar con ellas quiere comprobar que los archivos recibidos conservan el contenido que tenían al preparar el envío.

Trabajad **por parejas**, alternando los papeles de emisor y receptor. Enviaréis dos copias de un JSONL: una intacta y otra modificada después de registrar su huella. **Duración orientativa: 20–25 minutos.**


## 1. Prepara dos copias y registra su referencia

El emisor prepara **dos copias del mismo archivo original**, no dos partidas diferentes. Puedes hacerlo desde el explorador de archivos:

1. Elige **un solo JSONL** de una partida finalizada que tengas en `data/raw`.
2. Crea la carpeta `data/intercambio/envio` dentro de `bigdata-game`.
3. Copia el JSONL elegido a esa carpeta y renombra **la copia** como `partida_A.jsonl`.
4. Dentro de `data/intercambio/envio`, duplica `partida_A.jsonl` y llama a esa segunda copia `partida_B.jsonl`.

Ahora A y B contienen exactamente los mismos datos y solo cambia su nombre. El JSONL original permanece en `data/raw`, con su nombre y contenido intactos. Todas las modificaciones posteriores se harán sobre una de las copias de `envio`.

Antes de modificar ninguna de las dos copias:

1. Calcula sus huellas y tamaños mediante un pequeño script `scripts/actividades/06_verificar_envio.py`.
2. Comprueba que las dos huellas coinciden aunque los nombres sean diferentes.
3. Guarda los resultados en `referencia.txt`, indicando nombre, tamaño y SHA-256 de cada archivo.
4. Envía esa referencia a tu compañero por el canal de clase. El receptor debe conservarla sin modificar: será la referencia anterior a los cambios.


> **Resultado de la primera ronda:** Las copias `partida_A.jsonl` y `partida_B.jsonl` tenían el mismo tamaño, **250053 bytes**, y la misma huella SHA-256: `5fc57004976080f1e2cea279d8a4bf16dd0e1841ca1f5840c43367f58980701c`. Por tanto, eran copias idénticas antes de modificar una de ellas.

## 2. Introduce un cambio pequeño y envía los archivos

El emisor deja una copia intacta y modifica **solo la otra** con VS Code. No le digas todavía al receptor cuál has elegido.

- Cambia un único dígito de un valor numérico, por ejemplo `100` por `900`, si encuentras ese valor. También puedes cambiar otro dígito por uno distinto manteniendo un número JSON válido.
- No cambies `schema_version`, `run_id` ni `event_index`. No añadas ni elimines líneas y conserva la codificación y los saltos de línea.
- Guarda la copia modificada. **No actualices las huellas de `referencia.txt`: deben seguir siendo las calculadas antes del cambio.**

Anota en privado la línea, el campo y el valor anterior y posterior. Envía ambos JSONL como archivos adjuntos o en un ZIP; no pegues su contenido como texto en un mensaje. El receptor los guardará en `data/intercambio/recibido`.

> **Cambio realizado:** En `data/intercambio/envio/partida_A.jsonl`, línea 24, se cambió el campo `amount_after` del evento de recurso `food` de **4** a **5**. `partida_B.jsonl` se dejó intacto y las huellas de `referencia.txt` no se actualizaron.

## 3. Verifica lo recibido

El receptor adapta su script para recorrer los dos archivos recibidos y comparar cada huella actual con la referencia correspondiente. Las huellas esperadas pueden guardarse en un diccionario de Python, con el nombre de archivo como clave.

Debe mostrar para cada archivo:

- Nombre y tamaño recibido.
- Huella esperada y huella calculada.
- `COINCIDE` o `NO COINCIDE`.

Si falta un archivo, indica `NO RECIBIDO`; no lo clasifiques como una coincidencia. No calcules las huellas esperadas a partir de los archivos recibidos: eso compararía el archivo consigo mismo.

Antes de que el emisor revele el cambio, completa:

| Archivo | Tamaño esperado | Tamaño recibido | ¿Coincide SHA-256? | Conclusión |
| --- | ---: | ---: | --- | --- |
| Juane - `partida_A.jsonl` | 1139857 | 1139855 | No | Archivo modificado |
| Juane - `partida_B.jsonl` | 1139857 | 1139857 | Sí | Archivo intacto |
| David - `partida_A.jsonl` | 562306 | 562306 | Sí | Archivo intacto |
| David - `partida_B.jsonl` | 562306 | 562306 | No | Archivo modificado |

> **Resultado:** En la ronda de Juane, `partida_A.jsonl` no coincide y `partida_B.jsonl` sí. En la ronda de David, `partida_A.jsonl` coincide y `partida_B.jsonl` no.

## 4. Intercambia los papeles y explica

Repetid el ejercicio cambiando emisor y receptor. Usad subcarpetas distintas para cada ronda, conservando sus referencias y resultados.

Responded brevemente:

1. **¿Por qué pueden coincidir las huellas de dos archivos con distinto nombre?** Porque el nombre no forma parte del contenido; si los bytes son iguales, la huella también lo es.
2. **¿Puede un archivo mantener el tamaño y tener una huella diferente?** Sí. En la ronda de David, `partida_B.jsonl` mantuvo 562306 bytes, pero su huella cambió porque se modificó un valor.
3. **¿Permite la huella saber qué campo cambió?** No. Para localizarlo hay que comparar los archivos línea a línea y revisar el campo diferente.
4. **¿Por qué calculamos y conservamos la referencia antes de modificar la copia?** Para disponer de una huella original fiable con la que comparar el archivo después del envío.
5. **¿Una coincidencia demuestra que los datos de la partida son correctos?** No. Solo demuestra que el archivo recibido coincide con la referencia conservada.


