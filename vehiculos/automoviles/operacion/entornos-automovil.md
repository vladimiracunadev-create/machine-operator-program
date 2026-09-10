<!-- clase-meta
tipo_documento: clase
clase: 7
codigo: AUTOMOVILES-07
curso: automoviles
titulo: "Entornos de trabajo del automóvil"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AUTOMOVILES-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Automóviles."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Automóviles."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🌍 Entornos de trabajo del automóvil

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automóviles](../README.md) · 🌍 Entornos

Dónde opera un automóvil y cómo cambia la conducción según el entorno. Cada
entorno implica reglas, riesgos y ajustes distintos, y en simulación se traduce
en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚗 Automovil))
    Ciudad
      Trafico denso
      Semaforos y cruces
      Peatones y ciclistas
    Carretera
      Curvas y pendientes
      Adelantamientos
      Cruces de fauna
    Autopista
      Alta velocidad
      Incorporaciones
      Distancia amplia
    Montana
      Pendientes largas
      Curvas cerradas
      Freno motor
    Lluvia y noche
      Baja visibilidad
      Menor adherencia
      Aquaplaning
```

| Entorno | Características | Riesgos típicos | Ajuste de conducción |
| --- | --- | --- | --- |
| Ciudad | Tráfico, cruces, peatones. | Puntos ciegos, ciclistas, puertas. | Baja velocidad, anticipación, frenada suave. |
| Carretera | Velocidad sostenida, curvas. | Adelantar, fatiga, animales. | Distancia amplia, curvas progresivas. |
| Autopista | Alta velocidad, incorporaciones. | Cambios de carril, cansancio. | Vigilar espejos, mantener carril. |
| Montaña | Pendientes y curvas cerradas. | Pérdida de frenos, desprendimientos. | Freno motor, marcha corta, prudencia. |
| Lluvia / noche | Baja visibilidad y agarre. | Aquaplaning, deslumbramiento. | Luces, menor velocidad, mayor distancia. |

---

## 🌦️ Factores del entorno

- **Clima**: lluvia, hielo o niebla reducen la adherencia y la visibilidad.
- **Superficie**: asfalto, adoquín, ripio o tierra cambian el agarre.
- **Tráfico**: más vehículos, más puntos ciegos y decisiones.
- **Luz**: de noche o con niebla, ver y ser visto es tan importante como frenar.
- **Pendiente**: subidas y bajadas cambian el frenado y el consumo.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su superficie, clima, tráfico y pendiente. Ver
como se modela en el
[Clase 9: Diseño de simulación](../simulacion/diseno-simulador-automovil.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Entornos principales, Factores del entorno, Traducción a simulación y Guía de estudio aplicada** a **adaptar frenada de emergencia en una calzada con adherencia desigual a tres condiciones ambientales distintas**?

### Explicación razonada

El entorno no es decoración: modifica las fuerzas, la percepción y el tiempo disponible. En el caso «frenada de emergencia en una calzada con adherencia desigual», cambia el comportamiento de ruedas motrices y aumenta la probabilidad de perder estabilidad por combinar exceso de velocidad, giro y frenado tardío. La respuesta correcta empieza por reconocer qué variable cambió y después adaptar límites, ruta o misión.

Esta clase se conecta con el resto del curso mediante **transferencia de carga y reparto del círculo de adherencia entre frenar, girar y acelerar**. El hilo de
seguridad consiste en reconocer a tiempo **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío** y poder justificar la decisión
**crear margen de detención y dosificar dirección y freno según la superficie**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → diferencial → ruedas motrices**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Manuales para conductores](https://www.conaset.cl/manuales/) se usa para formación vial y seguridad. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Escenario base:** conserva la misión «frenada de emergencia en una calzada con adherencia desigual» para poder comparar.
2. **Cambiar una condición:** modifica sucesivamente superficie o medio, visibilidad y perturbación externa.
3. **Recalcular margen:** explica cómo cada cambio afecta **ruedas motrices** y acerca o aleja **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío**.
4. **Adaptar:** cambia límite, ruta, configuración o incluso cancela; no mantengas la misma respuesta por hábito.

### Comprueba tu comprensión

1. ¿Cómo cambiaría **ruedas motrices** si empeora la perturbación externa?
2. ¿Qué condición ambiental acerca más el escenario a **perder estabilidad por combinar exceso de velocidad, giro y frenado tardío**?
3. ¿Cuándo adaptarías la maniobra y cuándo la cancelarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Automóviles a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [CL-CONASET](https://www.conaset.cl/manuales/): Manuales para conductores, CONASET. Uso: formación vial y seguridad.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-automovil.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-automovil.md)
