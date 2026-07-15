# 🎯 Ejercicios y autoevaluación del SDF-1

[🏠 Inicio](../../../README.md) · [🏯 Curso: SDF-1](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni certifica conocimiento de
> ingeniería aeroespacial. La nave-fortaleza es ficción y el curso es análisis
> original con fines educativos; los derechos de las obras pertenecen a sus
> titulares. Sirve para comprobar si el curso se entendió y para detectar qué
> módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** Si duplicas cada dimensión de la nave sin cambiar su forma, ¿por cuánto
se multiplican su superficie y su masa?

<details>
<summary>Ver respuesta</summary>

La superficie se multiplica por **cuatro** (crece con el cuadrado del tamaño) y
la masa por **ocho** (crece con el cubo, igual que el volumen). Esa asimetría es
la ley del cubo-cuadrado y es el corazón del curso: agrandar no es "lo mismo
pero más grande", porque la masa se dispara mucho más rápido que la superficie.

Módulo 6: [🧪 Principios y operación](../operacion/principios-sdf-1.md).

</details>

**1.2.** ¿Por qué una nave colosal acelera muy despacio aunque tenga motores
enormes?

<details>
<summary>Ver respuesta</summary>

Porque la aceleración es el empuje dividido por la masa. Al agrandar la nave la
masa crece con el cubo del tamaño, así que por muy potentes que sean los
motores, la masa manda. Cambiar el rumbo o la velocidad lleva mucho tiempo y
consume cantidades descomunales de propelente.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md)
y [🧪 Principios](../operacion/principios-sdf-1.md).

</details>

**1.3.** ¿Por qué hacer las paredes más gruesas no resuelve el problema
estructural de un gigante?

<details>
<summary>Ver respuesta</summary>

Porque más grosor añade más masa, y esa masa extra exige a su vez más
estructura para sostenerse. Es un círculo del que la escala no deja escapar
fácilmente: en un gigante el mayor rival no es un enemigo, sino su propio peso.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md)
y [🧪 Principios](../operacion/principios-sdf-1.md).

</details>

**1.4.** En el vacío no hay gravedad que aplaste la nave. ¿Significa eso que su
estructura ya no sufre?

<details>
<summary>Ver respuesta</summary>

No. Sin gravedad externa el peso propio no la aplasta, pero **cualquier maniobra
o empuje genera esfuerzos** que la estructura debe repartir sin romperse. A esa
escala el casco flexiona y vibra en vez de moverse como un bloque rígido, y las
aceleraciones bruscas producirían esfuerzos enormes. Por eso el puente vigila la
tensión estructural como una variable crítica.

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-sdf-1.md).

</details>

**1.5.** ¿Por qué refrigerar una nave-ciudad es un problema de escala y no solo
de tener buenos radiadores?

<details>
<summary>Ver respuesta</summary>

Porque el calor lo generan los motores, la energía y miles de personas, es decir,
todo lo que llena el **volumen**, que crece con el cubo. Pero en el vacío el
calor solo sale por radiación a través de la **superficie**, que crece con el
cuadrado. Cuanto más grande es la nave, más calor produce en proporción a la
superficie de la que dispone para expulsarlo. Es la ley del cubo-cuadrado otra
vez, ahora en forma de calor.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md)
y [🧪 Principios](../operacion/principios-sdf-1.md).

</details>

**1.6.** ¿Qué son las "reglas del universo" y en qué se diferencian de las leyes
de la física?

<details>
<summary>Ver respuesta</summary>

Son acuerdos narrativos: convenciones que la obra establece sobre cómo se mueve,
resiste y se transforma la nave para que el relato sea grandioso y fácil de
seguir. Son coherentes dentro de la historia, pero **no** son leyes de la
naturaleza. Distinguirlas de la física real es el objetivo educativo del curso;
señalarlas no es criticar la obra, sino aprender la diferencia entre lo que
impresiona en pantalla y lo que ocurriría de verdad.

Módulo 8: [⚖️ Reglas del universo](../reglamentos/reglas-universo-sdf-1.md).

</details>

---

## 2. 🔬 Distingue la física de la licencia creativa

**2.1.** Una obra muestra la nave-fortaleza girando con soltura para esquivar un
ataque, como si fuera un caza. ¿Qué parte de eso es física real y qué parte es
licencia creativa?

<details>
<summary>Ver respuesta</summary>

**Real**: que una nave se mueva por empuje. Los motores empujan y la nave cambia
de velocidad; eso es física correcta.

