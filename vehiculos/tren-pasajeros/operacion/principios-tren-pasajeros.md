# 🧪 Principios y operación del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación certificada del operador
ferroviario ni los manuales del fabricante. Describe cómo se opera un tren en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Tracción**: los motores de tracción, alimentados por catenaria o por un grupo
  diesel-generador, entregan par a los ejes motrices.
- **Guía sobre rieles**: la rueda de pestaña con perfil cónico sigue el riel; el
  tren no cambia de rumbo por voluntad del maquinista, la vía lo guía.
- **Adherencia**: el contacto acero-acero tiene bajo agarre, lo que limita la
  fuerza de tracción y de freno antes de patinar o bloquear.
- **Gran masa**: la enorme inercia hace que el tren acelere y frene despacio, con
  distancias de frenado de cientos de metros.
- **Control por señales**: la circulación se ordena con señales de vía y ATP; el
  maquinista respeta la señal, no la vista libre del camino.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Presión de freno, puertas, luces, ATP. |
| Puesta en servicio | Activar la cabina | Tensión de línea, sentido de marcha, vigilante. |
| Arranque | Iniciar la marcha | Tracción progresiva, vigilar patinaje y señal. |
| Marcha | Circular con seguridad | Respetar límites, anticipar señales y andenes. |
| Frenado | Reducir con anticipación | Combinar freno dinámico y neumático, cuidar la adherencia. |
| Parada en andén | Detener en el punto exacto | Alinear puertas con el andén, freno suave. |
| Cierre | Dejar seguro | Puertas cerradas, freno aplicado, cabina apagada. |

## Frenado anticipado: idea general

1. Identificar la señal o el andén objetivo con mucha antelación.
2. Comenzar a frenar mucho antes que un vehículo de carretera.
3. Usar primero el freno dinámico o regenerativo para cuidar las zapatas.
4. Complementar con el freno neumático según la distancia restante.
5. Ajustar la fuerza a la adherencia disponible para no bloquear ruedas.

## Errores comunes que la simulación puede enseñar a evitar

- Frenar tarde, olvidando la gran masa y las distancias largas.
- Aplicar demasiada tracción y provocar patinaje en riel húmedo.
- Ignorar la señal o el límite del ATP.
- No alinear las puertas con el andén al detenerse.
- Descuidar la presión de la tubería de freno antes de arrancar.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: aplicar tracción, frenar y respetar señales.
- **Nivel 2 (simplificado)**: agregar inercia, gran masa y distancia de frenado.
- **Nivel 3 (técnico)**: sumar adherencia variable, freno dinámico, ATP y arenado.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tren-pasajeros.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tren-pasajeros.md)
