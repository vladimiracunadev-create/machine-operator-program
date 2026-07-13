# 🎮 Diseno de simulacion del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🎮 Simulacion

Simulacion educativa del lanzamiento y ascenso de un cohete. Modela con rigor la
fisica del empuje, las etapas y la orbita, y anade el reto de recuperar el
propulsor reutilizable.

```mermaid
stateDiagram-v2
    [*] --> EnPlataforma
    EnPlataforma --> CuentaAtras: iniciar cuenta
    CuentaAtras --> Ascenso: encender motores
    CuentaAtras --> EnPlataforma: abortar
    Ascenso --> Separacion: etapa agotada
    Separacion --> EnOrbita: insercion orbital
    Separacion --> RetornoPropulsor: recuperar etapa
    RetornoPropulsor --> EnTierra: aterrizar propulsor
    Ascenso --> Emergencia: falla o riesgo
    Emergencia --> EnPlataforma: abortar seguro
    EnOrbita --> [*]
    EnTierra --> [*]
```

## Objetivo de la simulacion

Que el usuario aprenda a preparar una cuenta atras, despegar con la relacion
empuje-peso correcta, ascender con un giro gradual, separar etapas en el momento
justo, alcanzar una orbita estable y, si el cohete lo permite, aterrizar el
propulsor para reutilizarlo.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificacion: el lanzamiento es la fase mas exigente del vuelo espacial, por lo
  que se recomienda como vehiculo avanzado.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Empuje | numerica | 0-100 porciento | Aceleracion | Regulable en motor liquido. |
| Masa total | numerica | baja al quemar | Relacion empuje-peso | Cae segun se gasta propelente. |
| Propelente | numerica | 0-100 porciento | Delta-v y empuje | Limita el alcance. |
| Altitud | numerica | 0-2000 km | Fase de vuelo | Sube durante el ascenso. |
| Velocidad horizontal | numerica | 0-8 km/s | Insercion orbital | Clave para quedar en orbita. |
| Angulo de ascenso | numerica | 0-90 grados | Trayectoria | Giro gradual a la horizontal. |
| Estado de etapas | discreta | unida o separada | Estructura y masa | Marca cada separacion. |
| Reserva de aterrizaje | numerica | 0-100 porciento | Retorno del propulsor | Propelente guardado para posar. |

## Ciclo basico

1. Leer entrada del usuario (empuje, angulo, separacion, retorno).
2. Actualizar masa, propelente y estado de etapas.
3. Calcular fuerzas: empuje, gravedad y resistencia del aire.
4. Aplicar el entorno (densidad del aire segun altitud, viento).
5. Actualizar altitud, velocidad y orbita.
6. Refrescar telemetria y alarmas (empuje, presion, propelente).

## Modos de juego futuros

- Tutorial de cuenta atras y despegue.
- Practica de ascenso y giro gravitatorio.
- Desafios de separacion de etapas en el momento justo.
- Misiones de insercion orbital con precision.
- Reto de aterrizaje del propulsor reutilizable.

## Elementos fuera de alcance

- Datos tecnicos sensibles de sistemas de lanzamiento reales o militares.
- Detalles que permitan replicar armamento o propulsion clasificada.
- Reproduccion de operaciones peligrosas como si fueran seguras.

## Pendientes

- [ ] Definir valores por defecto de empuje y masa por tipo de cohete.
- [ ] Prototipar el modelo de ascenso con giro gravitatorio.
- [ ] Ajustar el modelo de aterrizaje del propulsor.
- [ ] Agregar fuentes tecnicas publicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-cohete.md) · [➡️ Siguiente: Recursos](../recursos/recursos-cohete.md)
