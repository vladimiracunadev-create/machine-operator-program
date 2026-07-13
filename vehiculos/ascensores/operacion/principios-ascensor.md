# 🧪 Principios y operacion del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la instalacion, mantencion o
inspeccion por personal competente ni el manual del fabricante. Describe como
opera un ascensor en simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Equilibrio con contrapeso**: el contrapeso compensa la cabina, asi el motor
  solo mueve la diferencia de peso y gasta mucho menos.
- **Traccion por friccion**: la polea mueve los cables por agarre en sus ranuras;
  la tension del contrapeso hace posible esa friccion.
- **Marcha controlada**: el variador acelera y frena suave para el confort y la
  precision de parada.
- **Seguridad redundante**: freno del motor, gobernador de velocidad y freno de
  seguridad actuan de forma independiente.
- **Nivelacion**: el sistema detiene la cabina alineada con el piso para un
  acceso seguro.

## Fases de un viaje

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Llamada | El usuario pide la cabina | Registrar sentido y piso. |
| Asignacion | El control decide la ruta | Maniobra colectiva optimiza viajes. |
| Apertura | Puerta abierta en origen | Enclavamiento y sensor de obstaculo. |
| Aceleracion | La cabina inicia marcha | Arranque suave con variador. |
| Marcha | Viaje entre pisos | Velocidad estable, cabina guiada. |
| Frenado | Aproximacion al destino | Desaceleracion y nivelacion precisa. |
| Parada | Puerta abierta en destino | Freno del motor sostiene la cabina. |

## Un viaje seguro: idea general

1. El usuario llama la cabina indicando el sentido.
2. El control asigna el viaje y abre la puerta con enclavamiento.
3. La cabina arranca suave y viaja guiada por las guias.
4. Al aproximarse, desacelera y se nivela con el piso.
5. El freno del motor la sostiene mientras se abren las puertas.

## Errores y riesgos que la simulacion puede ensenar a evitar

- Sobrecargar la cabina e intentar arrancar.
- Forzar las puertas o bloquear los sensores de obstaculo.
- Ignorar el cartel de fuera de servicio.
- Confundir la parada de emergencia con un uso normal.
- Omitir la mantencion periodica que exige la ley.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: llamar, viajar entre pisos y abrir o cerrar puertas.
- **Nivel 2 (simplificado)**: agregar contrapeso, sobrecarga y nivelacion.
- **Nivel 3 (tecnico)**: sumar gobernador, freno de seguridad, maniobra colectiva
  y modo inspeccion.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-ascensor.md) · [➡️ Siguiente: Entornos de trabajo](entornos-ascensor.md)
