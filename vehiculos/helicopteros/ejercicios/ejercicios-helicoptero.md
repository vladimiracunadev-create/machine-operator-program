<!-- clase-meta
tipo_documento: clase
clase: 11
codigo: HELICOPTEROS-11
curso: helicopteros
titulo: "Ejercicios y autoevaluación del helicóptero"
modalidad: "evaluación auténtica"
duracion_minutos: 90
nivel: introductorio
prerrequisito: HELICOPTEROS-10
competencia: "integracion_de_competencias"
resultados_aprendizaje:
  - "Explicar comprensión, aplicación y transferencia a la simulación con vocabulario propio de Helicópteros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Helicópteros."
evidencia: "Respuestas justificadas y escenario final resuelto."
criterio_aprobacion: "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🎯 Ejercicios y autoevaluación del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la instrucción de
> vuelo certificada ni el manual del fabricante. Sirve para comprobar si el curso
> se entendió y para detectar qué módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué un helicóptero necesita rotor de cola y qué pasa si falla?

<details>
<summary>Ver respuesta</summary>

Porque al hacer girar el rotor principal el motor aplica un **par** sobre el
fuselaje, que por acción y reacción tiende a girar en sentido contrario. El rotor
de cola genera un empuje lateral que compensa ese par y además controla la
guiñada. Si falla, el helicóptero pierde el control de guiñada; por eso su
transmisión y su estado son críticos.

Los **rotores en tándem** resuelven lo mismo de otra forma: sus dos rotores giran
en sentidos opuestos y los pares se cancelan, así que no llevan rotor de cola.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md).

</details>

**1.2.** ¿Cuál es la diferencia entre el paso colectivo y el paso cíclico?

<details>
<summary>Ver respuesta</summary>

El **paso colectivo** cambia el ángulo de todas las palas **por igual**: sube o
baja la sustentación total, es decir, hace subir o bajar el helicóptero. El
**paso cíclico** cambia el paso de cada pala **según su posición en el giro**, lo
que inclina el disco rotor y traslada el helicóptero hacia donde se inclina.

Los dos llegan a las palas a través del **plato cíclico**: el colectivo lo sube o
baja en bloque, y el cíclico lo inclina.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md).

</details>

**1.3.** ¿Qué es la disimetría de sustentación y cuándo aparece?

<details>
<summary>Ver respuesta</summary>

Aparece en **vuelo hacia adelante**: la pala que avanza recibe más aire que la que
retrocede, así que no generarían la misma sustentación. La articulación de las
palas equilibra ese desnivel para que el vuelo sea estable.

En vuelo estacionario no se da, porque todas las palas ven el mismo aire.

Clase 6: [🧪 Principios y operación](../operacion/principios-helicoptero.md).

</details>

**1.4.** Si el motor falla en vuelo, ¿por qué el helicóptero no cae como una
piedra?

<details>
<summary>Ver respuesta</summary>

Por la **autorrotación**. Al descender, el flujo de aire que sube a través del
rotor lo mantiene girando, lo que permite un descenso controlado y un aterrizaje
seguro sin potencia. La **rueda libre** desconecta el motor detenido para que el
rotor pueda girar libre.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-helicoptero.md) y
[🧪 Principios](../operacion/principios-helicoptero.md).

</details>

**1.5.** Enumera los cuatro pasos de la técnica del vuelo estacionario y di por
qué hay que corregir de forma continua.

<details>
<summary>Ver respuesta</summary>

1. Ajustar el **colectivo** para que la sustentación iguale el peso.
2. Usar el **cíclico** con pequeños movimientos para no derivar sobre el punto.
3. Compensar el **par** con los **pedales** para mantener la nariz fija.
4. Vigilar el **rotor RPM** y el **variómetro** cerca de cero.

Se corrige de forma continua porque los tres mandos **se influyen entre sí**: al
subir colectivo aumenta el par, y ese par hay que compensarlo con pedal.

Clase 6: [🧪 Principios y operación](../operacion/principios-helicoptero.md).

</details>

**1.6.** ¿Qué licencia y qué documento personal exige Chile para pilotar un
helicóptero, y qué autoridad los otorga?

<details>
<summary>Ver respuesta</summary>

La licencia de piloto de helicóptero y sus habilitaciones están reguladas por la
**DAN 61** (edición vigente por confirmar), y se requiere además **certificado
médico aeronáutico**. Ambos los otorga la **Dirección General de Aeronáutica
Civil (DGAC)**, bajo el marco de la Ley 18.916 (Código Aeronáutico).

