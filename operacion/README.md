# Operación general

Esta carpeta reune criterios comunes para describir cómo se opera cualquier
máquina dentro de la simulación, sin convertirse en un manual real de uso.

## Enfoque

La operación se documenta a nivel general y educativo. No se incluyen
procedimientos reales completos de maquinaria peligrosa ni pasos que permitan
operar sin supervisión. Para uso real se consultan fuentes oficiales vigentes.

## Fases típicas de operación

| Fase | Descripción | Ejemplo genérico |
| --- | --- | --- |
| Inspección previa | Revisar estado antes de arrancar. | Niveles, luces, presión, amarras. |
| Arranque | Poner en marcha los sistemas. | Encendido, chequeo de tablero. |
| Puesta en movimiento | Iniciar el desplazamiento controlado. | Soltar freno, aplicar potencia gradual. |
| Conducción o gobierno | Mantener rumbo y velocidad segura. | Dirección, potencia, lectura de instrumentos. |
| Maniobras | Acciones específicas de cada entorno. | Adelantar, atracar, aterrizar, acoplar. |
| Detención | Reducir y detener de forma segura. | Frenado progresivo, apagado ordenado. |
| Cierre | Dejar la máquina en estado seguro. | Freno de parqueo, corte de energía. |

## Cómo documentar la operación de un vehículo

Cada archivo `operacion/principios-*.md` debería responder:

- ¿Qué revisa el operador antes de arrancar?
- Cómo se pone en marcha la máquina?
- ¿Qué principios físicos gobiernan su movimiento?
- ¿Qué instrumentos se vigilan durante la operación?
- ¿Qué maniobras básicas existen y en que orden?
- Cómo se detiene y se deja segura?
- ¿Qué errores comunes debe evitar el operador?

## Relación con la simulación

Las fases de operación se traducen luego en estados del simulador (por ejemplo
`inspeccion`, `en_marcha`, `maniobra`, `detenido`). Ver
`docs/03-niveles-de-realismo.md` para decidir cuanto detalle simular en cada
nivel.
