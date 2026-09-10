<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: PORTAVIONES-02
curso: portaviones
titulo: "Características funcionales del portaviones"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: PORTAVIONES-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Portaviones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Portaviones."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales del portaviones

[🏠 Inicio](../../../README.md) · [🛳️ Curso: Portaviones](../README.md) · 📋 Características

Que es un portaviones, que tipos históricos existieron y cual fue su papel
general. Contexto público antes de abrir la física naval (Clase 4). No se
documentan táctica ni sistemas de armas.

---

## 🧭 Definición

Un portaviones es un buque de guerra cuya función es operar aeronaves desde una
cubierta de vuelo. Como todo buque, flota por el principio de Arquímedes, avanza
por el empuje de sus hélices y gobierna con el timón. Su rasgo distintivo es la
gran cubierta plana y el hangar, descritos aquí solo a nivel divulgativo.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Cubierta de vuelo | Superficie plana para operar aeronaves. |
| Hangar | Espacio interior para guardar y mantener aeronaves. |
| Gran desplazamiento | Uno de los buques más grandes; enorme inercia. |
| Isla | Superestructura lateral con el puente. |
| Estabilidad | Cuidada por el peso alto de la cubierta y la isla. |
| Autonomía | Disenado para largas travesías oceánicas. |

---

## 🗂️ Tipos históricos

```mermaid
flowchart TD
    Porta[🛳️ Portaviones] --> Escolta[De escolta]
    Porta --> Flota[De flota]
    Porta --> Moderno[Cubierta angulada]
    Escolta --> Peque[Menor tamaño histórico]
    Flota --> Grande[Gran cubierta y hangar]
    Moderno --> Seguro[Operación más segura]
```

| Tipo | Época | Rasgo destacado |
| --- | --- | --- |
| De escolta | Histórico | Cubierta corta, menor tamaño. |
| De flota | Histórico y moderno | Cubierta y hangar amplios. |
| Cubierta angulada | Moderno | Operación más segura. |
| Buque museo | Actualidad | Uso patrimonial y educativo. |

---

## 🎯 Para qué se usó

- Operar aeronaves desde el mar (contexto histórico general).
- Impulsar avances en aviación, ingeniería naval y logística.
- Hoy, valor patrimonial como buques museo.
- En este repositorio: base para simulación educativa de navegación y cubierta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Tipos históricos y Para qué se usó** a **elegir una configuración adecuada para recuperación simulada de aeronaves con cubierta ocupada parcialmente**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Portaviones, la relación entre planta propulsora, generación y catapulta, cubierta de vuelo y aeronave determina capacidad, respuesta y límites. Por eso «portaaviones CATOBAR frente a STOVL» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada».

Esta clase se conecta con el resto del curso mediante **integración de viento relativo, movimiento del buque y secuencia segura de cubierta**. El hilo de
seguridad consiste en reconocer a tiempo **conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada** y poder justificar la decisión
**ordenar cubierta, rumbo y velocidad antes de iniciar la recuperación**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **planta propulsora → generación y catapulta → cubierta de vuelo → aeronave**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ships](https://www.history.navy.mil/browse-by-topic/ships.html) aporta historia pública de buques militares;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «recuperación simulada de aeronaves con cubierta ocupada parcialmente» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **portaaviones CATOBAR frente a STOVL** usando esos requisitos y la cadena **planta propulsora → generación y catapulta → cubierta de vuelo → aeronave**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **conflicto de trayectorias, objetos extraños o envolvente de viento inadecuada**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **aeronave** condiciona primero el caso «recuperación simulada de aeronaves con cubierta ocupada parcialmente»?
2. ¿Qué requisito descartaría una de las alternativas **portaaviones CATOBAR frente a STOVL**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Portaviones mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-portaviones.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-portaviones.md)
