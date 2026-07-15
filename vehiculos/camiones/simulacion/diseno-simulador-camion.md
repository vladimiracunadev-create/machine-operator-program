# 🎮 Diseño de simulación del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Apagado
    Apagado --> CargandoAire: encender motor
    CargandoAire --> Preparado: presion minima alcanzada
    Preparado --> EnMovimiento: soltar estacionamiento + acelerar
    EnMovimiento --> Preparado: detener
    EnMovimiento --> Emergencia: riesgo o falla
    Emergencia --> Preparado: orillar y controlar
    Preparado --> Apagado: apagar
    Apagado --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a operar un camión con seguridad: cargar el aire, elegir
marchas, gestionar la inercia de la masa, frenar con freno de motor y retarder en
pendiente, repartir la carga y maniobrar un vehículo articulado respetando el
barrido trasero.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el camión introduce la gestión de gran masa, el frenado
  neumático y la articulación, conceptos más complejos que los de la moto pero
  sin la carga de trabajo especializada de una grúa.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-100 km/h | Movimiento y frenado | Limitada por vía y carga. |
| Régimen del motor | numérica | 0-2500 rpm | Par disponible | El diesel gira bajo. |
| Marcha | discreta | N,1..16 | Fuerza y velocidad | Con gama alta/baja. |
| Carga | numérica | 0-100% del PBV | Inercia y frenado | Define distancia de frenado. |
| Reparto por eje | numérica | por eje | Agarre y legalidad | No debe exceder el límite por eje. |
| Presión de aire | numérica | 0-12 bar | Frenos | Bajo el mínimo no se circula. |
| Ángulo de articulación | numérica | -90..90 grados | Maniobra del semi | Riesgo de tijera si es extremo. |
| Adherencia | numérica | 0-1 | Freno, giro, tracción | Baja con lluvia y tierra. |

## Ciclo básico

1. Leer entrada del usuario (acelerador, frenos, retarder, marcha, dirección).
2. Actualizar estado del motor, la caja y la presión de aire.
3. Calcular fuerzas: propulsión, frenado combinado, gravedad y adherencia.
4. Aplicar restricciones del entorno (pendiente, superficie, clima, carga).
5. Actualizar velocidad, posición y ángulo de articulación.
6. Refrescar instrumentos y retroalimentación (sonido, testigos, avisos).

## Modos de juego futuros

- Tutorial guiado de mandos y carga de aire.
- Práctica de descenso de montaña con freno de motor y retarder.
- Misiones de reparto urbano con maniobras y puntos ciegos.
- Desafíos de estacionamiento y enganche del semirremolque.
- Reparto de carga por eje sin superar límites.

## Elementos fuera de alcance

- Conducción temeraria o exceso de velocidad presentados como objetivo.
- Sobrecarga deliberada como logro del juego.
- Datos que permitan alterar sistemas reales de frenado o emisiones.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de camión.
- [ ] Prototipar el modelo de presión de aire y frenado combinado.
- [ ] Ajustar el modelo de articulación y el efecto de tijera.
- [ ] Agregar fuentes técnicas públicas a
      [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-camion.md) · [➡️ Siguiente: Recursos](../recursos/recursos-camion.md)
