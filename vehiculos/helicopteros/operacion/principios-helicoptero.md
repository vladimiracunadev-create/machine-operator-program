# 🧪 Principios y operación del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye una instrucción de vuelo certificada
ni el manual del fabricante. Describe cómo se opera un helicóptero en simulación y
que principios físicos conviene representar.

## Principios de funcionamiento

- **Sustentación del rotor**: las palas son alas que giran; al aumentar su paso o
  su régimen, crean la fuerza que sostiene la aeronave.
- **Traslación**: al inclinar el disco rotor con el cíclico, parte de la
  sustentación se convierte en tracción horizontal y el helicóptero se desplaza.
- **Par y anti-par**: el motor que gira el rotor tiende a girar el fuselaje; el
  rotor de cola compensa ese par y controla la guiñada.
- **Vuelo estacionario (hover)**: equilibrio fino entre sustentación, peso, par y
  anti-par para mantenerse inmóvil sobre un punto.
- **Disimetría de sustentación**: en vuelo hacia adelante, la pala que avanza
  recibe más aire que la que retrocede; la articulación de las palas equilibra ese
  desnivel para que el vuelo sea estable.
- **Autorrotación**: sin motor, el flujo de aire que sube por el rotor lo mantiene
  girando y permite un descenso controlado.
- **Efecto suelo**: cerca del terreno, la sustentación aumenta y el estacionario
  cuesta menos potencia.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Palas, rotor de cola, niveles, combustible, mandos. |
| Arranque de rotor | Encender y estabilizar el rotor | Rotor RPM en rango antes de despegar. |
| Despegue vertical | Elevarse sobre el punto | Subir colectivo, compensar par con pedal. |
| Vuelo estacionario | Mantenerse inmóvil | Coordinar colectivo, cíclico y pedales. |
| Crucero | Desplazamiento sostenido | Cíclico adelante, vigilar velocidad y altitud. |
| Aproximación | Preparar aterrizaje | Reducir velocidad hasta el estacionario. |
| Aterrizaje | Posarse con suavidad | Descenso controlado, uso del efecto suelo. |

## Técnica clave: el vuelo estacionario

1. Ajustar el **colectivo** para que la sustentación iguale el peso.
2. Usar el **cíclico** con pequeños movimientos para no derivar sobre el punto.
3. Compensar el **par** con los **pedales** para mantener la nariz fija.
4. Vigilar el **rotor RPM** y el **variómetro** cerca de cero.
5. Corregir de forma continua: los tres mandos se influyen entre sí.

## Errores comunes que la simulación puede enseñar a evitar

- Subir colectivo sin compensar el par con el pedal.
- Sobrecontrolar el cíclico y provocar oscilaciones en el estacionario.
- Dejar caer el rotor RPM fuera de su rango de seguridad.
- Olvidar el efecto suelo al comparar potencia en altura y cerca del terreno.
- No practicar la entrada en autorrotación ante un fallo de motor.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: elevar, mantener el hover, trasladar y posar.
- **Nivel 2 (simplificado)**: agregar par, anti-par y efecto suelo.
- **Nivel 3 (técnico)**: sumar rotor RPM, disimetría de sustentación y
  autorrotación.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-helicoptero.md) · [➡️ Siguiente: Entornos de trabajo](entornos-helicoptero.md)
