# El parte de caza, de un vistazo

Ya has transformado los eventos de caza y calculado sus métricas. Ahora el creador de NevWorld quiere **ver qué tipos de presa aparecen más en las cacerías completadas**, sin tener que leer toda la tabla.

Convierte uno de los recuentos de la actividad 3 en un gráfico de barras. Trabaja con tu propia partida.


## 1. Decide qué vas a representar

Utiliza `data/processed/hunts.csv`, creado en la actividad 2. Si no existe, genera primero esa tabla. Antes de programar, responde:

- **¿Qué representa cada barra?** Cada barra representa un tipo de presa y muestra cuántas cacerías completadas registradas corresponden a ese tipo.
- **¿Qué cantidad y unidad aparecerán en el eje vertical?** Aparecerá el número de cacerías, expresado como cantidad de registros.
- **¿Por qué usar barras y no una línea que conecte las presas?** Porque las presas son categorías independientes.

Elige un título que deje claro que se representan **cacerías completadas registradas**, no cantidades de comida obtenida.

## 2. Crea el gráfico

Crea `scripts/actividades/04_grafico_caza.py` dentro de `bigdata-game`. El script debe:

1. Importar `Path`, pandas como `pd` y `matplotlib.pyplot` como `plt`.
2. Leer `hunts.csv` y obtener el recuento por `prey_type`.
3. Si no hay filas, mostrar un aviso y omitir el gráfico. No inventes presas ni cantidades.
4. Si hay datos, crear un gráfico de barras con título, ejes identificados, etiquetas legibles y un color a tu elección.
5. Guardar la imagen como `reports/charts/05_hunts_by_prey.png`, creando la carpeta si hace falta, y cerrar la figura.

Reutiliza las validaciones de la actividad anterior: cada cacería debe tener una presa informada. Un valor ausente en una fila existente no equivale a una tabla vacía.


## 3. Comprueba e interpreta

Compara las alturas de las barras con los recuentos de tu actividad 03. La suma de las cantidades representadas debe coincidir con el total de cacerías de esa misma partida. Comprueba que no se corten los títulos o etiquetas.

Escribe tres frases:

1. **Observación:** indica qué presa o presas tienen más registros y cuántos, incluyendo los empates. Las `sheep` tienen más registros, con 20 cacerías, frente a las 10 de `deer`.
2. **Límite:** explica por qué el gráfico no muestra cuánto tiempo se dedicó a cazar ni cuánta comida produjo cada presa. El gráfico solo cuenta cacerías; no indica cuánto duró cada una ni cuánta comida se obtuvo.
3. **Pregunta pendiente:** plantea algo que no puedas responder con este gráfico e indica qué dato adicional necesitarías. No se puede saber qué presa produjo más comida; harían falta datos sobre la cantidad obtenida en cada cacería.


