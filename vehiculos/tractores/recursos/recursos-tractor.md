---
tipo_documento: clase
clase: 10
codigo: TRACTORES-10
curso: tractores
titulo: "Recursos del tractor"
modalidad: "taller documental"
duracion_minutos: 45
nivel: introductorio
prerrequisito: TRACTORES-09
competencia: "alfabetizacion_tecnica"
resultados_aprendizaje:
  - "Explicar glosario, esquemas y trazabilidad de fuentes con vocabulario propio de Tractores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tractores."
evidencia: "Glosario aplicado y ficha breve de trazabilidad."
criterio_aprobacion: "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧰 Recursos del tractor

[🏠 Inicio](../../../README.md) · [🚜 Curso: Tractores](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de tractores. Amplia
el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Toma de fuerza (PTO) | Eje que transmite la potencia del motor a un apero. |
| Enganche de tres puntos | Triángulo de brazos que sujeta y controla un apero montado. |
| Tercer punto | Brazo superior que fija el ángulo del apero. |
| Control de esfuerzo | Regulación que sube el apero cuando aumenta la resistencia. |
| Barra de tiro | Punto bajo de enganche para arrastrar cargas con seguridad. |
| Lastre | Peso agregado que mejora el agarre y equilibra el apero. |
| Patinaje | Diferencia entre el giro de la rueda y el avance real. |
| Doble tracción | Sistema que tracciona también el eje delantero. |
| ROPS | Estructura antivuelco que protege al operador. |
| Bloqueo de diferencial | Mando que iguala el giro de ambas ruedas motrices. |

---

## 🗺️ Diagrama de estabilidad en pendiente

```mermaid
flowchart LR
    Pendiente[Pendiente] --> CG[Centro de gravedad alto]
    CG --> Riesgo[Riesgo de vuelco]
    Lastre[Lastre y vía ancha] --> Estable[Más estable]
    Recta[Subir/bajar en línea recta] --> Estable
    Riesgo --> Prudencia[Bajar velocidad, sin giros bruscos]
    Prudencia --> Estable
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Manuales oficiales del conductor (CONASET): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

## 🎓 Cierre de clase

- **Actividad:** Selecciona términos de glosario, esquemas y trazabilidad de fuentes, explícalos en contexto de Tractores y verifica la procedencia de las fuentes utilizadas.
- **Evidencia:** Glosario aplicado y ficha breve de trazabilidad.
- **Criterio de aprobación:** Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-AGRI](https://www.osha.gov/agricultural-operations/hazards): Agricultural Operations: Hazards and Controls, OSHA. Uso: tractores, aperos y riesgos agrícolas.
- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-tractor.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-tractor.md)
