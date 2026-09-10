---
tipo_documento: clase
clase: 8
codigo: GRUATORRE-08
curso: grua-torre
titulo: "Reglamentos de la grúa torre (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: GRUATORRE-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Grúa torre."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa torre."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos de la grúa torre (Chile)

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grúa torre](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad laboral y la normativa vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
sección 1.7 (Maquinaria de izaje fija).

## Ámbito

- País: Chile.
- Marco base: seguridad laboral, no Ley de Tránsito. La grúa torre es una grúa
  fija que NO circula por vía pública y NO requiere licencia de conducir.
- Leyes de referencia: Ley 16.744 (accidentes del trabajo) y D.S. 594 (MINSAL,
  condiciones sanitarias y ambientales en los lugares de trabajo).
- Autoridad: Dirección del Trabajo y mutuales (seguridad laboral); MINSAL
  (condiciones de trabajo).
- Tipo de vehículo: maquinaria de izaje fija.

## Habilitación y certificación

- No se necesita licencia de conducir: la grúa no circula por vía pública.
- La operación la realiza personal **certificado/competente**, no un conductor.
- Se opera con un **plan de izaje** y las tablas de carga del fabricante.
- Un **señalero (rigger)** coordina la maniobra desde tierra.
- Los detalles de certificación del operador están por confirmar (ver marco legal).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Seguro laboral | Ley 16.744 | Cobertura de accidentes del trabajo. | Contexto de seguridad del escenario. |
| Condiciones de trabajo | D.S. 594 (MINSAL) | Condiciones sanitarias y ambientales básicas. | Reglas de entorno de la obra. |
| Operador competente | Marco laboral (por confirmar) | Operador certificado/competente. | Modo habilitación por competencia. |
| Plan de izaje | Marco laboral | Plan con carga, radio, viento y área. | Chequeo previo simulado. |
| Señalero y área de exclusión | Marco laboral | Rigger y zona despejada bajo el giro. | Modelo de área de exclusión. |
| Montaje y desmontaje | Marco laboral (por confirmar) | Operación crítica con personal competente. | Escenario de trepado controlado. |

## Reglas de seguridad

- Verificar peso, radio y tabla de carga antes de cada izaje.
- Nivelar y anclar la base; confirmar el arriostramiento en grandes alturas.
- Delimitar el área de exclusión bajo la zona de giro y controlar personas.
- Respetar el límite de viento y pasar a veleta fuera de servicio.
- Tratar el montaje y el desmontaje como operación crítica con personal competente.

## Restricciones

- No circula por vía pública: sin licencia de conducir.
- Operación según manual del fabricante y límites de la máquina.
- Montaje y desmontaje solo con personal competente (por confirmar).

## Notas para simulación

- El núcleo educativo es la estabilidad: momento de carga, radio y viento.
- Modelar el área de exclusión, el señalero y el límite de viento.
- Marcar como "(por confirmar)" la certificación del operador y las reglas de montaje.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Grúa torre; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [OSHA-TOWER](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1435): 1926.1435 Tower Cranes, OSHA. Uso: requisitos específicos de grúas torre.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-torre.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua-torre.md)
