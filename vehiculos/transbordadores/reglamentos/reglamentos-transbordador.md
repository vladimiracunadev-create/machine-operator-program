---
tipo_documento: clase
clase: 8
codigo: TRANSBORDADO-08
curso: transbordadores
titulo: "Reglamentos del transbordador (marco público)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRANSBORDADO-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Transbordadores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Transbordadores."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos del transbordador (marco público)

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · ⚖️ Reglamentos

Referencia educativa e institucional. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md) sección 4.

## Ámbito

- Tipo de vehículo: transbordador espacial reutilizable de uso civil.
- Opera bajo la jurisdicción del **Estado de lanzamiento** y su agencia espacial,
  dentro del marco de los tratados internacionales.
- Chile no cuenta a la fecha con una ley espacial nacional integral; el marco
  interno es de política pública más los tratados internacionales.

## Estado de lanzamiento y su agencia

Como todo vehículo espacial, el transbordador responde ante un **Estado de
lanzamiento** que autoriza y supervisa la misión por medio de su agencia
espacial.

| Agencia o rol | Ejemplo | Función |
| --- | --- | --- |
| Agencia espacial nacional | NASA, ESA, Roscosmos, JAXA, CSA | Programa y opera las misiones. |
| Autoridad de rango | Regulador de seguridad | Vigila la trayectoria de despegue y regreso. |
| Estado de lanzamiento | País responsable | Responde por daños ante los tratados. |
| Marco nacional en Chile | Política Nacional Espacial | Orienta la actividad espacial del país. |

## Tratados internacionales (marco de UNOOSA)

| Tratado | Objeto |
| --- | --- |
| Tratado del Espacio Ultraterrestre (1967) | Principios de la actividad espacial de los Estados. |
| Acuerdo de Salvamento (1968) | Rescate de astronautas y devolución de objetos. |
| Convenio de Responsabilidad (1972) | Responsabilidad por daños de objetos espaciales. |
| Convenio de Registro (1975) | Registro de objetos lanzados al espacio. |

Principios útiles para el diseño: uso pacífico del espacio, responsabilidad del
Estado de lanzamiento y registro de cada objeto en órbita. El detalle chileno está
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md) sección 4.

## Enfoque permitido en simulación

- Principios físicos: despegue, órbita, reentrada y planeo sin motor.
- Seguridad de rango en el despegue y en el corredor de aterrizaje.
- Marco de tratados como reglas del "mundo" del simulador.

## Restricciones de contenido

- No incluir información sensible de sistemas de lanzamiento militar.
- Mantener el enfoque público, histórico y educativo.
- No detallar procedimientos que permitan replicar tecnología sensible.

## Notas para simulación

- Exigir sistemas en verde antes del despegue y del regreso.
- Usar avisos educativos en vez de castigos frustrantes.
- Registrar cada fuente pública en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Transbordadores; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SHUTTLE](https://www.nasa.gov/reference/the-space-shuttle/): The Space Shuttle, NASA. Uso: arquitectura y operación del transbordador.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-transbordador.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-transbordador.md)
