<!-- clase-meta
tipo_documento: clase
clase: 11
codigo: ASCENSORES-11
curso: ascensores
titulo: "Ejercicios y autoevaluación del ascensor"
modalidad: "evaluación auténtica"
duracion_minutos: 90
nivel: introductorio
prerrequisito: ASCENSORES-10
competencia: "integracion_de_competencias"
resultados_aprendizaje:
  - "Explicar comprensión, aplicación y transferencia a la simulación con vocabulario propio de Ascensores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Ascensores."
evidencia: "Respuestas justificadas y escenario final resuelto."
criterio_aprobacion: "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🎯 Ejercicios y autoevaluación del ascensor

[🏠 Inicio](../../../README.md) · [🛗 Curso: Ascensores](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación
> certificada ni la intervención de personal competente de una empresa
> autorizada. Sirve para comprobar si el curso se entendió y para detectar que
> módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué el contrapeso hace que el motor gaste mucho menos energía?

<details>
<summary>Ver respuesta</summary>

Porque el contrapeso compensa la cabina más parte de la carga nominal, así el
motor no mueve toda la cabina: solo mueve la **diferencia** de peso entre cabina
y contrapeso. Ese equilibrio es la característica central del ascensor de
tracción.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-ascensor.md)
y [🧪 Principios y operación](../operacion/principios-ascensor.md).

</details>

**1.2.** La cabina no cuelga de un tambor que enrolla el cable. ¿Cómo la mueve
entonces la polea, y que papel juega el contrapeso en ello?

<details>
<summary>Ver respuesta</summary>

Por **fricción, no por arrollamiento**: la polea de tracción es una rueda
ranurada y aprovecha el agarre del cable en sus ranuras. El contrapeso no solo
equilibra: su peso da la **tensión** que hace posible esa fricción. Sin tensión
no hay agarre.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-ascensor.md).

</details>

**1.3.** El freno del motor y el freno de seguridad no son lo mismo. ¿Qué hace
cada uno y quién dispara al segundo?

<details>
<summary>Ver respuesta</summary>

El **freno del motor** sostiene la cabina detenida en cada piso, en la operación
normal. El **freno de seguridad (paracaídas)** es mecánico: unas cunas muerden
las guías y detienen la cabina. Lo dispara el **gobernador de velocidad**, que
vigila la velocidad y actúa si se excede la permitida en el descenso.

Son sistemas **independientes**: esa redundancia es lo que evita la caída libre.

Clase 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-ascensor.md).

</details>

**1.4.** Ordena las siete fases de un viaje, desde que el usuario pide la cabina
hasta que se abre la puerta en el destino.

<details>
<summary>Ver respuesta</summary>

1. **Llamada**: el usuario pide la cabina indicando el sentido.
2. **Asignación**: el control decide la ruta; la maniobra colectiva optimiza
   viajes.
3. **Apertura** en origen, con enclavamiento y sensor de obstáculo.
4. **Aceleración**: arranque suave con el variador.
5. **Marcha**: velocidad estable, cabina guiada por las guías.
6. **Frenado**: desaceleración y nivelación precisa.
7. **Parada**: el freno del motor sostiene la cabina con la puerta abierta.

Clase 6: [🧪 Principios y operación](../operacion/principios-ascensor.md).

</details>

**1.5.** ¿Qué hito de 1853 volvió confiable al ascensor de pasajeros, y qué
permitió construir?

<details>
<summary>Ver respuesta</summary>

El **freno de seguridad de Otis**: un dispositivo que detiene la cabina si el
cable falla. Con esa seguridad el ascensor de pasajeros se volvió confiable, y
a partir de los ascensores eléctricos (1880-1900) hizo viables los rascacielos.

Clase 1: [📜 Historia](../historia/historia-ascensor.md).

</details>

**1.6.** ¿Qué licencia exige Chile para operar un ascensor y cuál es el núcleo de
la Ley 20.296?

<details>
<summary>Ver respuesta</summary>

**Ninguna licencia de conducir**: el ascensor es maquinaria fija y no circula por
vía pública. La Ley 20.296 regula la **instalación, mantención e inspección** de
ascensores y similares. La mantención es periódica y obligatoria, la realiza
personal competente de empresas autorizadas, la certificación la emite un
organismo autorizado y la fiscalización recae en la municipalidad (Dirección de
Obras). Los plazos exactos están por confirmar.

Clase 8: [⚖️ Reglamentos](../reglamentos/reglamentos-ascensor.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md), sección 1.8.

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Entra un grupo de personas, suena la alerta de sobrecarga y la cabina no
arranca. Alguien propone pulsar cierre de puerta con insistencia. ¿Qué está
pasando y qué corresponde hacer?

<details>
<summary>Ver respuesta</summary>

El indicador de sobrecarga detectó exceso de peso sobre la carga nominal y el
sistema **impide arrancar**: es una protección, no una falla. Insistir con el
botón de cierre no la anula, porque el estado de sobrecarga bloquea la marcha
hasta que se reduzca la carga.

Lo que corresponde es que salgan personas hasta que la alerta se apague. La
carga máxima está indicada en la cabina y respetarla es una regla de seguridad,
no una recomendación.

Clase 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-ascensor.md).

</details>