Clase 8: [⚖️ Reglamentos](../reglamentos/reglamentos-helicoptero.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Subes el colectivo para despegar y la nariz empieza a girar sola.
¿Qué está pasando y qué haces?

<details>
<summary>Ver respuesta</summary>

Al subir colectivo aumenta el paso de todas las palas, el motor entrega más
potencia y con ella crece el **par** sobre el fuselaje, que tiende a girar en
sentido contrario al rotor. La nariz gira porque el anti-par no se ajustó.

La corrección es **acompañar el colectivo con pedal**: los pedales cambian el paso
del rotor de cola y compensan el par. No es un fallo, es el comportamiento normal
del vehículo. De hecho, subir colectivo sin compensar con pedal es uno de los
errores comunes que la simulación debería enseñar a evitar.

Módulos 4 y 5:
[🎛️ Mandos](../mandos/manual-mandos-helicoptero.md) y
[🧪 Principios](../operacion/principios-helicoptero.md).

</details>

**2.2.** Un rescate en montaña, en un día caluroso. El helicóptero mantuvo el
estacionario sin problema a nivel del mar. ¿Qué cambia arriba y por qué?

<details>
<summary>Ver respuesta</summary>

La **densidad del aire** baja con la altura y con el calor, y con ella baja la
sustentación disponible: hace falta **más potencia** para sostener el mismo peso.
Se suma la turbulencia y el espacio reducido de la montaña, que complican el
estacionario y la aproximación.

Además se pierde una ayuda: el **efecto suelo**, que abarata el estacionario cerca
del terreno, no está disponible en un estacionario alto. Por eso la operación en
montaña pide más potencia y márgenes amplios.

Clase 7: [🌍 Entornos de trabajo](../operacion/entornos-helicoptero.md).

</details>

**2.3.** En un estacionario sobre el mar, el piloto novato corrige el cíclico una
y otra vez y el helicóptero oscila cada vez más. ¿Qué le dirías?

<details>
<summary>Ver respuesta</summary>

Está **sobrecontrolando el cíclico**, uno de los errores comunes del estacionario:
cada corrección grande genera una desviación que exige otra corrección, y se entra
en oscilación. El cíclico se usa con **pequeños** movimientos.

El mar lo agrava porque no hay referencias fijas y el oleaje engaña, así que
conviene apoyarse en los instrumentos: horizonte artificial para la actitud y
variómetro cerca de cero.

Módulos 5 y 6:
[🧪 Principios](../operacion/principios-helicoptero.md) y
[🌍 Entornos](../operacion/entornos-helicoptero.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe el par y el anti-par sin explicarlos con
texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer el **paso colectivo** y el **pedal / anti-par**, y
mostrar junto a ellos el par que el rotor aplica sobre el fuselaje y la guiñada
resultante. Así el usuario **ve** que al subir el colectivo el indicador de par
crece y la nariz empieza a irse, y descubre solo que el pedal es lo que lo
cancela.

La interfaz debe mostrar cómo un mando afecta a los otros: es justamente lo que
hace difícil al helicóptero.

Clase 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-helicoptero.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
autorrotación, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**, junto con el rotor RPM y la disimetría de
sustentación. En el nivel 1 la meta es elevar, mantener el hover, trasladar y
posar: la coordinación básica ya es exigente. El nivel 2 agrega par, anti-par y
efecto suelo, que son los conceptos físicos centrales del ala rotatoria.

La autorrotación llega al final porque depende de entender antes el rotor RPM y el
flujo de aire a través del rotor; sin esa base es una secuencia de teclas que se
memoriza sin comprender.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar el par y por qué hace falta compensarlo.
- [ ] Distingo el paso colectivo del paso cíclico y sé qué hace el plato cíclico.
- [ ] Puedo explicar la autorrotación sin decir "planea".
- [ ] Sé por qué el estacionario exige corregir los tres mandos de forma continua.
- [ ] Entiendo cómo la densidad del aire y el efecto suelo cambian la potencia
      necesaria.
- [ ] Conozco la licencia chilena aplicable, la autoridad y el certificado médico.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Comprueba lo que recuerdas, Aplica: casos de operación, Lleva a la simulación y Guía de estudio aplicada** a **defender una solución integral para vuelo estacionario fuera de efecto suelo con temperatura elevada**?

### Explicación razonada

La integración no consiste en repetir definiciones. Ante «vuelo estacionario fuera de efecto suelo con temperatura elevada» hay que reconstruir la cadena motor → transmisión → rotor principal → empuje y control, aplicar el principio «sustentación del rotor condicionada por paso colectivo, cíclico, potencia y rotor de cola», reconocer el riesgo y defender una decisión verificable: comprobar potencia disponible y mantener una vía de escape antes del estacionario.

Esta clase se conecta con el resto del curso mediante **sustentación del rotor condicionada por paso colectivo, cíclico, potencia y rotor de cola**. El hilo de
seguridad consiste en reconocer a tiempo **déficit de potencia, pérdida de rpm o control de guiñada** y poder justificar la decisión
**comprobar potencia disponible y mantener una vía de escape antes del estacionario**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → rotor principal → empuje y control**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Helicopter Flying Handbook](https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf) aporta aerodinámica y control de helicópteros;
[Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) se usa para aerodinámica, sistemas y operación. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Diagnosticar:** reconstruye **motor → transmisión → rotor principal → empuje y control** ante **vuelo estacionario fuera de efecto suelo con temperatura elevada**.
2. **Explicar:** aplica **sustentación del rotor condicionada por paso colectivo, cíclico, potencia y rotor de cola** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **comprobar potencia disponible y mantener una vía de escape antes del estacionario** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **helicóptero ligero frente a helicóptero de transporte**.

### Comprueba tu comprensión

1. ¿Cuál es tu diagnóstico causal de «vuelo estacionario fuera de efecto suelo con temperatura elevada»?
2. ¿Qué alternativa a **comprobar potencia disponible y mantener una vía de escape antes del estacionario** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve la autoevaluación de Helicópteros y defiende una decisión en un escenario integrador sin consultar las respuestas.
- **Evidencia:** Respuestas justificadas y escenario final resuelto.
- **Criterio de aprobación:** Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HELI](https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf): Helicopter Flying Handbook, FAA. Uso: aerodinámica y control de helicópteros.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-helicoptero.md)
