# Operacion general

Esta carpeta reune criterios comunes para describir como se opera cualquier
maquina dentro de la simulacion, sin convertirse en un manual real de uso.

## Enfoque

La operacion se documenta a nivel general y educativo. No se incluyen
procedimientos reales completos de maquinaria peligrosa ni pasos que permitan
operar sin supervision. Para uso real se consultan fuentes oficiales vigentes.

## Fases tipicas de operacion

| Fase | Descripcion | Ejemplo generico |
| --- | --- | --- |
| Inspeccion previa | Revisar estado antes de arrancar. | Niveles, luces, presion, amarras. |
| Arranque | Poner en marcha los sistemas. | Encendido, chequeo de tablero. |
| Puesta en movimiento | Iniciar el desplazamiento controlado. | Soltar freno, aplicar potencia gradual. |
| Conduccion o gobierno | Mantener rumbo y velocidad segura. | Direccion, potencia, lectura de instrumentos. |
| Maniobras | Acciones especificas de cada entorno. | Adelantar, atracar, aterrizar, acoplar. |
| Detencion | Reducir y detener de forma segura. | Frenado progresivo, apagado ordenado. |
| Cierre | Dejar la maquina en estado seguro. | Freno de parqueo, corte de energia. |

## Como documentar la operacion de un vehiculo

Cada archivo `operacion/principios-*.md` deberia responder:

- Que revisa el operador antes de arrancar?
- Como se pone en marcha la maquina?
- Que principios fisicos gobiernan su movimiento?
- Que instrumentos se vigilan durante la operacion?
- Que maniobras basicas existen y en que orden?
- Como se detiene y se deja segura?
- Que errores comunes debe evitar el operador?

## Relacion con la simulacion

Las fases de operacion se traducen luego en estados del simulador (por ejemplo
`inspeccion`, `en_marcha`, `maniobra`, `detenido`). Ver
`docs/03-niveles-de-realismo.md` para decidir cuanto detalle simular en cada
nivel.
