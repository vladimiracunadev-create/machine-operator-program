# 🎯 Ejercicios y autoevaluación de la grúa

[🏠 Inicio](../../../README.md) · [🏗️ Curso: Grúas](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y giran
sobre el mismo eje que el curso entero: la estabilidad. Las respuestas están
plegadas a propósito: intenta responder antes de abrirlas, porque el valor está
en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación de un
> operador certificado ni el manual del fabricante. Sirve para comprobar si el
> curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Qué es el momento de carga y por qué es el parámetro crítico de una
grúa?

<details>
<summary>Ver respuesta</summary>

Es el producto del **peso por el radio**. La carga actúa como una palanca sobre
el eje de giro: cuanto más lejos está del eje, mayor es el efecto de vuelco para
un mismo peso. Es crítico porque la grúa no vuelca por el peso en sí, sino por
el momento que ese peso genera a esa distancia.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md)
y [🧪 Principios y operación](../operacion/principios-grua.md).

</details>

**1.2.** ¿Por qué al aumentar el radio baja la capacidad de izaje?

<details>
<summary>Ver respuesta</summary>

Porque la grúa tiene un momento máximo que puede resistir, fijado por su
contrapeso y su base. Como el momento es peso por radio, si el radio aumenta el
peso debe disminuir en proporción inversa para no superar ese máximo.

El ejemplo del curso: con un momento máximo de 150 t·m, a 3 m de radio se izan
50 t (50 x 3 = 150), pero a 15 m ese mismo momento solo permite 10 t
(10 x 15 = 150).

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md).

</details>

**1.3.** Según la tabla de carga del curso (grúa de 50 t, estabilizadores
extendidos), ¿cuánto puede izar a 20 metros de radio y qué porcentaje del máximo
representa?

<details>
<summary>Ver respuesta</summary>

**5.5 toneladas**, que es el **11 %** de su capacidad nominal. A 3 m de radio iza
sus 50 t completas; a 20 m solo admite 5.5 t.

Conviene recordar además que la tabla corresponde siempre a una configuración
concreta (contrapeso, extensión de estabilizadores y largo de pluma): cambiar
cualquiera de esos datos obliga a usar otra tabla.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md).

</details>

**1.4.** ¿Qué hace el LMI y por qué es el instrumento central de la cabina?

<details>
<summary>Ver respuesta</summary>

El **LMI (Load Moment Indicator)** o indicador de momento de carga mide en tiempo
real el peso izado y el radio, calcula el momento y lo compara con el máximo de
la tabla. Avisa al acercarse al límite y corta los movimientos que agravan la
condición antes de llegar al vuelco.

Es central porque en una grúa la prioridad no es la velocidad sino el control del
momento de carga: debe estar siempre visible y ser el primer instrumento en el
campo de visión.

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-grua.md).

</details>

**1.5.** ¿Para qué sirven los estabilizadores y por qué su extensión cambia la
tabla de carga que se debe usar?

<details>
<summary>Ver respuesta</summary>

Son brazos que se extienden lateralmente y apoyan zapatas en el suelo, ampliando
la base de sustentación. Cuanto mayor es esa base, más lejos queda el punto de
vuelco y más momento resistente aporta la grúa.

Por eso su extensión (completa, media o nula) cambia el límite de capacidad y
obliga a usar la tabla correspondiente. Además la grúa debe quedar **nivelada**:
una inclinación pequeña desplaza el centro de gravedad y reduce la capacidad, y
el terreno debe soportar la presión de la zapata, porque si cede se pierde la
base.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md).

</details>

**1.6.** ¿Qué licencia exige Chile para operar una grúa y qué normativa la fija?

<details>
<summary>Ver respuesta</summary>

Licencia **Clase D** (especial) para maquinaria automotriz, según la Ley 18.290
Art. 12. Edad mínima 18 años, y el examen práctico se rinde sobre la maquinaria
específica a operar.

