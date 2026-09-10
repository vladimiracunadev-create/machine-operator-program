<!-- clase-meta
tipo_documento: clase
clase: 11
codigo: GRUATORRE-11
curso: grua-torre
titulo: "Ejercicios y autoevaluación de la grúa torre"
modalidad: "evaluación auténtica"
duracion_minutos: 90
nivel: introductorio
prerrequisito: GRUATORRE-10
competencia: "integracion_de_competencias"
resultados_aprendizaje:
  - "Explicar comprensión, aplicación y transferencia a la simulación con vocabulario propio de Grúa torre."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa torre."
evidencia: "Respuestas justificadas y escenario final resuelto."
criterio_aprobacion: "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🎯 Ejercicios y autoevaluación de la grúa torre

[🏠 Inicio](../../../README.md) · [🗼 Curso: Grúa torre](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada del operador ni el manual del fabricante. Sirve para comprobar si
> el curso se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué al alejar el carro hacia la punta de la pluma baja la carga
admisible?

<details>
<summary>Ver respuesta</summary>

Porque el momento de la carga es **peso por radio**, y la grúa tiene un momento
máximo de diseño que no puede superar. Si el radio aumenta, el peso debe bajar en
proporción inversa: con un momento máximo de 100 t·m, a radio 10 m se pueden izar
10 t, pero a radio 40 m solo 2.5 t. La tabla de carga indica cuánto se admite en
cada radio.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md).

</details>

**1.2.** ¿Qué equilibra el momento de la carga y sobre qué punto se mide la
estabilidad?

<details>
<summary>Ver respuesta</summary>

El **contrapeso** alojado en la contrapluma: su masa por su brazo genera el
momento resistente que equilibra el lado de la pluma sobre el eje de la torre.
Gracias a él la grúa no necesita una base enorme. La base o zapata es el punto de
vuelco de referencia: toda la estabilidad se mide respecto a ella, y por eso debe
estar nivelada.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md)
y [🧪 Principios](../operacion/principios-grua-torre.md).

</details>

**1.3.** Fuera de servicio, ¿por qué se libera el freno de giro en vez de fijar
la pluma?

<details>
<summary>Ver respuesta</summary>

Para dejar la pluma en **veleta** (weathervane): al girar libre se orienta sola
con el viento y reduce el empuje lateral sobre la estructura. Dejar la grúa fuera
de servicio con el giro frenado es uno de los errores comunes que el curso
señala.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md)
y [🧪 Principios](../operacion/principios-grua-torre.md).

</details>

**1.4.** ¿Cuál es la diferencia entre el limitador de carga y el limitador de
momento?

<details>
<summary>Ver respuesta</summary>

El **limitador de carga** impide izar más peso del admisible por el sistema de
cable. El **limitador de momento** impide superar el momento máximo, es decir la
combinación de peso **por** radio: un peso perfectamente izable cerca del eje
puede ser inadmisible con el carro en la punta. A ellos se suman los **finales de
carrera**, que detienen el carro y el gancho en sus posiciones límite.

Módulos 3 y 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md)
y [🎛️ Mandos e instrumentos](../mandos/manual-mandos-grua-torre.md).

</details>

**1.5.** Ordena las fases de operación, desde la inspección previa hasta el
cierre.

<details>
<summary>Ver respuesta</summary>

1. **Inspección previa**: base, cables, limitadores, anemómetro, área libre.
2. **Puesta en servicio**: nivel correcto, freno de giro, viento bajo el límite.
3. **Enganche**: eslingas correctas, señalero listo, radio segura.
4. **Izaje**: izaje lento, vigilar el limitador y el radio.
5. **Traslado y giro**: giro suave, controlar el péndulo, área despejada.
6. **Descenso**: bajada lenta, guiar con el señalero.
7. **Cierre**: gancho arriba, freno de giro liberado, veleta.

Clase 6: [🧪 Principios y operación](../operacion/principios-grua-torre.md).

</details>

**1.6.** ¿Qué licencia exige Chile para operar una grúa torre?

<details>
<summary>Ver respuesta</summary>

Ninguna licencia de conducir: la grúa torre es maquinaria de izaje **fija**, no
circula por vía pública y su marco no es la Ley de Tránsito sino la seguridad
laboral (Ley 16.744 y D.S. 594 del MINSAL). La opera personal
**certificado/competente**, con un plan de izaje y las tablas de carga del
fabricante, y con un señalero (rigger) coordinando desde tierra. Los detalles de
certificación del operador están por confirmar.

Clase 8: [⚖️ Reglamentos](../reglamentos/reglamentos-grua-torre.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** La carga está enganchada y el limitador marca un porcentaje cómodo, pero
el punto de descarga queda más lejos del eje. El impulso es trasladar el carro
hacia afuera sin más. ¿Qué falta comprobar?

<details>
<summary>Ver respuesta</summary>

Que el peso siga siendo admisible **en ese radio nuevo**. El porcentaje de
capacidad es momento actual sobre momento máximo, y el momento crece al alejar el
carro aunque la carga sea la misma: el limitador subirá y puede llegar a cortar.
La comprobación se hace antes, contrastando peso y radio contra la tabla de carga
al planificar el izaje, no descubriéndolo con la carga colgando.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-grua-torre.md)
y [🧪 Principios](../operacion/principios-grua-torre.md).

</details>

**2.2.** Durante el traslado el operador gira de golpe para ganar tiempo. ¿Qué
consecuencia tiene y qué se hace en su lugar?

