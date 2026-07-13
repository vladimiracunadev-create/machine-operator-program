# 🌍 Entornos de trabajo del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🌍 Entornos

Donde opera un buque mercante y como cambia la navegacion segun el entorno. Cada
entorno implica reglas, riesgos y ajustes distintos, y en simulacion se traduce
en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚢 Buque mercante))
    Puerto
      Muelles
      Remolcadores
      Practico
    Costa
      Aguas restringidas
      Trafico denso
      Bajos y canales
    Mar abierto
      Alta velocidad
      Rutas oceanicas
      Oleaje sostenido
    Clima
      Viento y mar
      Niebla
      Hielo y temporales
```

| Entorno | Caracteristicas | Riesgos tipicos | Ajuste de navegacion |
| --- | --- | --- | --- |
| Puerto | Espacio estrecho, muelles. | Colision, mala maniobra. | Baja velocidad, thruster, practico. |
| Costa | Aguas restringidas, trafico. | Varada, abordaje. | Vigilancia, ecosonda, COLREG. |
| Canales / esclusas | Paso estrecho controlado. | Encallar, obstruir. | Velocidad minima, remolcadores. |
| Mar abierto | Rutas largas, oleaje. | Temporales, fatiga. | Rumbo, guardias, meteorologia. |
| Niebla / noche | Baja visibilidad. | No ser visto, abordaje. | Radar, luces, senales acusticas. |

---

## 🌦️ Factores del entorno

- **Viento y mar**: el oleaje y el viento afectan rumbo, escora y confort.
- **Corrientes y mareas**: modifican la trayectoria real y el calado disponible.
- **Profundidad**: los bajos limitan las rutas segun el calado del buque.
- **Trafico**: mas buques implica mas decisiones y aplicacion del COLREG.
- **Visibilidad**: niebla y noche exigen radar, luces y senales.

---

## 🎮 Traduccion a simulacion

Cada entorno es un escenario con su profundidad, clima, corriente y trafico. Ver
como se modela en el
[Modulo 8: Diseno de simulacion](../simulacion/diseno-simulador-barco-mercante.md).

---

[⬅️ Anterior: Principios y operacion](principios-barco-mercante.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-barco-mercante.md)
