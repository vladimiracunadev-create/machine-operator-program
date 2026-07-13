# Principios y operacion: moto

Documento general y educativo. No sustituye un curso de conduccion certificado
ni el manual del fabricante. Describe como se opera una moto en simulacion y que
principios fisicos conviene representar.

## Principios de funcionamiento

- **Propulsion**: un motor (de combustion o electrico) entrega par a la rueda
  trasera a traves de la transmision. El acelerador regula esa entrega.
- **Direccion**: a baja velocidad se gira el manillar; a velocidad de marcha la
  moto cambia de rumbo sobre todo por inclinacion y contramanillar.
- **Equilibrio**: la estabilidad aumenta con la velocidad por el efecto
  giroscopico de las ruedas y la geometria de la direccion.
- **Frenado**: el freno delantero aporta la mayor parte de la capacidad de
  detencion porque el peso se transfiere hacia adelante al frenar.
- **Adherencia**: el agarre de los neumaticos limita cuanta aceleracion,
  frenado e inclinacion son posibles antes de perder control.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Neumaticos, luces, frenos, combustible, espejos. |
| Arranque | Encender el motor | Punto muerto o embrague, corte de motor desactivado. |
| Puesta en marcha | Iniciar movimiento | Primera marcha, soltar embrague mientras se acelera suave. |
| Conduccion | Circular con seguridad | Mirar lejos, mantener distancia, usar ambos frenos. |
| Maniobras | Curvas y cambios | Reducir antes de la curva, inclinar, acelerar a la salida. |
| Detencion | Parar de forma segura | Frenar progresivo, bajar marchas, dejar en primera o neutro. |
| Cierre | Dejar segura | Caballete, motor apagado, luces off. |

## Curvas: idea general

1. Ajustar la velocidad **antes** de entrar a la curva.
2. Mirar hacia la salida, no a la rueda delantera.
3. Inclinar la moto de forma progresiva.
4. Mantener o abrir suavemente el acelerador dentro de la curva.
5. Enderezar y acelerar a la salida.

## Errores comunes que la simulacion puede ensenar a evitar

- Usar solo el freno trasero en una detencion fuerte.
- Cerrar el acelerador de golpe en plena curva.
- Cambiar de marcha sin embrague en niveles realistas.
- Mirar demasiado cerca en vez de anticipar.
- Ignorar la transferencia de peso al frenar o acelerar.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y respetar senales.
- **Nivel 2 (simplificado)**: agregar inercia, transferencia de peso y limite
  de adherencia.
- **Nivel 3 (tecnico)**: sumar embrague, marchas, regimen del motor y frenada
  combinada.

Ver `docs/03-niveles-de-realismo.md` para el detalle de cada nivel.
