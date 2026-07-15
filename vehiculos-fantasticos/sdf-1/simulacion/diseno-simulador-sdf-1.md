# 🎮 Diseño de simulación del SDF-1

[🏠 Inicio](../../../README.md) · [🏯 Curso: SDF-1](../README.md) · 🎮 Simulación

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Como modelar de forma educativa y divertida una nave-fortaleza gigante. La idea
central es poder alternar entre la versión espectacular de la ficción y la
versión fiel a la física, para que el usuario compare ambas con la misma nave, y
sobre todo para que sienta como la escala vuelve lento y delicado cada
movimiento.

```mermaid
stateDiagram-v2
    [*] --> Estacion
    Estacion --> Maniobra: ordenar empuje o giro
    Maniobra --> Estacion: completar maniobra
    Maniobra --> Alerta: tension estructural alta
    Alerta --> Maniobra: suavizar la maniobra
    Estacion --> Sobrecalentando: mucho calor interno
    Sobrecalentando --> Estacion: radiar calor
    Estacion --> Emergencia: falla de energia o soporte vital
    Emergencia --> Estacion: estabilizar
    Estacion --> [*]
```

## Objetivo de la simulación

Que el usuario comprenda, jugando, que agrandar una nave no es gratis: la ley del
cubo-cuadrado dispara la masa, la maniobra se vuelve lentísima, la estructura
sufre y el calor cuesta expulsarse. El modo ficción sirve para engancharse; el
modo ciencia, para aprender.

## Modo ciencia o ficción

La variable más importante del simulador es el **modo**:

- **Modo ficción**: la nave gigante maniobra con soltura, la estructura aguanta
  todo y el calor no molesta. Es divertido y espectacular.
- **Modo ciencia**: se aplican la ley del cubo-cuadrado, la relación empuje/masa,
  la tensión estructural y el límite de disipación de calor. Todo se vuelve
  lento y delicado.

Al cambiar de modo, la interfaz avisa que reglas se activan o desactivan, para
que la comparación sea explícita y educativa.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Modo | discreta | ciencia / ficción | Todas las reglas | Interruptor central del aprendizaje. |
| Tamaño de la nave | numérica | grande a colosal | Masa y estructura | Aplica la ley del cubo-cuadrado. |
| Masa total | numérica | enorme | Aceleración y delta-v | Crece con el cubo del tamaño. |
| Empuje de motores | numérica | 0-100% | Cambio de velocidad | Aun al máximo, acelera despacio. |
| Tensión estructural | numérica | 0-100% | Integridad del casco | Limita la brusquedad de la maniobra. |
| Calor acumulado | numérica | 0-100% | Riesgo térmico | Se disipa lento por la superficie. |
| Estado de soporte vital | numérica | 0-100% | Habitabilidad | Aire, agua y temperatura interior. |
| Gravedad del entorno | numérica | 0-alta | Trayectoria y esfuerzos | Añade cargas a la estructura. |

## Ciclo básico

1. Leer entrada del usuario (empuje, giro, reparto de energía).
2. Comprobar el modo activo (ciencia o ficción).
3. Calcular la masa total según el tamaño (ley del cubo-cuadrado).
4. Calcular la aceleración como empuje dividido por masa.
5. En modo ciencia, actualizar la tensión estructural con cada maniobra.
6. Actualizar el calor: generado por dentro, radiado por la superficie.
7. Aplicar el entorno: gravedad y esfuerzos.
8. Refrescar instrumentos (velocidad, tensión, calor, soporte vital).

## Modos de juego futuros

- Tutorial de escala: comparar la maniobra de una nave pequeña y una colosal.
- Reto estructural: girar sin superar la tensión del casco.
- Comparador lado a lado: misma maniobra en modo ciencia y en modo ficción.
- Gestión térmica: mantener el calor bajo control con la superficie disponible.
- Operación de atraque en un astillero con apoyo estructural externo.

## Elementos fuera de alcance

- Presentar la maniobra ágil de la nave gigante como si fuera física real.
- Detalles de armamento presentados como datos técnicos reales.
- Cualquier contenido que confunda espectáculo con ciencia sin distinguirlos.

## Pendientes

- [ ] Definir la relación entre tamaño, masa y tensión estructural.
- [ ] Prototipar el ciclo básico con la ley del cubo-cuadrado.
- [ ] Ajustar el modelo de calor por superficie disponible.
- [ ] Agregar fuentes de divulgación a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

---

[⬅️ Anterior: Reglas del universo](../reglamentos/reglas-universo-sdf-1.md) · [➡️ Siguiente: Recursos](../recursos/recursos-sdf-1.md)
