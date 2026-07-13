# 🧪 Principios y operacion de la grua

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Gruas](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de operador certificado ni
el manual del fabricante. Describe como se opera una grua en simulacion y que
principios fisicos conviene representar. El nucleo es siempre la estabilidad.

## Principios de funcionamiento

- **Momento de carga y palanca**: la carga actua como una palanca sobre el eje de
  giro. El momento es peso por radio; cuanto mas lejos esta la carga, mayor es el
  efecto de vuelco para un mismo peso.
- **Centro de gravedad**: es el punto donde se concentra el peso del conjunto grua
  mas carga. Debe mantenerse siempre dentro de la base de apoyo.
- **Estabilidad y contrapeso**: la grua resiste el vuelco con su propio peso y el
  contrapeso. La estabilidad existe mientras el momento resistente supera al de
  vuelco.
- **Efecto del radio y el angulo**: subir la pluma acerca la carga al eje (menor
  radio, mas capacidad); bajarla o telescopiarla la aleja (mayor radio, menos
  capacidad).
- **Efecto del viento**: el viento empuja la carga y la pluma, aumenta el radio
  efectivo y el balanceo; por eso reduce el limite de izaje.
- **Izaje seguro**: se iza vertical, sin arrastrar la carga, con movimientos
  suaves y coordinados con el personal en tierra.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Planificacion | Estudio del izaje | Peso de la carga, radio, tabla de carga, obstaculos. |
| Posicionamiento | Ubicar la grua | Terreno firme, distancia a la carga y al montaje. |
| Estabilizacion | Extender outriggers | Nivelar la maquina y apoyar zapatas. |
| Izaje | Levantar la carga | Verificar LMI, izar vertical, sin tirones. |
| Traslado de carga | Girar y mover | Movimiento lento, controlar balanceo y radio. |
| Descenso | Depositar la carga | Bajar suave, coordinar con senalero. |
| Repliegue | Cierre de la maniobra | Recoger pluma, estabilizadores y bloquear giro. |

## Izaje seguro: idea general

1. Calcular el **peso real** de la carga y el **radio** de trabajo.
2. Consultar la **tabla de carga** y confirmar que hay margen.
3. **Estabilizar y nivelar** la grua antes de cargar el gancho.
4. Izar **vertical**, sin arrastrar, vigilando el **LMI**.
5. Girar y trasladar con **movimientos lentos** para no balancear la carga.
6. Descender de forma controlada y **coordinar** con el senalero en tierra.

## Errores comunes que la simulacion puede ensenar a evitar

- Izar sin extender o nivelar los estabilizadores.
- Superar el radio maximo de la tabla al bajar o telescopiar la pluma.
- Arrastrar la carga de lado en vez de izar vertical.
- Girar demasiado rapido y provocar balanceo peligroso.
- Ignorar el viento o el aviso del LMI.
- No confirmar el peso real de la carga antes de izar.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: estabilizar, izar, girar y depositar respetando el LMI.
- **Nivel 2 (simplificado)**: agregar radio, angulo, tabla de carga y balanceo.
- **Nivel 3 (tecnico)**: sumar viento, capacidad del terreno, reeving y margenes
  de momento de carga.

En todos los niveles el nucleo educativo es la **estabilidad**: entender que cada
movimiento cambia el radio y, con el, cuanto peso se puede sostener. Ver
[`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el
detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-grua.md) · [➡️ Siguiente: Entornos de trabajo](entornos-grua.md)
