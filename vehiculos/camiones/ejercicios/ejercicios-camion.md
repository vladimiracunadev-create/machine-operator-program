# 🎯 Ejercicios y autoevaluación del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> profesional certificada ni el manual del fabricante. Sirve para comprobar si el
> curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué el camión monta un motor diesel y no uno de gasolina?

<details>
<summary>Ver respuesta</summary>

Por su **alto par a bajas vueltas** y su eficiencia de consumo, ambos clave para
arrastrar gran masa. El diesel además no usa bujía: comprime el aire hasta que se
calienta e inyecta el combustible, que se enciende por la alta temperatura
(encendido por compresión).

Módulo 3: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md).

</details>

**1.2.** En una bajada larga, ¿por qué no basta con el freno de servicio y para
qué están el freno de motor y el retarder?

<details>
<summary>Ver respuesta</summary>

Porque usar solo el freno de servicio recalienta las zapatas y puede provocar
**fading**, es decir, pérdida de frenado por calor. El freno de motor (retención
por la compresión del diesel) y el retarder (auxiliar hidráulico o
electromagnético) frenan **sin fricción**: mantienen la velocidad controlada sin
desgastar ni recalentar el freno de servicio, que queda disponible para una
emergencia.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md)
y [🧪 Principios y operación](../operacion/principios-camion.md).

</details>

**1.3.** Define tara, carga útil y peso bruto vehicular (PBV). ¿Por qué no basta
con respetar el PBV total?

<details>
<summary>Ver respuesta</summary>

La **tara** es el peso del camión vacío; la **carga útil** es el peso de la
mercancía; el **PBV** es la suma de ambos y marca el límite legal y de diseño del
vehículo.

No basta con el total porque cada eje tiene su propio máximo permitido: la carga
debe repartirse para no exceder ningún eje, **aunque el total esté dentro del
límite**. Un mal reparto además reduce el agarre delantero y alarga el frenado.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md)
y [🧪 Principios y operación](../operacion/principios-camion.md).

</details>

**1.4.** ¿Qué pasa si la presión de aire cae bajo el mínimo?

<details>
<summary>Ver respuesta</summary>

Suena la alarma y no se debe circular. Si la presión cae de verdad, el **freno de
muelle** (spring brake) se aplica solo y detiene el camión: es un diseño a prueba
de fallos. Por eso el frenado se divide en **circuitos separados**, para que una
fuga no deje el camión sin frenos, y el manómetro de aire debe verse siempre.

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-camion.md).

</details>

**1.5.** Ordena los cinco puntos de la idea general de pendientes.

<details>
<summary>Ver respuesta</summary>

1. Elegir la marcha **antes** de la bajada, no durante.
2. Usar freno de motor y retarder para mantener la velocidad.
3. Reservar el freno de servicio para ajustes puntuales, no continuos.
4. En subida, no dejar caer el régimen: reducir a tiempo para no perder impulso.
5. Vigilar la temperatura del motor y de los frenos.

El orden importa: cambiar de marcha ya dentro de la bajada es tarde, y confiar el
descenso al freno de servicio es lo que lleva al fading.

Módulo 5: [🧪 Principios y operación](../operacion/principios-camion.md).

</details>

**1.6.** ¿Qué licencia exige Chile para un camión simple y cuál para uno
articulado?

<details>
<summary>Ver respuesta</summary>

Clase **A-4** (profesional) para vehículos simples de carga con peso bruto
vehicular superior a 3.500 kg, y clase **A-5** (profesional) para todo vehículo de
carga, simple o articulado, que además incluye la A-4. El tractocamion con
semirremolque requiere **A-5**. Ambas según la Ley 18.290, Art. 12. La edad mínima
es 18 años (Art. 13).

