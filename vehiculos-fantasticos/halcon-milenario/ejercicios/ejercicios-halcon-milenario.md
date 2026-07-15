# 🎯 Ejercicios y autoevaluación del Halcón Milenario

[🏠 Inicio](../../../README.md) · [🦅 Curso: Halcón Milenario](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura. Aquí no se trata de
recordar datos de una nave, sino de separar la física real de la licencia
creativa.

> 🦺 **Esto no es un examen.** No acredita nada ni habilita para operar ninguna
> máquina. La nave es ficción y este curso es análisis original con fines
> educativos: los derechos de las obras pertenecen a sus titulares. Sirve para
> comprobar si el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿De qué depende la aceleración de un carguero y por qué esa relación
decide si la nave se siente ágil o pesada?

<details>
<summary>Ver respuesta</summary>

De la **relación empuje/masa**: la aceleración es el empuje de los motores
dividido por la masa total de la nave más su carga. Más empuje acelera más;
más masa acelera menos. Un carguero "rápido" sería aquel con motores muy
grandes para su masa, no el que tenga mejor fama o mejor forma.

Módulo 5: [🧪 Principios y operación](../operacion/principios-halcon-milenario.md).

</details>

**1.2.** En el vacío, ¿qué pasa cuando el piloto apaga los motores?

<details>
<summary>Ver respuesta</summary>

Nada: la nave sigue con la misma velocidad y en la misma dirección, para
siempre. Es la primera ley de Newton. Sin aire no hay rozamiento que la frene,
así que frenar exige encender los motores en sentido contrario y gastar
propelente. La ficción hace que la nave "frene al soltar el acelerador" porque
da a las persecuciones un ritmo de coche, pero eso no ocurriría.

Módulo 5: [🧪 Principios y operación](../operacion/principios-halcon-milenario.md).

</details>

**1.3.** ¿Qué es el delta-v y por qué es una medida más útil que "cuánto queda
en el depósito"?

<details>
<summary>Ver respuesta</summary>

Es el cambio total de velocidad que la nave puede conseguir con el propelente
que lleva. Es el presupuesto de maniobra: cada encendido gasta una parte y cada
tonelada de carga extra lo recorta. Cuando se agota, la nave ya no puede
acelerar, frenar ni cambiar de rumbo, aunque le sobre energía eléctrica. Por eso
el nivel del depósito por sí solo no dice qué maniobras quedan disponibles.

Módulo 5: [🧪 Principios y operación](../operacion/principios-halcon-milenario.md)
y módulo 9: [🧰 Recursos](../recursos/recursos-halcon-milenario.md).

</details>

**1.4.** Si sobra energía en el reactor, ¿basta con eso para mover la nave?

<details>
<summary>Ver respuesta</summary>

No. Por la tercera ley de Newton, para empujarse hacia adelante hay que expulsar
masa hacia atrás. Sin propelente que lanzar no hay empuje, por mucha energía
disponible que haya. La "planta de energía casi infinita" de la ficción es
plausible como idea, pero no resuelve el problema real: la masa que se expulsa
siempre se gasta.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-halcon-milenario.md).

</details>

**1.5.** ¿Por qué el puesto de mando separa la orientación de la traslación, y
qué debe mostrar la interfaz a la vez?

<details>
<summary>Ver respuesta</summary>

Porque en el vacío no coinciden: hacia dónde apunta la nave y hacia dónde se
mueve son cosas independientes. Los propulsores de control rotan el casco, pero
el momento se conserva y el rumbo no cambia hasta encender los motores
principales. Por eso el mando de orientación y el de traslación están separados,
y la interfaz debe mostrar simultáneamente el indicador de orientación y el
vector de velocidad. La masa total también debe estar siempre visible, porque es
la que decide cuánto responde la nave.

Módulo 4: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-halcon-milenario.md).

</details>

**1.6.** ¿Qué son las "reglas del universo" y por qué el curso las corrige?

<details>
<summary>Ver respuesta</summary>

Son acuerdos narrativos: la ficción decide cómo vuelan, cargan y escapan las
naves para que el relato sea emocionante y fácil de seguir. Son coherentes
dentro de la historia, pero no son leyes de la naturaleza. El curso las contrasta
con la física real no para criticar la obra —son licencias creativas legítimas—
sino para aprender la diferencia entre lo que emociona en pantalla y lo que
ocurriría de verdad.

Módulo 7: [⚖️ Reglas del universo](../reglamentos/reglas-universo-halcon-milenario.md).

</details>

---

## 2. 🔬 Distingue la física de la licencia creativa

**2.1.** La ficción muestra al carguero corriendo igual de rápido con la bodega
vacía que repleta. ¿Qué parte de esa idea tiene base física y qué parte es
invención?

<details>
<summary>Ver respuesta</summary>

**Lo real**: se puede acelerar con carga. Un carguero cargado se mueve
perfectamente; no hay nada imposible en transportar masa por el espacio.

