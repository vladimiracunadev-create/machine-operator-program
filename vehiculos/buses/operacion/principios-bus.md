---
tipo_documento: clase
clase: 6
codigo: BUSES-06
curso: buses
titulo: "Principios y operación del bus"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: BUSES-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Buses."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Buses."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧪 Principios y operación del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conducción profesional
certificado ni el manual del fabricante. Describe cómo se opera un bus en
simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Masa e inercia**: el bus es muy pesado; acelerar y detener requiere más
  distancia y tiempo. La anticipación es la primera herramienta de seguridad.
- **Frenado con pasajeros de pie**: una frenada brusca lanza a las personas hacia
  adelante. El frenado debe ser suave y progresivo, iniciado con antelación.
- **Radio de giro y barrido trasero**: el bus necesita mucho espacio para girar y
  su parte trasera describe un arco que invade el carril contiguo.
- **Puntos ciegos**: la gran carrocería genera amplias zonas sin visión directa;
  se cubren con espejos y cámaras, y aun así exigen precaución.
- **Aproximación a paradas**: acercarse al andén de forma paralela y suave para
  facilitar el ascenso y descenso seguro.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Neumáticos, luces, frenos, presión de aire, puertas. |
| Carga de aire | Motor en marcha | Esperar la presión mínima antes de mover el bus. |
| Puesta en marcha | Iniciar servicio | Soltar freno de estacionamiento, seleccionar D, salir suave. |
| Conducción | Circular con pasajeros | Mirar lejos, frenar con antelación, vigilar puntos ciegos. |
| Aproximación a parada | Llegar al andén | Reducir suave, alinear paralelo, detener y arrodillar si aplica. |
| Servicio en parada | Ascenso y descenso | Abrir puertas, marcha enclavada, cerrar sin atrapar. |
| Detención final | Terminar el servicio | Freno de estacionamiento, puertas, motor apagado. |

## Aproximación a parada: idea general

1. Anticipar la parada y **reducir la velocidad con tiempo**.
2. Señalizar e ir alineando el bus **paralelo al andén**.
3. Frenar de forma **progresiva** para no desestabilizar a los de pie.
4. Detener completamente y aplicar el freno; **arrodillar** si hay accesibilidad.
5. Abrir puertas solo con el bus detenido; cerrar verificando los sensores.
6. Reincorporarse al tráfico mirando espejos y puntos ciegos.

## Errores comunes que la simulación puede enseñar a evitar

- Frenar tarde y brusco, desestabilizando a los pasajeros de pie.
- Girar sin dejar espacio para el barrido trasero.
- Abrir o mantener puertas abiertas con el bus en movimiento.
- Ignorar la presión de aire y mover el bus antes de tiempo.
- Olvidar los puntos ciegos al cambiar de carril o al salir de la parada.
- Abusar del freno de servicio en descensos en vez de usar el retardador.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar suave, parar en paradas y respetar señales.
- **Nivel 2 (simplificado)**: agregar inercia de la masa, barrido trasero y aforo.
- **Nivel 3 (técnico)**: sumar presión de aire, retardador, enclavamiento de
  puertas y gestión de la fatiga en jornada.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Buses explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
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

[⬅️ Anterior: Mandos](../mandos/manual-mandos-bus.md) · [➡️ Siguiente: Entornos de trabajo](entornos-bus.md)
