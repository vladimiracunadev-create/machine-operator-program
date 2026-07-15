# 🎯 Ejercicios y autoevaluación de la nave espacial

[🏠 Inicio](../../../README.md) · [🚀 Curso: Naves espaciales](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada de un programa espacial ni de una institución aeroespacial. Sirve
> para comprobar si el curso se entendió y para detectar que módulo conviene
> releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué un motor cohete funciona en el vacío y un motor de avión no?

<details>
<summary>Ver respuesta</summary>

Porque el cohete avanza por **propulsión por reacción**: expulsa masa a gran
velocidad y vale la tercera ley de Newton, sin necesitar aire. Para quemar sin
aire externo lleva su propio **oxidante** además del combustible. Un avión, en
cambio, depende del aire de la atmósfera.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md).

</details>

**1.2.** Estar en órbita, ¿es estar fuera del alcance de la gravedad?

<details>
<summary>Ver respuesta</summary>

No. Estar en órbita es **caer de forma continua** alrededor de la Tierra sin
chocar, porque se avanza lo bastante rápido de lado: la nave cae, pero la
superficie se curva a la misma tasa y nunca llega al suelo. Lo que se llama
**microgravedad** es ese estado de caída libre en el que todo "flota"; no es
ausencia de gravedad. Creer lo contrario es uno de los errores comunes que el
curso señala.

Módulo 6: [🧪 Principios y operación](../operacion/principios-nave-espacial.md).

</details>

**1.3.** ¿Qué es el delta-v y por qué condiciona toda la misión?

<details>
<summary>Ver respuesta</summary>

Es el cambio total de velocidad que la nave puede lograr, y mide su capacidad de
maniobra. Es un **presupuesto limitado**: cada maniobra lo gasta y depende del
propelente disponible. Sin propelente no hay maniobra, así que el presupuesto se
planifica de antemano y se guarda reserva para volver. Gastarlo todo sin reserva
es un error típico.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md)
y [🧪 Principios](../operacion/principios-nave-espacial.md).

</details>

**1.4.** Si en el espacio no hay aire, ¿cómo se orienta la nave?

<details>
<summary>Ver respuesta</summary>

Con el **control de actitud**, no con timones ni superficies aerodinámicas. Los
**propulsores RCS** son chorros pequeños que giran o trasladan la nave, y las
**ruedas de reacción** giran masas internas para orientar sin gastar propelente.
Los sensores de actitud (estrellas, Sol y giróscopos) indican la orientación.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md)
y Módulo 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-nave-espacial.md).

</details>

**1.5.** Ordena las fases de una misión, desde la plataforma hasta el suelo.

<details>
<summary>Ver respuesta</summary>

1. **Prelanzamiento**: checklist, propelente y sistemas vitales.
2. **Lanzamiento**: despegue con gran empuje para vencer gravedad y atmósfera.
3. **Ascenso y etapas**: ganar velocidad orbital y separar etapas al agotarse.
4. **Inserción orbital**: alcanzar velocidad de lado suficiente para la órbita.
5. **Operación en órbita**: maniobras, acoplamiento, ciencia.
6. **Desorbitación**: frenar con el motor en el momento justo.
7. **Reentrada**: orientar el escudo y soportar el calor.
8. **Aterrizaje o amerizaje**: paracaídas o descenso propulsado.

Módulo 6: [🧪 Principios y operación](../operacion/principios-nave-espacial.md).

</details>

**1.6.** ¿Qué marco legal regula la actividad espacial y cuál es la situación de
Chile?

<details>
<summary>Ver respuesta</summary>

El marco son los **tratados internacionales** del ámbito de UNOOSA: el Tratado
del Espacio Ultraterrestre (1967), el Acuerdo de Salvamento (1968), el Convenio
de Responsabilidad (1972) y el Convenio de Registro (1975). Chile **no cuenta a
la fecha con una ley espacial nacional integral**: su marco interno es de
política pública (Política Nacional Espacial, Decreto 30 del Ministerio de
Ciencia, Tecnología, Conocimiento e Innovación) más el Sistema Nacional
Satelital (SNSat), liderado por la FACH.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-nave-espacial.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Una misión llega a órbita y le quedan 2000 m/s de delta-v. La
tripulación quiere gastarlos en subir la órbita para mejorar la observación.
¿Qué falta en ese razonamiento?

