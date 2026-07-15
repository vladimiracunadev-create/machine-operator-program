# 🎯 Ejercicios y autoevaluación de la moto

[🏠 Inicio](../../../README.md) · [🏍️ Curso: Motos](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la evaluación de una
> escuela de conducción certificada. Sirve para comprobar si el curso se
> entendió y para detectar que módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** Al frenar fuerte, ¿por qué el freno delantero aporta la mayor parte de
la capacidad de detención?

<details>
<summary>Ver respuesta</summary>

Porque al frenar el peso se transfiere hacia adelante: la rueda delantera queda
más cargada y por tanto dispone de más adherencia para frenar sin bloquearse.
La trasera, aligerada, se bloquea antes. Por eso usar solo el freno trasero en
una detención fuerte es uno de los errores típicos.

Módulo 5: [🧪 Principios y operación](../operacion/principios-moto.md).

</details>

**1.2.** A velocidad de marcha, ¿qué hace girar realmente a la moto: el giro del
manillar o la inclinación?

<details>
<summary>Ver respuesta</summary>

La inclinación. A baja velocidad se gira el manillar, pero en marcha el cambio
de rumbo viene sobre todo de inclinar la moto, y la inclinación se inicia con el
**contramanillar**: se empuja el manillar hacia el lado contrario al que se
quiere ir.

Módulo 5: [🧪 Principios y operación](../operacion/principios-moto.md).

</details>

**1.3.** ¿Por qué una moto es más estable cuanto más rápido va?

<details>
<summary>Ver respuesta</summary>

Por el efecto giroscópico de las ruedas en giro y por la geometría de la
dirección, que tiende a autoalinearla. A muy baja velocidad esos dos efectos casi
desaparecen y el equilibrio depende del piloto.

Módulo 5: [🧪 Principios y operación](../operacion/principios-moto.md).

</details>

**1.4.** ¿Qué es la adherencia y por qué limita a la vez la aceleración, el
frenado y la inclinación?

<details>
<summary>Ver respuesta</summary>

Es el agarre disponible del neumático antes de deslizar. Es un presupuesto único
y compartido: lo que se gasta en frenar no está disponible para inclinar. Por eso
frenar fuerte y tumbar a la vez es lo que agota el margen y hace perder el tren
delantero.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-moto.md)
y [🧪 Principios](../operacion/principios-moto.md).

</details>

**1.5.** Ordena las cinco fases de una curva.

<details>
<summary>Ver respuesta</summary>

1. Ajustar la velocidad **antes** de entrar.
2. Mirar hacia la salida, no a la rueda delantera.
3. Inclinar de forma progresiva.
4. Mantener o abrir suavemente el acelerador dentro de la curva.
5. Enderezar y acelerar a la salida.

El orden importa: frenar ya dentro de la curva consume la adherencia que
sostiene la inclinación.

Módulo 5: [🧪 Principios y operación](../operacion/principios-moto.md).

</details>

**1.6.** ¿Qué licencia exige Chile para conducir una motocicleta y qué elemento
de seguridad es obligatorio?

<details>
<summary>Ver respuesta</summary>

Licencia **Clase C** (vehículos motorizados de dos o tres ruedas) y casco.

Módulo 7: [⚖️ Reglamentos](../reglamentos/reglamentos-moto.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Vas en una curva larga y notas que te has metido más rápido de lo que
querías. El impulso es cerrar el acelerador de golpe. ¿Por qué es mala idea y
qué conviene hacer?

<details>
<summary>Ver respuesta</summary>

Cerrar de golpe transfiere peso hacia adelante bruscamente y descarga la rueda
trasera justo cuando la moto está inclinada, es decir, cuando el margen de
adherencia ya está comprometido. Además tiende a enderezar la trayectoria y a
llevarte hacia el exterior.

Lo razonable es mantener la mirada en la salida, sostener el acelerador estable
y aumentar la inclinación si queda margen. La corrección de verdad ocurrió
antes: la velocidad se ajusta **antes** de entrar.

</details>

**2.2.** Un piloto novato frena siempre solo con el pie. ¿Qué dos consecuencias
tiene y qué le dirías?

<details>
<summary>Ver respuesta</summary>

Primera: la distancia de detención se alarga mucho, porque renuncia a la rueda
que más adherencia tiene al frenar. Segunda: la trasera, aligerada por la
transferencia de peso, se bloquea con facilidad y puede irse de lado.

La recomendación es usar **ambos** frenos, con el delantero llevando la mayor
parte y de forma progresiva, no de golpe.

</details>

**2.3.** Lluvia sobre asfalto urbano, con pintura de paso de cebra y tapas
metálicas. ¿Qué cambia respecto de la conducción en seco?

<details>
<summary>Ver respuesta</summary>

Baja la adherencia disponible, y baja de forma **irregular**: la pintura y el
metal mojados agarran mucho menos que el asfalto de al lado. Al reducirse el
presupuesto de agarre hay que estirar distancias, frenar antes y más suave, e
inclinar menos, evitando pisar esas superficies justo mientras se frena o se
tumba.

Módulo 6: [🌍 Entornos de trabajo](../operacion/entornos-moto.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la transferencia de peso sin explicarla
con texto. ¿Qué variable expondrías y como la mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: modelar la carga sobre cada rueda y mostrarla como un
indicador que se mueve al frenar y acelerar, junto al margen de adherencia
restante de cada neumático. Así el usuario **ve** que al frenar la barra
delantera crece y la trasera se vacía, y entiende solo por qué el freno trasero
bloquea antes.

Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-moto.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
embrague y las marchas, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es acelerar, frenar, girar y
respetar señales; meter embrague ahí añade carga de manejo que tapa lo que se
quiere enseñar. El nivel 2 introduce inercia, transferencia de peso y límite de
adherencia, que son los conceptos físicos centrales. El embrague, las marchas y
el régimen del motor son detalle mecánico y llegan al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué el freno delantero frena más.
- [ ] Puedo explicar el contramanillar sin recurrir a "se gira el manillar".
- [ ] Entiendo la adherencia como un presupuesto que se reparte.
- [ ] Sé ordenar las fases de una curva y decir por qué ese orden.
- [ ] Conozco la licencia chilena aplicable y el equipo obligatorio.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-moto.md)