**2.2.** Un ascensor tiene el cartel de fuera de servicio, pero la puerta de piso
cede un poco al empujarla. ¿Por qué no se toca y qué dos reglas se estarían
rompiendo?

<details>
<summary>Ver respuesta</summary>

Porque el estado fuera de servicio significa mantención o falla, y en él solo
opera un técnico en **modo inspección**, que está reservado a personal
competente. La cabina puede no estar detrás de esa puerta.

Se rompen dos reglas explícitas: no usar el ascensor fuera de servicio y no
forzar las puertas. Además el **enclavamiento** existe justo para que la cabina
no se mueva con una puerta abierta; manipularlo desarma esa protección.

Módulos 4 y 7: [🎛️ Mandos](../mandos/manual-mandos-ascensor.md) y
[⚖️ Reglamentos](../reglamentos/reglamentos-ascensor.md).

</details>

**2.3.** Mismo modelo de ascensor, dos edificios: una torre de oficinas y un
hospital. ¿Qué cambia en la operación de cada uno?

<details>
<summary>Ver respuesta</summary>

En **oficinas** el problema es el tráfico: picos de demanda diurnos, entradas y
salidas masivas. Se exige rapidez y reparto, y la respuesta es una maniobra
colectiva optimizada que agrupe llamadas.

En **hospital** el problema es la carga y la urgencia: camillas y equipos piden
cabina amplia, modo de prioridad y una nivelación exacta, porque una cabina mal
nivelada con el piso es un obstáculo real para una camilla.

Clase 7: [🌍 Entornos de trabajo](../operacion/entornos-ascensor.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la ventaja del contrapeso sin explicarla
con texto. ¿Qué variables expondrías y como las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: exponer la **carga** (0-100% del nominal) y el **contrapeso**
(fijo), y mostrar el esfuerzo del motor como un indicador que se mueve al variar
la carga. El ciclo básico ya calcula ese esfuerzo según carga y contrapeso.

Así el usuario **ve** que el indicador baja casi a cero cuando cabina y
contrapeso se equilibran, y sube cuando la carga se aleja de ese punto: entiende
solo que el motor mueve la diferencia, no todo el peso.

Clase 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-ascensor.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías el
gobernador y el modo inspección, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es llamar la cabina, viajar
entre pisos y abrir o cerrar puertas: sumar ahí un gobernador añade complejidad
que tapa lo que se quiere enseñar. El nivel 2 introduce contrapeso, sobrecarga y
nivelación, que son los conceptos centrales. El gobernador, el freno de
seguridad, la maniobra colectiva y el modo inspección son detalle técnico y
llegan al final.

Además el modo inspección es operación de personal competente, no uso público, y
la simulación debe distinguir claramente ambas cosas.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué el contrapeso reduce el consumo del motor.
- [ ] Puedo explicar la tracción por fricción sin decir "el cable se enrolla".
- [ ] Distingo el freno del motor del freno de seguridad y sé quién lo dispara.
- [ ] Sé ordenar las fases de un viaje y decir que ocurre en cada una.
- [ ] Conozco el marco legal chileno aplicable y por qué no hay licencia.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Comprueba lo que recuerdas, Aplica: casos de operación, Lleva a la simulación y Guía de estudio aplicada** a **defender una solución integral para viaje con carga variable seguido de una orden de parada en piso**?

### Explicación razonada

La integración no consiste en repetir definiciones. Ante «viaje con carga variable seguido de una orden de parada en piso» hay que reconstruir la cadena motor → polea tractora → cables → cabina y contrapeso, aplicar el principio «equilibrio de masas y control de aceleración, velocidad, nivelación y frenado», reconocer el riesgo y defender una decisión verificable: verificar enclavamientos y estado antes de autorizar el movimiento.

Esta clase se conecta con el resto del curso mediante **equilibrio de masas y control de aceleración, velocidad, nivelación y frenado**. El hilo de
seguridad consiste en reconocer a tiempo **movimiento con puertas inseguras, mala nivelación o pérdida de tracción** y poder justificar la decisión
**verificar enclavamientos y estado antes de autorizar el movimiento**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → polea tractora → cables → cabina y contrapeso**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [1917.116 Elevators and Escalators](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116) aporta inspección y riesgos de transporte vertical;
[Vehicle Safety](https://www.nhtsa.gov/vehicle-safety) se usa para seguridad de vehículos terrestres. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Diagnosticar:** reconstruye **motor → polea tractora → cables → cabina y contrapeso** ante **viaje con carga variable seguido de una orden de parada en piso**.
2. **Explicar:** aplica **equilibrio de masas y control de aceleración, velocidad, nivelación y frenado** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **verificar enclavamientos y estado antes de autorizar el movimiento** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **ascensor de tracción frente a ascensor hidráulico**.

### Comprueba tu comprensión

1. ¿Cuál es tu diagnóstico causal de «viaje con carga variable seguido de una orden de parada en piso»?
2. ¿Qué alternativa a **verificar enclavamientos y estado antes de autorizar el movimiento** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve la autoevaluación de Ascensores y defiende una decisión en un escenario integrador sin consultar las respuestas.
- **Evidencia:** Respuestas justificadas y escenario final resuelto.
- **Criterio de aprobación:** Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-ELEVATORS](https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116): 1917.116 Elevators and Escalators, OSHA. Uso: inspección y riesgos de transporte vertical.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-ascensor.md)
