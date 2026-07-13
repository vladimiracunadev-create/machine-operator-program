# 🧪 Principios y operacion del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la habilitacion de maquinista ni el
manual del operador ferroviario. Describe como se opera un tren de carga en
simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Gran masa e inercia**: el tren pesa miles de toneladas; cuesta mucho ponerlo
  en movimiento y mucho mas detenerlo.
- **Adherencia limitada**: el contacto acero-acero da poco agarre; se compensa con
  arenado para arrancar y para frenar sin patinar.
- **Distancias de frenado largas**: por la masa y la baja adherencia, la detencion
  toma cientos de metros o mas; hay que anticipar mucho.
- **Fuerzas longitudinales**: al traccionar o frenar aparecen estirones (tension) y
  compresiones entre vagones; manejarlas mal puede romper enganches o descarrilar.
- **Ruta fija**: el tren no elige trayectoria; sigue la via y obedece la senalizacion.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision del tren | Enganches, mangueras de aire, freno, carga. |
| Carga de aire | Presurizar la tuberia de freno | Esperar presion en toda la composicion. |
| Arranque | Iniciar movimiento | Traccion progresiva, arenado, vigilar patinaje. |
| Marcha | Circular con seguridad | Respetar senales y limites, anticipar mucho. |
| Frenado | Reducir velocidad | Freno dinamico primero, luego neumatico, sin bloquear. |
| Detencion | Parar de forma segura | Freno aplicado, aire cargado, tren asegurado. |
| Cierre | Dejar el tren seguro | Freno de estacionamiento, sistemas apagados. |

## Gestion de fuerzas longitudinales

1. Aplicar la traccion de forma **progresiva** para no dar un estiron seco.
2. Evitar mezclar tramos en tension y en compresion a la vez en el tren.
3. Usar el freno dinamico para controlar la velocidad de forma suave.
4. Anticipar pendientes: la carga empuja en bajada y frena en subida.
5. Coordinar las locomotoras remotas para repartir el esfuerzo.

## Errores comunes que la simulacion puede ensenar a evitar

- Aplicar traccion de golpe y provocar patinaje o un estiron brusco.
- Frenar tarde por no anticipar la larga distancia de detencion.
- Ignorar las fuerzas longitudinales entre vagones en pendiente.
- Olvidar el arenado al arrancar con gran carga o con riel humedo.
- No atender el hombre muerto o vigilante durante la marcha.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: traccionar, frenar y respetar senales de la via.
- **Nivel 2 (simplificado)**: agregar inercia, adherencia limitada y distancia de frenado.
- **Nivel 3 (tecnico)**: sumar fuerzas longitudinales, distributed power y freno dinamico.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tren-carga.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tren-carga.md)