**Licencia creativa**: la agilidad. Como la aceleración es el empuje dividido
por la masa, y la masa de una mole del tamaño de una ciudad es colosal, el
cambio de rumbo sería lentísimo y habría que planificarlo con mucha antelación.
La regla interna "la nave gigante maniobra con soltura" existe para que las
escenas sean dinámicas, no porque describa el mundo.

Módulos 5 y 7: [🧪 Principios](../operacion/principios-sdf-1.md) y
[⚖️ Reglas del universo](../reglamentos/reglas-universo-sdf-1.md).

</details>

**2.2.** "Es una nave normal, pero enorme." Explica por qué esa frase es el error
central que el curso quiere corregir.

<details>
<summary>Ver respuesta</summary>

Porque supone que el escalado es neutro, y no lo es. Al agrandar manteniendo la
forma, la superficie crece con el cuadrado y el volumen (y la masa) con el cubo.
La resistencia de una columna depende de su superficie, pero el peso que soporta
depende del volumen: pasado cierto tamaño, el propio peso supera lo que la
estructura puede aguantar. No es el mismo vehículo a otra escala, es un problema
de ingeniería distinto. La ficción se agranda "sin consecuencias" para
impresionar; la física cobra la factura en masa, estructura, empuje y calor.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md)
y [🧪 Principios](../operacion/principios-sdf-1.md).

</details>

**2.3.** La ficción presenta la autonomía total y la transformación de forma como
rasgos naturales de la nave. ¿Qué hay de plausible en cada uno y qué no?

<details>
<summary>Ver respuesta</summary>

**Autonomía**: el concepto es coherente y el reciclaje es posible de verdad. Lo
que no es realista es que funcione sin más. Sostener a miles de personas exige
aire, agua, temperatura, luz y reciclaje a escala de ciudad, y cada sistema añade
masa, que exige más estructura, que exige más empuje.

**Transformación**: existen mecanismos móviles y articulados reales, así que la
idea no es magia. Pero a la escala de un barrio entero, mover partes enormes de
la propia estructura sería un reto casi imposible: cada articulación tendría que
transmitir cargas gigantescas sin fallar.

En ambos casos el patrón se repite: la idea evoca algo real, pero la escala es
lo que la rompe.

Módulos 2, 5 y 7:
[📋 Características](../operacion/caracteristicas-sdf-1.md),
[🧪 Principios](../operacion/principios-sdf-1.md) y
[⚖️ Reglas del universo](../reglamentos/reglas-universo-sdf-1.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la ley del cubo-cuadrado sin explicarla
con texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: dejar el **tamaño de la nave** como control y mostrar al lado
la **masa total** y la **tensión estructural** actualizándose en vivo. Al mover
el tamaño un poco, el usuario ve que la masa se dispara mucho más rápido y que la
tensión sube, y entiende solo por qué agrandar no es gratis. El modo de juego
"tutorial de escala", que compara la maniobra de una nave pequeña y una colosal,
enseña lo mismo desde la experiencia: se ordena el mismo empuje y una responde y
la otra apenas se mueve.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-sdf-1.md).

</details>

**3.2.** El simulador tiene un modo ciencia y un modo ficción. ¿Por qué no basta
con implementar solo el modo ciencia, que es el correcto?

<details>
<summary>Ver respuesta</summary>

Porque el valor educativo está en la **comparación**, no en la corrección. El
modo ficción sirve para engancharse: la nave maniobra con soltura, la estructura
aguanta todo y el calor no molesta. El modo ciencia aplica la ley del
cubo-cuadrado, la relación empuje/masa, la tensión estructural y el límite de
disipación, y todo se vuelve lento y delicado. Ver la misma nave en los dos modos
—idealmente lado a lado, con la interfaz avisando qué regla se activó o se
desactivó al cambiar— es lo que hace visible la diferencia entre espectáculo y
física. Un simulador que solo aplicara la física sería correcto y mudo sobre
aquello que el curso quiere enseñar.

Módulos 7 y 8: [⚖️ Reglas del universo](../reglamentos/reglas-universo-sdf-1.md)
y [🎮 Diseño de simulación](../simulacion/diseno-simulador-sdf-1.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo enunciar la ley del cubo-cuadrado sin mirar los apuntes.
- [ ] Sé explicar por qué la masa, y no los motores, decide la aceleración.
- [ ] Entiendo por qué engrosar las paredes agrava el problema estructural.
- [ ] Puedo explicar por qué disipar calor se complica al agrandar la nave.
- [ ] Distingo una regla del universo de una ley de la física.
- [ ] Puedo nombrar tres variables que el simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-sdf-1.md)
