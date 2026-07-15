# 🎯 Ejercicios y autoevaluación del dron

[🏠 Inicio](../../../README.md) · [🕹️ Curso: Drones](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye una formación de
> piloto de RPAS certificada ni el manual del fabricante. Sirve para comprobar si
> el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** Un multirotor no tiene superficies móviles. ¿Cómo consigue entonces
cabecear, alabear y guiñar?

<details>
<summary>Ver respuesta</summary>

Variando el **rpm de rotores concretos**. Todo el control nace de la diferencia
de empuje: más empuje atrás y menos adelante inclina el dron y lo hace avanzar
(cabeceo); más empuje de un lado que del otro lo desplaza de lado (alabeo). Subir
o bajar el rpm de los cuatro rotores por igual produce ascenso o descenso.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-dron.md).

</details>

**1.2.** ¿Por qué las hélices de un cuadricóptero no giran todas en el mismo
sentido, y qué se aprovecha de eso para girar la nariz?

<details>
<summary>Ver respuesta</summary>

Giran en sentidos alternos —dos horario y dos antihorario— para que sus **pares
se cancelen**; si todas giraran igual, el dron rotaría sobre sí mismo. La guiñada
aprovecha justo ese equilibrio: al acelerar los rotores que giran en un sentido y
frenar los del otro, aparece un **par neto** que rota el dron sobre su eje
vertical.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-dron.md)
y [🧪 Principios](../operacion/principios-dron.md).

</details>

**1.3.** ¿Es un dron multirotor estable por sí mismo?

<details>
<summary>Ver respuesta</summary>

No. Su estabilidad es **por control activo**: la controladora de vuelo lee la IMU
muchas veces por segundo y corrige la actitud ajustando el rpm de cada motor. Sin
ese lazo de corrección continuo, el aparato no se sostiene.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-dron.md)
y [🧪 Principios](../operacion/principios-dron.md).

</details>

**1.4.** ¿Qué mando va en cada stick del radiocontrol?

<details>
<summary>Ver respuesta</summary>

- Stick izquierdo, vertical: **throttle** (empuje total, la altura).
- Stick izquierdo, horizontal: **guiñada** (gira la nariz).
- Stick derecho, vertical: **cabeceo** (avanza o retrocede).
- Stick derecho, horizontal: **alabeo** (desplaza a los lados).

Los dos sticks se coordinan de forma continua, y el modo de vuelo activo cambia
cómo responden.

Módulo 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-dron.md).

</details>

**1.5.** Ordena las seis fases de operación de un vuelo.

<details>
<summary>Ver respuesta</summary>

1. **Inspección previa**: hélices, batería, GPS, enlace, firmware, zona permitida.
2. **Armado**: confirmar modo, satélites suficientes, área despejada.
3. **Despegue**: subir throttle suave y verificar estabilidad.
4. **Misión**: mantener el enlace, vigilar batería y distancia.
5. **Retorno**: manual o automático, subiendo antes a altura segura.
6. **Aterrizaje**: descenso controlado y desarmar motores.

El orden importa: armar sin satélites suficientes o sin revisar la zona traslada
el problema al aire, donde ya no se puede resolver en tierra.

Módulo 6: [🧪 Principios y operación](../operacion/principios-dron.md).

</details>

**1.6.** ¿Qué autoridad y qué norma rigen la operación civil de drones en Chile?

<details>
<summary>Ver respuesta</summary>

La **DGAC** (Dirección General de Aeronáutica Civil), a través de la norma
**DAN 151**, sobre operaciones de aeronaves pilotadas a distancia. La DAN 151
cubre el registro del aparato, la responsabilidad del piloto a distancia y las
condiciones de operación, dentro del Código Aeronáutico.

Los umbrales concretos de peso, altura máxima y distancias dependen de la edición
vigente y en el curso se marcan como "(por confirmar)".

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-dron.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Vas a inspeccionar una torre metálica. Al acercarte, el dron empieza a
derivar y la estación muestra menos satélites. ¿Qué está pasando y qué haces?

<details>
<summary>Ver respuesta</summary>

