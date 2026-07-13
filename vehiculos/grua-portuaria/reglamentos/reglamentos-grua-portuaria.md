# ⚖️ Reglamentos de la grua portuaria (Chile)

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grua portuaria](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
operar se deben consultar la autoridad competente y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), seccion
1.7 (Maquinaria de izaje fija).

## Ambito

- Pais: Chile.
- Marco base: seguridad laboral, no Ley de Transito.
- Autoridad: Direccion del Trabajo y mutuales (seguridad laboral); en el recinto
  portuario, ademas, la Autoridad Maritima (DIRECTEMAR) y la autoridad del puerto.
- Tipo de vehiculo: grua fija de izaje sobre rieles del muelle.

## Habilitacion y certificacion

- Las gruas fijas **no circulan por via publica** y **no requieren licencia de
  conducir**.
- La operacion la realiza personal **certificado/competente**, con formacion
  especifica en el equipo.
- Se trabaja con **plan de izaje**, **senalero (rigger)** y **area de exclusion**.
- El detalle de certificacion del operador esta **(por confirmar)** en el marco
  legal, seccion 1.7.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Seguro de accidentes | Ley 16.744 | Seguro social contra accidentes del trabajo. | Contexto de operacion segura del escenario. |
| Condiciones de trabajo | D.S. 594 (MINSAL) | Condiciones sanitarias y ambientales basicas. | Reglas de entorno y jornada del escenario. |
| Operador competente | Seguridad laboral | Personal certificado para el equipo (por confirmar). | Modo habilitacion del operador. |
| Plan de izaje | Buenas practicas de izaje | Limites de carga, radios, secuencia. | Modelo de limite de carga y ciclo. |
| Senalero y exclusion | Prevencion de riesgos | Rigger y area libre de personas. | Escenario con area de exclusion. |
| Ambito portuario | Autoridad Maritima y del puerto | Normas del recinto portuario. | Reglas propias del terminal. |

## Reglas de seguridad

- Verificar limite de carga y estado del spreader antes de izar.
- Respetar el limite de viento del anemometro; detener la operacion si se supera.
- Delimitar el area de exclusion y controlar la presencia de personas en tierra.
- Coordinar cada movimiento con el senalero y con el flujo de camiones.
- No izar sin los twist-locks trabados ni con la carga mal calzada.

## Restricciones

- Operacion solo por personal certificado/competente (detalle por confirmar).
- Operacion segun manual del fabricante y limites del equipo.
- Cumplimiento de las normas del recinto portuario y de la Autoridad Maritima.

## Notas para simulacion

- El nucleo educativo es la seguridad del izaje: limite de carga, viento y area de exclusion.
- Modelar la coordinacion con el senalero y con los camiones.
- Usar avisos educativos en vez de castigos frustrantes.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-portuaria.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-grua-portuaria.md)
