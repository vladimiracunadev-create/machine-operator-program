---
tipo_documento: clase
clase: 10
codigo: MAQUINARIACO-10
curso: maquinaria-construccion
titulo: "Recursos de la maquinaria de construcción"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: MAQUINARIACO-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Maquinaria de construcción."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Maquinaria de construcción."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos de la maquinaria de construcción

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de maquinaria de
construcción. Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Hidráulica de trabajo | Sistema de aceite a presión que mueve brazos, cucharones y hojas. |
| Pluma (boom) | Primer tramo del brazo de una excavadora. |
| Balancín (arm) | Segundo tramo del brazo que acerca y aleja el cucharón. |
| Cucharón | Herramienta que recoge, corta y descarga material. |
| Hoja empujadora | Placa que empuja y nivela el terreno. |
| Escarificador (ripper) | Diente que rompe suelo duro antes de empujarlo. |
| Traslación | Movimiento de la máquina por giro de orugas o ruedas. |
| Giro diferencial | Virar moviendo una oruga más que la otra. |
| Momento de vuelco | Peso de la carga por su distancia al punto de vuelco. |
| Zona de exclusión | Radio de trabajo que debe estar libre de personas. |
| ROPS / FOPS | Estructuras que protegen del vuelco y de la caída de objetos. |

---

## 🗺️ Diagrama del ciclo de excavación

```mermaid
flowchart LR
    Penetrar[Penetrar el terreno] --> Arrastrar[Arrastrar cerrando el balancín]
    Arrastrar --> Llenar[Cerrar el cucharón]
    Llenar --> Levantar[Levantar la pluma]
    Levantar --> Girar[Girar al camión]
    Girar --> Descargar[Abrir el cucharón]
    Descargar --> Penetrar
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Manuales oficiales del conductor (CONASET): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Maquinaria de construcción y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CONSTRUCTION](https://www.osha.gov/construction): Construction Industry, OSHA. Uso: maquinaria y seguridad de obra.
- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-maquinaria.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-maquinaria.md)
