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

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-bus.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-bus.md)
