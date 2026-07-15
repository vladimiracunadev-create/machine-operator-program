# 🎯 Ejercicios y autoevaluación del Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación de un
> piloto de competición ni la ingeniería de un equipo real. Sirve para comprobar
> si el curso se entendió y para detectar que módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué un monoplaza puede tomar una curva más rápido cuanto más
rápido va?

<details>
<summary>Ver respuesta</summary>

Por la **carga aerodinámica**. Los alerones y el fondo generan una fuerza
vertical hacia el suelo que crece con la velocidad y pega los neumáticos al
asfalto, aumentando el agarre sin sumar peso. El **efecto suelo** aporta gran
parte de esa carga: el fondo forma un canal que acelera el aire por debajo, baja
la presión y genera una succión muy eficiente, porque cuesta poca resistencia.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md) y
[🧪 Principios y operación](../operacion/principios-formula-1.md).

</details>

**1.2.** ¿Qué componentes forman el ERS y de dónde saca la energía cada máquina
eléctrica?

<details>
<summary>Ver respuesta</summary>

El ERS (sistema de recuperación de energía) lo forman el **MGU-K**, el
**MGU-H**, la **batería** y su electrónica de control. El MGU-K recupera energía
de la **frenada** y la devuelve como empuje; el MGU-H recupera **calor de los
gases de escape** en el turbocompresor y además reduce el retardo del turbo. La
batería guarda lo recuperado y entrega un impulso eléctrico extra por vuelta.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md).

</details>

**1.3.** ¿Por qué la ventana de temperatura del neumático es tan importante?

<details>
<summary>Ver respuesta</summary>

Porque el neumático rinde solo dentro de un rango: **fríos o sobrecalentados
pierden agarre**. Y el neumático es el único contacto con el asfalto, así que
todo (acelerar, frenar y girar) pasa por él. Fuera de la ventana baja la
adherencia disponible y aparecen bloqueos y pérdidas de eje trasero. Lo mismo
ocurre con los frenos de carbono, que también necesitan calor para frenar bien.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md).

</details>

**1.4.** Ordena las fases de una curva rápida.

<details>
<summary>Ver respuesta</summary>

1. Frenar fuerte y **en línea recta** antes de la curva.
2. Bajar las marchas necesarias mientras se frena.
3. Soltar el freno de forma progresiva al girar hacia el vértice.
4. Pasar por el vértice a la velocidad mínima justa.
5. Acelerar de forma progresiva a la salida cuidando el agarre trasero.

El orden importa: frenar recto y soltar el freno de forma progresiva libera el
agarre que hace falta para girar.

Módulo 6: [🧪 Principios y operación](../operacion/principios-formula-1.md).

</details>

**1.5.** ¿Qué es el DRS y cuándo puede usarse?

<details>
<summary>Ver respuesta</summary>

El DRS (sistema de reducción de resistencia) abre una aleta del aleron trasero
para reducir la resistencia al avance y facilitar el adelantamiento. Solo se
puede usar en las **zonas permitidas**; al cerrarse, el coche recupera la carga
aerodinámica habitual. En simulación, el botón solo debe habilitarse cuando el
escenario permite la zona.

Módulos 3 y 4:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-formula-1.md) y
[🎛️ Mandos e instrumentos](../mandos/manual-mandos-formula-1.md).

</details>

**1.6.** ¿Qué autoridad rige la Fórmula 1 y qué habilitación exige para pilotar
en el campeonato?

<details>
<summary>Ver respuesta</summary>

La **FIA** (Federación Internacional del Automóvil). No se rige por la ley de
tránsito, porque el monoplaza no circula por vía pública: es una competición con
un reglamento **deportivo** (cómo se compite) y uno **técnico** (cómo es el
coche). No requiere licencia de conducir común, sino una **superlicencia
deportiva** de la FIA.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-formula-1.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md), sección 1.9.

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Un piloto gasta todo el impulso ERS en la primera mitad de la vuelta.
¿Qué consecuencia tiene y qué conviene hacer?

<details>
<summary>Ver respuesta</summary>

Se queda **sin impulso en la recta**, que es justo donde la energía eléctrica
más rinde: allí se despliega la energía y, si está habilitado, se abre el DRS.
La batería se carga y descarga por vuelta, así que el problema no es gastar,
sino gastar fuera de sitio.

Lo razonable es repartir el despliegue según el trazado, apoyándose en el estado
de energía que muestra la pantalla del volante, y recuperar en las frenadas con
el MGU-K.

Módulos 4 y 5:
[🎛️ Mandos e instrumentos](../mandos/manual-mandos-formula-1.md) y
[🧪 Principios y operación](../operacion/principios-formula-1.md).

</details>

**2.2.** Circuito urbano con muros cercanos y curvas lentas. ¿Qué cambia
respecto de un circuito permanente?

<details>
<summary>Ver respuesta</summary>

La tolerancia al error: sin escapatorias, un error mínimo termina en el muro. El
pilotaje pide **precisión**, reglaje de **alta carga aerodinámica** para las
curvas lentas y cuidado de los frenos. En un circuito permanente, con
escapatorias y curvas rápidas, el riesgo típico es otro: sobreexigir gomas y
frenos buscando ritmo y trazada limpia.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-formula-1.md).

</details>

**2.3.** Empieza a llover en mitad de la tanda. ¿Qué cambia y qué se ajusta?

<details>
<summary>Ver respuesta</summary>

Baja la adherencia disponible y aparecen riesgos propios del piso mojado:
aquaplaning y trompos. El ajuste pasa por **neumáticos de lluvia**, suavidad en
los mandos y más distancia. Además, el reglaje de lluvia aplica menos potencia a
las ruedas, y la goma fría cuesta más de meter en su ventana de temperatura, lo
que favorece los bloqueos al frenar.

Módulos 2 y 6:
[📋 Características](../operacion/caracteristicas-formula-1.md) y
[🌍 Entornos de trabajo](../operacion/entornos-formula-1.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la gestión de energía sin explicarla
con texto. ¿Qué variable expondrías y cómo la mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer la **energía ERS** de 0 a 100% y mostrarla en la
pantalla del volante como carga y despliegue en vivo, junto al **delta** de
tiempo respecto a una vuelta de referencia. Así el usuario **ve** que la barra
se vacía al desplegar y se recupera al frenar, y relaciona por sí mismo el gasto
con el tiempo ganado o perdido.

Módulo 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-formula-1.md).

</details>

**3.2.** El curso ofrece tres niveles de realismo. ¿En cuál introducirías la
gestión de energía ERS y el reparto de frenada, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es acelerar, frenar, girar y
seguir la trazada; añadir gestión de energía ahí tapa lo que se quiere enseñar.
El nivel 2 introduce carga aerodinámica, degradación de gomas y límite de
adherencia, que son los conceptos físicos centrales. La gestión de ERS, el
reparto de frenada, las ventanas de temperatura y la estrategia de neumáticos
son la capa técnica y llegan al final.

Módulo 6: [🧪 Principios y operación](../operacion/principios-formula-1.md) y
los [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar la carga aerodinámica y el efecto suelo sin confundirlos.
- [ ] Sé qué recupera el MGU-K y qué recupera el MGU-H.
- [ ] Entiendo por qué la ventana de temperatura limita el agarre.
- [ ] Sé ordenar las fases de una curva y decir por qué ese orden.
- [ ] Conozco la autoridad que rige la categoría y sus dos reglamentos.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-formula-1.md)
