# Reglamentos: automovil (Chile)

Referencia educativa y de diseno de simulacion. Marco general en
[`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md).

## Ambito

- Pais: Chile.
- Ley base: Ley 18.290 (Ley de Transito).
- Autoridad: CONASET, MTT, municipalidades, Carabineros.
- Tipo de vehiculo: automovil o camioneta particular hasta 3.500 kg.

## Licencia

- Clase **B** (no profesional), Ley 18.290 Art. 12.
- Edad minima: 18 anos (Art. 13).
- Habilita vehiculos de 3 o mas ruedas, hasta 9 asientos o carga hasta 3.500 kg.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Cinturon | Ley 18.290, Art. 79 | Obligatorio en asientos delanteros y traseros segun ano. | Exigir cinturon antes de partir. |
| Retencion infantil | Ley 20.904 (Art. 75) | Silla para ninos hasta 8 anos; menores de 12 atras. | Escenario con pasajeros infantiles. |
| Documentos | Ley 18.290 / Ley 18.490 | Padron, permiso de circulacion, revision tecnica, SOAP. | Chequeo previo simulado. |
| Velocidad urbana | Ley 21.103 | 50 km/h general. | Limite del escenario urbano. |
| Alcohol | Ley 20.770 (Ley Emilia) | Sanciones por conducir bajo la influencia del alcohol. | Modo educativo sobre consecuencias. |

## Reglas de seguridad

- Uso obligatorio de cinturon en todos los asientos ocupados.
- Respetar senales, semaforos y prioridades de paso.
- Mantener distancia de seguimiento y velocidad prudente.
- No usar el telefono mientras se conduce.

## Restricciones

- Edad minima 18 anos para licencia clase B.
- Menores de 12 anos deben viajar en el asiento trasero.
- Zonas con limites y restricciones segun senalizacion municipal.

## Notas para simulacion

- Modelar cinturon, retencion infantil y respeto de senales.
- Usar avisos educativos ante infracciones.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).
