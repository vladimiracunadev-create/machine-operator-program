---
tipo_documento: clase
clase: 8
codigo: HELICOPTEROS-08
curso: helicopteros
titulo: "Reglamentos del helicóptero (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: HELICOPTEROS-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Helicópteros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Helicópteros."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos del helicóptero (Chile)

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad aeronáutica y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
3.2 (Helicópteros).

## Ámbito

- País: Chile.
- Ley base: Ley 18.916 (Código Aeronáutico).
- Autoridad: Dirección General de Aeronáutica Civil (DGAC).
- Tipo de aeronave: helicóptero civil (aeronave de ala rotatoria).

## Licencia y habilitación

- La licencia de piloto de helicóptero y sus habilitaciones están reguladas por la
  reglamentación **DAN 61** (licencias para pilotos y sus habilitaciones), edición
  vigente por confirmar.
- Se otorga por la DGAC y requiere **certificado médico aeronáutico**.
- Se rige por el mismo marco que la aviación civil: Código Aeronáutico y
  fiscalización de la DGAC.

## Requisitos y elementos

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Licencia | DAN 61 (edición por confirmar) | Licencia de piloto de helicóptero y habilitaciones. | Requisito de piloto habilitado. |
| Certificado médico | Reglamentación DGAC | Aptitud psicofísica del piloto. | Requisito antes de volar. |
| Matrícula | Código Aeronáutico, Art. 32 | Inscripción que confiere nacionalidad chilena a la aeronave. | Estado documental de la aeronave. |
| Aeronavegabilidad | Código Aeronáutico, Art. 52 | Certificado de aeronavegabilidad vigente. | Chequeo previo al vuelo. |
| Espacio aéreo | Código Aeronáutico, Art. 1 | Soberanía y reglas del espacio aéreo. | Reglas de tráfico aéreo del escenario. |

## Reglas de seguridad

- Completar la inspección previa al vuelo antes de despegar.
- Respetar el espacio aéreo controlado y las instrucciones de tráfico.
- Vigilar combustible, meteorología, densidad del aire y peso y balance.
- Practicar la entrada en autorrotación ante un fallo de motor.

## Restricciones

- Volar solo con licencia y certificado médico vigentes.
- Operación según las reglas de vuelo aplicables y la autoridad aeronáutica.
- Zonas restringidas y controladas según la DGAC.

## Notas para simulación

- El núcleo educativo son el vuelo estacionario, el anti-par y la autorrotación.
- Modelar chequeos previos, plan de vuelo y comunicaciones básicas.
- Marcar como "(por confirmar)" la edición vigente de la DAN 61. Fuente:
  <https://www.dgac.gob.cl>.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Helicópteros; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HELI](https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf): Helicopter Flying Handbook, FAA. Uso: aerodinámica y control de helicópteros.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-helicoptero.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-helicoptero.md)
