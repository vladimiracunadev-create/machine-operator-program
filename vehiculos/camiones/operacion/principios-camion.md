---
tipo_documento: clase
clase: 6
codigo: CAMIONES-06
curso: camiones
titulo: "Principios y operación del camión"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: CAMIONES-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Camiones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Camiones."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧪 Principios y operación del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conducción profesional
ni el manual del fabricante. Describe cómo se opera un camión en simulación y que
principios físicos conviene representar.

## Principios de funcionamiento

- **Propulsión**: el motor diesel entrega mucho par a bajas vueltas, que la caja
  multimarcha adapta a la carga y a la pendiente.
- **Masa e inercia**: un camión cargado tiene enorme inercia; tarda mucho más en
  acelerar y en detenerse que un automóvil.
- **Frenado por energía**: la energía cinética crece con la masa y con el
  cuadrado de la velocidad, por eso se combinan frenos de servicio, de motor y
  retarder para no recalentar.
- **Reparto de peso**: la carga debe repartirse por eje; un mal reparto reduce
  agarre delantero, alarga el frenado o sobrecarga un eje.
- **Estabilidad**: un centro de gravedad alto (cisterna, carga apilada) aumenta
  el riesgo de vuelco en curva; la velocidad de paso debe reducirse.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión del vehículo y la carga | Neumáticos, luces, presión de aire, amarre de carga. |
| Carga de aire | Subir la presión del sistema | Esperar el rango normal antes de mover. |
| Arranque | Iniciar movimiento | Soltar estacionamiento, marcha corta, soltar embrague suave. |
| Conducción | Circular con seguridad | Anticipar, mantener gran distancia, vigilar puntos ciegos. |
| Pendientes | Subir y bajar cargado | Marcha adecuada, freno de motor y retarder en bajada. |
| Maniobras | Girar y estacionar | Considerar barrido trasero y espacio del semirremolque. |
| Detención | Parar de forma segura | Frenar progresivo, aplicar estacionamiento, calzar si procede. |

## Pendientes: idea general

1. Elegir la marcha **antes** de la bajada, no durante.
2. Usar freno de motor y retarder para mantener la velocidad.
3. Reservar el freno de servicio para ajustes puntuales, no continuos.
4. En subida, no dejar caer el régimen: reducir a tiempo para no perder impulso.
5. Vigilar la temperatura del motor y de los frenos.

## Errores comunes que la simulación puede enseñar a evitar

- Bajar una pendiente larga usando solo el freno de servicio (riesgo de fading).
- Subestimar la distancia de frenado con el camión cargado.
- Girar demasiado cerca de un obstáculo e ignorar el barrido trasero.
- Circular con presión de aire insuficiente.
- Cargar mal el vehículo y superar el límite de un eje.
- Entrar a una curva con carga alta a demasiada velocidad.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y respetar señales con carga.
- **Nivel 2 (simplificado)**: agregar inercia por masa, distancia de frenado y
  distribución básica de la carga.
- **Nivel 3 (técnico)**: sumar caja multimarcha, freno de motor y retarder,
  presión de aire, reparto por eje y articulación del semirremolque.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md)
para el detalle de cada nivel.

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Camiones explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
- **Evidencia:** Resolución argumentada de un escenario operacional.
- **Criterio de aprobación:** Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-camion.md) · [➡️ Siguiente: Entornos de trabajo](entornos-camion.md)
