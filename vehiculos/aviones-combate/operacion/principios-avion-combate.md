# 🧪 Principios y operación del avión de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🧪 Principios

Documento general, público y divulgativo. No sustituye entrenamiento real ni
manuales oficiales, y **no** describe táctica, doctrina ni sistemas de armas. Solo
trata la física del vuelo a reacción y fases generales de vuelo.

## Principios de funcionamiento

- **Sustentación**: las alas generan sostén al moverse por el aire, como en todo avión.
- **Empuje a reacción**: el motor expulsa gases hacia atrás e impulsa el avión adelante.
- **Vuelo a alta velocidad**: cerca del sonido cambian la resistencia y el control.
- **Cargas G**: en las maniobras la aceleración multiplica el peso aparente.
- **Vuelo en tres ejes**: cabeceo, alabeo y guiñada, asistidos por mandos eléctricos.

## Cargas G a nivel conceptual

```mermaid
flowchart LR
    Maniobra[Maniobra cerrada] --> G[Mayor carga G]
    G --> Estructura[Esfuerzo en la estructura]
    G --> Piloto[Esfuerzo físico en el piloto]
    Estructura --> Limite[Límite estructural]
    Piloto --> Limite2[Límite fisiológico]
```

Una maniobra cerrada aumenta la carga G: la estructura y el propio piloto sienten
un peso aparente varias veces mayor. Por eso el avión se disena reforzado y el
piloto usa equipo especial. En simulación, esto se representa como un límite.

## Fases de operación (marco general)

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Prevuelo | Inspección y checklist | Estado de la aeronave y sistemas generales. |
| Rodaje | Mover el avión en tierra | Control con pedales y frenos. |
| Despegue | Acelerar y elevarse | Empuje alto, velocidad de rotación, ascenso. |
| Ascenso | Ganar altitud | Gestión de empuje y energía. |
| Crucero | Vuelo sostenido | Navegar y mantener parámetros estables. |
| Maniobra | Cambios de actitud | Controlar cargas G y no perder energía. |
| Descenso | Bajar de altitud | Reducir empuje y controlar velocidad. |
| Aterrizaje | Tomar tierra | Configurar, aproximar y frenar con control. |

## Energía y maniobra: idea general

1. La velocidad y la altitud son "energía" disponible para maniobrar.
2. Una maniobra cerrada gasta energía y sube la carga G.
3. Recuperar energía exige empuje o cambiar altitud por velocidad.
4. Volar suave conserva energía y control.
5. Respetar los límites estructurales y fisiológicos es prioritario.

## Errores comunes que la simulación puede enseñar a evitar

- Exceder los límites de carga G en una maniobra.
- Perder energía y quedar lento a baja altura.
- Ignorar la velocidad cercana al sonido y sus efectos.
- No completar el checklist de cada fase.
- Descuidar el combustible en vuelo prolongado.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: despegar, volar, virar y aterrizar un reactor.
- **Nivel 2 (simplificado)**: agregar cargas G, energía y efectos de alta velocidad.
- **Nivel 3 (técnico)**: sumar gestión de empuje, límites estructurales y Mach.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-avion-combate.md) · [➡️ Siguiente: Entornos de trabajo](entornos-avion-combate.md)
