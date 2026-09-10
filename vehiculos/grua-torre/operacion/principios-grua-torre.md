---
tipo_documento: clase
clase: 6
codigo: GRUATORRE-06
curso: grua-torre
titulo: "Principios y operación de la grúa torre"
modalidad: "resolución de problemas"
duracion_minutos: 90
nivel: introductorio
prerrequisito: GRUATORRE-05
competencia: "razonamiento_operacional"
resultados_aprendizaje:
  - "Explicar principios físicos, fases de operación, decisiones y errores frecuentes con vocabulario propio de Grúa torre."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa torre."
evidencia: "Resolución argumentada de un escenario operacional."
criterio_aprobacion: "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🧪 Principios y operación de la grúa torre

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grúa torre](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación certificada del operador
ni el manual del fabricante. Describe cómo se opera una grúa torre en simulación
y que principios físicos conviene representar.

## Principios de funcionamiento

- **Equilibrio de momentos**: la carga por su radio genera un momento que el
  contrapeso de la contrapluma equilibra sobre el eje de la torre.
- **Estabilidad de la base**: la base anclada y nivelada resiste el vuelco; una
  base mal apoyada o inclinada reduce la seguridad.
- **Momento y radio**: cuanto más lejos del eje está el carro, mayor es el
  momento y menor el peso admisible.
- **Límite de viento**: el viento empuja la carga y la estructura; por encima de
  un umbral la grúa no puede operar.
- **Control del péndulo**: la carga colgada oscila; el izaje y el giro lentos
  evitan que el péndulo se vuelva peligroso.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspección previa | Revisión básica | Base, cables, limitadores, anemómetro, área libre. |
| Puesta en servicio | Habilitar la grúa | Nivel correcto, freno de giro, viento bajo el límite. |
| Enganche | Amarrar la carga | Eslingas correctas, señalero listo, radio segura. |
| Izaje | Levantar la carga | Izaje lento, vigilar el limitador y el radio. |
| Traslado y giro | Llevar la carga | Giro suave, controlar el péndulo, área despejada. |
| Descenso | Depositar la carga | Bajada lenta, guiar con el señalero. |
| Cierre | Dejar segura | Gancho arriba, freno de giro liberado, veleta. |

## Izaje seguro: idea general

1. Confirmar el **peso** y el **radio** contra la tabla de carga antes de izar.
2. Coordinar con el **señalero** por radio o gestos.
3. Tensar el cable despacio y despegar la carga sin tirones.
4. Girar y trasladar el carro con movimientos suaves para no balancear.
5. Depositar la carga lento y liberar el gancho con seguridad.

## Errores comunes que la simulación puede enseñar a evitar

- Izar sin comprobar el peso y el radio contra la tabla de carga.
- Alejar el carro sin notar que la capacidad baja.
- Operar con viento por encima del límite de servicio.
- Girar de golpe y provocar un péndulo peligroso.
- Dejar la grúa fuera de servicio con el giro frenado en vez de veleta.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: izar, girar, trasladar el carro y respetar el limitador.
- **Nivel 2 (simplificado)**: agregar momento de carga, radio y límite de viento.
- **Nivel 3 (técnico)**: sumar péndulo de la carga, trepado y arriostramiento.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

## 🎓 Cierre de clase

- **Actividad:** Resuelve un escenario de Grúa torre explicando, paso a paso, cómo intervienen principios físicos, fases de operación, decisiones y errores frecuentes.
- **Evidencia:** Resolución argumentada de un escenario operacional.
- **Criterio de aprobación:** Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [OSHA-TOWER](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1435): 1926.1435 Tower Cranes, OSHA. Uso: requisitos específicos de grúas torre.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-grua-torre.md) · [➡️ Siguiente: Entornos de trabajo](entornos-grua-torre.md)
