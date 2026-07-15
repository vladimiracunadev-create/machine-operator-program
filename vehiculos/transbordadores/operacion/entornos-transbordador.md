# 🌍 Entornos de trabajo del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🌍 Entornos

Dónde opera un transbordador y cómo cambian las condiciones a lo largo de la
misión. Cada fase implica un entorno distinto, con riesgos y ajustes propios, y en
simulación se traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🛬 Transbordador))
    Plataforma
      Carga de propelente
      Torre de servicio
      Cuenta atras
    Ascenso
      Aire denso
      Separacion de propulsores
      Separacion del tanque
    Orbita
      Microgravedad
      Bahia de carga abierta
      Brazo robotico
    Reentrada y planeo
      Calor extremo
      Escudo por delante
      Aterrizaje en pista
```

| Entorno | Características | Riesgos típicos | Ajuste de operación |
| --- | --- | --- | --- |
| Plataforma | Vehículo cargado y sujeto. | Fuga de propelente, clima. | Checklist, ventana de lanzamiento. |
| Ascenso | Aire denso y gran empuje. | Separaciones a destiempo. | Guiar, separar propulsores y tanque. |
| Órbita | Microgravedad, sin aire. | Colisiones, basura orbital. | Control de actitud, operar la carga. |
| Reentrada | Calor y frenado por el aire. | Mala orientación del escudo. | Escudo por delante, ángulo correcto. |
| Planeo y pista | Descenso sin motor. | Quedar corto o largo, viento. | Administrar energía, un solo intento. |

---

## 🌦️ Factores del entorno

- **Clima**: viento y visibilidad afectan tanto el despegue como el aterrizaje.
- **Ventana de lanzamiento**: momento preciso para alcanzar la órbita objetivo.
- **Calor de reentrada**: depende del ángulo y de la velocidad de reingreso.
- **Estado de la pista**: viento cruzado y longitud influyen en el aterrizaje.

---

## 🎮 Traducción a simulación

Cada fase es un escenario con su densidad de aire, su gravedad efectiva y su
régimen de vuelo o planeo. Ver cómo se modela en el
[Módulo 8: Diseño de simulación](../simulacion/diseno-simulador-transbordador.md).

---

[⬅️ Anterior: Principios y operación](principios-transbordador.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-transbordador.md)
