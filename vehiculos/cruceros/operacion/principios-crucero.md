<!-- clase-meta
tipo_documento: clase
clase: 6
codigo: CRUCEROS-06
curso: cruceros
titulo: "Principios y operación del crucero"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: CRUCEROS-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Cruceros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cruceros."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧪 Principios y operación del crucero

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación náutica certificada
(STCW) ni los manuales del fabricante. Describe cómo se opera un crucero en
simulación y que principios físicos conviene representar, con el pasaje como eje.

## Principios de funcionamiento

- **Flotación**: el buque flota porque desplaza un peso de agua igual al suyo
  (principio de Arquímedes). El empuje vertical sostiene el casco.
- **Propulsión**: los pods o la hélice empujan agua hacia atrás y, por reacción,
  el buque avanza (tercera ley de Newton).
- **Gobierno**: se cambia el rumbo orientando el empuje de los pods o desviando el
  agua con el timón; el pod mantiene autoridad a baja velocidad.
- **Inercia**: por su gran masa, el crucero tarda mucho en acelerar, frenar o
  girar; toda maniobra se anticipa con minutos y millas de margen.
- **Estabilidad**: el reparto de peso, la carga y el lastre determinan que el
  buque vuelva a la vertical; los estabilizadores mejoran el confort del pasaje.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Preparación | Revisión antes de zarpar | Máquina, gobierno, seguridad, combustible. |
| Embarque | Suben los pasajeros | Conteo, control de acceso, briefing de seguridad. |
| Ejercicio de muster | Instrucción de seguridad | Puntos de reunión, uso de chalecos, rutas. |
| Desatraque | Salir del muelle | Thruster, cabos, remolcadores si aplica. |
| Maniobra de puerto | Navegar el canal | Baja velocidad, práctico, señales. |
| Navegación | Travesía entre escalas | Rumbo, guardias, vigilancia radar, confort. |
| Aproximación | Acercarse al puerto destino | Reducir velocidad con anticipación. |
| Atraque | Amarrar en muelle | Maniobra fina, pods, thruster, cabos. |
| Desembarque | Bajan los pasajeros | Control de acceso, seguridad en pasarela. |

## Maniobras: idea general

1. Anticipar toda maniobra por la **inercia** del buque de pasaje.
2. Reducir la velocidad **mucho antes** de la aproximación.
3. Aprovechar los **pods** y los **thrusters** en espacios estrechos.
4. Respetar las **reglas de rumbo** COLREG frente a otros buques.
5. Vigilar calado y **profundidad** para no varar, y el **viento** por la gran obra muerta.

## El pasaje como eje de la operación

- El **ejercicio de muster** debe realizarse antes o poco después de zarpar.
- Cada tripulante tiene un **rol de seguridad** para guiar y contar pasajeros.
- La **evacuación** ordenada a botes y balsas es la maniobra crítica del buque.
- El **confort** (balance, climatización) forma parte de la operación normal.

## Errores comunes que la simulación puede enseñar a evitar

- Subestimar la distancia de frenado por la inercia.
- Ignorar el efecto del viento sobre la alta obra muerta al maniobrar.
- Descuidar el conteo del pasaje en el ejercicio de muster.
- No respetar la prioridad de paso según COLREG.
- Mala estiba o lastre que compromete la estabilidad.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: rumbo, velocidad y respetar señales básicas.
- **Nivel 2 (simplificado)**: agregar inercia, distancia de frenado y viento.
- **Nivel 3 (técnico)**: sumar estabilidad, gobierno por pods, procedimiento de
  muster y maniobra de puerto con thrusters y remolcadores.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Principios de funcionamiento, Fases de operación, Maniobras: idea general y El pasaje como eje de la operación** a **resolver atraque con viento sobre una superestructura de gran superficie sin agotar el margen operacional**?

### Explicación razonada

El principio rector puede resumirse así: maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas. Esto explica por qué una misma orden produce resultados distintos cuando cambian velocidad, carga, configuración o entorno. Operar bien consiste en leer la tendencia antes de agotar el margen y tomar esta decisión: coordinar propulsión, remolcadores y límites de viento antes de aproximar.

```mermaid
flowchart LR
    C["condición inicial"] --> P["maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas"]
    P --> R["riesgo: contacto con muelle o pérdida de separación por subestimar abatimiento"]
    R --> D["decisión: coordinar propulsión, remolcadores y límites de viento antes de aproximar"]
```

Esta clase se conecta con el resto del curso mediante **maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas**. El hilo de
seguridad consiste en reconocer a tiempo **contacto con muelle o pérdida de separación por subestimar abatimiento** y poder justificar la decisión
**coordinar propulsión, remolcadores y límites de viento antes de aproximar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **generación eléctrica → propulsión → hélices o pods → casco y gobierno**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) aporta navegación, SOLAS, COLREG y STCW;
[Collision Regulations](https://www.imo.org/en/about/conventions/pages/colreg.aspx) se usa para prevención de abordajes. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Datos:** reconoce condiciones, configuración y margen disponibles en **atraque con viento sobre una superestructura de gran superficie**.
2. **Modelo:** aplica **maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas** para predecir una tendencia antes de actuar.
3. **Riesgo:** explica mediante qué cadena de causas podría ocurrir **contacto con muelle o pérdida de separación por subestimar abatimiento**.
4. **Decisión:** ejecuta mentalmente **coordinar propulsión, remolcadores y límites de viento antes de aproximar** y define qué observación confirmaría que funcionó.

### Comprueba tu comprensión

1. ¿Qué variable del principio «maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas» cambia primero en el caso?
2. ¿Cómo se propaga ese cambio hasta **casco y gobierno**?
3. ¿Qué evidencia confirmaría que **coordinar propulsión, remolcadores y límites de viento antes de aproximar** conservó margen operacional?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Cruceros explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
- **Evidencia:** Resolución argumentada de un escenario operacional.
- **Criterio de aprobación:** Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-crucero.md) · [➡️ Siguiente: Entornos de trabajo](entornos-crucero.md)