<details>
<summary>Ver respuesta</summary>

La carga colgada oscila: un giro brusco provoca un **péndulo** peligroso, que
además desplaza la carga fuera de la vertical prevista y complica depositarla. Por
eso las palancas son proporcionales y el motor de giro rota despacio.

Lo correcto es el movimiento suave, con izaje y giro lentos, el área despejada
debajo y el señalero coordinando. En la grúa torre la prioridad no es la velocidad
sino la precisión y el control del momento de carga.

Módulos 4 y 5: [🎛️ Mandos](../mandos/manual-mandos-grua-torre.md) y
[🧪 Principios](../operacion/principios-grua-torre.md).

</details>

**2.3.** Obra en ciudad densa y el anemómetro empieza a subir con la carga en el
aire. ¿Qué cambia respecto de un día tranquilo?

<details>
<summary>Ver respuesta</summary>

El viento es el límite operacional principal: empuja la carga y la estructura, y
por encima de un umbral la grúa no puede operar. En ciudad densa el problema se
agrava porque la pluma gira sobre la vía pública y sobre vecinos, y una carga
balanceada por rachas puede invadir predios o quedar sobre personas.

La secuencia razonable es bajar la carga y pasar a veleta, que es el estado de
"viento alto" previsto: alarma del anemómetro, depositar y dejar girar libre. En
esos entornos la pluma abatible reduce la invasión del espacio vecino.

Clase 7: [🌍 Entornos de trabajo](../operacion/entornos-grua-torre.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la relación entre radio y capacidad sin
explicarla con texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar de forma **continua** el radio del carro y el
porcentaje de capacidad del limitador, uno junto al otro. Así, al trasladar el
carro con la misma carga colgando, el usuario **ve** que el porcentaje sube solo
por alejarse del eje y deduce que el límite es peso por radio, no peso a secas.
El curso pide exactamente eso: radio y porcentaje siempre visibles para que cada
movimiento se relacione con la estabilidad.

Módulos 4 y 8: [🎛️ Mandos](../mandos/manual-mandos-grua-torre.md) y
[🎮 Diseño de simulación](../simulacion/diseno-simulador-grua-torre.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
péndulo de la carga, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**, junto con el trepado y el arriostramiento. En el
nivel 1 la meta es izar, girar, trasladar el carro y respetar el limitador. El
nivel 2 agrega el momento de carga, el radio y el límite de viento, que son el
núcleo educativo de la grúa torre. El péndulo es un refinamiento del control:
llega cuando el usuario ya entiende por qué el radio manda.

Clase 6: [🧪 Principios](../operacion/principios-grua-torre.md) y los
[🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué al alejar el carro baja la capacidad.
- [ ] Entiendo el momento de carga como peso por radio respecto al eje.
- [ ] Sé qué hace el contrapeso y por qué la base debe estar nivelada.
- [ ] Distingo el limitador de carga del limitador de momento.
- [ ] Sé ordenar las fases de operación y decir por qué ese orden.
- [ ] Puedo explicar la veleta y cuándo se pasa a ella.
- [ ] Conozco el marco chileno aplicable y por qué no exige licencia de conducir.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Comprueba lo que recuerdas, Aplica: casos de operación, Lleva a la simulación y Guía de estudio aplicada** a **defender una solución integral para traslado de una carga desde radio corto hacia el extremo de pluma**?

### Explicación razonada

La integración no consiste en repetir definiciones. Ante «traslado de una carga desde radio corto hacia el extremo de pluma» hay que reconstruir la cadena alimentación → cabrestante → carro y pluma → gancho y carga, aplicar el principio «equilibrio de momentos: el efecto de la carga crece cuando aumenta su radio», reconocer el riesgo y defender una decisión verificable: consultar tabla de carga y viento antes de autorizar cada trayectoria.

Esta clase se conecta con el resto del curso mediante **equilibrio de momentos: el efecto de la carga crece cuando aumenta su radio**. El hilo de
seguridad consiste en reconocer a tiempo **sobrepasar capacidad, inducir péndulo o trabajar sobre una zona no aislada** y poder justificar la decisión
**consultar tabla de carga y viento antes de autorizar cada trayectoria**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **alimentación → cabrestante → carro y pluma → gancho y carga**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Crane, Derrick and Hoist Safety](https://www.osha.gov/cranes-derricks) aporta izaje, riesgos y controles;
[1926.1435 Tower Cranes](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1435) se usa para requisitos específicos de grúas torre. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Diagnosticar:** reconstruye **alimentación → cabrestante → carro y pluma → gancho y carga** ante **traslado de una carga desde radio corto hacia el extremo de pluma**.
2. **Explicar:** aplica **equilibrio de momentos: el efecto de la carga crece cuando aumenta su radio** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **consultar tabla de carga y viento antes de autorizar cada trayectoria** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **grúa de pluma horizontal frente a pluma abatible**.

### Comprueba tu comprensión

1. ¿Cuál es tu diagnóstico causal de «traslado de una carga desde radio corto hacia el extremo de pluma»?
2. ¿Qué alternativa a **consultar tabla de carga y viento antes de autorizar cada trayectoria** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve la autoevaluación de Grúa torre y defiende una decisión en un escenario integrador sin consultar las respuestas.
- **Evidencia:** Respuestas justificadas y escenario final resuelto.
- **Criterio de aprobación:** Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [OSHA-TOWER](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1435): 1926.1435 Tower Cranes, OSHA. Uso: requisitos específicos de grúas torre.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-grua-torre.md)
