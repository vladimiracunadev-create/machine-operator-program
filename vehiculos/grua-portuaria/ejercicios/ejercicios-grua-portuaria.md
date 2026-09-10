<!-- clase-meta
tipo_documento: clase
clase: 11
codigo: GRUAPORTUARI-11
curso: grua-portuaria
titulo: "Ejercicios y autoevaluación de la grúa portuaria"
modalidad: "evaluación auténtica"
duracion_minutos: 90
nivel: introductorio
prerrequisito: GRUAPORTUARI-10
competencia: "integracion_de_competencias"
resultados_aprendizaje:
  - "Explicar comprensión, aplicación y transferencia a la simulación con vocabulario propio de Grúa portuaria."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa portuaria."
evidencia: "Respuestas justificadas y escenario final resuelto."
criterio_aprobacion: "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🎯 Ejercicios y autoevaluación de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada del operador ni el manual del fabricante. Sirve para comprobar si
> el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** La grúa tiene cuatro movimientos principales. Nómbralos y di qué mueve
cada uno.

<details>
<summary>Ver respuesta</summary>

- **Gantry**: traslada todo el pórtico sobre los rieles, a lo largo del muelle,
  para alinear la grúa con otra bahía del buque.
- **Trolley**: mueve el carro sobre la viga, perpendicular al muelle, acercando
  o alejando la carga del agua.
- **Hoist**: izaje vertical; sube y baja el spreader con la carga.
- **Boom**: abate la pluma a vertical para liberar el gabarito del buque y la
  baja a horizontal para operar.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md).

</details>

**1.2.** ¿Por qué la carga colgada se bambolea y qué la mantiene quieta?

<details>
<summary>Ver respuesta</summary>

Porque cuelga como un **péndulo**: todo arranque o frenado brusco del trolley la
hace bambolear. Lo que la mantiene quieta son los movimientos suaves del
operador y el sistema **anti-sway**, que mide o anticipa el bamboleo y corrige
el trolley y el izaje para que el contenedor llegue quieto al punto de apoyo.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md) y
[🧪 Principios y operación](../operacion/principios-grua-portuaria.md).

</details>

**1.3.** ¿Qué peso ve el indicador de carga y por qué importa la distinción?

<details>
<summary>Ver respuesta</summary>

Ve el peso del contenedor **más el peso propio del spreader**. Importa porque el
límite de carga se aplica a esa suma, no solo a la caja: superar el límite
sumando el peso del spreader es uno de los errores comunes que la simulación
debe enseñar a evitar.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md) y
[🧪 Principios y operación](../operacion/principios-grua-portuaria.md).

</details>

**1.4.** ¿Cómo agarra el spreader un contenedor y qué debe ocurrir antes de
izar?

<details>
<summary>Ver respuesta</summary>

El spreader es un marco telescópico que se ajusta a la longitud del contenedor
(20, 40 o 45 pies), baja sobre la caja guiado por sus flippers, calza los cuatro
**twist-locks** en las esquinas ISO y gira los pernos para trabar la carga.
Antes de izar deben estar los twist-locks trabados: un sensor solo habilita el
izaje con la carga trabada, y los sensores de asiento confirman apoyo en las
cuatro esquinas.

Módulos 2 y 3:
[📋 Características](../operacion/caracteristicas-grua-portuaria.md) y
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md).

</details>

**1.5.** Ordena las fases de un ciclo de descarga de buque a muelle.

<details>
<summary>Ver respuesta</summary>

1. El **gantry** posiciona la grúa frente a la bahía del buque a descargar.
2. El **trolley** lleva el spreader sobre la celda del contenedor objetivo.
3. El **hoist** baja el spreader y los **twist-locks** traban el contenedor.
4. El hoist iza el contenedor fuera de la celda, con **anti-sway** activo.
5. El trolley traslada la carga desde el buque hacia el muelle.
6. El hoist baja el contenedor sobre el camión o la zona de acopio.
7. Los twist-locks liberan la caja y el spreader sube vacío.
8. La grúa repite el ciclo con el siguiente contenedor.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-portuaria.md).

