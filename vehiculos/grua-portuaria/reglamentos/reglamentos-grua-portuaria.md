---
tipo_documento: clase
clase: 8
codigo: GRUAPORTUARI-08
curso: grua-portuaria
titulo: "Reglamentos de la grúa portuaria (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: GRUAPORTUARI-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Grúa portuaria."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa portuaria."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos de la grúa portuaria (Chile)

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad competente y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
1.7 (Maquinaria de izaje fija).

## Ámbito

- País: Chile.
- Marco base: seguridad laboral, no Ley de Tránsito.
- Autoridad: Dirección del Trabajo y mutuales (seguridad laboral); en el recinto
  portuario, además, la Autoridad Marítima (DIRECTEMAR) y la autoridad del puerto.
- Tipo de vehículo: grúa fija de izaje sobre rieles del muelle.

## Habilitación y certificación

- Las grúas fijas **no circulan por vía pública** y **no requieren licencia de
  conducir**.
- La operación la realiza personal **certificado/competente**, con formación
  específica en el equipo.
- Se trabaja con **plan de izaje**, **señalero (rigger)** y **área de exclusión**.
- El detalle de certificación del operador está **(por confirmar)** en el marco
  legal, sección 1.7.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Seguro de accidentes | Ley 16.744 | Seguro social contra accidentes del trabajo. | Contexto de operación segura del escenario. |
| Condiciones de trabajo | D.S. 594 (MINSAL) | Condiciones sanitarias y ambientales básicas. | Reglas de entorno y jornada del escenario. |
| Operador competente | Seguridad laboral | Personal certificado para el equipo (por confirmar). | Modo habilitación del operador. |
| Plan de izaje | Buenas prácticas de izaje | Límites de carga, radios, secuencia. | Modelo de límite de carga y ciclo. |
| Señalero y exclusión | Prevención de riesgos | Rigger y área libre de personas. | Escenario con área de exclusión. |
| Ámbito portuario | Autoridad Marítima y del puerto | Normas del recinto portuario. | Reglas propias del terminal. |

## Reglas de seguridad

- Verificar límite de carga y estado del spreader antes de izar.
- Respetar el límite de viento del anemómetro; detener la operación si se supera.
- Delimitar el área de exclusión y controlar la presencia de personas en tierra.
- Coordinar cada movimiento con el señalero y con el flujo de camiones.
- No izar sin los twist-locks trabados ni con la carga mal calzada.

## Restricciones

- Operación solo por personal certificado/competente (detalle por confirmar).
- Operación según manual del fabricante y límites del equipo.
- Cumplimiento de las normas del recinto portuario y de la Autoridad Marítima.

## Notas para simulación

- El núcleo educativo es la seguridad del izaje: límite de carga, viento y área de exclusión.
- Modelar la coordinación con el señalero y con los camiones.
- Usar avisos educativos en vez de castigos frustrantes.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Grúa portuaria; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-portuaria.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md)
