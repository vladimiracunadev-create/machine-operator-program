---
tipo_documento: clase
clase: 8
codigo: AUTOMOVILES-08
curso: automoviles
titulo: "Reglamentos del automóvil (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AUTOMOVILES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Automóviles."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Automóviles."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos del automóvil (Chile)

[🏠 Inicio](../../../README.md) · [🚗 Curso: Automóviles](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.290 (Ley de Tránsito).
- Autoridad: CONASET, MTT, municipalidades, Carabineros.
- Tipo de vehículo: automóvil o camioneta particular hasta 3.500 kg.

## Licencia

- Clase **B** (no profesional), Ley 18.290 Art. 12.
- Edad mínima: 18 años (Art. 13).
- Habilita vehículos de 3 o más ruedas, hasta 9 asientos o carga hasta 3.500 kg.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Cinturón | Ley 18.290, Art. 79 | Obligatorio en asientos delanteros y traseros según año. | Exigir cinturón antes de partir. |
| Retención infantil | Ley 20.904 (Art. 75) | Silla para ninos hasta 8 años; menores de 12 atrás. | Escenario con pasajeros infantiles. |
| Documentos | Ley 18.290 / Ley 18.490 | Padrón, permiso de circulación, revisión técnica, SOAP. | Chequeo previo simulado. |
| Velocidad urbana | Ley 21.103 | 50 km/h general. | Límite del escenario urbano. |
| Alcohol | Ley 20.770 (Ley Emilia) | Sanciones por conducir bajo la influencia del alcohol. | Modo educativo sobre consecuencias. |

## Reglas de seguridad

- Uso obligatorio de cinturón en todos los asientos ocupados.
- Respetar señales, semaforos y prioridades de paso.
- Mantener distancia de seguimiento y velocidad prudente.
- No usar el teléfono mientras se conduce.

## Restricciones

- Edad mínima 18 años para licencia clase B.
- Menores de 12 años deben viajar en el asiento trasero.
- Zonas con límites y restricciones según señalización municipal.

## Notas para simulación

- Modelar cinturón, retención infantil y respeto de señales.
- Usar avisos educativos ante infracciones.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Automóviles; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [CL-CONASET](https://www.conaset.cl/manuales/): Manuales para conductores, CONASET. Uso: formación vial y seguridad.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-automovil.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-automovil.md)