<details>
<summary>Ver respuesta</summary>

Falta la **reserva para volver**. La desorbitación también es una maniobra: hay
que encender el motor en contra del movimiento para bajar la órbita y reentrar,
y eso cuesta delta-v. Gastar todo el presupuesto en subir deja a la nave sin
capacidad de frenar para regresar, que es justamente uno de los errores comunes
que el curso quiere enseñar a evitar.

Además, el momento importa tanto como la cantidad: dónde en la órbita se enciende
el motor decide qué parte de la órbita cambia.

Módulo 6: [🧪 Principios y operación](../operacion/principios-nave-espacial.md).

</details>

**2.2.** Durante la reentrada, la nave no logra mantener el escudo térmico al
frente. ¿Qué está en juego y qué sistemas intervienen?

<details>
<summary>Ver respuesta</summary>

En la reentrada la fricción con el aire genera calor y el **escudo térmico** es
lo que protege a la nave. Si la orientación es mala, el calor incide donde no hay
protección: el curso lista "reentrar con mala orientación del escudo" y
"sobrecalentamiento, mala orientación" como riesgos propios de este entorno.

Quien resuelve es el **control de actitud** (propulsores RCS y ruedas de
reacción), y el instrumento a vigilar es la **temperatura del escudo**, crítica
al reingresar. El ajuste de operación es escudo al frente y ángulo correcto.

Módulos 3 y 6: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md)
y [🌍 Entornos de trabajo](../operacion/entornos-nave-espacial.md).

</details>

**2.3.** Una misión a espacio profundo y una estancia en órbita baja parecen
"lo mismo" para el diseño. ¿En qué se diferencian de verdad?

<details>
<summary>Ver respuesta</summary>

En órbita baja hay microgravedad y vueltas rápidas; los riesgos son la basura
orbital y la radiación parcial, y la operación se centra en el control de actitud
y la gestión de recursos.

En espacio profundo cambian las distancias y la luz: hay **retardo de
comunicación** y más radiación, así que la nave necesita **autonomía** y
planificación de energía. Ahí el Sol es más débil, por lo que la energía puede
depender de generadores nucleares en vez de paneles solares, y reciclar aire y
agua deja de ser opcional porque no hay cómo reabastecerse.

Módulos 3 y 6: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-nave-espacial.md)
y [🌍 Entornos de trabajo](../operacion/entornos-nave-espacial.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que la órbita es caída libre y no
"ausencia de gravedad", sin explicarlo con texto. ¿Qué variables expondrías y
cómo?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar el **indicador de órbita** con apogeo y perigeo junto
a la **velocidad orbital**, y dejar que el usuario vea que al reducir la
velocidad de lado el perigeo baja y la trayectoria termina cortando la
atmósfera. La gravedad nunca se apaga en el modelo: el ciclo básico calcula la
física orbital con la gravedad siempre presente, y lo que cambia es la velocidad.

Así el usuario **ve** que flotar y caer son lo mismo, y entiende solo por qué
frenar equivale a reentrar.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-nave-espacial.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
planificación de maniobras y el acoplamiento, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es lanzar, llegar a órbita y
reentrar de forma guiada; añadir ahí un editor de nodos de maniobra tapa lo que
se quiere enseñar. El nivel 2 introduce delta-v, órbitas y microgravedad, que son
los conceptos físicos centrales. La planificación de maniobras, el acoplamiento y
la gestión de recursos son el detalle operativo y llegan al final.

El acoplamiento, además, exige controles finos y una vista clara del objetivo:
carga de manejo que solo tiene sentido cuando la mecánica orbital ya se entiende.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-nave-espacial.md)
y [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué un cohete no necesita aire para empujar.
- [ ] Puedo explicar la órbita como caída libre, sin decir "no hay gravedad".
- [ ] Entiendo el delta-v como un presupuesto que se planifica y se reserva.
- [ ] Sé cómo se orienta una nave sin superficies aerodinámicas.
- [ ] Sé ordenar las fases de la misión y decir qué ocurre en cada una.
- [ ] Conozco los cuatro tratados espaciales y la situación de Chile.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.
- [ ] Distingo la ciencia real de la ficción en cada módulo del curso.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-nave-espacial.md)
