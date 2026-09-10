<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: ESTRELLADELA-08
curso: estrella-de-la-muerte
titulo: "Reglas del universo de la Estrella de la Muerte"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: ESTRELLADELA-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Estrella de la Muerte."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Estrella de la Muerte."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglas del universo de la Estrella de la Muerte

[🏠 Inicio](../../../README.md) · [🌑 Curso: Estrella de la Muerte](../README.md) · ⚖️ Reglas del universo

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

En la ficción, un vehículo no obedece la física real sino las "reglas internas"
que la obra decide para que la historia funcione. Esta clase describe con
nuestras palabras esas convenciones del estilo "Star Wars" y, junto a cada una,
aclara que dice la física real. No se citan textos ni especificaciones oficiales:
es análisis original. Ver también el
[aviso de derechos del catálogo](../../README.md).

## Que son las reglas del universo

Son acuerdos narrativos: la ficción establece cómo funciona la estación-mundo
para que el relato sea grandioso y fácil de seguir. Son coherentes dentro de la
historia, pero no son leyes de la naturaleza. Distinguirlas de la física real es
justo el objetivo educativo del curso.

## Convenciones típicas del género

| Regla interna de la ficción | Para que sirve en el relato | Que dice la física real |
| --- | --- | --- |
| Energía prácticamente infinita | Poder abrumador | Habría un presupuesto de energía con límites. |
| Un gran disparo sin coste | Impacto dramático | Concentrar tanta energía dejaría sin margen al resto. |
| El calor nunca es problema | No distraer con detalles | Disiparlo sería un reto enorme por la escala. |
| Maniobra con relativa soltura | Escenas dinámicas | Su masa la hace lentísima de mover. |
| La estructura aguanta todo | Mantener el escenario | Soportar su propio peso sería muy exigente. |
| Autonomía total garantizada | Servir de base segura | Sostener millones de personas es colosal. |

## Nota importante: no es ley real

Estas reglas son licencias creativas legítimas para contar una buena historia,
pero **no** describen cómo funciona el universo. La física real dice otra cosa:
mandan la gravedad por masa propia, la conservación de la energía, el presupuesto
de potencia y el límite de disipación de calor. Cuando el curso "corrige" a la
ficción no es para criticar la obra, sino para aprender la diferencia entre lo que
impresiona en pantalla y lo que ocurriría de verdad.

## Cómo lo usa la simulación

- Ofrecer un **modo ficción** que respeta las reglas del género para divertirse.
- Ofrecer un **modo ciencia** que aplica la física real para aprender.
- Mostrar en pantalla, al cambiar de modo, que regla se activó o se desactivó.

De esta forma el usuario ve, lado a lado, la versión espectacular y la versión
realista de la misma estación-mundo.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Que son las reglas del universo, Convenciones típicas del género, Nota importante: no es ley real y Cómo lo usa la simulación** a **interrumpir la cadena que podría producir crear un sistema invulnerable o sin propagación comprensible de fallas**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «crear un sistema invulnerable o sin propagación comprensible de fallas» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Estrella de la Muerte.

Esta clase se conecta con el resto del curso mediante **una megaestructura debe modelarse como red de subsistemas y dependencias, no como un solo vehículo**. El hilo de
seguridad consiste en reconocer a tiempo **crear un sistema invulnerable o sin propagación comprensible de fallas** y poder justificar la decisión
**mapear dependencias, redundancias y estados degradados antes de decidir**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **reactor ficticio → distribución → propulsión y control → estación**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Death Star](https://www.starwars.com/databank/death-star) aporta canon narrativo de la estación;
[Spaceships and Rockets](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/) se usa para naves, sistemas y misiones. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **crear un sistema invulnerable o sin propagación comprensible de fallas** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **mapear dependencias, redundancias y estados degradados antes de decidir** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **crear un sistema invulnerable o sin propagación comprensible de fallas**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Estrella de la Muerte; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARWARS-DEATHSTAR](https://www.starwars.com/databank/death-star): Death Star, Lucasfilm. Uso: canon narrativo de la estación.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos](../operacion/entornos-estrella-de-la-muerte.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-estrella-de-la-muerte.md)
