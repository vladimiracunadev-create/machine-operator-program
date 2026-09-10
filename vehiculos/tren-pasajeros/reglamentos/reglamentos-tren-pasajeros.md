---
tipo_documento: clase
clase: 8
codigo: TRENPASAJERO-08
curso: tren-pasajeros
titulo: "Reglamentos del tren de pasajeros (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENPASAJERO-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Tren de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de pasajeros."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos del tren de pasajeros (Chile)

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad de transporte y la ley vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Operador estatal histórico: Empresa de los Ferrocarriles del Estado (EFE).
- Autoridad reguladora: Ministerio de Transportes (MTT).
- Tipo de vehículo: tren de pasajeros sobre red ferroviaria.

## Habilitación del personal de conducción

A diferencia de un vehículo de vía pública, el tren **no** se opera con una
licencia de conducir común. El personal de conducción, el maquinista, requiere
una **habilitación o certificación específica del operador** ferroviario.

- No aplica licencia de conducir de vía pública (clases A, B o C).
- La habilitación la define el operador (EFE) según su normativa interna.
- El régimen exacto de habilitación de maquinistas queda **por confirmar** en la
  fuente oficial.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Marco ferroviario | Ley General de Ferrocarriles (por confirmar) | Base legal del transporte por ferrocarril. | Reglas generales del escenario. |
| Habilitación del maquinista | Certificación del operador (por confirmar) | Personal de conducción habilitado por EFE. | Requisito previo antes de operar. |
| Señalización y ATP | Normativa del sector (por confirmar) | Respetar señales y límites del ATP. | Control de velocidad por señal. |
| Pasos a nivel | Normativa del sector (por confirmar) | Advertir y proteger cruces con carretera. | Escenarios de paso a nivel. |
| Ancho de vía | Estandar de la red (por confirmar) | Trocha compatible con el material. | Parámetro fijo del escenario. |

## Reglas de seguridad

- Operar solo con habilitación vigente del operador.
- Respetar en todo momento las señales de vía y los límites del ATP.
- Advertir con el silbato en pasos a nivel y al aproximarse a andenes.
- Verificar la presión de freno y el enclavamiento de puertas antes de arrancar.
- Comunicar por radio cualquier incidencia al puesto de control.

## Restricciones

- Circulación solo por vías autorizadas y según el horario del servicio.
- Velocidad limitada por la señalización y el ATP de cada tramo.
- Distancias mínimas entre trenes garantizadas por el bloqueo por tramos.

## Notas para simulación

- Modelar señales, ATP, pasos a nivel y paradas en andén.
- Representar la habilitación del maquinista como requisito previo del escenario.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Enlazar el marco a [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md)
  sección 1.6 y a los datos por reconfirmar. Fuente institucional: efe.cl.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Tren de pasajeros; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-pasajeros.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-pasajeros.md)
