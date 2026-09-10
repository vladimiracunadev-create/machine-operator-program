<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: GRUAS-02
curso: gruas
titulo: "Características funcionales de la grúa"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: GRUAS-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Grúas."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúas."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales de la grúa

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Grúas](../README.md) · 📋 Características

Que es una grúa, que tipos existen y para que sirve cada uno. Esta clase da el
contexto antes de abrir la mecánica y el izaje (Clase 4).

---

## 🧭 Definición

Una grúa es una máquina de izaje que eleva, gira y traslada cargas mediante una
pluma y un cabrestante. A diferencia de otros vehículos, su desafío no es
desplazarse, sino levantar pesos elevados manteniendo la estabilidad: toda la
operación gira en torno a no superar el momento de vuelco.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Capacidad de izaje | Peso máximo que puede levantar, siempre según radio y ángulo. |
| Radio de trabajo | Distancia horizontal del eje de giro al gancho; a mayor radio, menor capacidad. |
| Momento de carga | Producto de peso por radio; es el parámetro crítico de estabilidad. |
| Estabilizadores | Amplian la base de apoyo para resistir el vuelco. |
| Contrapeso | Masa que equilibra el momento de la carga. |
| Alcance y altura | Longitud de pluma que define hasta dónde y cuán alto se iza. |
| Giro (swing) | Rotación de la superestructura para posicionar la carga. |

---

## 🗂️ Tipos de grúa

```mermaid
flowchart TD
    Grua[🏗️ Grúa] --> Movil[Móviles]
    Grua --> Fija[Fijas]
    Grua --> Industrial[Industriales]
    Movil --> Camion[Sobre camión]
    Movil --> RT[Todo terreno RT]
    Movil --> Orugas[Sobre orugas]
    Movil --> Articulada[Articulada / pluma articulada]
    Fija --> Torre[Torre]
    Industrial --> Puente[Puente grúa]
```

| Tipo | Uso típico | Rasgo destacado |
| --- | --- | --- |
| Móvil sobre camión | Montaje itinerante en ciudad y obra | Circula por carretera, opera con estabilizadores. |
| Todo terreno (RT) | Terreno irregular y compacto de obra | Tracción total, chasis único, muy maniobrable. |
| Sobre orugas | Grandes obras de larga duración | Iza sin estabilizadores, se mueve con carga. |
| Torre | Edificación en altura | Fija, gran altura y alcance, pluma horizontal. |
| Articulada / pluma articulada | Carga y descarga sobre camión | Pluma plegable de brazos, compacta al replegar. |
| Puente grúa | Naves y talleres industriales | Recorre un carril elevado, izaje vertical preciso. |

---

## 🎯 Para qué se usa

- Montaje de estructuras y prefabricados en construcción.
- Carga y descarga de contenedores en puertos.
- Instalación de equipos pesados en industria y energía.
- Rescate y remoción de vehículos o escombros.
- Movimiento de materiales dentro de naves industriales.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Tipos de grúa y Para qué se usa** a **elegir una configuración adecuada para izaje de una carga conocida cuyo destino exige aumentar el radio**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Grúas, la relación entre motor, bombas hidráulicas, cabrestante y pluma y gancho y carga determina capacidad, respuesta y límites. Por eso «grúa móvil telescópica frente a grúa de celosía» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «exceder la tabla de carga o perder estabilidad del apoyo».

Esta clase se conecta con el resto del curso mediante **momento de vuelco igual a carga por radio, condicionado por apoyos y configuración**. El hilo de
seguridad consiste en reconocer a tiempo **exceder la tabla de carga o perder estabilidad del apoyo** y poder justificar la decisión
**confirmar peso, radio, configuración y suelo antes de levantar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → bombas hidráulicas → cabrestante y pluma → gancho y carga**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Crane, Derrick and Hoist Safety](https://www.osha.gov/cranes-derricks) aporta izaje, riesgos y controles;
[Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) se usa para marco legal chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «izaje de una carga conocida cuyo destino exige aumentar el radio» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **grúa móvil telescópica frente a grúa de celosía** usando esos requisitos y la cadena **motor → bombas hidráulicas → cabrestante y pluma → gancho y carga**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **exceder la tabla de carga o perder estabilidad del apoyo**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **gancho y carga** condiciona primero el caso «izaje de una carga conocida cuyo destino exige aumentar el radio»?
2. ¿Qué requisito descartaría una de las alternativas **grúa móvil telescópica frente a grúa de celosía**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Grúas mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-grua.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-grua.md)
