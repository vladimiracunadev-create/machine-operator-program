# 🎮 Diseno de simulacion del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🎮 Simulacion

```mermaid
stateDiagram-v2
    [*] --> Apagado
    Apagado --> CargandoAire: encender
    CargandoAire --> Preparado: presion normal
    Preparado --> EnServicio: soltar freno + acelerar
    EnServicio --> EnParada: detener y abrir puertas
    EnParada --> EnServicio: cerrar puertas + acelerar
    EnServicio --> Emergencia: riesgo o falla
    Emergencia --> Preparado: orillar y controlar
    Preparado --> Apagado: apagar
    Apagado --> [*]
```

## Objetivo de la simulacion

Que el usuario aprenda a conducir un bus de forma segura y suave: gestionar la
gran masa, frenar con antelacion pensando en los pasajeros de pie, aproximarse a
las paradas, operar las puertas con enclavamiento y respetar las normas del
transporte publico.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificacion: el bus suma sobre la moto la gestion de masa, el sistema
  neumatico y la operacion con pasajeros, por lo que se ubica en dificultad
  intermedia dentro del catalogo.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numerica | 0-100 km/h | Movimiento y frenado | Central para todo. |
| Aforo | numerica | 0-100% | Inercia y confort | Pasajeros sentados y de pie. |
| Presion de aire | numerica | 0-12 bar | Frenos, puertas, suspension | No arrancar bajo el minimo. |
| Estado de puertas | discreta | abiertas/cerradas | Enclavamiento de marcha | Bloquea avance si abiertas. |
| Marcha | discreta | R,N,D | Sentido de la marcha | Automatica, sin embrague. |
| Retardador | discreta | 0..3 niveles | Frenado sin friccion | Para descensos largos. |
| Adherencia | numerica | 0-1 | Freno y giro | Baja con lluvia. |
| Combustible/energia | numerica | 0-100% | Autonomia | Diesel, gas o bateria. |

## Ciclo basico

1. Leer entrada del usuario (acelerador, freno, retardador, direccion, puertas).
2. Actualizar estado del motor, transmision y presion de aire.
3. Calcular fuerzas: propulsion, frenado, inercia de la masa y adherencia.
4. Aplicar restricciones del entorno (piso, pendiente, clima) y el aforo.
5. Verificar enclavamientos (no avanzar con puertas abiertas o sin presion).
6. Actualizar velocidad y posicion; refrescar instrumentos y confort del pasaje.

## Modos de juego futuros

- Tutorial guiado de mandos y sistema neumatico.
- Practica libre en un circuito cerrado con paradas.
- Misiones de ruta urbana con horarios y aforo.
- Desafios de frenado suave con pasajeros de pie.
- Situaciones de accesibilidad (rampa y arrodillamiento) y descensos con retardador.

## Elementos fuera de alcance

- Conduccion temeraria o a exceso de velocidad presentada como objetivo.
- Sobrecarga de pasajeros mostrada como algo positivo.
- Datos tecnicos que permitan alterar sistemas reales de un bus.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de bus.
- [ ] Prototipar el ciclo basico con el sistema neumatico simplificado.
- [ ] Modelar el enclavamiento de puertas y el arrodillamiento.
- [ ] Agregar fuentes tecnicas publicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-bus.md) · [➡️ Siguiente: Recursos](../recursos/recursos-bus.md)
