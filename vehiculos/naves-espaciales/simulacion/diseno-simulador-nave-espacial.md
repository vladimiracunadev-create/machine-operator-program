# 🎮 Diseno de simulacion de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🎮 Simulacion

Simulacion educativa del vuelo espacial. Separa siempre la ciencia real de la
ficcion: la fisica orbital se modela con rigor y los elementos inventados se
marcan como escenario.

```mermaid
stateDiagram-v2
    [*] --> EnPlataforma
    EnPlataforma --> Ascenso: lanzar
    Ascenso --> EnOrbita: insercion orbital
    EnOrbita --> Maniobra: encender motor
    Maniobra --> EnOrbita: completar maniobra
    EnOrbita --> Reentrada: desorbitar
    Reentrada --> EnTierra: aterrizar o amerizar
    EnOrbita --> Emergencia: falla o riesgo
    Emergencia --> EnOrbita: estabilizar
    EnTierra --> [*]
```

## Objetivo de la simulacion

Que el usuario aprenda a lanzar, alcanzar una orbita estable, planificar maniobras
con delta-v, gestionar energia y soporte vital, y reentrar con seguridad,
entendiendo la fisica orbital real.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificacion: la mecanica orbital es el tema mas abstracto del repositorio, por
  lo que se recomienda como vehiculo avanzado.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Altitud orbital | numerica | 0-2000 km | Forma de la orbita | Apogeo y perigeo. |
| Velocidad orbital | numerica | 0-11 km/s | Estabilidad de la orbita | Alta cerca de la Tierra. |
| Delta-v disponible | numerica | 0-9000 m/s | Capacidad de maniobra | Depende del propelente. |
| Actitud | vectorial | 3 ejes | Orientacion | Controlada por RCS y ruedas. |
| Propelente | numerica | 0-100% | Delta-v y empuje | Limitado, se planifica. |
| Recursos vitales | numerica | 0-100% | Tripulacion | Aire, agua, CO2, energia. |
| Temperatura del escudo | numerica | 0-2000 grados | Reentrada | Critica al reingresar. |
| Modo ciencia/ficcion | discreta | real / ficcion | Reglas fisicas | Etiqueta el escenario. |

## Ciclo basico

1. Leer entrada del usuario (actitud, traslacion, empuje, maniobras).
2. Actualizar propelente, energia y recursos vitales.
3. Calcular la fisica orbital (gravedad, velocidad, orbita).
4. Aplicar el entorno (atmosfera en reentrada, radiacion, distancia).
5. Actualizar orbita, actitud y estado de la nave.
6. Refrescar instrumentos y alarmas (delta-v, recursos, temperatura).

## Modos de juego futuros

- Tutorial de lanzamiento y orbita basica.
- Practica de maniobras orbitales con delta-v.
- Misiones de acoplamiento con una estacion.
- Desafios de reentrada y aterrizaje.
- Escenarios de ficcion claramente marcados, sin mezclar con la ciencia real.

## Elementos fuera de alcance

- Presentar ficcion como si fuera ciencia comprobada.
- Datos tecnicos sensibles de sistemas de lanzamiento reales.
- Detalles de uso militar del espacio.
- Reproduccion de operaciones peligrosas como si fueran seguras.

## Pendientes

- [ ] Definir valores por defecto de orbita y delta-v por tipo de nave.
- [ ] Prototipar el modelo de mecanica orbital simplificada.
- [ ] Ajustar el modelo de reentrada y calor del escudo.
- [ ] Agregar fuentes tecnicas publicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-nave-espacial.md) · [➡️ Siguiente: Recursos](../recursos/recursos-nave-espacial.md)
