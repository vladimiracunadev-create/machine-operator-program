<!-- clase-meta
tipo_documento: clase
clase: 7
codigo: AVIONESPEQUE-07
curso: aviones-pequenos
titulo: "Entornos de trabajo del avión pequeño"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AVIONESPEQUE-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Aviones pequeños."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones pequeños."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🌍 Entornos de trabajo del avión pequeño

[🏠 Inicio](../../../README.md) · [🛩️ Curso: Aviones pequeños](../README.md) · 🌍 Entornos

Dónde opera un avión pequeño y cómo cambia el vuelo según el entorno. Cada entorno
implica reglas, riesgos y ajustes distintos, y en simulación se traduce en
escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🛩️ Avion pequeno))
    Aerodromo
      Pista y rodaje
      Circuito de trafico
      Torre o sin control
    Espacio aereo
      Controlado
      No controlado
      Zonas restringidas
    Meteorologia
      Viento y rafagas
      Nubes y visibilidad
      Hielo y turbulencia
    Geografia
      Montana
      Costa y mar
      Zonas aisladas
```

| Entorno | Características | Riesgos típicos | Ajuste de vuelo |
| --- | --- | --- | --- |
| Aeródromo | Pista, rodaje, circuito de tráfico. | Tráfico cercano, viento cruzado. | Circuito estandar, comunicación, velocidad estable. |
| Espacio aéreo controlado | Control por torre o radar. | Interferir con otros vuelos. | Seguir instrucciones, transponder activo. |
| Espacio aéreo no controlado | Sin control activo. | Ver y evitar por cuenta propia. | Vigilancia visual, comunicación en frecuencia común. |
| Meteorología adversa | Viento, nubes, poca visibilidad. | Pérdida de referencias, turbulencia. | Volar solo si las condiciones lo permiten. |
| Montaña | Terreno alto, corrientes. | Turbulencia, menor rendimiento. | Margen de altura, planificar rutas de escape. |
| Costa y zonas aisladas | Pocas ayudas en tierra. | Distancia a aeródromos, mar. | Buena planificación y combustible de reserva. |

---

## 🌦️ Factores del entorno

- **Viento**: el viento cruzado dificulta despegue y aterrizaje; la ráfaga sorprende.
- **Visibilidad**: nubes, niebla o lluvia reducen las referencias visuales.
- **Densidad del aire**: calor y altitud reducen sustentación y potencia.
- **Hielo y turbulencia**: afectan el control y el rendimiento del avión.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su tipo de espacio aéreo, su clima y su terreno.
Ver cómo se modela en el
[Clase 9: Diseño de simulación](../simulacion/diseno-simulador-avion-pequeno.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Entornos principales, Factores del entorno, Traducción a simulación y Guía de estudio aplicada** a **adaptar aproximación con viento cruzado y pista corta a tres condiciones ambientales distintas**?

### Explicación razonada

El entorno no es decoración: modifica las fuerzas, la percepción y el tiempo disponible. En el caso «aproximación con viento cruzado y pista corta», cambia el comportamiento de alas y mandos y aumenta la probabilidad de pérdida aerodinámica o salida de pista por velocidad y trayectoria inestables. La respuesta correcta empieza por reconocer qué variable cambió y después adaptar límites, ruta o misión.

Esta clase se conecta con el resto del curso mediante **balance entre sustentación, peso, empuje y resistencia dentro de una envolvente limitada**. El hilo de
seguridad consiste en reconocer a tiempo **pérdida aerodinámica o salida de pista por velocidad y trayectoria inestables** y poder justificar la decisión
**estabilizar aproximación y frustrar si no se cumplen criterios antes del umbral**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → hélice → flujo de aire → alas y mandos**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) aporta aerodinámica, sistemas y operación;
[Normativa aeronáutica](https://www.dgac.gob.cl/normativa/) se usa para marco aeronáutico chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Escenario base:** conserva la misión «aproximación con viento cruzado y pista corta» para poder comparar.
2. **Cambiar una condición:** modifica sucesivamente superficie o medio, visibilidad y perturbación externa.
3. **Recalcular margen:** explica cómo cada cambio afecta **alas y mandos** y acerca o aleja **pérdida aerodinámica o salida de pista por velocidad y trayectoria inestables**.
4. **Adaptar:** cambia límite, ruta, configuración o incluso cancela; no mantengas la misma respuesta por hábito.

### Comprueba tu comprensión

1. ¿Cómo cambiaría **alas y mandos** si empeora la perturbación externa?
2. ¿Qué condición ambiental acerca más el escenario a **pérdida aerodinámica o salida de pista por velocidad y trayectoria inestables**?
3. ¿Cuándo adaptarías la maniobra y cuándo la cancelarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Aviones pequeños a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-avion-pequeno.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-avion-pequeno.md)
