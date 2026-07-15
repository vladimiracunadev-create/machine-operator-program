# 🎯 Ejercicios y autoevaluación del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la instrucción de
> vuelo certificada ni el manual del fabricante. Sirve para comprobar si el curso
> se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué un helicóptero necesita rotor de cola y qué pasa si falla?

<details>
<summary>Ver respuesta</summary>

Porque al hacer girar el rotor principal el motor aplica un **par** sobre el
fuselaje, que por acción y reacción tiende a girar en sentido contrario. El rotor
de cola genera un empuje lateral que compensa ese par y además controla la
guiñada. Si falla, el helicóptero pierde el control de guiñada; por eso su
transmisión y su estado son críticos.

Los **rotores en tándem** resuelven lo mismo de otra forma: sus dos rotores giran
en sentidos opuestos y los pares se cancelan, así que no llevan rotor de cola.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md).

</details>

**1.2.** ¿Cuál es la diferencia entre el paso colectivo y el paso cíclico?

<details>
<summary>Ver respuesta</summary>

El **paso colectivo** cambia el ángulo de todas las palas **por igual**: sube o
baja la sustentación total, es decir, hace subir o bajar el helicóptero. El
**paso cíclico** cambia el paso de cada pala **según su posición en el giro**, lo
que inclina el disco rotor y traslada el helicóptero hacia donde se inclina.

Los dos llegan a las palas a través del **plato cíclico**: el colectivo lo sube o
baja en bloque, y el cíclico lo inclina.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md).

</details>

**1.3.** ¿Qué es la disimetría de sustentación y cuándo aparece?

<details>
<summary>Ver respuesta</summary>

Aparece en **vuelo hacia adelante**: la pala que avanza recibe más aire que la que
retrocede, así que no generarían la misma sustentación. La articulación de las
palas equilibra ese desnivel para que el vuelo sea estable.

En vuelo estacionario no se da, porque todas las palas ven el mismo aire.

Módulo 6: [🧪 Principios y operación](../operacion/principios-helicoptero.md).

</details>

**1.4.** Si el motor falla en vuelo, ¿por qué el helicóptero no cae como una
piedra?

<details>
<summary>Ver respuesta</summary>

Por la **autorrotación**. Al descender, el flujo de aire que sube a través del
rotor lo mantiene girando, lo que permite un descenso controlado y un aterrizaje
seguro sin potencia. La **rueda libre** desconecta el motor detenido para que el
rotor pueda girar libre.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md) y
[🧪 Principios](../operacion/principios-helicoptero.md).

</details>

**1.5.** Enumera los cuatro pasos de la técnica del vuelo estacionario y di por
qué hay que corregir de forma continua.

<details>
<summary>Ver respuesta</summary>

1. Ajustar el **colectivo** para que la sustentación iguale el peso.
2. Usar el **cíclico** con pequeños movimientos para no derivar sobre el punto.
3. Compensar el **par** con los **pedales** para mantener la nariz fija.
4. Vigilar el **rotor RPM** y el **variómetro** cerca de cero.

Se corrige de forma continua porque los tres mandos **se influyen entre sí**: al
subir colectivo aumenta el par, y ese par hay que compensarlo con pedal.

Módulo 6: [🧪 Principios y operación](../operacion/principios-helicoptero.md).

</details>

**1.6.** ¿Qué licencia y qué documento personal exige Chile para pilotar un
helicóptero, y qué autoridad los otorga?

<details>
<summary>Ver respuesta</summary>

La licencia de piloto de helicóptero y sus habilitaciones están reguladas por la
**DAN 61** (edición vigente por confirmar), y se requiere además **certificado
médico aeronáutico**. Ambos los otorga la **Dirección General de Aeronáutica
Civil (DGAC)**, bajo el marco de la Ley 18.916 (Código Aeronáutico).

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-helicoptero.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Subes el colectivo para despegar y la nariz empieza a girar sola.
¿Qué está pasando y qué haces?

