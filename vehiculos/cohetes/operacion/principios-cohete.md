# 🧪 Principios y operacion del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🧪 Principios

Documento general y educativo. Describe como se opera un cohete en simulacion y
que principios fisicos conviene representar. Todo es **ciencia real**: la fisica
del empuje y de la orbita se modela con rigor.

## Principios de funcionamiento

- **Empuje por reaccion**: el cohete expulsa gases hacia atras y es empujado
  hacia adelante (tercera ley de Newton). No necesita aire.
- **Relacion empuje-peso**: para despegar, el empuje debe ser mayor que el peso.
  Si la relacion es 1, el cohete flota; si es menor, no despega.
- **Ecuacion del cohete (Tsiolkovski)**: el cambio de velocidad que logra un
  cohete depende de la velocidad de salida de sus gases y de cuanta masa quema
  frente a su masa final. Cuanto mas propelente gasta y mas rapido lo expulsa,
  mas delta-v obtiene.
- **Etapas**: soltar masa vacia mejora la relacion entre propelente y peso, por
  eso los cohetes se dividen en etapas.
- **Velocidad orbital**: para quedar en orbita baja hace falta avanzar de lado a
  unos 7,8 km/s (aproximado), no solo subir alto.

## El empuje en una idea

```mermaid
flowchart LR
    Quema[Quemar propelente] --> Gases[Expulsar gases hacia atras]
    Gases --> Reaccion[Reaccion hacia adelante]
    Reaccion --> Sube[El cohete acelera si el empuje supera el peso]
```

Subir alto no basta: si el cohete solo ganara altura, caeria de vuelta. La clave
es ganar **velocidad horizontal** suficiente para entrar en orbita.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prelanzamiento | Carga de propelente y revision | Checklist, presion de tanques, clima. |
| Cuenta atras | Secuencia sincronizada final | Sistemas en verde, autorizacion de rango. |
| Despegue | Encendido y liberacion | Empuje mayor que el peso, torre despejada. |
| Ascenso | Ganar altura y velocidad | Giro gradual hacia la horizontal. |
| Separacion de etapas | Soltar la etapa agotada | Momento justo, encender la siguiente. |
| Insercion orbital | Alcanzar velocidad orbital | Velocidad de lado suficiente. |
| Retorno del propulsor | La primera etapa vuelve | Encendidos de reentrada y aterrizaje. |

## Maniobra de ascenso: idea general

1. Despegar vertical para salir del aire mas denso.
2. Inclinar poco a poco hacia la horizontal (giro gravitatorio).
3. Regular el empuje para no exceder el esfuerzo estructural.
4. Separar la etapa inferior al agotarse.
5. Con la etapa superior, ganar la velocidad orbital final.

## Errores comunes que la simulacion puede ensenar a evitar

- Creer que basta con subir alto sin ganar velocidad horizontal.
- Despegar con relacion empuje-peso menor que 1.
- Separar la etapa demasiado pronto o demasiado tarde.
- Gastar todo el propelente sin reserva para el aterrizaje del propulsor.
- Inclinar el cohete demasiado rapido y sobrecargar la estructura.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, ascender y llegar a orbita de forma guiada.
- **Nivel 2 (simplificado)**: agregar relacion empuje-peso, etapas y velocidad orbital.
- **Nivel 3 (tecnico)**: sumar ecuacion del cohete, giro gravitatorio y retorno del propulsor.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-cohete.md) · [➡️ Siguiente: Entornos de trabajo](entornos-cohete.md)
