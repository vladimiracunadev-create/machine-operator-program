<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: TANQUES-02
curso: tanques
titulo: "Características funcionales del tanque (marco público)"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: TANQUES-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Tanques."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tanques."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales del tanque (marco público)

[🏠 Inicio](../../../README.md) · [🪖 Curso: Tanques](../README.md) · 📋 Características

Que es un carro de combate como vehículo, que familias existen según su movilidad
y para que sirve el tren de orugas. Solo enfoque público y divulgativo; sin
armamento ni táctica. Esta clase da contexto antes de la mecánica (Clase 4).

---

## 🧭 Definición

Un carro de combate es un vehículo terrestre de orugas, pesado y de alta
movilidad en terreno difícil. Desde el punto de vista técnico que trata este
curso, es una plataforma que reparte un gran peso sobre el suelo mediante orugas
para avanzar donde las ruedas se hundirían.

---

## 🧬 Características clave (aspectos públicos)

| Característica | Descripción |
| --- | --- |
| Tracción por orugas | Reparte el peso en una superficie amplia y da agarre en barro. |
| Baja presión sobre el suelo | Menor hundimiento que una rueda para el mismo peso. |
| Dirección diferencial | Gira frenando o acelerando una oruga respecto a la otra. |
| Alta masa | Gran peso que exige mucho motor y afecta la inercia. |
| Movilidad todo terreno | Supera pendientes, zanjas y obstáculos. |
| Protección como masa | El blindaje se menciona solo como peso que influye en la movilidad. |

---

## 🗂️ Familias por movilidad

```mermaid
flowchart TD
    Veh[🪖 Vehículo de orugas] --> Peso[Según peso]
    Veh --> Rodaje[Según tren de rodaje]
    Peso --> Ligero[Ligero]
    Peso --> Medio[Medio]
    Peso --> Pesado[Pesado]
    Rodaje --> Torsion[Suspensión de barras de torsión]
    Rodaje --> Hidro[Suspensión hidroneumatica]
```

| Familia | Rasgo de movilidad | Nota |
| --- | --- | --- |
| Ligero | Más velocidad y menos presión al suelo | Mejor en terreno blando. |
| Medio | Equilibrio entre peso y movilidad | Uso general histórico. |
| Pesado | Más masa y menos agilidad | Exige más motor y consumo. |
| Suspensión de torsión | Marcha robusta y sencilla | Muy común históricamente. |
| Suspensión hidroneumatica | Mejor confort y control de altura | Solución más moderna. |

---

## 🎯 Para qué se usa (enfoque público)

- Movilidad en terreno difícil donde una rueda se hundiría.
- Estudio de la física de vehículos de orugas.
- Contexto histórico e institucional público.
- Simulación educativa de conducción todo terreno, sin contenido sensible.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave (aspectos públicos), Familias por movilidad y Para qué se usa (enfoque público)** a **elegir una configuración adecuada para cruce simulado de suelo blando con cambio de pendiente**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Tanques, la relación entre motor, transmisión, ruedas tractoras y orugas determina capacidad, respuesta y límites. Por eso «carro pesado frente a vehículo blindado ligero» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «atasco, pérdida de movilidad o exposición por elegir una ruta incompatible».

Esta clase se conecta con el resto del curso mediante **tracción y presión sobre el terreno condicionadas por masa, reparto y resistencia al avance**. El hilo de
seguridad consiste en reconocer a tiempo **atasco, pérdida de movilidad o exposición por elegir una ruta incompatible** y poder justificar la decisión
**reconocer capacidad del terreno y escoger ruta, velocidad y orientación del casco**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → ruedas tractoras → orugas**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Tank Collection](https://tankmuseum.org/tank-nuts/tank-collection) aporta historia pública de vehículos blindados;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «cruce simulado de suelo blando con cambio de pendiente» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **carro pesado frente a vehículo blindado ligero** usando esos requisitos y la cadena **motor → transmisión → ruedas tractoras → orugas**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **atasco, pérdida de movilidad o exposición por elegir una ruta incompatible**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **orugas** condiciona primero el caso «cruce simulado de suelo blando con cambio de pendiente»?
2. ¿Qué requisito descartaría una de las alternativas **carro pesado frente a vehículo blindado ligero**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Tanques mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [TANK-MUSEUM](https://tankmuseum.org/tank-nuts/tank-collection): Tank Collection, The Tank Museum. Uso: historia pública de vehículos blindados.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-tanque.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-tanque.md)
