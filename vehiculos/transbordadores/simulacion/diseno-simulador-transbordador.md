---
tipo_documento: clase
clase: 9
codigo: TRANSBORDADO-09
curso: transbordadores
titulo: "Diseño de simulación del transbordador"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: TRANSBORDADO-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Transbordadores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Transbordadores."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🎮 Simulación

Simulación educativa del transbordador. Modela con rigor el despegue de cohete, la
órbita y, sobre todo, el reto distintivo: la reentrada con escudo y el planeo sin
motor hasta la pista.

```mermaid
stateDiagram-v2
    [*] --> EnPlataforma
    EnPlataforma --> Ascenso: despegar
    Ascenso --> EnOrbita: insercion orbital
    EnOrbita --> Desorbitacion: frenar
    Desorbitacion --> Reentrada: caer a la atmosfera
    Reentrada --> Planeo: pasar el pico de calor
    Planeo --> EnPista: aterrizar
    Ascenso --> Emergencia: falla o riesgo
    Emergencia --> EnPlataforma: abortar seguro
    EnPista --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a despegar como cohete, alcanzar una órbita estable,
desplegar carga, frenar para desorbitar, reingresar con el escudo bien orientado y
completar un planeo sin motor hasta aterrizar en la pista en un solo intento.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: la reentrada alada y el aterrizaje sin motor son de los retos más
  exigentes del repositorio, por lo que se recomienda como vehículo avanzado.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Altitud | numérica | 0-600 km | Fase de vuelo | Sube al ascender, baja al reingresar. |
| Velocidad | numérica | 0-8 km/s | Órbita y reentrada | Muy alta en órbita, baja en pista. |
| Ángulo de reentrada | numérica | 0-10 grados | Calor y frenado | Ni muy plano ni muy pronunciado. |
| Orientación del escudo | discreta | correcta o incorrecta | Supervivencia | El escudo debe ir por delante. |
| Temperatura del escudo | numérica | 0-1600 grados | Estructura | Crítica en la reentrada. |
| Energía de planeo | numérica | altura más velocidad | Alcance a la pista | Se administra sin motor. |
| Estado de separaciones | discreta | pendiente o hecha | Masa y empuje | Propulsores y tanque. |
| Masa en bahía | numérica | vacía a máxima | Ascenso, planeo y centrado | Se suelta en órbita: el regreso pesa menos que la ida. |
| Tren de aterrizaje | discreta | recogido o desplegado | Aterrizaje | Se despliega antes del toque. |

La **masa en bahía** es fácil de olvidar porque el resto del curso trata la bahía
como algo que se abre y se opera, no como peso. Pero es peso: encarece el
ascenso, desplaza el centro de masa y cambia el planeo, que se administra sin
motor y por tanto no admite compensar con empuje. Y es una masa **viva**: la
carga se suelta en órbita, así que el orbitador vuelve más ligero de lo que
subió. Ver [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## Ciclo básico

1. Leer entrada del usuario (empuje, actitud, palanca, timón, tren).
2. Actualizar propelente, energía, masa en bahía y estado de separaciones.
3. Calcular la física según la fase (cohete, órbita o planeo).
4. Aplicar el entorno (densidad del aire, viento, calor de reentrada).
5. Actualizar altitud, velocidad, órbita y temperatura del escudo.
6. Refrescar instrumentos y alarmas (escudo, senda de planeo, tren).

## Modos de juego futuros

- Tutorial de despegue y órbita básica.
- Práctica de despliegue de carga con el brazo robotico.
- Desafíos de reentrada con ángulo y orientación correctos.
- Reto de planeo y aterrizaje sin motor de un solo intento.
- Escenarios de viento cruzado en la pista.

## Elementos fuera de alcance

- Datos técnicos sensibles de sistemas de lanzamiento reales o militares.
- Detalles que permitan replicar tecnología clasificada.
- Reproducción de operaciones peligrosas como si fueran seguras.

## Pendientes

- [ ] Definir valores por defecto de órbita y calor de reentrada.
- [ ] Prototipar el modelo de planeo sin motor.
- [ ] Ajustar el modelo de calor del escudo según ángulo y velocidad.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Transbordadores basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SHUTTLE](https://www.nasa.gov/reference/the-space-shuttle/): The Space Shuttle, NASA. Uso: arquitectura y operación del transbordador.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-transbordador.md) · [➡️ Siguiente: Recursos](../recursos/recursos-transbordador.md)
