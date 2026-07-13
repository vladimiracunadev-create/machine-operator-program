# 🧪 Principios y operacion del helicoptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicopteros](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye una instruccion de vuelo certificada
ni el manual del fabricante. Describe como se opera un helicoptero en simulacion y
que principios fisicos conviene representar.

## Principios de funcionamiento

- **Sustentacion del rotor**: las palas son alas que giran; al aumentar su paso o
  su regimen, crean la fuerza que sostiene la aeronave.
- **Traslacion**: al inclinar el disco rotor con el ciclico, parte de la
  sustentacion se convierte en traccion horizontal y el helicoptero se desplaza.
- **Par y anti-par**: el motor que gira el rotor tiende a girar el fuselaje; el
  rotor de cola compensa ese par y controla la guinada.
- **Vuelo estacionario (hover)**: equilibrio fino entre sustentacion, peso, par y
  anti-par para mantenerse inmovil sobre un punto.
- **Disimetria de sustentacion**: en vuelo hacia adelante, la pala que avanza
  recibe mas aire que la que retrocede; la articulacion de las palas equilibra ese
  desnivel para que el vuelo sea estable.
- **Autorrotacion**: sin motor, el flujo de aire que sube por el rotor lo mantiene
  girando y permite un descenso controlado.
- **Efecto suelo**: cerca del terreno, la sustentacion aumenta y el estacionario
  cuesta menos potencia.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Palas, rotor de cola, niveles, combustible, mandos. |
| Arranque de rotor | Encender y estabilizar el rotor | Rotor RPM en rango antes de despegar. |
| Despegue vertical | Elevarse sobre el punto | Subir colectivo, compensar par con pedal. |
| Vuelo estacionario | Mantenerse inmovil | Coordinar colectivo, ciclico y pedales. |
| Crucero | Desplazamiento sostenido | Ciclico adelante, vigilar velocidad y altitud. |
| Aproximacion | Preparar aterrizaje | Reducir velocidad hasta el estacionario. |
| Aterrizaje | Posarse con suavidad | Descenso controlado, uso del efecto suelo. |

## Tecnica clave: el vuelo estacionario

1. Ajustar el **colectivo** para que la sustentacion iguale el peso.
2. Usar el **ciclico** con pequenos movimientos para no derivar sobre el punto.
3. Compensar el **par** con los **pedales** para mantener la nariz fija.
4. Vigilar el **rotor RPM** y el **variometro** cerca de cero.
5. Corregir de forma continua: los tres mandos se influyen entre si.

## Errores comunes que la simulacion puede ensenar a evitar

- Subir colectivo sin compensar el par con el pedal.
- Sobrecontrolar el ciclico y provocar oscilaciones en el estacionario.
- Dejar caer el rotor RPM fuera de su rango de seguridad.
- Olvidar el efecto suelo al comparar potencia en altura y cerca del terreno.
- No practicar la entrada en autorrotacion ante un fallo de motor.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: elevar, mantener el hover, trasladar y posar.
- **Nivel 2 (simplificado)**: agregar par, anti-par y efecto suelo.
- **Nivel 3 (tecnico)**: sumar rotor RPM, disimetria de sustentacion y
  autorrotacion.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-helicoptero.md) · [➡️ Siguiente: Entornos de trabajo](entornos-helicoptero.md)
