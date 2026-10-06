## Ficha

| Dato de mi partida | Resultado |
| --- | --- |
| Nombre del archivo JSONL |nevworld_584527806812332210_20261005_182846.jsonl|
| Número total de eventos |5618 |
| Número de columnas | 36|
| Nombres de las columnas | `schema_version`<br>`run_id`<br>`seed`<br>`event_index`<br>`tick`<br>`type`<br>`started_at_utc`<br>`building_id`<br>`building_type`<br>`cell_x`<br>`cell_y`<br>`width`<br>`height`<br>`villager_id`<br>`activity`<br>`resource_type`<br>`amount_before`<br>`amount_after`<br>`amount_delta`<br>`population`<br>`constructed_buildings`<br>`wood_stock`<br>`food_stock`<br>`gold_stock`<br>`day`<br>`prey_type`<br>`actor_id`<br>`target_id`<br>`interaction_type`<br>`topic`<br>`relationship_actor_to_target_after`<br>`relationship_target_to_actor_after`<br>`need_type`<br>`state`<br>`name`<br>`age`|
| Tipo del primer evento registrado |simulation_started |
| Tipo de evento más frecuente y cantidad | `villager_activity_changed`: 3343 |
| Recuento de todos los tipos de evento | `villager_activity_changed`: 3343<br>`villager_need_changed`: 683<br>`world_snapshot`: 469<br>`resource_changed`: 445<br>`social_interaction`: 307<br>`villager_drank`: 131<br>`villager_ate`: 102<br>`construction_abandoned`: 56<br>`hunt_completed`: 30<br>`construction_expired`: 24<br>`building_created`: 20<br>`villager_created`: 6<br>`simulation_started`: 1<br>`age_changed`: 1 |
| `run_id`, semilla y versión del esquema de la primera fila | `run_id`: 20261005_182846_584527806812332210_fc1f232ca2d448adb990e9c7a84fd93d<br>`semilla`: 584527806812332210<br>`versión del esquema`: 2 |
| Tick mínimo y tick máximo | `Tick mínimo`: 0<br>`Tick máximo`: 281640 |
| Resultado de las validaciones | VALIDACIÓN BÁSICA: OK|


### 1. ¿Qué te permite afirmar el recuento sobre tu partida y por qué el tipo más frecuente no tiene que ser el más importante?
- Que la simulación tiene 5.618 eventos y que lo más común es que cambien las actividades de los aldeanos. Eso indica que la partida está marcada por acciones repetitivas.
- El evento más frecuente no tiene por qué ser el más importante porque puede ser algo normal y muy repetido. Por ejemplo, las muertes de los aldeanos pueden ser muy importantes para entender la partida, aunque no aparezcan tantas veces.

### 2. ¿Por qué una celda vacía no significa necesariamente que el registro esté mal?
- Porque cada tipo de evento usa columnas distintas. Si un dato no aplica a ese evento, aparece vacío y eso no significa que haya un error.

### 3. ¿Qué sabes ahora del archivo y por qué se crean tan pocos aldeanos en tanto tiempo de partida?
- Sabemos que es un archivo válido de simulación, con 36 columnas y un patrón claro de actividad en la partida.
- La pregunta que tendría que estudiar después es por qué se crean tan pocos aldeanos en tanto tiempo de partida, y para responderla habría que mirar cómo evolucionan los recursos, las necesidades y las decisiones del juego.