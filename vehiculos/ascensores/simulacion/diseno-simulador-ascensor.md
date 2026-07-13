# 🎮 Diseno de simulacion del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🎮 Simulacion

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

## Objetivo de la simulacion

Que el usuario entienda como funciona un ascensor: llamar la cabina, viajar entre
pisos con contrapeso, respetar la carga maxima y el rol de los frenos de
seguridad, de forma segura y progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificacion: el ascensor permite ensenar equilibrio con contrapeso, traccion
  por friccion y seguridad redundante con baja complejidad.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Posicion | numerica | piso 0..n | Estado del viaje | Nivel actual de la cabina. |
| Velocidad | numerica | 0-3 m/s | Confort y tiempo | Perfil suave con variador. |
| Carga | numerica | 0-100% nominal | Arranque y consumo | Sobre el limite, no arranca. |
| Contrapeso | numerica | fijo | Esfuerzo del motor | Equilibra la cabina. |
| Estado de puerta | discreta | abierta/cerrada | Seguridad | Enclavamiento activo. |
| Cola de llamadas | lista | pisos pedidos | Ruta de la cabina | Maniobra colectiva. |
| Estado de servicio | discreta | operativo/inspeccion | Disponibilidad | Depende de mantencion. |
| Velocidad de descenso | numerica | derivada | Freno de seguridad | Dispara el gobernador. |

## Ciclo basico

1. Leer entradas (llamadas de piso y de cabina, puertas).
2. Actualizar la cola de llamadas con la maniobra colectiva.
3. Calcular esfuerzo del motor segun carga y contrapeso.
4. Aplicar limites (sobrecarga, finales de carrera, enclavamiento).
5. Actualizar posicion, velocidad y estado de puertas.
6. Refrescar indicadores y retroalimentacion (posicion, flechas, alarmas).

## Modos de juego futuros

- Tutorial guiado de llamadas y viajes.
- Gestion de trafico en hora punta de oficinas.
- Escenario de hospital con prioridad de camillas.
- Desafios de eficiencia con maniobra colectiva.
- Situaciones de mantencion y fuera de servicio, sin contenido sensible.

## Elementos fuera de alcance

- Instrucciones para intervenir un ascensor real sin personal competente.
- Anular o burlar los sistemas de seguridad.
- Datos tecnicos que permitan alterar equipos reales.

## Pendientes

- [ ] Definir valores por defecto por tipo de edificio.
- [ ] Prototipar la maniobra colectiva en un motor simple.
- [ ] Ajustar el perfil de velocidad y nivelacion.
- [ ] Agregar fuentes tecnicas publicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-ascensor.md) · [➡️ Siguiente: Recursos](../recursos/recursos-ascensor.md)
