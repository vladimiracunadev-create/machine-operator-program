<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: ESTACIONESPA-02
curso: estacion-espacial
titulo: "Características funcionales de la estación espacial"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: ESTACIONESPA-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Estación espacial (ISS)."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Estación espacial (ISS)."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales de la estación espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estación espacial (ISS)](../README.md) · 📋 Características

Que es una estación espacial, cuales son sus partes y para que sirve. Esta clase
da el contexto antes de abrir los sistemas de la estación (Clase 4).

---

## 🧭 Definición

Una estación espacial es un habitat permanente en órbita baja donde una
tripulación vive y trabaja durante largos periodos. No despega ni aterriza como
una nave: se ensambla en órbita a partir de **módulos** y se mantiene cayendo de
forma continua alrededor de la Tierra. Su valor está en ser un laboratorio de
microgravedad ocupado sin interrupción.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Habitat permanente | Alberga tripulación de forma continua. |
| Estructura modular | Se compone de módulos unidos en órbita. |
| Microgravedad | Todo flota en caída libre continua. |
| Soporte vital de ciclo cerrado | Recicla aire y agua para durar más. |
| Energía solar | Grandes paneles alimentan la estación. |
| Puertos de acoplamiento | Recibe naves de carga y de tripulación. |

---

## 🗂️ Partes de la estación

```mermaid
flowchart TD
    Estacion[🛰️ Estación espacial] --> Presurizado[Zona presurizada]
    Estacion --> Externo[Estructura externa]
    Presurizado --> Laboratorio[Módulos de laboratorio]
    Presurizado --> Habitat[Módulos habitat]
    Presurizado --> Nodo[Nodos de unión]
    Externo --> Paneles[Paneles solares]
    Externo --> Radiadores[Radiadores térmicos]
    Externo --> Brazo[Brazo robotico]
    Presurizado --> Puertos[Puertos de acoplamiento]
```

| Parte | Uso típico | Rasgo destacado |
| --- | --- | --- |
| Módulo de laboratorio | Experimentos en microgravedad | Interior presurizado. |
| Módulo habitat | Vivir, dormir y comer | Zona de descanso e higiene. |
| Nodo de unión | Conectar módulos | Distribuye el paso interno. |
| Paneles solares | Generar energía | Se orientan hacia el Sol. |
| Radiadores | Expulsar el calor sobrante | Regulan la temperatura. |
| Puerto de acoplamiento | Recibir naves | Une carga y tripulación. |

---

## 🎯 Para qué se usa

- Investigación científica en microgravedad (biología, materiales, medicina).
- Estudiar como afecta el espacio a la salud humana en misiones largas.
- Observar la Tierra y el espacio desde una plataforma estable.
- Probar tecnología para futuras misiones lejanas.
- Educación, cooperación internacional y simulación de la vida en órbita.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Partes de la estación y Para qué se usa** a **elegir una configuración adecuada para pérdida parcial de generación durante una actividad planificada**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Estación espacial (ISS), la relación entre paneles solares, distribución eléctrica, soporte vital y módulos y tripulación determina capacidad, respuesta y límites. Por eso «segmento presurizado frente a estructura externa» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «degradación de soporte vital o energía por priorización tardía».

Esta clase se conecta con el resto del curso mediante **equilibrio continuo de energía, atmósfera, calor y orientación orbital**. El hilo de
seguridad consiste en reconocer a tiempo **degradación de soporte vital o energía por priorización tardía** y poder justificar la decisión
**aislar la falla y priorizar cargas esenciales antes de recuperar la misión**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **paneles solares → distribución eléctrica → soporte vital → módulos y tripulación**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [International Space Station](https://www.nasa.gov/reference/international-space-station/) aporta módulos, órbita y soporte vital;
[Space Law Treaties and Principles](https://www.unoosa.org/oosa/SpaceLaw/treaties.html) se usa para derecho espacial internacional. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «pérdida parcial de generación durante una actividad planificada» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **segmento presurizado frente a estructura externa** usando esos requisitos y la cadena **paneles solares → distribución eléctrica → soporte vital → módulos y tripulación**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **degradación de soporte vital o energía por priorización tardía**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **módulos y tripulación** condiciona primero el caso «pérdida parcial de generación durante una actividad planificada»?
2. ¿Qué requisito descartaría una de las alternativas **segmento presurizado frente a estructura externa**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Estación espacial (ISS) mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-ISS](https://www.nasa.gov/reference/international-space-station/): International Space Station, NASA. Uso: módulos, órbita y soporte vital.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-estacion-espacial.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-estacion-espacial.md)
