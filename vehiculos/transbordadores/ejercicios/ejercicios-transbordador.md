# 🎯 Ejercicios y autoevaluación del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada de una agencia espacial ni ninguna habilitación de vuelo. Sirve
> para comprobar si el curso se entendió y para detectar qué módulo conviene
> releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** Un transbordador combina tres vehículos distintos en uno. ¿Cuáles son y
en qué fase actúa cada uno?

<details>
<summary>Ver respuesta</summary>

Es **cohete** en el despegue, **nave tripulada** en la órbita y **planeador** en
el regreso. Despega vertical con propulsores y tanque externo, trabaja en órbita
con su cabina y su bahía de carga, y vuelve planeando sin motor hasta una pista.

Módulo 2: [📋 Características](../operacion/caracteristicas-transbordador.md).

</details>

**1.2.** ¿Por qué se dice que la reentrada no es "caer"?

<details>
<summary>Ver respuesta</summary>

Porque la nave llega a la atmósfera muy rápido y lo que hace es **frenar contra
el aire de forma controlada**. El roce con el aire cada vez más denso genera un
calor enorme, y para sobrevivir hace falta el escudo por delante y un ángulo
correcto: ni muy plano ni muy pronunciado.

Módulo 6: [🧪 Principios y operación](../operacion/principios-transbordador.md).

</details>

**1.3.** ¿Qué pasa si el ángulo de reentrada es demasiado plano y qué pasa si es
demasiado pronunciado?

<details>
<summary>Ver respuesta</summary>

Muy plano: la nave **rebota** contra la atmósfera. Muy pronunciado: el frenado
es tan brusco que aparece **calor extremo** sobre el escudo. Por eso el ángulo
de reentrada es un instrumento de prioridad alta y una variable central del
simulador.

Módulos 5 y 8:
[🧪 Principios](../operacion/principios-transbordador.md) y
[🎮 Diseño de simulación](../simulacion/diseno-simulador-transbordador.md).

</details>

**1.4.** En el planeo final no hay empuje. ¿Cuál es entonces el "combustible" del
descenso?

<details>
<summary>Ver respuesta</summary>

La **altura y la velocidad**. Esa energía es lo único que queda para llegar a la
pista, y se administra: gastarla demasiado pronto significa quedar corto, y no
hay forma de acelerar en el descenso final. De ahí que cada aterrizaje sea un
único intento.

Módulo 6: [🧪 Principios y operación](../operacion/principios-transbordador.md).

</details>

**1.5.** Nombra las tres partes del grupo de despegue y di cuál de ellas regresa
entera.

<details>
<summary>Ver respuesta</summary>

**Propulsores laterales** (dan gran empuje los primeros minutos y luego se
separan; se recuperaban del mar), **tanque externo** (guarda el propelente de
los motores del orbitador y se desecha en el ascenso) y **motores del
orbitador**. La única parte que regresa entera es el **orbitador**.

Módulos 3 y 2:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-transbordador.md) y
[📋 Características](../operacion/caracteristicas-transbordador.md).

</details>

**1.6.** ¿Bajo qué jurisdicción opera un transbordador y qué tratado responde por
los daños que cause un objeto espacial?

<details>
<summary>Ver respuesta</summary>

Opera bajo la jurisdicción del **Estado de lanzamiento** y su agencia espacial,
dentro del marco de los tratados internacionales. El **Convenio de
Responsabilidad (1972)** cubre la responsabilidad por daños de objetos
espaciales. Chile no cuenta a la fecha con una ley espacial nacional integral: el
marco interno es de política pública más los tratados.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-transbordador.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Estás en desorbitación y la actitud de la nave no coincide con lo que
pide la fase de reentrada. ¿Por qué es lo primero que hay que corregir?

<details>
<summary>Ver respuesta</summary>

Porque la regla clave del escudo térmico es que la nave debe reingresar **con el
escudo por delante, no las alas**. Las losetas cerámicas y el borde de ataque
reforzado están donde se espera el calor; una orientación incorrecta expone
estructura que no está protegida. Por eso la orientación del escudo se modela
como una variable discreta —correcta o incorrecta— que afecta directamente a la
supervivencia, y el indicador de actitud es el que permite apuntarlo.

Módulos 3 y 4:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-transbordador.md) y
[🎛️ Mandos e instrumentos](../mandos/manual-mandos-transbordador.md).

</details>

**2.2.** Vienes en planeo y ves que vas a quedar largo de la pista. El impulso es
buscar más empuje. ¿Qué falla en ese razonamiento y cuándo se decidía realmente
el resultado?

<details>
<summary>Ver respuesta</summary>

Falla la premisa: en el descenso final **no hay motor**. No existe empuje que
corregir. Lo único disponible es la aerodinámica: palanca y timones sobre alas y
elevones para gestionar la senda de planeo, y luego tren y frenos en la pista.

El resultado se decidió antes, en cómo se administró la energía de altura y
velocidad durante todo el descenso. Es uno de los errores comunes que el curso
señala: pensar que se puede "acelerar" cuando ya no hay con qué.

Módulo 6: [🧪 Principios y operación](../operacion/principios-transbordador.md).

</details>

**2.3.** Misión completa: la nave sobrevivió a la reentrada, pasó el pico de
calor y llegó bien encarada a la pista. ¿Qué queda por hacer y qué error de la
lista del curso sigue vivo hasta el último segundo?

<details>
<summary>Ver respuesta</summary>

Queda **desplegar el tren de aterrizaje** antes del toque, usar timón y frenos
en la pista, y el paracaídas de frenado para reducir la velocidad tras tocar
tierra. El error que sigue vivo es olvidar el tren a tiempo: figura entre los
errores comunes del Módulo 6, y por eso el tren es una variable discreta del
simulador —recogido o desplegado— con su propia alarma.

Los entornos de pista añaden lo suyo: viento cruzado y longitud de pista
influyen en el aterrizaje.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-transbordador.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que el planeo se paga con energía, sin
explicarlo con texto. ¿Qué variable expondrías y cómo la mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer la **energía de planeo** (altura más velocidad) junto
a la **senda de planeo** hacia la pista, y mostrarlas como un indicador único que
se vacía a medida que se desciende, contrastado con lo que falta para llegar.
Así el usuario **ve** que cada maniobra gasta un presupuesto que no se recarga, y
entiende solo por qué quedar corto no tiene arreglo.

Módulo 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-transbordador.md).

</details>

**3.2.** El curso ofrece tres niveles de realismo. ¿En cuál introducirías las
separaciones y el aterrizaje de un solo intento, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es despegar, orbitar y
aterrizar de forma guiada; añadir ahí el momento justo de cada separación tapa
lo que se quiere enseñar. El nivel 2 introduce la órbita, el ángulo de reentrada
y el planeo, que son los conceptos físicos centrales. Las separaciones, la
gestión de energía y el aterrizaje de un solo intento llegan al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué el transbordador es cohete, nave y planeador.
- [ ] Entiendo la reentrada como un frenado controlado, no como una caída.
- [ ] Sé qué pasa con un ángulo de reentrada muy plano y con uno muy pronunciado.
- [ ] Puedo explicar la energía del planeo sin recurrir a "acelerar".
- [ ] Conozco el papel del Estado de lanzamiento y los tratados espaciales.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-transbordador.md)
