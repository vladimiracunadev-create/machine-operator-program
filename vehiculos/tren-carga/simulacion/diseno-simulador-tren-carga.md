---
tipo_documento: clase
clase: 9
codigo: TRENCARGA-09
curso: tren-carga
titulo: "Diseño de simulación del tren de carga"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: TRENCARGA-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Tren de carga."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de carga."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del tren de carga

[🏠 Inicio](../../../README.md) · [🚂 Curso: Tren de carga](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Detenido
    Detenido --> Preparado: cargar aire de freno
    Preparado --> EnMarcha: aplicar traccion
    EnMarcha --> Frenando: freno dinamico o neumatico
    Frenando --> Detenido: velocidad cero
    EnMarcha --> Emergencia: riesgo o falla
    Emergencia --> Detenido: freno de emergencia
    Detenido --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a arrancar con gran carga usando arenado, a mantener la
velocidad respetando la señalización, a anticipar la larga distancia de frenado y
a manejar las fuerzas longitudinales del tren, de forma segura y progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el tren de carga lleva al extremo la gestión de masa, por eso se
  ubica como vehículo avanzado, después de la moto y del camión.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-120 km/h | Movimiento y frenado | Central para respetar la vía. |
| Esfuerzo de tracción | numérica | 0-100% | Aceleración | Limitado por la adherencia. |
| Presión de tubería de freno | numérica | 0-10 bar | Frenado del tren | Bajo el mínimo no se debe circular. |
| Adherencia rueda-riel | numérica | 0-1 | Tracción y frenado | Baja con lluvia; sube con arenado. |
| Masa total | numérica | fija + carga | Inercia y frenado | Miles de toneladas según composición. |
| Fuerza longitudinal | numérica | tensión/compresión | Enganches y estabilidad | Riesgo de rotura o descarrilo. |
| Pendiente | numérica | -grados..+grados | Empuje y retención | La carga empuja en bajada. |

## Ciclo básico

1. Leer entrada del usuario (tracción, freno automático, freno independiente, freno dinámico, arenado, sentido).
2. Actualizar estado de tracción y de la tubería de freno en todo el tren.
3. Calcular fuerzas: tracción, frenado, gravedad en pendiente y adherencia.
4. Calcular las fuerzas longitudinales entre vagones (tensión y compresión).
5. Aplicar restricciones del entorno (vía, pendiente, clima, señalización).
6. Actualizar velocidad y posición sobre la vía.
7. Refrescar instrumentos y retroalimentación (sonido, testigos, patinaje).

## Modos de juego futuros

- Tutorial guiado del puesto del maquinista.
- Práctica libre en un corredor de carga.
- Misiones de armado de tren en patio de maniobras.
- Desafíos de frenado y anticipación en pendiente.
- Situaciones de baja adherencia (riel húmedo) sin contenido sensible.

## Elementos fuera de alcance

- Maniobras peligrosas presentadas como recomendables.
- Reproducción de operación temeraria como objetivo del juego.
- Datos técnicos que permitan alterar sistemas reales de un tren.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de tren.
- [ ] Prototipar el ciclo básico en un motor simple.
- [ ] Ajustar el modelo de adherencia rueda-riel con lluvia y arenado.
- [ ] Modelar las fuerzas longitudinales entre vagones.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Tren de carga basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-tren-carga.md) · [➡️ Siguiente: Recursos](../recursos/recursos-tren-carga.md)
