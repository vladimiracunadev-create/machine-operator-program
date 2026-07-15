# 🎯 Ejercicios y autoevaluación del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada de un maquinista ni los manuales del fabricante y del administrador
> de la infraestructura. Sirve para comprobar si el curso se entendió y para
> detectar que módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** Por encima de 250 km/h, ¿cuál es la principal fuerza que se opone al
avance del tren y por qué obliga a cuidar tanto la forma?

<details>
<summary>Ver respuesta</summary>

La **resistencia aerodinámica**. Crece con el cuadrado de la velocidad, así que a
alta velocidad domina sobre las demás fuerzas de oposición. Por eso la forma
importa tanto como la potencia: nariz larga, bajos carenados, juntas entre coches
cuidadas y hasta el propio pantógrafo se diseñan para reducirla, y además para
suavizar la onda de presión al entrar en túneles o cruzarse con otro tren.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md)
y [🧪 Principios](../operacion/principios-tren-alta-velocidad.md).

</details>

**1.2.** ¿Qué diferencia la tracción distribuida (EMU) de la concentrada, y qué
ventaja aporta repartir los motores?

<details>
<summary>Ver respuesta</summary>

En la **tracción distribuida (EMU)** los motores se reparten en varios coches; en
la **concentrada** la potencia va en una locomotora en cabeza (y a veces en cola)
que remolca coches sin motor.

Repartir los motores mejora la adherencia, porque hay más ejes motores, y reparte
el esfuerzo. Importa porque el contacto rueda-riel es acero contra acero y tiene
poca fricción: con toda la potencia en un solo punto es más fácil patinar al
acelerar. El Shinkansen es el ejemplo de distribuida y el TGV el de concentrada.

Módulos 2 y 3: [📋 Características](../operacion/caracteristicas-tren-alta-velocidad.md)
y [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md).

</details>

**1.3.** ¿Por qué a alta velocidad no se usan señales laterales y qué las
reemplaza?

<details>
<summary>Ver respuesta</summary>

Porque a esa velocidad el maquinista **no alcanza a leerlas**: pasan demasiado
rápido. Las reemplaza la **señalización en cabina ETCS/ERTMS**: las balizas de la
vía informan al equipo embarcado, que muestra la velocidad objetivo en la
pantalla **DMI** del pupitre. Además el sistema supervisa: si el tren excede el
límite, aplica el freno automáticamente.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md).

</details>

**1.4.** Nombra los cuatro tipos de freno del tren y di cuál hace el trabajo a
alta velocidad y cuál completa la detención.

<details>
<summary>Ver respuesta</summary>

- **Regenerativo**: el motor actúa como generador y devuelve energía a la línea.
- **Dinámico**: el motor genera electricidad que se disipa como calor.
- **Neumático**: aire comprimido aprieta zapatas o discos en las ruedas.
- **De Foucault (eddy)**: corrientes inducidas frenan sobre el riel sin contacto.

El **regenerativo** y el **dinámico** hacen la mayor parte del trabajo a alta
velocidad, sin desgaste; el **neumático** completa la detención final. Se combinan
porque la energía cinética es enorme y el freno de fricción solo no bastaría ni
disiparía el calor con seguridad.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-tren-alta-velocidad.md).

</details>

**1.5.** Ordena los pasos de un frenado anticipado hasta la parada en estación.

<details>
<summary>Ver respuesta</summary>

1. Conocer la **velocidad objetivo** que marca el DMI mucho antes del punto.
2. Iniciar el frenado con **kilómetros** de anticipación, no metros.
3. Usar primero el **freno regenerativo y dinámico**, que no desgastan.
4. Completar con el **freno neumático** para la detención final.
5. Detener con precisión para alinear las puertas con el andén.

El orden importa: la frenada se planifica respecto a la señal objetivo, no se
improvisa al verla. Frenar tarde es el error típico, y si se ignora el objetivo
del DMI la supervisión frena sola.

Módulo 6: [🧪 Principios y operación](../operacion/principios-tren-alta-velocidad.md).

</details>

**1.6.** ¿Qué habilitación exige Chile para conducir un tren de alta velocidad?

<details>
<summary>Ver respuesta</summary>

No hay licencia de vía pública como en los vehículos de carretera: se exige
**habilitación o certificación de maquinista**, con formación específica del
sistema. Ahora bien, el detalle está **por confirmar**, porque Chile aún no cuenta
con alta velocidad comercial. El marco de referencia es el ferroviario general
(Ley General de Ferrocarriles, con número y fecha por confirmar), el MTT como
regulador y EFE como operador estatal histórico; para la operación se usan como
referencia los estándares internacionales de alta velocidad, incluida la
señalización embarcada ETCS/ERTMS.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-tren-alta-velocidad.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md), sección 1.6.

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** El DMI baja la velocidad objetivo para un tramo que está adelante. El
impulso de quien viene de conducir un auto es esperar a ver el punto y frenar
ahí. ¿Por qué no funciona en un tren de alta velocidad?