Entre estructuras metálicas la señal de GPS se degrada y el metal altera la
brújula, así que el dron pierde el mantenimiento de posición: por eso deriva. El
modo GPS ya no puede sostener el punto.

Lo razonable es pasar a **modo estabilizado**, que nivela la actitud sin fijar la
posición, y volar con control manual fino y márgenes amplios respecto de la
estructura. Conviene tener presente que en ese modo el dron ya no se queda quieto
solo: el piloto corrige de forma continua.

Módulos 6 y 4: [🌍 Entornos de trabajo](../operacion/entornos-dron.md) y
[🎛️ Mandos](../mandos/manual-mandos-dron.md).

</details>

**2.2.** Un piloto novato vuela lejos, en campo abierto y con viento. Ignora el
aviso de batería baja porque "todavía marca algo". ¿Qué dos riesgos acumula?

<details>
<summary>Ver respuesta</summary>

Primero: el viento se compensa **gastando batería**, así que la autonomía real es
menor que la que sugiere el porcentaje, y el retorno contra el viento consume aún
más. Segundo: a distancia larga el retorno tarda, y si la carga se agota en el
aire el dron no vuelve, se cae.

La regla del curso es que la batería y la distancia se vigilan durante todo el
vuelo, no al final. El aviso de batería baja existe precisamente para que el
retorno se inicie mientras todavía hay energía para completarlo.

Módulos 5 y 6: [🧪 Principios](../operacion/principios-dron.md) y
[🌍 Entornos](../operacion/entornos-dron.md).

</details>

**2.3.** Un cliente pide grabar el público de un evento al aire libre, cerca de un
aeródromo. ¿Qué respondes?

<details>
<summary>Ver respuesta</summary>

Que no se opera. No es un vuelo que se ajuste con más cuidado: son dos
restricciones a la vez. Está prohibido **sobrevolar aglomeraciones de personas** y
está prohibido **operar cerca de aeropuertos y aeródromos**, por el riesgo grave
para la aviación. En estos entornos la regla es no volar, no adaptar el vuelo.

A eso se suma el respeto de la privacidad al usar la cámara.

Módulos 6 y 7: [🌍 Entornos](../operacion/entornos-dron.md) y
[⚖️ Reglamentos](../reglamentos/reglamentos-dron.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe por qué se pierde un dron sin explicarlo
con texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar de forma permanente **batería, distancia y enlace de
radio**, que son las tres que limitan el vuelo, y hacerlas visiblemente
dependientes entre sí. El enlace baja con la distancia y la interferencia; la
batería cae más rápido cuando el viento obliga a compensar. Así el usuario **ve**
que alejarse cuesta energía y señal a la vez, y entiende solo por qué el retorno
hay que iniciarlo antes de lo que parece.

La interfaz debería avisar **antes** de que el enlace o la batería lleguen al
límite, no cuando ya llegaron.

Módulos 8 y 4: [🎮 Diseño de simulación](../simulacion/diseno-simulador-dron.md)
y [🎛️ Mandos](../mandos/manual-mandos-dron.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
pérdida de GPS y el fail-safe, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es despegar, mantener el hover,
trasladar y aterrizar: con el modo GPS sosteniendo el punto, el usuario aprende a
coordinar los dos sticks sin más carga. El nivel 2 agrega viento, autonomía de
batería y límite de enlace, que son los conceptos de gestión centrales. Los modos
de vuelo, la pérdida de GPS y el fail-safe son la capa que obliga a resolver una
emergencia, y solo tienen sentido cuando lo anterior ya está sólido.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md) y el
[🎮 diseño de simulación](../simulacion/diseno-simulador-dron.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar cómo se controla un multirotor sin superficies móviles.
- [ ] Puedo explicar la guiñada por par sin recurrir a "gira porque sí".
- [ ] Entiendo que la estabilidad del dron es activa, no natural.
- [ ] Sé qué mando va en cada stick y qué hace cada modo de vuelo.
- [ ] Sé ordenar las fases de operación y decir por qué ese orden.
- [ ] Conozco la autoridad y la norma chilenas aplicables, y las zonas prohibidas.
- [ ] Puedo nombrar tres variables que un simulador de dron debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-dron.md)
