---
tipo_documento: clase
clase: 7
codigo: MAQUINARIACO-07
curso: maquinaria-construccion
titulo: "Entornos de trabajo de la maquinaria de construcción"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: MAQUINARIACO-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Maquinaria de construcción."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Maquinaria de construcción."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo de la maquinaria de construcción

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · 🌍 Entornos

Dónde opera la maquinaria de construcción y cómo cambia la operación según el
entorno. Cada entorno implica reglas, riesgos y ajustes distintos, y en
simulación se traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚧 Maquinaria))
    Obra civil
      Fundaciones
      Zanjas
      Edificacion
    Mineria
      Rajo abierto
      Carga de mineral
      Grandes equipos
    Vialidad
      Movimiento de tierra
      Nivelacion
      Caminos
    Demolicion
      Escombros
      Martillo
      Polvo
```

| Entorno | Características | Riesgos típicos | Ajuste de operación |
| --- | --- | --- | --- |
| Obra civil | Zanjas, fundaciones, poco espacio. | Ductos ocultos, personas cerca. | Radio controlado, señaleros. |
| Minería a rajo | Grandes volumenes, equipos pesados. | Tráfico de camiones, polvo. | Reglas de faena, distancia y radio. |
| Vialidad | Movimiento de tierra y nivelación. | Tráfico vehicular, taludes. | Señalización, hoja y pendiente controladas. |
| Demolición | Escombros y estructuras. | Caída de material, polvo. | FOPS, riego, área despejada. |
| Terreno blando / lluvia | Barro, suelo que cede. | Hundimiento, deslizamiento. | Orugas anchas, base firme, baja velocidad. |

---

## 🌦️ Factores del entorno

- **Terreno**: firmeza, pendiente y humedad definen estabilidad y agarre.
- **Espacio**: en obra urbana el radio de giro y los servicios enterrados limitan.
- **Personas**: la faena suele tener trabajadores a pie; el radio de trabajo es
  zona de exclusión.
- **Clima**: lluvia, polvo y calor afectan visibilidad, suelo y la máquina.
- **Otros equipos**: camiones y máquinas comparten la faena y deben coordinarse.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su terreno, espacio, clima y presencia de
personas y equipos. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-maquinaria.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Maquinaria de construcción a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CONSTRUCTION](https://www.osha.gov/construction): Construction Industry, OSHA. Uso: maquinaria y seguridad de obra.
- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-maquinaria.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-maquinaria.md)
