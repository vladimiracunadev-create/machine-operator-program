---
tipo_documento: clase
clase: 9
codigo: DRONES-09
curso: drones
titulo: "Diseño de simulación del dron"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: DRONES-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Drones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Drones."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del dron

[🏠 Inicio](../../../README.md) · [🕹️ Curso: Drones](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Apagado
    Apagado --> Armado: armar motores
    Armado --> EnVuelo: subir throttle
    EnVuelo --> Estacionario: soltar sticks
    Estacionario --> EnVuelo: mover sticks
    EnVuelo --> Retorno: activar RTH o bateria baja
    Retorno --> Armado: aterrizar
    EnVuelo --> Emergencia: fallo o riesgo
    Emergencia --> Retorno: retorno automatico
    Armado --> Apagado: desarmar
    Apagado --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a armar los motores, despegar en vertical, mantener el
vuelo estacionario, trasladarse coordinando los dos sticks, gestionar la batería y
el enlace, y respetar las zonas prohibidas, de forma segura y progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el dron es de dificultad intermedia; la controladora estabiliza
  el vuelo, lo que baja la carga respecto del helicóptero, pero agrega la gestión
  del enlace, la batería y las zonas restringidas.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Throttle | numérica | 0-100% | Empuje total | Sube o baja el dron. |
| Cabeceo | numérica | -30..30 grados | Avance y retroceso | Del stick derecho. |
| Alabeo | numérica | -30..30 grados | Desplazamiento lateral | Del stick derecho. |
| Guiñada | numérica | -100..100% | Rumbo de la nariz | Del stick izquierdo. |
| Batería | numérica | 0-100% | Autonomía y avisos | Dispara el retorno automático. |
| Viento | numérica | 0-alto | Deriva y consumo | Puede superar el empuje. |
| Calidad de GPS | numérica | 0-100% | Mantenimiento de posición | Baja entre obstáculos. |
| Enlace de radio | numérica | 0-100% | Control y fail-safe | Baja con distancia e interferencia. |
| Peso del conjunto | numérica | fijo + carga | Empuje necesario | Incluye cámara o carga útil. |

## Ciclo básico

1. Leer entrada del usuario (throttle, cabeceo, alabeo, guiñada, modo).
2. Actualizar el estado de la controladora, la batería y el enlace.
3. Calcular fuerzas: empuje de cada rotor, peso, viento y par.
4. Aplicar restricciones del entorno (GPS, interferencia, zona prohibida).
5. Actualizar posición, altura, actitud y rumbo.
6. Refrescar instrumentos y retroalimentación (telemetría, avisos, video).

## Modos de juego futuros

- Tutorial guiado de los dos sticks y del vuelo estacionario.
- Práctica libre de despegue y aterrizaje vertical.
- Misiones de fotografía y de mapeo por waypoints.
- Inspección de torres y líneas manteniendo distancia segura.
- Gestión de emergencias: batería baja, pérdida de enlace y retorno a casa.

## Elementos fuera de alcance

- Maniobras que presenten como recomendable volar sobre personas o aeropuertos.
- Reproducción de vuelo temerario o invasivo como objetivo del juego.
- Datos técnicos que permitan alterar sistemas reales o burlar restricciones.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de dron.
- [ ] Prototipar el ciclo básico del vuelo estacionario en un motor simple.
- [ ] Ajustar el modelo de viento y de consumo de batería.
- [ ] Confirmar los umbrales de la DAN 151 y reflejarlos en las zonas del escenario.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Drones basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-UAS](https://www.faa.gov/uas): Unmanned Aircraft Systems, FAA. Uso: operación y normativa RPAS.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-dron.md) · [➡️ Siguiente: Recursos](../recursos/recursos-dron.md)
