# 🧪 Principios y operacion del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye un curso de conduccion profesional
certificado ni el manual del fabricante. Describe como se opera un bus en
simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Masa e inercia**: el bus es muy pesado; acelerar y detener requiere mas
  distancia y tiempo. La anticipacion es la primera herramienta de seguridad.
- **Frenado con pasajeros de pie**: una frenada brusca lanza a las personas hacia
  adelante. El frenado debe ser suave y progresivo, iniciado con antelacion.
- **Radio de giro y barrido trasero**: el bus necesita mucho espacio para girar y
  su parte trasera describe un arco que invade el carril contiguo.
- **Puntos ciegos**: la gran carroceria genera amplias zonas sin vision directa;
  se cubren con espejos y camaras, y aun asi exigen precaucion.
- **Aproximacion a paradas**: acercarse al anden de forma paralela y suave para
  facilitar el ascenso y descenso seguro.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Neumaticos, luces, frenos, presion de aire, puertas. |
| Carga de aire | Motor en marcha | Esperar la presion minima antes de mover el bus. |
| Puesta en marcha | Iniciar servicio | Soltar freno de estacionamiento, seleccionar D, salir suave. |
| Conduccion | Circular con pasajeros | Mirar lejos, frenar con antelacion, vigilar puntos ciegos. |
| Aproximacion a parada | Llegar al anden | Reducir suave, alinear paralelo, detener y arrodillar si aplica. |
| Servicio en parada | Ascenso y descenso | Abrir puertas, marcha enclavada, cerrar sin atrapar. |
| Detencion final | Terminar el servicio | Freno de estacionamiento, puertas, motor apagado. |

## Aproximacion a parada: idea general

1. Anticipar la parada y **reducir la velocidad con tiempo**.
2. Senalizar e ir alineando el bus **paralelo al anden**.
3. Frenar de forma **progresiva** para no desestabilizar a los de pie.
4. Detener completamente y aplicar el freno; **arrodillar** si hay accesibilidad.
5. Abrir puertas solo con el bus detenido; cerrar verificando los sensores.
6. Reincorporarse al trafico mirando espejos y puntos ciegos.

## Errores comunes que la simulacion puede ensenar a evitar

- Frenar tarde y brusco, desestabilizando a los pasajeros de pie.
- Girar sin dejar espacio para el barrido trasero.
- Abrir o mantener puertas abiertas con el bus en movimiento.
- Ignorar la presion de aire y mover el bus antes de tiempo.
- Olvidar los puntos ciegos al cambiar de carril o al salir de la parada.
- Abusar del freno de servicio en descensos en vez de usar el retardador.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: acelerar, frenar suave, parar en paradas y respetar senales.
- **Nivel 2 (simplificado)**: agregar inercia de la masa, barrido trasero y aforo.
- **Nivel 3 (tecnico)**: sumar presion de aire, retardador, enclavamiento de
  puertas y gestion de la fatiga en jornada.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-bus.md) · [➡️ Siguiente: Entornos de trabajo](entornos-bus.md)