Módulo 7: [⚖️ Reglamentos](../reglamentos/reglamentos-camion.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Llevas una cisterna de combustible y te acercas a una curva cerrada a la
misma velocidad a la que la tomarías con el camión vacío. ¿Qué riesgo asumes?

<details>
<summary>Ver respuesta</summary>

El de **vuelco**. Una cisterna tiene el centro de gravedad alto y una carga
líquida que se mueve, y un centro de gravedad alto aumenta el riesgo de vuelco en
curva. El curso lo señala como error común: entrar a una curva con carga alta a
demasiada velocidad.

La velocidad de paso debe reducirse **antes** de la curva, no dentro. La carga no
solo pesa: su altura y el hecho de ser líquida o suelta cambian la dinámica del
vehículo.

Módulos 2, 5 y 6:
[📋 Características](../operacion/caracteristicas-camion.md),
[🧪 Principios](../operacion/principios-camion.md) y
[🌍 Entornos de trabajo](../operacion/entornos-camion.md).

</details>

**2.2.** Un conductor gira en una calle estrecha de reparto mirando solo el
espejo de la cabina y roza un poste con el semirremolque. ¿Qué ignoró?

<details>
<summary>Ver respuesta</summary>

El **barrido trasero**. En un articulado el semirremolque pivota sobre el perno
maestro, y su parte trasera describe un arco menor que el tracto: recorta la
curva. Girar demasiado cerca de un obstáculo ignorando el barrido trasero es uno
de los errores comunes que la simulación puede enseñar a evitar.

En ciudad se suma que la cabina alta amplía la visión lejana pero crea puntos
ciegos cercanos y laterales. El ajuste es baja velocidad y maniobras lentas.

Módulos 3, 4 y 6:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-camion.md),
[🎛️ Mandos](../mandos/manual-mandos-camion.md) y
[🌍 Entornos de trabajo](../operacion/entornos-camion.md).

</details>

**2.3.** Arrancas la jornada, enciendes el motor y quieres salir de inmediato con
el camión cargado. ¿Qué te saltas y por qué importa?

<details>
<summary>Ver respuesta</summary>

Dos fases previas. La **inspección previa**: neumáticos, luces, presión de aire y
amarre de carga. Y la **carga de aire**: hay que subir la presión del sistema y
esperar el rango normal antes de mover, porque circular con presión de aire
insuficiente es un error común y el reglamento exige verificar la presión antes
de mover el camión.

Recién entonces viene el arranque: soltar el estacionamiento, marcha corta y
soltar el embrague suave.

Módulos 5 y 7: [🧪 Principios y operación](../operacion/principios-camion.md) y
[⚖️ Reglamentos](../reglamentos/reglamentos-camion.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que la masa cambia el frenado, sin
explicarlo con texto. ¿Qué variables expondrías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer la **carga** (0-100% del PBV) y dejar que el usuario
la varíe entre intentos del mismo escenario de frenada. La carga define la
distancia de frenado, así que el usuario **ve** que el mismo pedal, en el mismo
punto, ya no detiene el camión a tiempo. Subestimar la distancia de frenado con el
camión cargado es un error común del curso.

Complementa con el **reparto por eje** y la **adherencia**, que también afectan al
freno. En niveles de realismo, la inercia por masa y la distancia de frenado
entran en el nivel 2.

Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-camion.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
presión de aire y la articulación del semirremolque, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es acelerar, frenar, girar y
respetar señales con carga; añadir la carga de aire y el ángulo de articulación
ahí tapa lo que se quiere enseñar. El nivel 2 introduce inercia por masa,
distancia de frenado y distribución básica de la carga, que es el núcleo educativo
del camión. La caja multimarcha, el freno de motor y el retarder, la presión de
aire, el reparto por eje y la articulación llegan al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md) y el
Módulo 8: [🎮 Diseño de simulación](../simulacion/diseno-simulador-camion.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué el camión usa motor diesel y no gasolina.
- [ ] Entiendo qué es el fading y cómo lo evitan el freno de motor y el retarder.
- [ ] Distingo tara, carga útil y PBV, y sé por qué el reparto por eje importa.
- [ ] Sé qué ocurre si la presión de aire cae bajo el mínimo.
- [ ] Puedo ordenar la idea general de pendientes y decir por qué ese orden.
- [ ] Conozco la diferencia entre licencia A-4 y A-5 en Chile.
- [ ] Puedo nombrar tres variables que un simulador de camión debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-camion.md)
