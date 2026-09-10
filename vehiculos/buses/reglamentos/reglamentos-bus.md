---
tipo_documento: clase
clase: 8
codigo: BUSES-08
curso: buses
titulo: "Reglamentos del bus (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: BUSES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Buses."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Buses."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos del bus (Chile)

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito) y D.S. 212/1992 MTT (servicios de
  transporte público de pasajeros).
- Autoridad: MTT, CONASET, Carabineros.
- Tipo de vehículo: bus de transporte público de pasajeros.

## Licencia

- Clase **A-3** (profesional) para buses sin límite de asientos, Ley 18.290
  Art. 12.
- Clase **A-2** para vehículos de 10 a 17 asientos.
- Requiere edad mayor y experiencia previa con licencia clase B (Art. 13).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Reglamento de servicios | D.S. 212/1992 MTT | Condiciones del transporte público. | Reglas de rutas y paradas. |
| Jornada del conductor | Código del Trabajo, Art. 25 | Máximo 5 horas continuas de conducción; descansos mínimos. | Modelo de fatiga y descansos. |
| Velocidad | Ley 18.290, Art. 150 | Urbano 50 km/h; interurbano hasta 100 km/h. | Límites por escenario. |
| Documentos | Ley 18.290 / Ley 18.490 | Padrón, permiso, revisión técnica, SOAP. | Chequeo previo simulado. |

## Reglas de seguridad

- Detenerse solo en paradas autorizadas.
- Respetar aforo y no transportar más pasajeros que los permitidos.
- Controlar la fatiga con descansos reglamentarios.
- Priorizar el descenso y ascenso seguro de pasajeros.

## Restricciones

- Licencia profesional clase A-2 o A-3 según capacidad.
- Jornada de conducción limitada por ley.
- Rutas y frecuencias según la autorización del servicio.

## Notas para simulación

- Modelar paradas, aforo, jornada y fatiga del conductor.
- Incluir misiones de ruta urbana con horarios.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Buses; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-bus.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-bus.md)
