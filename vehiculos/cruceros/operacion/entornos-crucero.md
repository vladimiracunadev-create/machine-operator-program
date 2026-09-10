---
tipo_documento: clase
clase: 7
codigo: CRUCEROS-07
curso: cruceros
titulo: "Entornos de trabajo del crucero"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: CRUCEROS-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Cruceros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cruceros."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo del crucero

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · 🌍 Entornos

Dónde opera un crucero y cómo cambia la navegación según el entorno. Cada entorno
implica reglas, riesgos y ajustes distintos, y en simulación se traduce en
escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((⛴️ Crucero))
    Puerto
      Terminal de pasajeros
      Remolcadores
      Practico
    Costa
      Escalas turisticas
      Aguas restringidas
      Fondeo y tenders
    Mar abierto
      Rutas entre escalas
      Oleaje sostenido
      Confort del pasaje
    Clima
      Viento y mar
      Niebla
      Zonas frias o polares
```

| Entorno | Características | Riesgos típicos | Ajuste de navegación |
| --- | --- | --- | --- |
| Puerto | Terminal de pasaje, muelles. | Colisión, mala maniobra. | Baja velocidad, pods, thruster, práctico. |
| Fondeo frente a escala | Sin muelle disponible. | Garreo, riesgo en tenders. | Vigilar ancla, embarcar pasaje con cuidado. |
| Costa | Aguas restringidas, tráfico. | Varada, abordaje. | Vigilancia, ecosonda, COLREG. |
| Mar abierto | Rutas largas, oleaje. | Temporales, mareo del pasaje. | Rumbo, guardias, estabilizadores. |
| Niebla / noche | Baja visibilidad. | No ser visto, abordaje. | Radar, luces, señales acústicas. |
| Zonas frías o polares | Hielo, apoyo escaso. | Avería lejos de puerto. | Casco reforzado, rutas planificadas. |

---

## 🌦️ Factores del entorno

- **Viento y mar**: el oleaje y el viento afectan rumbo, escora y el confort del
  pasaje; la alta obra muerta hace al crucero muy sensible al viento.
- **Corrientes y mareas**: modifican la trayectoria real y el calado disponible.
- **Profundidad**: los bajos limitan las rutas según el calado del buque.
- **Tráfico**: más buques implica más decisiones y aplicación del COLREG.
- **Visibilidad**: niebla y noche exigen radar, luces y señales.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su profundidad, clima, corriente y tráfico. Ver
como se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-crucero.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Cruceros a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-crucero.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-crucero.md)