<details>
<summary>Ver respuesta</summary>

Al subir colectivo aumenta el paso de todas las palas, el motor entrega más
potencia y con ella crece el **par** sobre el fuselaje, que tiende a girar en
sentido contrario al rotor. La nariz gira porque el anti-par no se ajustó.

La corrección es **acompañar el colectivo con pedal**: los pedales cambian el paso
del rotor de cola y compensan el par. No es un fallo, es el comportamiento normal
del vehículo. De hecho, subir colectivo sin compensar con pedal es uno de los
errores comunes que la simulación debería enseñar a evitar.

Módulos 4 y 5:
[🎛️ Mandos](../mandos/manual-mandos-helicoptero.md) y
[🧪 Principios](../operacion/principios-helicoptero.md).

</details>

**2.2.** Un rescate en montaña, en un día caluroso. El helicóptero mantuvo el
estacionario sin problema a nivel del mar. ¿Qué cambia arriba y por qué?

<details>
<summary>Ver respuesta</summary>

La **densidad del aire** baja con la altura y con el calor, y con ella baja la
sustentación disponible: hace falta **más potencia** para sostener el mismo peso.
Se suma la turbulencia y el espacio reducido de la montaña, que complican el
estacionario y la aproximación.

Además se pierde una ayuda: el **efecto suelo**, que abarata el estacionario cerca
del terreno, no está disponible en un estacionario alto. Por eso la operación en
montaña pide más potencia y márgenes amplios.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-helicoptero.md).

</details>

**2.3.** En un estacionario sobre el mar, el piloto novato corrige el cíclico una
y otra vez y el helicóptero oscila cada vez más. ¿Qué le dirías?

<details>
<summary>Ver respuesta</summary>

Está **sobrecontrolando el cíclico**, uno de los errores comunes del estacionario:
cada corrección grande genera una desviación que exige otra corrección, y se entra
en oscilación. El cíclico se usa con **pequeños** movimientos.

El mar lo agrava porque no hay referencias fijas y el oleaje engaña, así que
conviene apoyarse en los instrumentos: horizonte artificial para la actitud y
variómetro cerca de cero.

Módulos 5 y 6:
[🧪 Principios](../operacion/principios-helicoptero.md) y
[🌍 Entornos](../operacion/entornos-helicoptero.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe el par y el anti-par sin explicarlos con
texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer el **paso colectivo** y el **pedal / anti-par**, y
mostrar junto a ellos el par que el rotor aplica sobre el fuselaje y la guiñada
resultante. Así el usuario **ve** que al subir el colectivo el indicador de par
crece y la nariz empieza a irse, y descubre solo que el pedal es lo que lo
cancela.

La interfaz debe mostrar cómo un mando afecta a los otros: es justamente lo que
hace difícil al helicóptero.

Módulo 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-helicoptero.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
autorrotación, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**, junto con el rotor RPM y la disimetría de
sustentación. En el nivel 1 la meta es elevar, mantener el hover, trasladar y
posar: la coordinación básica ya es exigente. El nivel 2 agrega par, anti-par y
efecto suelo, que son los conceptos físicos centrales del ala rotatoria.

La autorrotación llega al final porque depende de entender antes el rotor RPM y el
flujo de aire a través del rotor; sin esa base es una secuencia de teclas que se
memoriza sin comprender.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar el par y por qué hace falta compensarlo.
- [ ] Distingo el paso colectivo del paso cíclico y sé qué hace el plato cíclico.
- [ ] Puedo explicar la autorrotación sin decir "planea".
- [ ] Sé por qué el estacionario exige corregir los tres mandos de forma continua.
- [ ] Entiendo cómo la densidad del aire y el efecto suelo cambian la potencia
      necesaria.
- [ ] Conozco la licencia chilena aplicable, la autoridad y el certificado médico.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-helicoptero.md)