Módulo 7: [⚖️ Reglamentos](../reglamentos/reglamentos-grua.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Tienes la carga tomada y el LMI marca un porcentaje cómodo, pero la
carga queda corta: falta alcance. El impulso es telescopiar la pluma para
llegar. ¿Qué pasa con la estabilidad y qué alternativa hay?

<details>
<summary>Ver respuesta</summary>

Telescopiar extiende la pluma y **aleja la carga del eje**: aumenta el radio y,
con el mismo peso colgando, sube el momento de carga. El porcentaje del LMI que
parecía cómodo empieza a subir sin que la carga haya cambiado de peso. Es
exactamente el error de superar el radio máximo de la tabla al bajar o
telescopiar la pluma.

La alternativa es ganar alcance sin ganar radio donde se pueda: reposicionar la
grúa más cerca del punto de montaje, que es una decisión de la fase de
posicionamiento, no de la de izaje. Si hay que trabajar a ese radio, se vuelve a
la tabla de carga y se confirma que el peso cabe; si no cabe, la maniobra no se
hace.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md)
y [🧪 Principios y operación](../operacion/principios-grua.md).

</details>

**2.2.** Un operador novato iza sin extender los estabilizadores porque "la carga
es liviana y va a ser rápido". ¿Qué le dirías?

<details>
<summary>Ver respuesta</summary>

Que sin estabilizadores la base de sustentación es mucho menor, el punto de
vuelco queda más cerca del eje y el momento resistente cae. La grúa está usando
una condición que no corresponde a ninguna tabla de carga válida para esa
maniobra, y "liviana" no significa nada mientras no se conozca el radio: el
momento es peso **por radio**.

Además la máquina debe quedar nivelada antes de cargar el gancho. El orden del
curso no es decorativo: planificación, posicionamiento, **estabilización**,
izaje. El sistema, de hecho, debería impedir el izaje si la grúa no está
estabilizada y nivelada.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua.md)
y [🧪 Principios y operación](../operacion/principios-grua.md).

</details>

**2.3.** Izaje en puerto con contenedores y viento marino en aumento. ¿Qué
cambia respecto de una obra cerrada?

<details>
<summary>Ver respuesta</summary>

El viento empuja la carga y la pluma: aumenta el **radio efectivo** y el
balanceo, y por eso reduce el límite de izaje. Sobre cierto umbral la operación
se suspende. El anemómetro pasa a ser un instrumento de decisión, no un adorno,
y el ritmo alto del puerto no justifica saltarse esa lectura.

El balanceo se controla además con movimientos lentos de giro y traslado:
girar demasiado rápido lo provoca por sí solo, y una carga balanceando cambia el
radio real de forma que la tabla no contempla.

Módulos 5 y 6: [🧪 Principios y operación](../operacion/principios-grua.md) y
[🌍 Entornos de trabajo](../operacion/entornos-grua.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la relación radio-capacidad sin
explicarla con texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar de forma continua el **radio**, el **peso de la
carga** y el **porcentaje de capacidad** del LMI, y dejar que el usuario vea cómo
el porcentaje sube al bajar o telescopiar la pluma **sin que el peso cambie**. El
número que se mueve solo cuando se mueve la geometría enseña la idea mejor que un
párrafo.

Por eso el curso recomienda mostrar el radio y el porcentaje de capacidad de
forma continua, para que el usuario relacione cada movimiento con la estabilidad.

Módulos 4 y 8: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-grua.md) y
[🎮 Diseño de simulación](../simulacion/diseno-simulador-grua.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
viento y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**, junto con la capacidad del terreno, el reeving y los
márgenes de momento de carga. En el nivel 1 la meta es estabilizar, izar, girar y
depositar respetando el LMI; añadir viento ahí mete una variable que altera el
resultado sin que el usuario domine todavía lo básico. El nivel 2 introduce
radio, ángulo, tabla de carga y balanceo, que son el núcleo conceptual.

El viento es un factor real e importante, pero se entiende cuando ya se entiende
el radio: lo que hace es aumentar el radio efectivo y el balanceo.

Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-grua.md) y los
[🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar el momento de carga como peso por radio.
- [ ] Sé por qué al alejar la carga del eje baja la capacidad.
- [ ] Puedo leer una tabla de carga y decir qué configuración supone.
- [ ] Entiendo qué mide el LMI y por qué avisa y corta.
- [ ] Sé por qué se estabiliza y se nivela antes de tocar el gancho.
- [ ] Conozco la licencia chilena aplicable a la maquinaria automotriz.
- [ ] Puedo nombrar tres variables que un simulador de grúa debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-grua.md)
