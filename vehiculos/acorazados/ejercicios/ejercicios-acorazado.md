# 🎯 Ejercicios y autoevaluación del acorazado

[🏠 Inicio](../../../README.md) · [🛡️ Curso: Acorazados](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye formación náutica
> certificada. Sirve para comprobar si el curso se entendió y para detectar que
> módulo conviene releer. Como todo el curso, se mantiene dentro del marco
> histórico y público: nada de táctica ni de sistemas de armas.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué flota un buque de miles de toneladas de acero blindado?

<details>
<summary>Ver respuesta</summary>

Por el principio de Arquímedes: el casco desplaza un peso de agua igual al peso
total del buque. El acero pesa, pero lo que decide la flotación es el volumen
estanco que el casco encierra, no el material.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md)
y [🧪 Principios y operación](../operacion/principios-acorazado.md).

</details>

**1.2.** El blindaje protege, pero ¿qué le cuesta al buque en física?

<details>
<summary>Ver respuesta</summary>

Añade mucha masa, y eso se paga tres veces: aumenta la inercia (acelerar, frenar
y girar cuesta más), aumenta el calado, y —si el peso queda alto— sube el centro
de gravedad y reduce la estabilidad. De ahí el compromiso de diseño: más
protección implica más peso y menor velocidad o autonomía, y hay que cuidar
donde va cada tonelada.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md).

</details>

**1.3.** ¿Por qué el timón no sirve con el buque casi parado?

<details>
<summary>Ver respuesta</summary>

Porque el gobierno funciona desviando el flujo de agua en la popa: la pala del
timón necesita que haya agua corriendo sobre ella para generar la fuerza que
hace rotar el buque. Sin velocidad no hay flujo, y sin flujo no hay giro.
Intentar gobernar con el buque casi parado es uno de los errores comunes que la
simulación puede enseñar a evitar.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md)
y [🧪 Principios y operación](../operacion/principios-acorazado.md).

</details>

**1.4.** ¿Qué papel juegan el lastre y la compartimentación en la estabilidad?

<details>
<summary>Ver respuesta</summary>

El **lastre** es agua de ajuste en el fondo: baja el centro de gravedad que el
blindaje había subido, y así mejora la estabilidad. La **compartimentación** son
los mamparos estancos que dividen el casco: limitan el agua que entra a una sola
zona en lugar de dejarla inundar todo. Los dos apuntan al mismo objetivo, que el
buque vuelva a la vertical tras una escora.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md)
y [🧪 Principios y operación](../operacion/principios-acorazado.md).

</details>

**1.5.** Nombra tres instrumentos del puente y di que vigila cada uno.

<details>
<summary>Ver respuesta</summary>

Del módulo de mandos, por ejemplo:

- **Compás / giroscópica**: el rumbo, en grados.
- **Corredera**: la velocidad respecto al agua, en nudos.
- **Inclinómetro**: la escora, en grados; vigila la estabilidad.
- **Sonda**: la profundidad bajo la quilla, en metros; evita varar.

El rumbo, la velocidad y la escora deben verse en todo momento.

Módulo 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-acorazado.md).

</details>

**1.6.** ¿Por qué un buque de guerra no se rige por la Ley de Navegación
mercante, y que marco internacional sí lo alcanza?

<details>
<summary>Ver respuesta</summary>

Porque los buques de guerra quedan fuera del DL 2.222 (Ley de Navegación
mercante) y se rigen por normativa militar. En Chile el marco institucional es
la Armada de Chile, dependiente del Ministerio de Defensa Nacional, bajo la Ley
18.948. En lo internacional aplica la CONVEMAR (D.S. RREE 1.393/1997), con el
derecho de paso inocente (Arts. 17 a 26) y el régimen e inmunidad de los buques
de guerra (Arts. 29 a 32).

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-acorazado.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Vas en aproximación a puerto y te das cuenta de que llegas con
demasiada velocidad. El impulso es dar atrás toda. ¿Por qué eso no te salva y
qué debió pasar antes?

<details>
<summary>Ver respuesta</summary>

