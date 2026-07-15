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
- El detalle de certificación del operador esta **(por confirmar)** en el marco
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

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-portuaria.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md)