</details>

**1.6.** ¿Necesita licencia de conducir el operador de una grúa portuaria en
Chile? ¿Qué marco legal se le aplica?

<details>
<summary>Ver respuesta</summary>

No. Las grúas fijas no circulan por vía pública y no requieren licencia de
conducir. El marco base es la **seguridad laboral**, no la Ley de Tránsito:
Ley 16.744 (seguro social contra accidentes del trabajo) y D.S. 594 del MINSAL
(condiciones sanitarias y ambientales). La autoridad es la Dirección del Trabajo
y las mutuales, y en el recinto portuario además la Autoridad Marítima
(DIRECTEMAR) y la autoridad del puerto. La operación la realiza personal
certificado/competente, aunque el **detalle de la certificación del operador
está (por confirmar)** en el marco legal, sección 1.7: el curso no lo resuelve.

Clase 8: [⚖️ Reglamentos](../reglamentos/reglamentos-grua-portuaria.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Vas trasladando un contenedor del buque al muelle y el anemómetro sube
por encima del límite. El buque tiene turno y quedan pocas cajas. ¿Qué haces?

<details>
<summary>Ver respuesta</summary>

Se detiene la operación. El viento es el factor crítico del entorno: por encima
del límite del anemómetro la carga colgada se vuelve incontrolable, deriva y
bambolea, y puede golpear el buque o las guías. El propio sistema lo contempla
como estado de **emergencia** (sobrecarga, viento o falla), con alarma y luz
roja, y las acciones disponibles son parar, bajar la carga y asegurar.

El cierre correcto deja la grúa segura: pluma arriba, frenos de riel puestos y
grúa anclada contra el desplazamiento por viento. La productividad se logra
repitiendo un ciclo estable y seguro, no forzando el turno.

Módulos 6 y 5: [🌍 Entornos de trabajo](../operacion/entornos-grua-portuaria.md)
y [🧪 Principios y operación](../operacion/principios-grua-portuaria.md).

</details>

**2.2.** Un operador nuevo arranca y frena el trolley de golpe para ganar
segundos por ciclo. ¿Qué dos consecuencias tiene y qué le dirías?

<details>
<summary>Ver respuesta</summary>

Primera: el tirón hace bambolear la carga, que cuelga como un péndulo, así que
el contenedor llega oscilando al punto de apoyo y hay que esperar a que se
calme, perdiendo el tiempo que se creía ganar. Segunda: un contenedor que se
balancea puede golpear el buque o las guías de la celda al bajar.

Lo razonable es lo contrario: iniciar el movimiento del trolley de forma suave,
mantener el anti-sway activo durante el traslado, anticipar el frenado para que
la carga llegue quieta y bajar con velocidad reducida en el tramo final. Los
joysticks son proporcionales justamente para evitar movimientos bruscos.

Módulos 5 y 4: [🧪 Principios y operación](../operacion/principios-grua-portuaria.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-grua-portuaria.md).

</details>

**2.3.** Operación nocturna, con camiones circulando bajo la grúa para recibir
las cajas. ¿Qué cambia respecto de la operación diurna y qué protege al personal
en tierra?

<details>
<summary>Ver respuesta</summary>

De noche baja la visibilidad del punto de apoyo y la jornada continua añade
fatiga, así que aparecen errores por poca luz y cansancio. Se compensa con
iluminación, con las cámaras que apoyan el posicionamiento fino y con un ritmo
controlado, no acelerado.

Al personal en tierra lo protegen el **área de exclusión** libre de personas, la
coordinación de cada movimiento con el **señalero (rigger)** y el control del
flujo de camiones antes de depositar la caja. El riesgo típico aquí es el
atropello y el depósito sobre un camión mal ubicado.

Módulos 6 y 7: [🌍 Entornos de trabajo](../operacion/entornos-grua-portuaria.md)
y [⚖️ Reglamentos](../reglamentos/reglamentos-grua-portuaria.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe que el límite de carga incluye el
spreader, sin explicarlo con texto. ¿Qué expondrías y cómo?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer el peso de la carga como variable y mostrar en el
indicador de carga el total izado en toneladas junto al porcentaje de carga
actual frente a la máxima, que avisa y corta al acercarse al límite. Si el
indicador ya marca peso con el spreader vacío colgando, el usuario **ve** que la
grúa arrastra ese peso antes de tomar nada, y entiende solo por qué una caja que
"cabe" en el límite puede no caber.

Clase 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md) y
Clase 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-grua-portuaria.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
anti-sway y los enclavamientos, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es posicionar, izar,
trasladar y depositar un contenedor: añadir anti-sway ahí tapa el gesto básico
que se quiere enseñar. El nivel 2 introduce el balanceo de la carga, el límite
de carga y el viento, que son los conceptos físicos centrales, y conviene que el
usuario sufra el balanceo antes de darle la herramienta que lo corrige. El
anti-sway, los enclavamientos, la precisión de celda y el ciclo cronometrado
llegan al final.

Clase 6: [🧪 Principios y operación](../operacion/principios-grua-portuaria.md)
y los [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo nombrar los cuatro movimientos y decir qué mueve cada uno.
- [ ] Puedo explicar el balanceo como un péndulo y qué hace el anti-sway.
- [ ] Sé que el límite de carga incluye el peso propio del spreader.
- [ ] Puedo describir cómo el spreader traba un contenedor y qué habilita el izaje.
- [ ] Sé ordenar el ciclo de descarga de buque a muelle.
- [ ] Conozco el marco legal chileno aplicable y sé qué queda por confirmar.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Comprueba lo que recuerdas, Aplica: casos de operación, Lleva a la simulación y Guía de estudio aplicada** a **defender una solución integral para traslado de un contenedor desde buque con ráfagas laterales**?

### Explicación razonada

La integración no consiste en repetir definiciones. Ante «traslado de un contenedor desde buque con ráfagas laterales» hay que reconstruir la cadena alimentación → accionamientos → carro y cables → spreader y contenedor, aplicar el principio «control del péndulo y productividad sin superar límites estructurales ni de viento», reconocer el riesgo y defender una decisión verificable: detener o suavizar el ciclo según viento, señalización y estabilidad de la carga.

Esta clase se conecta con el resto del curso mediante **control del péndulo y productividad sin superar límites estructurales ni de viento**. El hilo de
seguridad consiste en reconocer a tiempo **oscilación, enganche incompleto o ingreso de personas al área de caída** y poder justificar la decisión
**detener o suavizar el ciclo según viento, señalización y estabilidad de la carga**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **alimentación → accionamientos → carro y cables → spreader y contenedor**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Crane, Derrick and Hoist Safety](https://www.osha.gov/cranes-derricks) aporta izaje, riesgos y controles;
[Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) se usa para navegación, SOLAS, COLREG y STCW. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Diagnosticar:** reconstruye **alimentación → accionamientos → carro y cables → spreader y contenedor** ante **traslado de un contenedor desde buque con ráfagas laterales**.
2. **Explicar:** aplica **control del péndulo y productividad sin superar límites estructurales ni de viento** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **detener o suavizar el ciclo según viento, señalización y estabilidad de la carga** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **grúa pórtico STS frente a grúa móvil portuaria**.

### Comprueba tu comprensión

1. ¿Cuál es tu diagnóstico causal de «traslado de un contenedor desde buque con ráfagas laterales»?
2. ¿Qué alternativa a **detener o suavizar el ciclo según viento, señalización y estabilidad de la carga** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve la autoevaluación de Grúa portuaria y defiende una decisión en un escenario integrador sin consultar las respuestas.
- **Evidencia:** Respuestas justificadas y escenario final resuelto.
- **Criterio de aprobación:** Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-grua-portuaria.md)
