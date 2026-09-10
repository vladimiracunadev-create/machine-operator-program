<!-- clase-meta
tipo_documento: clase
clase: 7
codigo: NAUTILUS-07
curso: nautilus
titulo: "Entornos del Nautilus"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: NAUTILUS-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Nautilus."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Nautilus."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🌍 Entornos del Nautilus

[🏠 Inicio](../../../README.md) · [🐙 Curso: Nautilus](../README.md) · 🌍 Entornos

> ⚖️ Material educativo original; el Nautilus de Julio Verne (1870) es de dominio público; otros derechos pertenecen a sus titulares.

Dónde opera el Nautilus y cómo cambia la física según la profundidad. Cada
franja del océano tiene su presión, su luz y sus riesgos, y en simulación se
traduce en escenarios distintos.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((Nautilus))
    Superficie
      Aire renovable
      Presion baja
      Oleaje y clima
    Aguas medias
      Poca luz
      Presion creciente
      Corrientes
    Gran profundidad
      Oscuridad total
      Presion extrema
      Frio intenso
    Fondo oceanico
      Relieve submarino
      Fauna abisal
      Riesgo de choque
```

| Entorno | Características | Riesgos típicos | Ajuste de operación |
| --- | --- | --- | --- |
| Superficie | Aire renovable, presión baja. | Oleaje, clima, ser visto. | Ventilar, cargar energía, navegar suave. |
| Aguas medias | Poca luz, presión moderada. | Corrientes, desorientación. | Flotabilidad neutra, rumbo estable. |
| Gran profundidad | Oscuridad y presión muy alta. | Aplastamiento del casco. | No pasar la profundidad límite. |
| Fondo oceánico | Relieve, fauna, sedimento. | Choque, quedar atrapado. | Velocidad baja, iluminación, cautela. |

---

## 🌡️ Factores del entorno

- **Presión**: aumenta de forma continua con la profundidad; es el factor que
  marca hasta donde puede bajar la nave.
- **Luz**: se pierde rápido bajo la superficie; a partir de cierta profundidad
  reina la oscuridad total y hace falta iluminación propia.
- **Temperatura**: el agua profunda es muy fría, lo que afecta a equipos y
  tripulación.
- **Corrientes**: empujan la nave y complican mantener rumbo y posición.
- **Relieve del fondo**: montañas, fosas y cananos submarinos que hay que
  esquivar cerca del lecho.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su presión, su luz y sus corrientes. La
profundidad deja de ser un número y se vuelve el eje del desafío: cuanto más
abajo, más cerca del límite del casco y más dependencia de la energía y el aire.
Ver cómo se modela en el
[Clase 9: Diseño de simulación](../simulacion/diseno-simulador-nautilus.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Entornos principales, Factores del entorno, Traducción a simulación y Guía de estudio aplicada** a **adaptar inmersión narrativa cerca de relieve submarino a tres condiciones ambientales distintas**?

### Explicación razonada

El entorno no es decoración: modifica las fuerzas, la percepción y el tiempo disponible. En el caso «inmersión narrativa cerca de relieve submarino», cambia el comportamiento de casco y timones y aumenta la probabilidad de colisión o exceso de profundidad al tomar la descripción literaria como procedimiento real. La respuesta correcta empieza por reconocer qué variable cambió y después adaptar límites, ruta o misión.

Esta clase se conecta con el resto del curso mediante **lectura doble: tecnología imaginada por Verne y principios reales de flotabilidad y presión**. El hilo de
seguridad consiste en reconocer a tiempo **colisión o exceso de profundidad al tomar la descripción literaria como procedimiento real** y poder justificar la decisión
**citar el canon y contrastar cada maniobra con física y navegación reales**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **energía descrita en la obra → motor → hélice → casco y timones**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Twenty Thousand Leagues under the Sea](https://www.gutenberg.org/ebooks/164) aporta obra primaria en dominio público;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Escenario base:** conserva la misión «inmersión narrativa cerca de relieve submarino» para poder comparar.
2. **Cambiar una condición:** modifica sucesivamente superficie o medio, visibilidad y perturbación externa.
3. **Recalcular margen:** explica cómo cada cambio afecta **casco y timones** y acerca o aleja **colisión o exceso de profundidad al tomar la descripción literaria como procedimiento real**.
4. **Adaptar:** cambia límite, ruta, configuración o incluso cancela; no mantengas la misma respuesta por hábito.

### Comprueba tu comprensión

1. ¿Cómo cambiaría **casco y timones** si empeora la perturbación externa?
2. ¿Qué condición ambiental acerca más el escenario a **colisión o exceso de profundidad al tomar la descripción literaria como procedimiento real**?
3. ¿Cuándo adaptarías la maniobra y cuándo la cancelarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Nautilus a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [GUTENBERG-20000](https://www.gutenberg.org/ebooks/164): Twenty Thousand Leagues under the Sea, Project Gutenberg. Uso: obra primaria en dominio público.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-nautilus.md) · [➡️ Siguiente: Reglas del universo](../reglamentos/reglas-universo-nautilus.md)
