# Reglamentos: bus (Chile)

Referencia educativa y de diseno de simulacion. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ambito

- Pais: Chile.
- Ley base: Ley 18.290 (Ley de Transito) y D.S. 212/1992 MTT (servicios de
  transporte publico de pasajeros).
- Autoridad: MTT, CONASET, Carabineros.
- Tipo de vehiculo: bus de transporte publico de pasajeros.

## Licencia

- Clase **A-3** (profesional) para buses sin limite de asientos, Ley 18.290
  Art. 12.
- Clase **A-2** para vehiculos de 10 a 17 asientos.
- Requiere edad mayor y experiencia previa con licencia clase B (Art. 13).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Reglamento de servicios | D.S. 212/1992 MTT | Condiciones del transporte publico. | Reglas de rutas y paradas. |
| Jornada del conductor | Codigo del Trabajo, Art. 25 | Maximo 5 horas continuas de conduccion; descansos minimos. | Modelo de fatiga y descansos. |
| Velocidad | Ley 18.290, Art. 150 | Urbano 50 km/h; interurbano hasta 100 km/h. | Limites por escenario. |
| Documentos | Ley 18.290 / Ley 18.490 | Padron, permiso, revision tecnica, SOAP. | Chequeo previo simulado. |

## Reglas de seguridad

- Detenerse solo en paradas autorizadas.
- Respetar aforo y no transportar mas pasajeros que los permitidos.
- Controlar la fatiga con descansos reglamentarios.
- Priorizar el descenso y ascenso seguro de pasajeros.

## Restricciones

- Licencia profesional clase A-2 o A-3 segun capacidad.
- Jornada de conduccion limitada por ley.
- Rutas y frecuencias segun la autorizacion del servicio.

## Notas para simulacion

- Modelar paradas, aforo, jornada y fatiga del conductor.
- Incluir misiones de ruta urbana con horarios.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).
