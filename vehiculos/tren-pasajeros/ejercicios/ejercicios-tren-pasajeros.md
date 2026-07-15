# 🎯 Ejercicios y autoevaluación del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada del operador ferroviario ni los manuales del fabricante. Sirve para
> comprobar si el curso se entendió y para detectar que módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué el maquinista no dirige la trayectoria del tren, y de qué
depende entonces su seguridad?

<details>
<summary>Ver respuesta</summary>

Porque la vía lo guía: la rueda de pestaña con perfil cónico sigue el riel y el
tren no cambia de rumbo por voluntad del maquinista. Su trabajo es regular la
tracción y el freno, vigilar la señalización y respetar las velocidades. La
seguridad depende de la señalización y de las distancias de frenado, no de
esquivar a la vista.

Módulos 2 y 5: [📋 Características](../operacion/caracteristicas-tren-pasajeros.md)
y [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md).

</details>

**1.2.** En la tracción diesel-eléctrica, ¿el motor diesel mueve las ruedas?

<details>
<summary>Ver respuesta</summary>

No. El motor diesel mueve un **generador**, que produce electricidad, y esa
electricidad alimenta los motores de tracción que sí mueven los ejes. Son la
misma familia de motores que usa la tracción eléctrica pura; solo cambia de
dónde viene la corriente. La ventaja es que no necesita catenaria y sirve en
vías sin electrificar.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md).

</details>

**1.3.** ¿Qué es la adherencia rueda-riel y por qué limita a la vez la tracción y
el frenado?

<details>
<summary>Ver respuesta</summary>

Es el agarre disponible del contacto acero-acero antes de que la rueda patine o
se bloquee. Ese contacto es muy pequeño y su coeficiente de adherencia es
**bajo**, mucho menor que el de un neumático sobre asfalto. Toda la tracción y
todo el frenado pasan por ahí, así que el mismo límite corta las dos cosas:
demasiada tracción hace patinar, demasiado freno bloquea. La humedad, las hojas
y la grasa lo reducen aún más; el arenado lo aumenta de forma puntual, y más
peso por eje da más adherencia disponible.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md).

</details>

**1.4.** ¿Por qué el freno neumático se considera a prueba de fallos?

<details>
<summary>Ver respuesta</summary>

Porque trabaja con aire comprimido en una tubería de freno que recorre todo el
tren, y **al bajar la presión** cada vehículo aplica sus zapatas. Si la tubería
se corta, la presión cae y el tren frena solo. Por eso el manómetro de la tubería
de freno es un instrumento de alta importancia y la presión debe verificarse
antes de arrancar.

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-tren-pasajeros.md).

</details>

**1.5.** Ordena los cinco pasos de un frenado anticipado.

<details>
<summary>Ver respuesta</summary>

1. Identificar la señal o el andén objetivo con mucha antelación.
2. Comenzar a frenar mucho antes que un vehículo de carretera.
3. Usar primero el freno dinámico o regenerativo para cuidar las zapatas.
4. Complementar con el freno neumático según la distancia restante.
5. Ajustar la fuerza a la adherencia disponible para no bloquear ruedas.

El orden importa: la gran masa obliga a decidir temprano, y el dinámico va
primero porque ahorra desgaste de zapatas y, en su variante regenerativa,
devuelve energía a la catenaria.

Módulo 5: [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md).

</details>

**1.6.** ¿Qué habilitación exige Chile para conducir un tren de pasajeros?

<details>
<summary>Ver respuesta</summary>

No aplica una licencia de conducir de vía pública (clases A, B o C). El
maquinista requiere una **habilitación o certificación específica del operador**
ferroviario, que define EFE según su normativa interna. El régimen exacto de
habilitación de maquinistas queda por confirmar en la fuente oficial. La
autoridad reguladora es el Ministerio de Transportes (MTT).

Módulo 7: [⚖️ Reglamentos](../reglamentos/reglamentos-tren-pasajeros.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md), sección 1.6.

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Arrancas en un tramo con riel húmedo y hojas, y notas patinaje. El
impulso es aplicar más tracción. ¿Por qué es mala idea y qué conviene hacer?

