# ⚖️ Reglamentos de la grua torre (Chile)

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grua torre](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
operar se deben consultar la autoridad laboral y la normativa vigente. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
seccion 1.7 (Maquinaria de izaje fija).

## Ambito

- Pais: Chile.
- Marco base: seguridad laboral, no Ley de Transito. La grua torre es una grua
  fija que NO circula por via publica y NO requiere licencia de conducir.
- Leyes de referencia: Ley 16.744 (accidentes del trabajo) y D.S. 594 (MINSAL,
  condiciones sanitarias y ambientales en los lugares de trabajo).
- Autoridad: Direccion del Trabajo y mutuales (seguridad laboral); MINSAL
  (condiciones de trabajo).
- Tipo de vehiculo: maquinaria de izaje fija.

## Habilitacion y certificacion

- No se necesita licencia de conducir: la grua no circula por via publica.
- La operacion la realiza personal **certificado/competente**, no un conductor.
- Se opera con un **plan de izaje** y las tablas de carga del fabricante.
- Un **senalero (rigger)** coordina la maniobra desde tierra.
- Los detalles de certificacion del operador estan por confirmar (ver marco legal).

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Seguro laboral | Ley 16.744 | Cobertura de accidentes del trabajo. | Contexto de seguridad del escenario. |
| Condiciones de trabajo | D.S. 594 (MINSAL) | Condiciones sanitarias y ambientales basicas. | Reglas de entorno de la obra. |
| Operador competente | Marco laboral (por confirmar) | Operador certificado/competente. | Modo habilitacion por competencia. |
| Plan de izaje | Marco laboral | Plan con carga, radio, viento y area. | Chequeo previo simulado. |
| Senalero y area de exclusion | Marco laboral | Rigger y zona despejada bajo el giro. | Modelo de area de exclusion. |
| Montaje y desmontaje | Marco laboral (por confirmar) | Operacion critica con personal competente. | Escenario de trepado controlado. |

## Reglas de seguridad

- Verificar peso, radio y tabla de carga antes de cada izaje.
- Nivelar y anclar la base; confirmar el arriostramiento en grandes alturas.
- Delimitar el area de exclusion bajo la zona de giro y controlar personas.
- Respetar el limite de viento y pasar a veleta fuera de servicio.
- Tratar el montaje y el desmontaje como operacion critica con personal competente.

## Restricciones

- No circula por via publica: sin licencia de conducir.
- Operacion segun manual del fabricante y limites de la maquina.
- Montaje y desmontaje solo con personal competente (por confirmar).

## Notas para simulacion

- El nucleo educativo es la estabilidad: momento de carga, radio y viento.
- Modelar el area de exclusion, el senalero y el limite de viento.
- Marcar como "(por confirmar)" la certificacion del operador y las reglas de montaje.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-grua-torre.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-grua-torre.md)
