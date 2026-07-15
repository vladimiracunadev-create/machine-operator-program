# 🧪 Principios y operación del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la habilitación de maquinista ni el
manual del operador ferroviario. Describe cómo se opera un tren de carga en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Gran masa e inercia**: el tren pesa miles de toneladas; cuesta mucho ponerlo
  en movimiento y mucho más detenerlo.
- **Adherencia limitada**: el contacto acero-acero da poco agarre; se compensa con
  arenado para arrancar y para frenar sin patinar.
- **Distancias de frenado largas**: por la masa y la baja adherencia, la detención
  toma cientos de metros o más; hay que anticipar mucho.
- **Fuerzas longitudinales**: al traccionar o frenar aparecen estirones (tensión) y
  compresiones entre vagones; manejarlas mal puede romper enganches o descarrilar.
- **Ruta fija**: el tren no elige trayectoria; sigue la vía y obedece la señalización.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión del tren | Enganches, mangueras de aire, freno, carga. |
| Carga de aire | Presurizar la tubería de freno | Esperar presión en toda la composición. |
| Arranque | Iniciar movimiento | Tracción progresiva, arenado, vigilar patinaje. |
| Marcha | Circular con seguridad | Respetar señales y límites, anticipar mucho. |
| Frenado | Reducir velocidad | Freno dinámico primero, luego neumático, sin bloquear. |
| Detención | Parar de forma segura | Freno aplicado, aire cargado, tren asegurado. |
| Cierre | Dejar el tren seguro | Freno de estacionamiento, sistemas apagados. |

## Gestión de fuerzas longitudinales

1. Aplicar la tracción de forma **progresiva** para no dar un estirón seco.
2. Evitar mezclar tramos en tensión y en compresión a la vez en el tren.
3. Usar el freno dinámico para controlar la velocidad de forma suave.
4. Anticipar pendientes: la carga empuja en bajada y frena en subida.
5. Coordinar las locomotoras remotas para repartir el esfuerzo.

## Errores comunes que la simulación puede enseñar a evitar

- Aplicar tracción de golpe y provocar patinaje o un estirón brusco.
- Frenar tarde por no anticipar la larga distancia de detención.
- Ignorar las fuerzas longitudinales entre vagones en pendiente.
- Olvidar el arenado al arrancar con gran carga o con riel húmedo.
- No atender el hombre muerto o vigilante durante la marcha.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: traccionar, frenar y respetar señales de la vía.
- **Nivel 2 (simplificado)**: agregar inercia, adherencia limitada y distancia de frenado.
- **Nivel 3 (técnico)**: sumar fuerzas longitudinales, distributed power y freno dinámico.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tren-carga.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tren-carga.md)
