---
tipo_documento: clase
clase: 10
codigo: HALCONMILENA-10
curso: halcon-milenario
titulo: "Recursos del Halcón Milenario"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: HALCONMILENA-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Halcón Milenario."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Halcón Milenario."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos del Halcón Milenario

[🏠 Inicio](../../../README.md) · [🦅 Curso: Halcón Milenario](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Glosario específico, enlaces y diagramas de apoyo del curso del carguero rápido.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Empuje | Fuerza que impulsa la nave, resultado de expulsar masa. |
| Masa total | Suma de la nave y su carga; decide cuanto acelera. |
| Relación empuje/masa | Cociente que indica lo ágil o pesada que se siente la nave. |
| Aceleración | Cambio de velocidad; igual al empuje dividido por la masa. |
| Delta-v | Cambio total de velocidad que la nave puede lograr con su propelente. |
| Propelente | Masa que el motor expulsa para generar empuje por reacción. |
| Momento | Producto de masa por velocidad; se conserva sin fuerzas externas. |
| Hiperimpulso | Salto de ficción a la velocidad de la luz; sin base en la física actual. |
| Carga útil | Masa transportada en la bodega; recorta agilidad y delta-v. |
| Reentrada | Entrada a una atmósfera, donde aparecen aire, calor y rozamiento. |

---

## 🗺️ Diagrama: por qué la carga pesa

```mermaid
flowchart LR
    Motor[Mismo empuje de motores] --> Acel[Aceleración]
    Carga[Añadir carga] --> Masa[Sube la masa total]
    Masa --> Acel
    Acel --> Menos[Con más masa, menos aceleración]
    Menos --> Idea[La carga no viaja gratis]
```

---

## 🔗 Enlaces y fuentes

- Portada del curso: [🦅 Curso: Halcón Milenario](../README.md)
- Catálogo de naves de ficción: [🌌 Naves de ficción](../../README.md)
- Glosario general: [📖 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Niveles de realismo: [🎚️ docs/03-niveles-de-realismo.md](../../../docs/03-niveles-de-realismo.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, respetando el aviso de
derechos del catálogo de naves de ficción.

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Halcón Milenario y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARWARS-FALCON](https://www.starwars.com/databank/millennium-falcon): Millennium Falcon, Lucasfilm. Uso: canon narrativo del vehículo.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-halcon-milenario.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-halcon-milenario.md)
