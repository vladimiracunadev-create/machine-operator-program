<!-- clase-meta
tipo_documento: clase
clase: 6
codigo: PORTAVIONES-06
curso: portaviones
titulo: "Principios y operación del portaviones"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: PORTAVIONES-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Portaviones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Portaviones."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧪 Principios y operación del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 🧪 Principios

Documento general, educativo e histórico. Trata solo principios físicos públicos
de flotación, estabilidad y logística de cubierta. No sustituye formación náutica
ni describe operación militar real, táctica o sistemas de armas.

## Principios de funcionamiento

- **Flotación**: el buque flota porque desplaza un peso de agua igual al suyo
  (principio de Arquímedes).
- **Propulsión**: las hélices empujan agua hacia atrás y, por reacción, el buque
  avanza (tercera ley de Newton).
- **Gobierno**: la pala del timón desvia el flujo de agua en popa; necesita
  velocidad para responder.
- **Inercia**: la enorme masa hace que toda maniobra sea muy lenta y anticipada.
- **Viento relativo**: navegar contra el viento aumenta el viento sobre la
  cubierta, un concepto físico útil para las operaciones aéreas.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Preparación | Revisión antes de zarpar | Máquina, gobierno, cubierta despejada. |
| Desatraque | Salir del muelle | Baja velocidad, remolcadores si aplica. |
| Salida de puerto | Navegar el canal | Práctico, señales, margen amplio. |
| Navegación | Travesía oceánica | Rumbo, guardias, vigilancia. |
| Cubierta activa | Coordinación de cubierta | Rumbo al viento, logística general. |
| Aproximación | Acercarse a puerto | Reducir velocidad con mucha antelación. |
| Cierre | Dejar segura la nave | Máquina parada, cubierta ordenada. |

## Cubierta al viento: idea general

1. La cubierta necesita **viento relativo** para las operaciones aéreas.
2. El buque **acelera y pone proa al viento** para aumentarlo.
3. La **velocidad del buque** se suma al viento natural.
4. La **estabilidad** debe cuidarse por el peso alto de la cubierta.
5. Todo se coordina de forma segura entre puente y cubierta.

## Errores comunes que la simulación puede enseñar a evitar

- Subestimar la enorme distancia de frenado por la inercia.
- Intentar gobernar con el buque casi parado.
- Ignorar el viento relativo en las operaciones de cubierta.
- Descuidar el reparto de peso y la estabilidad.
- Olvidar la profundidad bajo la quilla y varar.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: rumbo, velocidad y flotación básica.
- **Nivel 2 (simplificado)**: agregar inercia, viento relativo y distancia de
  frenado.
- **Nivel 3 (técnico)**: sumar estabilidad, escora, lastre y logística de
  cubierta a nivel general.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Principios de funcionamiento, Fases de operación, Cubierta al viento: idea general y Errores comunes que la simulación puede enseñar a evitar** a **resolver recuperación simulada de aeronaves con cubierta ocupada parcialmente sin agotar el margen operacional**?

### Explicación razonada

El principio rector puede resumirse así: integración de viento relativo, movimiento del buque y secuencia segura de cubierta. Esto explica por qué una misma orden produce resultados distintos cuando cambian velocidad, carga, configuración o entorno. Operar bien consiste en leer la tendencia antes de agotar el margen y tomar esta decisión: ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación.

```mermaid
flowchart LR
    C["condición inicial"] --> P["integración de viento relativo, movimiento del buque y secuencia segura de cubierta"]
    P --> R["riesgo: conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada"]
    R --> D["decisión: ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación"]
```

Esta clase se conecta con el resto del curso mediante **integración de viento relativo, movimiento del buque y secuencia segura de cubierta**. El hilo de
seguridad consiste en reconocer a tiempo **conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada** y poder justificar la decisión
**ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **planta propulsora → generación y catapulta → cubierta de vuelo → aeronave**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ships](https://www.history.navy.mil/browse-by-topic/ships.html) aporta historia pública de buques militares;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Datos:** reconoce condiciones, configuración y margen disponibles en **recuperación simulada de aeronaves con cubierta ocupada parcialmente**.
2. **Modelo:** aplica **integración de viento relativo, movimiento del buque y secuencia segura de cubierta** para predecir una tendencia antes de actuar.
3. **Riesgo:** explica mediante qué cadena de causas podría ocurrir **conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada**.
4. **Decisión:** ejecuta mentalmente **ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación** y define qué observación confirmaría que funcionó.

### Comprueba tu comprensión

1. ¿Qué variable del principio «integración de viento relativo, movimiento del buque y secuencia segura de cubierta» cambia primero en el caso?
2. ¿Cómo se propaga ese cambio hasta **aeronave**?
3. ¿Qué evidencia confirmaría que **ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación** conservó margen operacional?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Portaviones explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
- **Evidencia:** Resolución argumentada de un escenario operacional.
- **Criterio de aprobación:** Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-portaviones.md) · [➡️ Siguiente: Entornos de trabajo](entornos-portaviones.md)