<details>
<summary>Ver respuesta</summary>

Porque el tren no se detiene en metros: la gran masa a gran velocidad acumula
muchísima energía cinética y la distancia de frenado se mide en **kilómetros**.
Cuando el punto ya se ve, el espacio disponible se agotó hace rato.

Lo que corresponde es leer la velocidad objetivo del DMI **mucho antes** del punto
e iniciar la frenada con kilómetros de anticipación, apoyándose primero en el
freno regenerativo y dinámico. Si se llega excedido, la supervisión ETCS aplica el
freno automático: no es una ayuda, es la señal de que la planificación falló.

Módulo 6: [🧪 Principios y operación](../operacion/principios-tren-alta-velocidad.md).

</details>

**2.2.** Circulas por un viaducto con rachas de viento fuerte y más adelante hay
un túnel largo. ¿Qué cambia en cada tramo?

<details>
<summary>Ver respuesta</summary>

En el **viaducto** el riesgo es el viento lateral sobre grandes vanos elevados: el
ajuste es reducir la velocidad con viento fuerte. Es además una de las reglas de
seguridad del curso, junto con el clima adverso en general.

En el **túnel largo** el problema no es el viento sino la **onda de presión**: al
entrar se genera un golpe de presión y un estampido a la salida, y la sección del
túnel junto con la forma del tren definen el confort de oídos de los pasajeros.
Ahí lo que se ajusta es la velocidad y la ventilación.

Mismo tren, dos entornos, dos motivos distintos para moderar la marcha.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-tren-alta-velocidad.md).

</details>

**2.3.** El tren está detenido en la estación y los pasajeros esperan. ¿Por qué
no basta con parar y abrir las puertas?

<details>
<summary>Ver respuesta</summary>

Porque la parada tiene que ser **precisa**: las puertas deben quedar alineadas con
el andén. Detener veinte metros más allá no es un detalle estético, deja las
puertas fuera de sitio.

Y la apertura pasa por el **enclavamiento** con la marcha: no se abren puertas sin
él ni con el tren mal alineado, porque el riesgo son los atrapamientos. Abrir sin
enclavamiento figura entre los errores comunes que la simulación busca enseñar a
evitar. El cierre después es bajar el pantógrafo, dejar el freno aplicado y los
sistemas apagados.

Módulos 5 y 6: [🧪 Principios](../operacion/principios-tren-alta-velocidad.md) y
[🌍 Entornos de trabajo](../operacion/entornos-tren-alta-velocidad.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que la distancia de frenado se mide en
kilómetros, sin explicarlo con texto. ¿Qué variables expondrías y cómo?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar juntas la **velocidad** actual, la **velocidad
objetivo** del DMI y la **masa del tren**, y sobre la vía el punto donde el tren
quedaría detenido si se frenara ahora. Así el usuario **ve** que ese punto está
kilómetros adelante y que solo se acerca cuando baja la velocidad, mucho antes de
tener el objetivo a la vista.

El ciclo básico ya calcula tracción, resistencia aerodinámica y frenado combinado,
y supervisa la velocidad objetivo con frenado automático al excederla: la
supervisión saltando es la retroalimentación de que se frenó tarde. Conviene que
sea un aviso educativo y no un castigo frustrante.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-tren-alta-velocidad.md).

</details>

**3.2.** El curso ofrece tres niveles de realismo. ¿En cuál introducirías la
gestión de varios frenos y la tensión de línea, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es traccionar, frenar a tiempo y
respetar la señal objetivo; añadir ahí la gestión de cuatro frenos y el estado de
la catenaria tapa lo que se quiere enseñar. El nivel 2 introduce energía cinética,
resistencia aerodinámica y distancia de frenado realista, que son los conceptos
físicos centrales. Repartir el esfuerzo entre regenerativo, dinámico, neumático y
de Foucault, vigilar la tensión de línea, el vigilante y la supervisión ETCS es
detalle de operación y llega al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué la aerodinámica domina por encima de 250 km/h.
- [ ] Distingo la tracción distribuida de la concentrada y sé qué aporta cada una.
- [ ] Sé por qué la señalización va en cabina y qué hace el DMI.
- [ ] Puedo nombrar los cuatro frenos y decir cuál actúa en cada momento.
- [ ] Entiendo el frenado anticipado como planificación, no como reacción.
- [ ] Conozco la habilitación de referencia y sé qué queda por confirmar en Chile.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-tren-alta-velocidad.md)
