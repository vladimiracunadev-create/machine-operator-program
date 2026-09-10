<!-- clase-meta
tipo_documento: clase
clase: 6
codigo: AVIONESCOMBA-06
curso: aviones-combate
titulo: "Principios y operación del avión de combate"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: AVIONESCOMBA-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Aviones de combate."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones de combate."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧪 Principios y operación del avión de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🧪 Principios

Documento general, público y divulgativo. No sustituye entrenamiento real ni
manuales oficiales, y **no** describe táctica, doctrina ni sistemas de armas. Solo
trata la física del vuelo a reacción y fases generales de vuelo.

## Principios de funcionamiento

- **Sustentación**: las alas generan sostén al moverse por el aire, como en todo avión.
- **Empuje a reacción**: el motor expulsa gases hacia atrás e impulsa el avión adelante.
- **Vuelo a alta velocidad**: cerca del sonido cambian la resistencia y el control.
- **Cargas G**: en las maniobras la aceleración multiplica el peso aparente.
- **Vuelo en tres ejes**: cabeceo, alabeo y guiñada, asistidos por mandos eléctricos.

## Cargas G a nivel conceptual

```mermaid
flowchart LR
    Maniobra[Maniobra cerrada] --> G[Mayor carga G]
    G --> Estructura[Esfuerzo en la estructura]
    G --> Piloto[Esfuerzo físico en el piloto]
    Estructura --> Limite[Límite estructural]
    Piloto --> Limite2[Límite fisiológico]
```

Una maniobra cerrada aumenta la carga G: la estructura y el propio piloto sienten
un peso aparente varias veces mayor. Por eso el avión se disena reforzado y el
piloto usa equipo especial. En simulación, esto se representa como un límite.

## Fases de operación (marco general)

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prevuelo | Inspección y checklist | Estado de la aeronave y sistemas generales. |
| Rodaje | Mover el avión en tierra | Control con pedales y frenos. |
| Despegue | Acelerar y elevarse | Empuje alto, velocidad de rotación, ascenso. |
| Ascenso | Ganar altitud | Gestión de empuje y energía. |
| Crucero | Vuelo sostenido | Navegar y mantener parámetros estables. |
| Maniobra | Cambios de actitud | Controlar cargas G y no perder energía. |
| Descenso | Bajar de altitud | Reducir empuje y controlar velocidad. |
| Aterrizaje | Tomar tierra | Configurar, aproximar y frenar con control. |

## Energía y maniobra: idea general

1. La velocidad y la altitud son "energía" disponible para maniobrar.
2. Una maniobra cerrada gasta energía y sube la carga G.
3. Recuperar energía exige empuje o cambiar altitud por velocidad.
4. Volar suave conserva energía y control.
5. Respetar los límites estructurales y fisiológicos es prioritario.

## Errores comunes que la simulación puede enseñar a evitar

- Exceder los límites de carga G en una maniobra.
- Perder energía y quedar lento a baja altura.
- Ignorar la velocidad cercana al sonido y sus efectos.
- No completar el checklist de cada fase.
- Descuidar el combustible en vuelo prolongado.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, volar, virar y aterrizar un reactor.
- **Nivel 2 (simplificado)**: agregar cargas G, energía y efectos de alta velocidad.
- **Nivel 3 (técnico)**: sumar gestión de empuje, límites estructurales y Mach.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Principios de funcionamiento, Cargas G a nivel conceptual, Fases de operación (marco general) y Energía y maniobra: idea general** a **resolver maniobra simulada de alta carga con combustible limitado sin agotar el margen operacional**?

### Explicación razonada

El principio rector puede resumirse así: intercambio entre energía cinética, altura, carga estructural y capacidad de giro. Esto explica por qué una misma orden produce resultados distintos cuando cambian velocidad, carga, configuración o entorno. Operar bien consiste en leer la tendencia antes de agotar el margen y tomar esta decisión: preservar margen de energía y carga antes de ordenar una maniobra.

```mermaid
flowchart LR
    C["condición inicial"] --> P["intercambio entre energía cinética, altura, carga estructural y capacidad de giro"]
    P --> R["riesgo: exceder envolvente, perder energía o conciencia situacional"]
    R --> D["decisión: preservar margen de energía y carga antes de ordenar una maniobra"]
```

Esta clase se conecta con el resto del curso mediante **intercambio entre energía cinética, altura, carga estructural y capacidad de giro**. El hilo de
seguridad consiste en reconocer a tiempo **exceder envolvente, perder energía o conciencia situacional** y poder justificar la decisión
**preservar margen de energía y carga antes de ordenar una maniobra**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → tobera → flujo → superficies y control de vuelo**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) aporta aerodinámica, sistemas y operación;
[Beginner's Guide to Aeronautics](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/) se usa para contraste con física y vuelo reales. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Datos:** reconoce condiciones, configuración y margen disponibles en **maniobra simulada de alta carga con combustible limitado**.
2. **Modelo:** aplica **intercambio entre energía cinética, altura, carga estructural y capacidad de giro** para predecir una tendencia antes de actuar.
3. **Riesgo:** explica mediante qué cadena de causas podría ocurrir **exceder envolvente, perder energía o conciencia situacional**.
4. **Decisión:** ejecuta mentalmente **preservar margen de energía y carga antes de ordenar una maniobra** y define qué observación confirmaría que funcionó.

### Comprueba tu comprensión

1. ¿Qué variable del principio «intercambio entre energía cinética, altura, carga estructural y capacidad de giro» cambia primero en el caso?
2. ¿Cómo se propaga ese cambio hasta **superficies y control de vuelo**?
3. ¿Qué evidencia confirmaría que **preservar margen de energía y carga antes de ordenar una maniobra** conservó margen operacional?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Aviones de combate explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
- **Evidencia:** Resolución argumentada de un escenario operacional.
- **Criterio de aprobación:** Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-avion-combate.md) · [➡️ Siguiente: Entornos de trabajo](entornos-avion-combate.md)