**La invención**: que se comporte igual. Cada tonelada extra tiene dos costes.
Primero, sube la masa total y por tanto reduce la aceleración con los mismos
motores. Segundo, para lograr el mismo cambio de velocidad hace falta más
propelente, así que la carga recorta el delta-v disponible. Un carguero lleno
maniobra más lento y llega más justo que uno vacío. La ficción lo ignora para no
complicar la acción con logística, pero es justo la esencia de mover masa por el
vacío: la carga no viaja gratis.

Módulos 5 y 7:
[🧪 Principios](../operacion/principios-halcon-milenario.md) y
[⚖️ Reglas del universo](../reglamentos/reglas-universo-halcon-milenario.md).

</details>

**2.2.** En pantalla, las naves viran en el vacío como aviones de caza, con
giros cerrados y vistosos. ¿Qué hay de cierto en esa maniobra?

<details>
<summary>Ver respuesta</summary>

**Lo real**: la nave sí puede rotar. Pares de propulsores de control opuestos la
hacen girar sobre su eje, y un propulsor aislado la desplaza de lado.

**La invención**: el viraje bancado. Un avión vira apoyándose en el aire; en el
vacío no hay contra qué apoyarse, así que no existen los virajes de ese tipo.
Reorientar el morro no cambia por sí solo la dirección en que la nave se mueve
—el momento se conserva—: para cambiar de rumbo hay que encender los motores
principales y gastar delta-v. Además, con la bodega llena tanto iniciar el giro
como detenerlo cuesta más. La maniobra realista es lenta y planificada con
antelación, no brusca.

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-halcon-milenario.md)
y módulo 7: [⚖️ Reglas del universo](../reglamentos/reglas-universo-halcon-milenario.md).

</details>

**2.3.** El "salto a la luz" cruza la galaxia casi al instante. ¿Por qué es la
licencia más grande del género y por qué no es un fallo de la obra?

<details>
<summary>Ver respuesta</summary>

**Lo real**: se puede viajar por el espacio, y el empuje por reacción funciona.

**La invención**: alcanzar la velocidad de la luz. Ningún objeto con masa puede
hacerlo: cuanto más te acercas, más energía hace falta, y esa energía crece sin
límite. Cruzar la galaxia en minutos no tiene base en la física actual, y la
energía que exigiría el salto apenas se menciona en el relato. Las distancias
reales son enormes: incluso a gran velocidad el viaje llevaría años.

No es un fallo: es un recurso narrativo que resuelve un problema concreto,
avanzar entre mundos lejanos sin aburrir al espectador. El curso solo pide que
no se presente como física real sin avisarlo.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-halcon-milenario.md) y
[🧪 Principios](../operacion/principios-halcon-milenario.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que la carga no viaja gratis, sin
explicarlo con texto. ¿Qué variables expondrías y cómo lo plantearías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mantener siempre visibles la **masa de carga**, la
**aceleración** resultante y el **delta-v restante**, y montar un tutorial de
carga que repita la misma maniobra con la bodega vacía y luego llena. El usuario
no lee que la carga pesa: **ve** que con los mismos aceleradores la nave tarda
más en cambiar de velocidad y que el presupuesto de maniobra se vacía antes.

El ciclo básico ya lo soporta: calcula la masa total sumando nave más carga, y
después la aceleración como empuje dividido por masa.

Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-halcon-milenario.md).

</details>

**3.2.** El simulador ofrece modo ciencia y modo ficción. ¿Por qué el modo es la
variable más importante y qué debe hacer la interfaz al cambiarlo?

<details>
<summary>Ver respuesta</summary>

Porque es el interruptor central del aprendizaje: gobierna todas las demás
reglas. En **modo ficción** la nave corre igual llena o vacía, frena al soltar el
acelerador y puede saltar a la luz; sirve para engancharse. En **modo ciencia**
se aplican las leyes de Newton, la relación empuje/masa, la conservación del
momento y el límite de delta-v; sirve para aprender.

Al cambiar de modo, la interfaz debe avisar **qué regla se activó o se
desactivó**. Sin ese aviso la comparación no es educativa, y presentar el salto
como si fuera física real sin advertirlo está explícitamente fuera de alcance.
Lo valioso es ver la versión espectacular y la realista del mismo carguero, lado
a lado.

Módulos 7 y 8:
[⚖️ Reglas del universo](../reglamentos/reglas-universo-halcon-milenario.md) y
[🎮 Diseño de simulación](../simulacion/diseno-simulador-halcon-milenario.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué un carguero cargado acelera menos con los mismos motores.
- [ ] Sé qué le pasa a la nave al apagar los motores y por qué.
- [ ] Entiendo el delta-v como un presupuesto de maniobra que la carga recorta.
- [ ] Puedo explicar por qué apuntar la nave no cambia hacia dónde se mueve.
- [ ] Sé distinguir una regla del universo de una ley física real.
- [ ] Puedo nombrar tres variables que un simulador de nave debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-halcon-milenario.md)
