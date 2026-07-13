# ⚖️ Reglamentos del tren de alta velocidad (Chile)

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseno de simulacion. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Chile aun no
cuenta con alta velocidad comercial, por lo que este modulo trata el marco
ferroviario general y usa estandares internacionales como referencia. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
seccion 1.6 (Ferroviario).

## Ambito

- Pais: Chile.
- Ley base: Ley General de Ferrocarriles (numero y fecha por confirmar).
- Autoridad: MTT como regulador y EFE (Empresa de los Ferrocarriles del Estado)
  como operador estatal historico.
- Tipo de vehiculo: tren de alta velocidad sobre via dedicada.
- No aplica licencia de via publica: la conduccion exige habilitacion o
  certificacion de maquinista (por confirmar).

## Habilitacion y certificacion del maquinista

- No existe una licencia de via publica como en los vehiculos de carretera.
- La conduccion requiere **habilitacion o certificacion de maquinista**, con
  formacion especifica del sistema; los requisitos exactos en Chile quedan por
  confirmar.
- Como referencia se usan los **estandares internacionales de alta velocidad**,
  incluida la senalizacion embarcada ETCS/ERTMS.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicacion en simulacion |
| --- | --- | --- | --- |
| Habilitacion de maquinista | Marco ferroviario (por confirmar) | Certificacion especifica del sistema. | Modo habilitacion antes de conducir. |
| Senalizacion en cabina | Estandar ETCS/ERTMS (referencia) | Respetar la velocidad objetivo del DMI. | Supervision y frenado automatico. |
| Vigilante / hombre muerto | Reglamento de operacion (por confirmar) | Confirmar atencion de forma periodica. | Frenado si no se confirma. |
| Via dedicada | Estandar de alta velocidad (referencia) | Sin pasos a nivel, curvas amplias. | Trazado del escenario sin cruces. |
| Ancho de via | Trocha internacional (referencia) | Valor exacto para Chile por confirmar. | Parametro del escenario. |
| Documentos de operacion | Marco ferroviario (por confirmar) | Autorizacion de circulacion del tren. | Chequeo previo simulado. |

## Reglas de seguridad

- Respetar siempre la velocidad objetivo que muestra la senalizacion en cabina.
- Confirmar el dispositivo de hombre muerto o vigilante de forma periodica.
- Iniciar el frenado con la anticipacion que exige la enorme distancia de frenado.
- Reducir la velocidad ante viento fuerte en viaductos o clima adverso.
- No abrir puertas sin el enclavamiento y con el tren alineado al anden.

## Restricciones

- Conduccion solo por personal habilitado o certificado (por confirmar).
- Circulacion sujeta a la asignacion de via y agujas del control de trafico.
- Limites de velocidad segun el tramo, el clima y el estado de la catenaria.

## Notas para simulacion

- El nucleo educativo es la gestion de la energia cinetica: distancia de frenado,
  aerodinamica y respeto de la senal objetivo.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la supervision ETCS como frenado automatico al exceder el limite.
- Marcar como por confirmar los datos legales locales que aun no existen en Chile.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md). Fuente institucional:
  <https://www.efe.cl>.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-alta-velocidad.md) · [➡️ Siguiente: Diseno de simulacion](../simulacion/diseno-simulador-tren-alta-velocidad.md)
