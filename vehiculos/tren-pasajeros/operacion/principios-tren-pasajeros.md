# 🧪 Principios y operacion del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion certificada del operador
ferroviario ni los manuales del fabricante. Describe como se opera un tren en
simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Traccion**: los motores de traccion, alimentados por catenaria o por un grupo
  diesel-generador, entregan par a los ejes motrices.
- **Guia sobre rieles**: la rueda de pestana con perfil conico sigue el riel; el
  tren no cambia de rumbo por voluntad del maquinista, la via lo guia.
- **Adherencia**: el contacto acero-acero tiene bajo agarre, lo que limita la
  fuerza de traccion y de freno antes de patinar o bloquear.
- **Gran masa**: la enorme inercia hace que el tren acelere y frene despacio, con
  distancias de frenado de cientos de metros.
- **Control por senales**: la circulacion se ordena con senales de via y ATP; el
  maquinista respeta la senal, no la vista libre del camino.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Presion de freno, puertas, luces, ATP. |
| Puesta en servicio | Activar la cabina | Tension de linea, sentido de marcha, vigilante. |
| Arranque | Iniciar la marcha | Traccion progresiva, vigilar patinaje y senal. |
| Marcha | Circular con seguridad | Respetar limites, anticipar senales y andenes. |
| Frenado | Reducir con anticipacion | Combinar freno dinamico y neumatico, cuidar la adherencia. |
| Parada en anden | Detener en el punto exacto | Alinear puertas con el anden, freno suave. |
| Cierre | Dejar seguro | Puertas cerradas, freno aplicado, cabina apagada. |

## Frenado anticipado: idea general

1. Identificar la senal o el anden objetivo con mucha antelacion.
2. Comenzar a frenar mucho antes que un vehiculo de carretera.
3. Usar primero el freno dinamico o regenerativo para cuidar las zapatas.
4. Complementar con el freno neumatico segun la distancia restante.
5. Ajustar la fuerza a la adherencia disponible para no bloquear ruedas.

## Errores comunes que la simulacion puede ensenar a evitar

- Frenar tarde, olvidando la gran masa y las distancias largas.
- Aplicar demasiada traccion y provocar patinaje en riel humedo.
- Ignorar la senal o el limite del ATP.
- No alinear las puertas con el anden al detenerse.
- Descuidar la presion de la tuberia de freno antes de arrancar.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: aplicar traccion, frenar y respetar senales.
- **Nivel 2 (simplificado)**: agregar inercia, gran masa y distancia de frenado.
- **Nivel 3 (tecnico)**: sumar adherencia variable, freno dinamico, ATP y arenado.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tren-pasajeros.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tren-pasajeros.md)
