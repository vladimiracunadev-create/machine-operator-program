<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: SUBMARINOS-02
curso: submarinos
titulo: "Características funcionales del submarino"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: SUBMARINOS-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Submarinos."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Submarinos."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 📋 Características

Que es un submarino, que tipos históricos existieron y cual fue su papel general.
Contexto público antes de abrir la física de inmersión (Clase 4). No se
documentan táctica ni sistemas de armas.

---

## 🧭 Definición

Un submarino es un buque capaz de navegar en superficie y bajo el agua
controlando su flotabilidad. En superficie flota como cualquier buque; para
sumergirse inunda tanques de lastre y aumenta su peso hasta igualar el empuje.
Su rasgo distintivo es la **flotabilidad variable** y el casco resistente a la
presión.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Flotabilidad variable | Se sumerge o emerge ajustando el lastre. |
| Casco resistente | Soporta la presión del agua a profundidad. |
| Control de profundidad | Usa lastre y planos de inmersión. |
| Soporte vital | Renueva el aire y sostiene a la tripulación. |
| Autonomía | Puede permanecer sumergido largos periodos. |
| Sigilo | Disenado para navegar de forma discreta. |

---

## 🗂️ Tipos históricos

```mermaid
flowchart TD
    Sub[🌊 Submarino] --> Experimental[Experimental]
    Sub --> Convencional[Diesel-electrico]
    Sub --> Nuclear[Propulsión nuclear]
    Sub --> Civil[Investigación civil]
    Experimental --> Manual[Lastre y hélice manual]
    Convencional --> Bateria[Motor y batería]
    Nuclear --> Autonomia[Gran autonomía]
    Civil --> Exploracion[Exploración oceánica]
```

| Tipo | Época | Rasgo destacado |
| --- | --- | --- |
| Experimental | Histórico | Lastre y propulsión manual. |
| Diesel-eléctrico | Clásico | Motor en superficie, batería sumergido. |
| Propulsión nuclear | Moderno | Gran autonomía sumergida. |
| Investigación civil | Actual | Exploración científica de profundidades. |

---

## 🎯 Para qué se usó

- Navegación sumergida (contexto histórico general).
- Investigación científica de las profundidades (sumergibles civiles).
- Avances en ingeniería de presión y soporte vital.
- En este repositorio: base para simulación educativa de flotabilidad e inmersión.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Tipos históricos y Para qué se usó** a **elegir una configuración adecuada para cambio de profundidad manteniendo rumbo y discreción**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Submarinos, la relación entre fuente de energía, motor, hélice o propulsor y planos y tanques de lastre determina capacidad, respuesta y límites. Por eso «submarino diésel-eléctrico frente a nuclear» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «exceso de profundidad, pérdida de control o colisión por conciencia situacional limitada».

Esta clase se conecta con el resto del curso mediante **equilibrio entre flotabilidad, peso, profundidad, trimado y control hidrodinámico**. El hilo de
seguridad consiste en reconocer a tiempo **exceso de profundidad, pérdida de control o colisión por conciencia situacional limitada** y poder justificar la decisión
**coordinar velocidad, planos y lastre observando tendencia, no solo profundidad instantánea**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **fuente de energía → motor → hélice o propulsor → planos y tanques de lastre**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ships](https://www.history.navy.mil/browse-by-topic/ships.html) aporta historia pública de buques militares;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «cambio de profundidad manteniendo rumbo y discreción» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **submarino diésel-eléctrico frente a nuclear** usando esos requisitos y la cadena **fuente de energía → motor → hélice o propulsor → planos y tanques de lastre**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **exceso de profundidad, pérdida de control o colisión por conciencia situacional limitada**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **planos y tanques de lastre** condiciona primero el caso «cambio de profundidad manteniendo rumbo y discreción»?
2. ¿Qué requisito descartaría una de las alternativas **submarino diésel-eléctrico frente a nuclear**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Submarinos mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-submarino.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-submarino.md)
