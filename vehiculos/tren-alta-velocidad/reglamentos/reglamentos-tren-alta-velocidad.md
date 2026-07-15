# ⚖️ Reglamentos del tren de alta velocidad (Chile)

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Chile aún no
cuenta con alta velocidad comercial, por lo que este módulo trata el marco
ferroviario general y usa estandares internacionales como referencia. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Autoridad: MTT como regulador y EFE (Empresa de los Ferrocarriles del Estado)
  como operador estatal histórico.
- Tipo de vehículo: tren de alta velocidad sobre vía dedicada.
- No aplica licencia de vía pública: la conducción exige habilitación o
  certificación de maquinista (por confirmar).

## Habilitación y certificación del maquinista

- No existe una licencia de vía pública como en los vehículos de carretera.
- La conducción requiere **habilitación o certificación de maquinista**, con
  formación específica del sistema; los requisitos exactos en Chile quedan por
  confirmar.
- Como referencia se usan los **estandares internacionales de alta velocidad**,
  incluida la señalización embarcada ETCS/ERTMS.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Habilitación de maquinista | Marco ferroviario (por confirmar) | Certificación específica del sistema. | Modo habilitación antes de conducir. |
| Señalización en cabina | Estandar ETCS/ERTMS (referencia) | Respetar la velocidad objetivo del DMI. | Supervisión y frenado automático. |
| Vigilante / hombre muerto | Reglamento de operación (por confirmar) | Confirmar atención de forma periódica. | Frenado si no se confirma. |
| Vía dedicada | Estandar de alta velocidad (referencia) | Sin pasos a nivel, curvas amplias. | Trazado del escenario sin cruces. |
| Ancho de vía | Trocha internacional (referencia) | Valor exacto para Chile por confirmar. | Parámetro del escenario. |
| Documentos de operación | Marco ferroviario (por confirmar) | Autorización de circulación del tren. | Chequeo previo simulado. |

## Reglas de seguridad

- Respetar siempre la velocidad objetivo que muestra la señalización en cabina.
- Confirmar el dispositivo de hombre muerto o vigilante de forma periódica.
- Iniciar el frenado con la anticipación que exige la enorme distancia de frenado.
- Reducir la velocidad ante viento fuerte en viaductos o clima adverso.
- No abrir puertas sin el enclavamiento y con el tren alineado al andén.

## Restricciones

- Conducción solo por personal habilitado o certificado (por confirmar).
- Circulación sujeta a la asignación de vía y agujas del control de tráfico.
- Límites de velocidad según el tramo, el clima y el estado de la catenaria.

## Notas para simulación

- El núcleo educativo es la gestión de la energía cinética: distancia de frenado,
  aerodinámica y respeto de la señal objetivo.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la supervisión ETCS como frenado automático al exceder el límite.
- Marcar como por confirmar los datos legales locales que aún no existen en Chile.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md). Fuente institucional:
  <https://www.efe.cl>.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-alta-velocidad.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-alta-velocidad.md)