Porque la masa manda. La inercia de un buque de miles de toneladas hace que la
distancia de frenado sea enorme: dar atrás toda no detiene el buque donde
querrías, solo empieza un proceso muy largo. Y además te deja con poca o ninguna
velocidad de avance, justo cuando necesitas gobernar: sin flujo sobre la pala,
el timón deja de responder y pierdes el control del rumbo.

La corrección de verdad ocurrió antes: en la fase de aproximación se reduce la
velocidad **con mucha antelación**. Toda maniobra se anticipa; subestimar la
distancia de frenado es un error típico del curso.

Módulo 6: [🧪 Principios y operación](../operacion/principios-acorazado.md).

</details>

**2.2.** Navegando en costa, una vía de agua inunda un compartimento de un solo
costado y el inclinómetro empieza a marcar escora. ¿Qué está pasando y qué
conceptos de flotabilidad entran en juego?

<details>
<summary>Ver respuesta</summary>

Es una **inundación asimétrica**: entra peso en un costado y no en el otro, así
que el buque escora hacia ese lado. La compartimentación ya está haciendo su
trabajo, contener el agua en esa zona en vez de dejarla correr por el casco.

Los conceptos que entran son el achique y la **contrainundación**, es decir,
igualar el peso entre costados para corregir la escora. Y hay contexto que
agrava: en costa el riesgo típico es varar por el gran calado, y una escora
cambia el calado disponible. La sonda importa tanto como el inclinómetro. El
módulo de simulación trata este estado como **Emergencia**, con alarmas activas.

Módulos 3, 4 y 6: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-acorazado.md),
[🎛️ Mandos](../mandos/manual-mandos-acorazado.md) y
[🌍 Entornos de trabajo](../operacion/entornos-acorazado.md).

</details>

**2.3.** Temporal en mar abierto: viento fuerte y mar gruesa. ¿Qué cambia
respecto de una travesía tranquila?

<details>
<summary>Ver respuesta</summary>

El oleaje afecta al rumbo, a la escora y a los esfuerzos del casco a la vez, y
el viento añade deriva. El ajuste de navegación es reducir velocidad y cuidar la
estabilidad, no mantener el ritmo de travesía. Es el entorno donde el centro de
gravedad alto del blindaje se nota más: la escora deja de ser un número tranquilo
en el inclinómetro y pasa a ser lo que se vigila.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-acorazado.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la inercia sin explicarla con texto.
¿Qué expondrías y como lo mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: hacer visible el **retardo entre orden y respuesta**. Mostrar
juntos el régimen ordenado en el telégrafo y el régimen real de la máquina, y el
ángulo de timón ordenado frente al rumbo que efectivamente va cambiando. El
usuario ve que la orden ya está dada y el buque todavía no la ha obedecido, y
entiende solo por qué toda maniobra se anticipa.

El módulo de mandos lo pide explícitamente: la simulación debe reflejar el gran
retardo entre orden y respuesta.

Módulos 4 y 8: [🎛️ Mandos](../mandos/manual-mandos-acorazado.md) y
[🎮 Diseño de simulación](../simulacion/diseno-simulador-acorazado.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
escora, el lastre y la compartimentación, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es rumbo, velocidad y
flotación básica; meter estabilidad ahí añade carga que tapa lo que se quiere
enseñar. El nivel 2 introduce la inercia, la distancia de frenado y el viento,
que son lo que de verdad define navegar una gran masa. La estabilidad, la escora,
el lastre y la compartimentación son la capa fina y llegan al final.

Módulo 6: [🧪 Principios y operación](../operacion/principios-acorazado.md).
Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué flota un casco de acero blindado.
- [ ] Entiendo que el blindaje se paga en inercia, calado y estabilidad.
- [ ] Sé por qué el timón necesita velocidad para gobernar.
- [ ] Puedo explicar lastre, compartimentación y contrainundación.
- [ ] Conozco los instrumentos del puente y que vigila cada uno.
- [ ] Sé por qué un buque de guerra no cae bajo la ley mercante.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-acorazado.md)
