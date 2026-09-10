---
tipo_documento: clase
clase: 7
codigo: TRENALTAVELO-07
curso: tren-alta-velocidad
titulo: "Entornos de trabajo del tren de alta velocidad"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENALTAVELO-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Tren de alta velocidad."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de alta velocidad."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🌍 Entornos

Dónde opera un tren de alta velocidad y cómo cambia la conducción según el
entorno. Cada entorno implica reglas, riesgos y ajustes distintos, y en
simulación se traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚄 Tren de alta velocidad))
    Corredor de alta velocidad
      Via dedicada
      Curvas amplias
      Velocidad sostenida
    Tuneles largos
      Onda de presion
      Confort de oidos
      Ventilacion
    Viaductos
      Viento lateral
      Grandes vanos
    Estaciones terminales
      Andenes
      Enclavamiento de puertas
      Paradas precisas
    Clima
      Viento fuerte
      Nieve y hielo
```

| Entorno | Características | Riesgos típicos | Ajuste de conducción |
| --- | --- | --- | --- |
| Corredor de alta velocidad | Vía dedicada, curvas amplias. | Objetos en la vía, fallas de catenaria. | Velocidad sostenida, respetar el DMI. |
| Túneles largos | Cambios de presión, ruido. | Onda de presión, confort de oidos. | Velocidad y ventilación adecuadas. |
| Viaductos | Grandes vanos elevados. | Viento lateral, rachas. | Reducir velocidad con viento fuerte. |
| Estaciones terminales | Andenes y agujas. | Mala alineación, atrapamientos. | Frenado preciso, enclavamiento de puertas. |
| Clima adverso | Viento, nieve, hielo. | Menor adherencia, catenaria helada. | Límites reducidos por condiciones. |

---

## 🌦️ Factores del entorno

- **Clima**: el viento lateral en viaductos y la nieve o hielo en la catenaria
  obligan a reducir la velocidad.
- **Infraestructura**: túneles y viaductos imponen condiciones de presión y viento
  que cambian la marcha.
- **Tráfico ferroviario**: el control asigna la vía y las agujas; el tren no elige
  su ruta.
- **Cruce de trenes**: al cruzarse dos trenes a alta velocidad se genera una onda
  de presión que la aerodinámica debe absorber.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su vía, clima y condiciones de infraestructura.
Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-tren-alta-velocidad.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Tren de alta velocidad a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-tren-alta-velocidad.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-tren-alta-velocidad.md)