<details>
<summary>Ver respuesta</summary>

Porque el patinaje ya indica que se agotó la adherencia disponible: la humedad y
las hojas la reducen, y añadir tracción solo hace girar la rueda más rápido sin
convertir esa fuerza en avance. Aplicar demasiada tracción y provocar patinaje en
riel húmedo es uno de los errores comunes que la simulación busca enseñar a
evitar.

Lo razonable es reducir la tracción hasta recuperar el agarre y aplicarla de
forma progresiva, no en on/off. Si el arranque sigue siendo difícil, están los
**areneros**, que dejan caer arena sobre el riel para aumentar el agarre de forma
puntual.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-pasajeros.md)
y [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md).

</details>

**2.2.** Un maquinista novato conduce mirando la vía por delante, como haría en
un auto, y frena cuando ve el andén. ¿Qué dos problemas tiene?

<details>
<summary>Ver respuesta</summary>

Primero: la gran masa. La enorme inercia hace que el tren frene despacio, con
distancias de cientos de metros a alta velocidad. Cuando ve el andén ya es tarde;
frenar tarde olvidando la masa es un error típico.

Segundo: el tren no se detiene a la vista, obedece señales. La circulación se
ordena con señales de vía y ATP, y el maquinista respeta la señal, no la vista
libre del camino. El panel ATP repite la señal en cabina y puede frenar el tren
si el maquinista no responde.

Lo correcto es identificar la señal o el andén objetivo con mucha antelación y
anticipar, sobre todo en interurbano, donde las distancias de frenado son muy
largas.

Módulos 5 y 6: [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md)
y [🌍 Entornos de trabajo](../operacion/entornos-tren-pasajeros.md).

</details>

**2.3.** Llegas a una estación y detienes el tren, pero las puertas quedan
desalineadas con el andén. ¿Por qué importa y qué lo evita?

<details>
<summary>Ver respuesta</summary>

Importa porque en estaciones y andenes el riesgo típico es el atrapamiento en
puertas y el hueco al andén, durante el ascenso y descenso de pasajeros. No
alinear las puertas con el andén al detenerse es uno de los errores comunes del
módulo de operación.

Lo evita la parada en el punto exacto con freno suave, que es una fase propia de
la operación, junto con el enclavamiento de puertas, que impide abrir con el tren
en marcha. Por eso el curso propone desafíos de frenado de precisión en andén
como modo de juego.

Módulos 5 y 6: [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md)
y [🌍 Entornos de trabajo](../operacion/entornos-tren-pasajeros.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la gran masa sin explicarla con texto.
¿Qué variables expondrías y como las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: modelar la **masa del tren** (fijo más pasajeros) y la
**adherencia** (0 a 1), y mostrar junto al velocímetro la distancia de frenado
proyectada con el freno aplicado en ese momento, contra la distancia que falta
hasta la señal o el andén. Así el usuario **ve** que la marca de frenado pasa
antes que el objetivo cuando decidió tarde, y entiende solo por qué hay que
frenar mucho antes que en un vehículo de carretera.

Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-tren-pasajeros.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
adherencia variable y el arenado, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es aplicar tracción, frenar y
respetar señales; meter adherencia variable ahí añade una capa que tapa lo que se
quiere enseñar. El nivel 2 introduce la inercia, la gran masa y la distancia de
frenado, que son los conceptos físicos centrales del tren. La adherencia variable,
el freno dinámico, el ATP y el arenado son el detalle técnico y llegan al final.

Módulo 5: [🧪 Principios y operación](../operacion/principios-tren-pasajeros.md).
Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué la vía guía al tren y el maquinista no lo dirige.
- [ ] Sé decir qué mueve el motor diesel en la tracción diesel-eléctrica.
- [ ] Entiendo la adherencia rueda-riel como el límite común de tracción y freno.
- [ ] Puedo explicar por qué el freno neumático es a prueba de fallos.
- [ ] Sé ordenar los pasos de un frenado anticipado y decir por qué ese orden.
- [ ] Conozco la habilitación chilena aplicable al maquinista.
- [ ] Puedo nombrar tres variables que un simulador de tren debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-tren-pasajeros.md)
