# 🎯 Ejercicios y autoevaluación del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada de una agencia espacial ni de un programa de ingeniería. Sirve para
> comprobar si el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué un cohete puede acelerar en el vacío, donde no hay aire contra
el que empujarse?

<details>
<summary>Ver respuesta</summary>

Porque el empuje es **por reacción**: el cohete expulsa gases hacia atrás y la
tercera ley de Newton lo empuja hacia adelante. No necesita apoyarse en el aire.
Además lleva su **propio oxidante**, así que la mezcla arde sin oxígeno externo.

Módulos 2 y 5: [📋 Características](../operacion/caracteristicas-cohete.md) y
[🧪 Principios y operación](../operacion/principios-cohete.md).

</details>

**1.2.** Subir muy alto no pone nada en órbita. ¿Qué falta?

<details>
<summary>Ver respuesta</summary>

Falta **velocidad horizontal**. Si el cohete solo ganara altura, caería de
vuelta. Para quedar en órbita baja hay que avanzar de lado a unos 7,8 km/s
(aproximado). Por eso el ascenso no es vertical: tras despegar se inclina poco a
poco hacia la horizontal en un **giro gravitatorio**.

Módulo 6: [🧪 Principios y operación](../operacion/principios-cohete.md).

</details>

**1.3.** ¿Qué dice la relación empuje-peso y qué pasa en cada uno de sus tres
casos?

<details>
<summary>Ver respuesta</summary>

Es el cociente entre el empuje del motor y el peso del cohete. Si el empuje es
**mayor** que el peso, despega; si es **igual**, flota; si es **menor**, no
despega. Como la masa baja al quemar propelente, la relación mejora durante el
ascenso aunque el empuje se mantenga.

Módulos 5 y 9: [🧪 Principios](../operacion/principios-cohete.md) y el
[🧰 diagrama de empuje-peso](../recursos/recursos-cohete.md).

</details>

**1.4.** ¿Por qué se divide un cohete en etapas, y con qué idea física conecta
esa decisión?

<details>
<summary>Ver respuesta</summary>

Para soltar la **masa vacía** y no arrastrar peso muerto. Conecta directamente
con la **ecuación del cohete (Tsiolkovski)**: el delta-v depende de la velocidad
de salida de los gases y de cuánta masa se quema frente a la masa final. Tirar
un tanque agotado mejora esa relación, así que la etapa siguiente rinde más.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-cohete.md)
y [🧪 Principios](../operacion/principios-cohete.md).

</details>

**1.5.** Motor líquido y motor sólido: nombra la diferencia que más condiciona la
operación y di dónde se usa cada uno.

<details>
<summary>Ver respuesta</summary>

El **control del empuje**. El motor líquido se regula, se apaga y a veces se
reenciende; el sólido da mucho empuje de arranque pero **no** se apaga a voluntad
una vez encendido. Por eso el líquido va en las etapas que necesitan control
fino, incluido el aterrizaje del propulsor, y el sólido se usa como refuerzo de
despegue.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-cohete.md).

</details>

**1.6.** ¿Quién autoriza un lanzamiento y bajo qué marco responde por él?

<details>
<summary>Ver respuesta</summary>

El **Estado de lanzamiento**, a través de su agencia espacial o autoridad de
licencias, dentro del marco de los tratados internacionales (UNOOSA). Ese Estado
responde por daños ante la comunidad internacional. Chile no cuenta a la fecha
con una ley espacial nacional integral: su marco interno es de política pública
más los tratados.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-cohete.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Durante el ascenso, el impulso es dejar el empuje al máximo e inclinar
rápido hacia la horizontal para ganar velocidad orbital cuanto antes. ¿Por qué es
mala idea?

<details>
<summary>Ver respuesta</summary>

Porque el cohete atraviesa aire denso y hay un punto del ascenso con **máxima
presión aerodinámica**. Empujar al máximo ahí, o inclinar demasiado rápido,
sobrecarga la estructura: son dos de los errores comunes que el curso señala.

La operación correcta es despegar vertical para salir del aire denso, regular el
empuje para no exceder el esfuerzo estructural e inclinar de forma **gradual**.
La velocidad horizontal se gana igual, pero sin romper nada.

Módulos 5 y 6: [🧪 Principios](../operacion/principios-cohete.md) y
[🌍 Entornos de trabajo](../operacion/entornos-cohete.md).

</details>

**2.2.** El propulsor se separa habiendo quemado hasta la última gota de
propelente. La misión pone la carga en órbita. ¿Se cumplió el objetivo?

<details>
<summary>Ver respuesta</summary>

A medias. La carga llegó, pero si el cohete es recuperable se perdió el
propulsor: el retorno necesita una **reserva de aterrizaje**, propelente guardado
para el encendido de reentrada y el encendido final que lo posa sobre sus patas.
Gastar todo el propelente sin reserva es un error común del curso, y la reserva
es una variable explícita del simulador.

Módulos 3 y 8: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-cohete.md)
y [🎮 Diseño de simulación](../simulacion/diseno-simulador-cohete.md).

</details>

**2.3.** Cuenta atrás en curso. La presión de un tanque no está en verde, pero el
clima es bueno y la ventana de lanzamiento se cierra en minutos. ¿Qué manda?

<details>
<summary>Ver respuesta</summary>

Manda el estado de los sistemas: la autorización de lanzamiento **requiere todos
los sistemas en verde**, y la presión de tanques es lo que evita que fallen las
turbobombas que alimentan la cámara de combustión. La ventana de lanzamiento es
una restricción de la órbita deseada, no una razón para saltarse el checklist.

Lo que corresponde es abortar con el corte de emergencia y buscar otra ventana.
El propio curso pide que la simulación exija sistemas en verde y autorización
antes de encender motores.

Módulos 4, 6 y 7: [🎛️ Mandos](../mandos/manual-mandos-cohete.md),
[🌍 Entornos](../operacion/entornos-cohete.md) y
[⚖️ Reglamentos](../reglamentos/reglamentos-cohete.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe por qué las etapas existen, sin explicar
la ecuación del cohete con texto. ¿Qué variables expondrías y cómo?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar juntas la **masa total**, el **propelente** restante
y el **estado de etapas**, con la relación empuje-peso al lado. Al separar, el
usuario **ve** que la masa cae de golpe y que la aceleración salta sin tocar el
acelerador. El concepto se entiende por el salto del indicador, no por la
fórmula.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-cohete.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
retorno del propulsor, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**, junto con la ecuación del cohete y el giro
gravitatorio. En el nivel 1 la meta es despegar, ascender y llegar a órbita de
forma guiada; en el nivel 2 entran la relación empuje-peso, las etapas y la
velocidad orbital, que son el núcleo conceptual. El retorno añade reserva de
aterrizaje, encendidos de reentrada y rejillas de guiado: es una misión completa
encima de la anterior y tapa lo que se quiere enseñar si llega antes.

Módulo 6 y [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué un cohete acelera sin aire.
- [ ] Entiendo que la órbita es velocidad horizontal, no altura.
- [ ] Sé qué pasa en los tres casos de la relación empuje-peso.
- [ ] Puedo conectar las etapas con la ecuación del cohete.
- [ ] Distingo motor líquido de sólido por su control de empuje.
- [ ] Sé quién autoriza un lanzamiento y bajo qué marco responde.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-cohete.md)
