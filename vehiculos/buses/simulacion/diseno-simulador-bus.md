---
tipo_documento: clase
clase: 9
codigo: BUSES-09
curso: buses
titulo: "Diseño de simulación del bus"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: BUSES-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Buses."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Buses."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🎮 Simulación

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

## Objetivo de la simulación

Que el usuario aprenda a conducir un bus de forma segura y suave: gestionar la
gran masa, frenar con antelación pensando en los pasajeros de pie, aproximarse a
las paradas, operar las puertas con enclavamiento y respetar las normas del
transporte público.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el bus suma sobre la moto la gestión de masa, el sistema
  neumático y la operación con pasajeros, por lo que se ubica en dificultad
  intermedia dentro del catálogo.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-100 km/h | Movimiento y frenado | Central para todo. |
| Aforo | numérica | 0-100% | Inercia y confort | Pasajeros sentados y de pie. |
| Presión de aire | numérica | 0-12 bar | Frenos, puertas, suspensión | No arrancar bajo el mínimo. |
| Estado de puertas | discreta | abiertas/cerradas | Enclavamiento de marcha | Bloquea avance si abiertas. |
| Marcha | discreta | R,N,D | Sentido de la marcha | Automática, sin embrague. |
| Retardador | discreta | 0..3 niveles | Frenado sin fricción | Para descensos largos. |
| Adherencia | numérica | 0-1 | Freno y giro | Baja con lluvia. |
| Combustible/energía | numérica | 0-100% | Autonomía | Diesel, gas o batería. |

## Ciclo básico

1. Leer entrada del usuario (acelerador, freno, retardador, dirección, puertas).
2. Actualizar estado del motor, transmisión y presión de aire.
3. Calcular fuerzas: propulsión, frenado, inercia de la masa y adherencia.
4. Aplicar restricciones del entorno (piso, pendiente, clima) y el aforo.
5. Verificar enclavamientos (no avanzar con puertas abiertas o sin presión).
6. Actualizar velocidad y posición; refrescar instrumentos y confort del pasaje.

## Modos de juego futuros

- Tutorial guiado de mandos y sistema neumático.
- Práctica libre en un circuito cerrado con paradas.
- Misiones de ruta urbana con horarios y aforo.
- Desafíos de frenado suave con pasajeros de pie.
- Situaciones de accesibilidad (rampa y arrodillamiento) y descensos con retardador.

## Elementos fuera de alcance

- Conducción temeraria o a exceso de velocidad presentada como objetivo.
- Sobrecarga de pasajeros mostrada como algo positivo.
- Datos técnicos que permitan alterar sistemas reales de un bus.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de bus.
- [ ] Prototipar el ciclo básico con el sistema neumático simplificado.
- [ ] Modelar el enclavamiento de puertas y el arrodillamiento.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Buses basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-bus.md) · [➡️ Siguiente: Recursos](../recursos/recursos-bus.md)
