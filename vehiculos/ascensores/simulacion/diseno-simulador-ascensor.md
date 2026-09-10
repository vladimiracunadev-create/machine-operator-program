---
tipo_documento: clase
clase: 9
codigo: ASCENSORES-09
curso: ascensores
titulo: "Diseño de simulación del ascensor"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: ASCENSORES-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Ascensores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Ascensores."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Reposo
    Reposo --> Viajando: llamada asignada
    Viajando --> EnParada: llegar al piso
    EnParada --> Viajando: nuevo destino
    EnParada --> Reposo: sin llamadas
    Viajando --> Sobrecarga: exceso de peso
    Sobrecarga --> EnParada: reducir carga
    Reposo --> FueraDeServicio: mantencion o falla
    FueraDeServicio --> Reposo: equipo certificado
    Reposo --> [*]
```

## Objetivo de la simulación

Que el usuario entienda cómo funciona un ascensor: llamar la cabina, viajar entre
pisos con contrapeso, respetar la carga máxima y el rol de los frenos de
seguridad, de forma segura y progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el ascensor permite enseñar equilibrio con contrapeso, tracción
  por fricción y seguridad redundante con baja complejidad.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Posición | numérica | piso 0..n | Estado del viaje | Nivel actual de la cabina. |
| Velocidad | numérica | 0-3 m/s | Confort y tiempo | Perfil suave con variador. |
| Carga | numérica | 0-100% nominal | Arranque y consumo | Sobre el límite, no arranca. |
| Contrapeso | numérica | fijo | Esfuerzo del motor | Equilibra la cabina. |
| Estado de puerta | discreta | abierta/cerrada | Seguridad | Enclavamiento activo. |
| Cola de llamadas | lista | pisos pedidos | Ruta de la cabina | Maniobra colectiva. |
| Estado de servicio | discreta | operativo/inspección | Disponibilidad | Depende de mantención. |
| Velocidad de descenso | numérica | derivada | Freno de seguridad | Dispara el gobernador. |

## Ciclo básico

1. Leer entradas (llamadas de piso y de cabina, puertas).
2. Actualizar la cola de llamadas con la maniobra colectiva.
3. Calcular esfuerzo del motor según carga y contrapeso.
4. Aplicar límites (sobrecarga, finales de carrera, enclavamiento).
5. Actualizar posición, velocidad y estado de puertas.
6. Refrescar indicadores y retroalimentación (posición, flechas, alarmas).

## Modos de juego futuros

- Tutorial guiado de llamadas y viajes.
- Gestión de tráfico en hora punta de oficinas.
- Escenario de hospital con prioridad de camillas.
- Desafíos de eficiencia con maniobra colectiva.
- Situaciones de mantención y fuera de servicio, sin contenido sensible.

## Elementos fuera de alcance

- Instrucciones para intervenir un ascensor real sin personal competente.
- Anular o burlar los sistemas de seguridad.
- Datos técnicos que permitan alterar equipos reales.

## Pendientes

- [ ] Definir valores por defecto por tipo de edificio.
- [ ] Prototipar la maniobra colectiva en un motor simple.
- [ ] Ajustar el perfil de velocidad y nivelación.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Ascensores basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-ELEVATORS](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116): 1917.116 Elevators and Escalators, OSHA. Uso: inspección y riesgos de transporte vertical.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-ascensor.md) · [➡️ Siguiente: Recursos](../recursos/recursos-ascensor.md)
