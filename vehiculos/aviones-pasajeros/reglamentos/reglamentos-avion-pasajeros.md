# ⚖️ Reglamentos del avión de pasajeros (Chile)

[🏠 Inicio](../../../README.md) · [🛫 Curso: Aviones de pasajeros](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ámbito

- País: Chile.
- Ley base: Ley 18.916 (Código Aeronáutico).
- Autoridad: Dirección General de Aeronáutica Civil (DGAC).
- Marco internacional: OACI / ICAO (Convenio de Chicago, 1944).
- Tipo de operación: transporte aéreo comercial de pasajeros.

## Licencias del personal

- Otorgadas por la DGAC según la reglamentación DAR-01 y normas DAN.
- Para volar un avión de pasajeros en línea se requiere la licencia de **Piloto de
  Transporte de Línea Aérea (ATP)**, el nivel más alto de piloto.
- La ATP exige experiencia y horas de vuelo muy superiores a la PPL o la CPL,
  examenes teóricos y prácticos, y habilitación de vuelo por instrumentos.
- Cada piloto necesita **habilitación de tipo** para el modelo de avión y un
  **certificado médico** aeronáutico de la clase correspondiente vigente.

## Operación comercial (AOC)

- El transporte comercial se realiza bajo un **Certificado de Operador Aéreo
  (AOC)** emitido por la DGAC, que autoriza a la aerolinea a operar.
- La operación se rige por un manual de operaciones, procedimientos aprobados y
  limitaciones de tiempo de servicio de la tripulación.
- La aeronave debe mantener su **certificado de aeronavegabilidad** mediante un
  programa de mantenimiento aprobado.

## Requisitos y normas

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Matrícula | Código Aeronáutico, Art. 32 | Inscripción en el Registro Nacional de Aeronaves. | Estado documental de la aeronave. |
| Aeronavegabilidad | Código Aeronáutico, Art. 52 | Certificado de aeronavegabilidad vigente. | Chequeo previo al vuelo. |
| Licencia ATP | DAR-01 / normas DAN | Piloto de transporte de línea con habilitación de tipo. | Perfil de tripulación del escenario. |
| Operador aéreo | Código Aeronáutico / DAN | Certificado de operador aéreo (AOC) para operar comercial. | Marco de operación de la aerolinea. |
| Espacio aéreo | Código Aeronáutico, Art. 1 | Soberanía y reglas del espacio aéreo. | Reglas de tráfico aéreo del escenario. |
| Reglas de vuelo | Normas DAN | Vuelo por instrumentos (IFR) en operación de línea. | Aproximaciones y aerovias del escenario. |

## Reglas de seguridad

- Volar con licencia ATP, habilitación de tipo y certificado médico vigentes.
- Completar las listas de verificación y el briefing antes de cada fase.
- Respetar el espacio aéreo controlado y las instrucciones del control de tráfico.
- Vigilar combustible, meteorología y peso y balance dentro de límites.
- Operar bajo el AOC y los procedimientos aprobados del operador.

## Restricciones

- Operación de línea solo bajo un certificado de operador aéreo (AOC).
- Limitaciones de tiempo de vuelo y de servicio de la tripulación.
- Reglas de vuelo por instrumentos y mínimos de aeropuerto según la autoridad.
- Zonas restringidas y controladas según la autoridad aeronáutica.

## Notas para simulación

- El núcleo educativo son la operación en tripulación, los instrumentos y los procedimientos.
- Modelar plan de vuelo, comunicaciones, checklist y aproximaciones instrumentales.
- Representar la operación comercial (AOC) como marco, sin datos sensibles reales.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-avion-pasajeros.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-avion-pasajeros.md)
