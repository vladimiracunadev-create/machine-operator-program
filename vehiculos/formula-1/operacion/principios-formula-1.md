# 🧪 Principios y operacion de la Formula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Formula 1](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion de un piloto de
competicion ni la ingenieria de un equipo real. Describe como se opera un
monoplaza en simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Propulsion**: la unidad hibrida entrega par a las ruedas traseras; el
  acelerador y la gestion de energia regulan esa entrega.
- **Carga aerodinamica**: la aerodinamica y el efecto suelo aumentan el agarre
  con la velocidad, permitiendo curvas mas rapidas.
- **Frenada**: los frenos de carbono y la recuperacion del MGU-K desaceleran el
  coche con fuerzas de varias g.
- **Adherencia**: el neumatico, dentro de su ventana de temperatura, limita
  cuanta aceleracion, frenada y giro son posibles antes de deslizar.
- **Gestion de energia**: la bateria se carga y descarga por vuelta; usarla bien
  marca el tiempo.

## Fases de una vuelta

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Recta | Maxima velocidad | Desplegar energia, DRS si esta habilitado. |
| Frenada | Reducir antes de curva | Frenar fuerte y recto, bajar marchas. |
| Entrada | Girar hacia el vertice | Soltar freno de forma progresiva. |
| Vertice | Punto mas interior | Velocidad minima justa, buscar traccion. |
| Salida | Acelerar hacia la recta | Abrir acelerador sin perder el eje trasero. |
| Gestion | Cuidar el coche | Neumaticos, frenos y energia dentro de rango. |

## Una curva rapida: idea general

1. Frenar fuerte y en linea recta antes de la curva.
2. Bajar las marchas necesarias mientras se frena.
3. Soltar el freno de forma progresiva al girar hacia el vertice.
4. Pasar por el vertice a la velocidad minima justa.
5. Acelerar de forma progresiva a la salida cuidando el agarre trasero.

## Errores comunes que la simulacion puede ensenar a evitar

- Frenar demasiado tarde y pasarse de la curva.
- Bloquear un neumatico por exceso de freno o goma fria.
- Acelerar de golpe a la salida y perder el eje trasero.
- Malgastar la energia ERS y quedar sin impulso en la recta.
- Ignorar la ventana de temperatura de neumaticos y frenos.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y seguir la trazada.
- **Nivel 2 (simplificado)**: agregar carga aerodinamica, degradacion de gomas y
  limite de adherencia.
- **Nivel 3 (tecnico)**: sumar gestion de energia ERS, reparto de frenada,
  ventanas de temperatura y estrategia de neumaticos.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-formula-1.md) · [➡️ Siguiente: Entornos de trabajo](entornos-formula-1.md)
