# 🧪 Principios y operación de la Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación de un piloto de
competición ni la ingeniería de un equipo real. Describe cómo se opera un
monoplaza en simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Propulsión**: la unidad híbrida entrega par a las ruedas traseras; el
  acelerador y la gestión de energía regulan esa entrega.
- **Carga aerodinámica**: la aerodinámica y el efecto suelo aumentan el agarre
  con la velocidad, permitiendo curvas más rápidas.
- **Frenada**: los frenos de carbono y la recuperación del MGU-K desaceleran el
  coche con fuerzas de varias g.
- **Adherencia**: el neumático, dentro de su ventana de temperatura, limita
  cuanta aceleración, frenada y giro son posibles antes de deslizar.
- **Gestión de energía**: la batería se carga y descarga por vuelta; usarla bien
  marca el tiempo.

## Fases de una vuelta

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Recta | Máxima velocidad | Desplegar energía, DRS si está habilitado. |
| Frenada | Reducir antes de curva | Frenar fuerte y recto, bajar marchas. |
| Entrada | Girar hacia el vértice | Soltar freno de forma progresiva. |
| Vértice | Punto más interior | Velocidad mínima justa, buscar tracción. |
| Salida | Acelerar hacia la recta | Abrir acelerador sin perder el eje trasero. |
| Gestión | Cuidar el coche | Neumáticos, frenos y energía dentro de rango. |

## Una curva rápida: idea general

1. Frenar fuerte y en línea recta antes de la curva.
2. Bajar las marchas necesarias mientras se frena.
3. Soltar el freno de forma progresiva al girar hacia el vértice.
4. Pasar por el vértice a la velocidad mínima justa.
5. Acelerar de forma progresiva a la salida cuidando el agarre trasero.

## Errores comunes que la simulación puede enseñar a evitar

- Frenar demasiado tarde y pasarse de la curva.
- Bloquear un neumático por exceso de freno o goma fría.
- Acelerar de golpe a la salida y perder el eje trasero.
- Malgastar la energía ERS y quedar sin impulso en la recta.
- Ignorar la ventana de temperatura de neumáticos y frenos.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar, girar y seguir la trazada.
- **Nivel 2 (simplificado)**: agregar carga aerodinámica, degradación de gomas y
  límite de adherencia.
- **Nivel 3 (técnico)**: sumar gestión de energía ERS, reparto de frenada,
  ventanas de temperatura y estrategia de neumáticos.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-formula-1.md) · [➡️ Siguiente: Entornos de trabajo](entornos-formula-1.md)
