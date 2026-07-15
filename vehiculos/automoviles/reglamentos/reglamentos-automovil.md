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

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-automovil.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-automovil.md)
