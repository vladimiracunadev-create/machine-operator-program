# 🧪 Principios y operación del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🧪 Principios

Documento general y educativo. Describe cómo se opera un cohete en simulación y
que principios físicos conviene representar. Todo es **ciencia real**: la física
del empuje y de la órbita se modela con rigor.

## Principios de funcionamiento

- **Empuje por reacción**: el cohete expulsa gases hacia atrás y es empujado
  hacia adelante (tercera ley de Newton). No necesita aire.
- **Relación empuje-peso**: para despegar, el empuje debe ser mayor que el peso.
  Si la relación es 1, el cohete flota; si es menor, no despega.
- **Ecuación del cohete (Tsiolkovski)**: el cambio de velocidad que logra un
  cohete depende de la velocidad de salida de sus gases y de cuanta masa quema
  frente a su masa final. Cuanto más propelente gasta y más rápido lo expulsa,
  más delta-v obtiene.
- **Etapas**: soltar masa vacía mejora la relación entre propelente y peso, por
  eso los cohetes se dividen en etapas.
- **Velocidad orbital**: para quedar en órbita baja hace falta avanzar de lado a
  unos 7,8 km/s (aproximado), no solo subir alto.

## El empuje en una idea

```mermaid
flowchart LR
    Quema[Quemar propelente] --> Gases[Expulsar gases hacia atrás]
    Gases --> Reaccion[Reacción hacia adelante]
    Reaccion --> Sube[El cohete acelera si el empuje supera el peso]
```

Subir alto no basta: si el cohete solo ganara altura, caeria de vuelta. La clave
es ganar **velocidad horizontal** suficiente para entrar en órbita.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prelanzamiento | Carga de propelente y revisión | Checklist, presión de tanques, clima. |
| Cuenta atrás | Secuencia sincronizada final | Sistemas en verde, autorización de rango. |
| Despegue | Encendido y liberación | Empuje mayor que el peso, torre despejada. |
| Ascenso | Ganar altura y velocidad | Giro gradual hacia la horizontal. |
| Separación de etapas | Soltar la etapa agotada | Momento justo, encender la siguiente. |
| Inserción orbital | Alcanzar velocidad orbital | Velocidad de lado suficiente. |
| Retorno del propulsor | La primera etapa vuelve | Encendidos de reentrada y aterrizaje. |

## Maniobra de ascenso: idea general

1. Despegar vertical para salir del aire más denso.
2. Inclinar poco a poco hacia la horizontal (giro gravitatorio).
3. Regular el empuje para no exceder el esfuerzo estructural.
4. Separar la etapa inferior al agotarse.
5. Con la etapa superior, ganar la velocidad orbital final.

## Errores comunes que la simulación puede enseñar a evitar

- Creer que basta con subir alto sin ganar velocidad horizontal.
- Despegar con relación empuje-peso menor que 1.
- Separar la etapa demasiado pronto o demasiado tarde.
- Gastar todo el propelente sin reserva para el aterrizaje del propulsor.
- Inclinar el cohete demasiado rápido y sobrecargar la estructura.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, ascender y llegar a órbita de forma guiada.
- **Nivel 2 (simplificado)**: agregar relación empuje-peso, etapas y velocidad orbital.
- **Nivel 3 (técnico)**: sumar ecuación del cohete, giro gravitatorio y retorno del propulsor.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-cohete.md) · [➡️ Siguiente: Entornos de trabajo](entornos-cohete.md)
