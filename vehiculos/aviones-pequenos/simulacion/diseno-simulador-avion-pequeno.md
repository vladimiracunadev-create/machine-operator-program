---
tipo_documento: clase
clase: 9
codigo: AVIONESPEQUE-09
curso: aviones-pequenos
titulo: "Diseño de simulación del avión pequeño"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: AVIONESPEQUE-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Aviones pequeños."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones pequeños."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del avión pequeño

[🏠 Inicio](../../../README.md) · [🛩️ Curso: Aviones pequeños](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> EnTierra
    EnTierra --> MotorEnMarcha: encender
    MotorEnMarcha --> EnVuelo: despegar
    EnVuelo --> Aproximacion: iniciar descenso
    Aproximacion --> EnTierra: aterrizar
    EnVuelo --> Emergencia: falla o riesgo
    Emergencia --> Aproximacion: estabilizar y desviar
    MotorEnMarcha --> EnTierra: apagar
    EnTierra --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a despegar, volar nivelado, virar coordinado, gestionar la
altitud y aterrizar con seguridad, respetando el circuito de tráfico y las reglas
básicas del espacio aéreo, de forma progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el avión pequeño agrega el vuelo en tres ejes y la meteorología,
  por lo que se recomienda tras dominar un vehículo terrestre.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad (IAS) | numérica | 0-160 nudos | Sustentación y control | Clave para evitar la pérdida. |
| Altitud | numérica | 0-15000 pies | Rendimiento y navegación | Ligada a la presión local. |
| Actitud (cabeceo/alabeo) | numérica | -60..60 grados | Trayectoria de vuelo | Referencia del horizonte artificial. |
| Ángulo de ataque | numérica | 0-18 grados | Sustentación y pérdida | Supera el límite y hay pérdida. |
| Potencia del motor | numérica | 0-100% | Empuje disponible | Regulada por el acelerador. |
| Configuración de flaps | discreta | 0..3 etapas | Sustentación y resistencia | Para despegue y aterrizaje. |
| Combustible | numérica | 0-100% | Autonomía | Incluye reserva obligatoria. |
| Viento | vectorial | dirección + fuerza | Rumbo y aterrizaje | El cruzado exige corrección. |

## Ciclo básico

1. Leer entrada del usuario (yugo, pedales, potencia, flaps, trim).
2. Actualizar estado del motor y la configuración aerodinámica.
3. Calcular fuerzas: sustentación, peso, empuje y resistencia.
4. Aplicar el entorno (viento, densidad del aire, terreno).
5. Actualizar velocidad, altitud, actitud y posición.
6. Refrescar instrumentos y retroalimentación (sonido, alertas de pérdida).

## Modos de juego futuros

- Tutorial guiado de cabina y checklist.
- Práctica de circuito de tráfico y aterrizajes.
- Misiones de navegación entre aeródromos.
- Desafíos de viento cruzado y meteorología.
- Situaciones de emergencia controladas (falla de motor) sin contenido sensible.

## Elementos fuera de alcance

- Maniobras acrobaticas peligrosas presentadas como recomendables.
- Reproducción de vuelo temerario como objetivo del juego.
- Datos técnicos que permitan alterar sistemas reales de una aeronave.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de avión.
- [ ] Prototipar el modelo de sustentación y pérdida.
- [ ] Ajustar el modelo de viento cruzado en aterrizaje.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Aviones pequeños basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-avion-pequeno.md) · [➡️ Siguiente: Recursos](../recursos/recursos-avion-pequeno.md)
