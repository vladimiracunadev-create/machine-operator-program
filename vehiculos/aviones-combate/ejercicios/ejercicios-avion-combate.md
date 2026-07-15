# 🎯 Ejercicios y autoevaluación del avión de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura. Todo se mantiene en el
marco público del curso: física del vuelo, historia y principios generales.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye formación
> aeronáutica certificada ni entrenamiento militar real. Sirve para comprobar si
> el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Qué principio físico explica que un motor a reacción impulse el avión
hacia adelante?

<details>
<summary>Ver respuesta</summary>

La tercera ley de Newton: el motor expulsa gases hacia atrás a gran velocidad y
esa masa expulsada impulsa el avión hacia adelante. El recorrido interno es toma
de aire, compresor, cámara de combustión, turbina y tobera; el posquemador añade
empuje extra quemando más combustible en la tobera.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-combate.md).

</details>

**1.2.** ¿Para qué sirve el ala en flecha y por qué no se usa un ala recta en un
reactor rápido?

<details>
<summary>Ver respuesta</summary>

El ala en flecha va inclinada hacia atrás y **retrasa los efectos del vuelo
cercano al sonido**, lo que permite volar rápido con control estable. El ala
recta pertenece a los primeros reactores, de velocidad subsónica alta. El ala
delta es la otra opción para alta velocidad, con una estructura resistente.

Módulos 1 y 3: [📜 Historia](../historia/historia-avion-combate.md) y
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-combate.md).

</details>

**1.3.** Nombra los tres ejes de vuelo, su superficie de control y el mando de
cabina que los gobierna.

<details>
<summary>Ver respuesta</summary>

- **Alabeo** (eje longitudinal): alerones, con la palanca a izquierda o derecha.
- **Cabeceo** (eje lateral): estabilizador o timón de profundidad, con la
  palanca adelante o atrás.
- **Guiñada** (eje vertical): timón de dirección, con los pedales.

En muchos reactores la cola horizontal se mueve entera (estabilizador móvil).

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-combate.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-avion-combate.md).

</details>

**1.4.** ¿Qué es la carga G y por qué impone dos límites distintos?

<details>
<summary>Ver respuesta</summary>

Es el peso aparente que la maniobra multiplica: una maniobra cerrada hace que la
aceleración multiplique el peso que sienten tanto la aeronave como el piloto. De
ahí salen dos límites separados: el **estructural**, porque la célula reforzada
resiste hasta cierto punto, y el **fisiológico**, porque el piloto también tiene
un tope y por eso usa equipo especial. En la cabina se vigila con el
acelerómetro, y en simulación se representa como un límite.

Módulo 6: [🧪 Principios y operación](../operacion/principios-avion-combate.md).

</details>

**1.5.** ¿Qué significa "energía" en el vuelo de un reactor y cómo se recupera?

<details>
<summary>Ver respuesta</summary>

La energía es la velocidad y la altitud disponibles para maniobrar; el curso la
trata como energía total, suma de ambas. Una maniobra cerrada la gasta y además
sube la carga G. Se recupera con empuje, o cambiando altitud por velocidad.
Volar suave la conserva, y quedar lento a baja altura es justamente uno de los
errores que la simulación busca enseñar a evitar.

Módulo 6: [🧪 Principios y operación](../operacion/principios-avion-combate.md).

</details>

**1.6.** ¿Por qué un avión de combate no se rige por las licencias civiles de la
DGAC en Chile?

<details>
<summary>Ver respuesta</summary>

Porque es una aeronave militar. Se enmarca en la Fuerza Aérea de Chile (FACH),
dependiente del Ministerio de Defensa Nacional, bajo la Ley 18.948, y se rige
por normativa militar; no le aplican las licencias civiles de la DGAC ni la
matrícula civil del Código Aeronáutico.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-avion-combate.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** El mismo reactor despega desde el nivel del mar y luego vuela a gran
altitud. ¿Qué cambia en el vuelo y por qué?

<details>
<summary>Ver respuesta</summary>

A gran altura el aire es poco denso y frío. Menos densidad significa menos
sustentación para la misma ala y un rendimiento distinto del motor, así que la
gestión de energía pesa más y hay menos margen para maniobrar. Además el piloto
depende de la presurización y del sistema de oxígeno, que son parte de los
sistemas generales de la aeronave.

Módulos 3 y 6: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-avion-combate.md)
y [🌍 Entornos de trabajo](../operacion/entornos-avion-combate.md).

</details>

**2.2.** Un alumno de simulador encadena maniobras cerradas una tras otra y
termina lento y bajo. ¿Qué le explicarías?

<details>
<summary>Ver respuesta</summary>

Que cada maniobra cerrada cobra dos veces: gasta energía y sube la carga G. Si
se encadenan sin recuperar con empuje o sin cambiar altitud por velocidad, la
energía total se agota, y quedar lento a baja altura es uno de los errores
comunes que el curso identifica. La lectura útil aquí es el acelerómetro junto a
la velocidad: volar suave conserva energía y control.

Módulo 6: [🧪 Principios y operación](../operacion/principios-avion-combate.md).

</details>

**2.3.** Meteorología adversa en la aproximación: viento, nubes y turbulencia.
¿Qué cambia respecto de un día despejado?

<details>
<summary>Ver respuesta</summary>

Se pierden las referencias visuales, así que hay que volar por instrumentos y
trabajar con márgenes amplios. El viento y la turbulencia afectan despegue,
vuelo y aterrizaje, y la aproximación exige configurar el avión —tren y
aerofrenos— y alinear con más anticipación. El HUD ayuda precisamente porque
permite volar sin bajar la vista.

Módulos 4 y 6: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-avion-combate.md)
y [🌍 Entornos de trabajo](../operacion/entornos-avion-combate.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe el límite de carga G sin explicarlo con
texto. ¿Qué variable expondrías y cómo la mostrarías?

<details>
<summary>Ver respuesta</summary>

La carga G ya está entre las variables principales del curso, con rango de -3 a
9 G. Una idea razonable es mostrarla como un acelerómetro visible junto a la
energía total, con una alerta de exceso de G en el mismo lugar donde aparece la
alerta de baja velocidad. Así el usuario **ve** que al cerrar la maniobra la
aguja sube y la energía cae, y entiende solo por qué existen el límite
estructural y el fisiológico.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-avion-combate.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
gestión de empuje y el número de Mach, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es despegar, volar, virar y
aterrizar un reactor; añadir Mach y gestión de empuje ahí tapa lo que se quiere
enseñar. El nivel 2 introduce cargas G, energía y efectos de alta velocidad, que
son los conceptos físicos centrales. La gestión de empuje, los límites
estructurales y el Mach son detalle técnico y llegan al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar el empuje a reacción con la tercera ley de Newton.
- [ ] Sé para qué sirve el ala en flecha en el vuelo cercano al sonido.
- [ ] Nombro los tres ejes con su superficie de control y su mando.
- [ ] Distingo el límite estructural del fisiológico en las cargas G.
- [ ] Entiendo la energía total como velocidad más altitud.
- [ ] Conozco el marco institucional chileno aplicable a una aeronave militar.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-avion-combate.md)
