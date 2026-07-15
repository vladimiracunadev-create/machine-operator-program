# 🌍 Entornos de trabajo del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🌍 Entornos

Dónde opera un helicóptero y cómo cambia el vuelo según el entorno. Cada entorno
implica reglas, riesgos y ajustes distintos, y en simulación se traduce en
escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚁 Helicoptero))
    Helipuertos
      Superficie preparada
      Trafico controlado
      Reabastecimiento
    Rescate
      Montana
      Mar
      Grua de rescate
    Sanitario
      Hospitales
      Azoteas
      Traslado de pacientes
    Incendios
      Carga externa de agua
      Humo y calor
      Terreno agreste
```

| Entorno | Características | Riesgos típicos | Ajuste de vuelo |
| --- | --- | --- | --- |
| Helipuerto | Superficie preparada y senalizada. | Tráfico, obstáculos cercanos. | Aproximación estandar, vigilar viento. |
| Rescate en montaña | Altura, espacio reducido. | Aire menos denso, turbulencia. | Más potencia, margenes amplios. |
| Rescate en mar | Sin referencias fijas, oleaje. | Desorientación, spray de agua. | Estacionario preciso, uso de grúa. |
| Hospital | Azoteas y helipuertos elevados. | Espacio estrecho, público cercano. | Aproximación suave y controlada. |
| Incendio forestal | Humo, calor, carga externa. | Baja visibilidad, aire caliente. | Vuelo con carga, rutas de escape. |

---

## 🌦️ Factores del entorno

- **Densidad del aire**: la altura y el calor reducen la densidad y con ella la
  sustentación; se necesita más potencia.
- **Viento y turbulencia**: afectan el estacionario y la aproximación, sobre todo
  cerca de obstáculos y en montaña.
- **Visibilidad**: humo, niebla o spray de mar dificultan mantener referencias.
- **Espacio disponible**: azoteas y claros exigen precisión y margenes de rotor.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su superficie, clima, densidad del aire y
obstáculos. Ver cómo se modela en el
[Módulo 8: Diseño de simulación](../simulacion/diseno-simulador-helicoptero.md).

---

[⬅️ Anterior: Principios y operación](principios-helicoptero.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-helicoptero.md)
