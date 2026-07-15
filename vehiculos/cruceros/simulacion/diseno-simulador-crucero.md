# 🎮 Diseño de simulación del crucero

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Atracado
    Atracado --> Embarque: embarcar pasaje
    Embarque --> Maniobra: cerrar acceso y desatracar
    Maniobra --> Navegacion: salir de puerto
    Navegacion --> Maniobra: aproximar a puerto
    Navegacion --> Fondeado: fondear frente a escala
    Fondeado --> Navegacion: levar ancla
    Maniobra --> Atracado: atracar
    Navegacion --> Emergencia: riesgo o falla
    Emergencia --> Navegacion: controlar situacion
    Atracado --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a gobernar un crucero respetando la inercia, manejar la
propulsión por pods y el gobierno, aplicar reglas básicas de navegación (COLREG),
gestionar la seguridad del pasaje (muster y evacuación) y realizar maniobras de
puerto de forma segura y progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el crucero suma a la navegación de gran buque la gestión de miles
  de pasajeros y la evacuación, por lo que es un curso avanzado respecto del
  carguero.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-24 nudos | Avance y gobierno | Los pods mantienen autoridad a baja velocidad. |
| Rumbo | numérica | 0-359 grados | Dirección | Cambia con retardo por la inercia. |
| Empuje de pods | numérica | -100..100 % | Avance y maniobra | Combina propulsión y gobierno. |
| Ángulo de pods | numérica | -180..180 grados | Vector de empuje | Permite maniobra lateral. |
| Estabilizadores | discreta | retraído / desplegado | Balance y confort | Reduce el mareo del pasaje. |
| Pasajeros a bordo | numérica | 0-maximo | Seguridad y muster | Debe contarse en evacuación. |
| Estabilidad (GM) | numérica | positiva | Escora y seguridad | Depende de la estiba y el lastre. |
| Viento y corriente | vectorial | variable | Deriva | Muy sensible por la obra muerta. |
| Combustible | numérica | 0-100% | Autonomía | Consumo por propulsión y hotel. |

## Ciclo básico

1. Leer entrada del usuario (pods, timón, thruster, estabilizadores, piloto automático).
2. Actualizar estado de la planta eléctrica, la propulsión y el gobierno.
3. Calcular fuerzas: empuje, resistencia del agua, viento y corriente.
4. Aplicar la inercia de la masa del buque al cambio de velocidad y rumbo.
5. Actualizar posición, rumbo, escora y estado del pasaje.
6. Refrescar instrumentos (radar, GPS, ECDIS), estabilizadores y paneles de seguridad.

## Modos de juego futuros

- Tutorial guiado del puente y las palancas de pod.
- Práctica libre de maniobra de puerto con pods y thrusters.
- Travesía costera entre escalas respetando COLREG.
- Ejercicio de muster y evacuación ordenada del pasaje.
- Situaciones de baja visibilidad con radar, sin contenido sensible.

## Elementos fuera de alcance

- Maniobras temerarias presentadas como recomendables.
- Reproducción de accidentes o victimas de forma sensacionalista.
- Datos que permitan alterar sistemas reales de un buque.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de crucero.
- [ ] Prototipar el modelo de propulsión por pods y maniobra lateral.
- [ ] Modelar el procedimiento de muster y el conteo del pasaje.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-crucero.md) · [➡️ Siguiente: Recursos](../recursos/recursos-crucero.md)
