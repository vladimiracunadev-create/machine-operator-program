<!-- clase-meta
tipo_documento: clase
clase: 11
codigo: BARCOSMERCAN-11
curso: barcos-mercantes
titulo: "Ejercicios y autoevaluación del barco mercante"
modalidad: "evaluación auténtica"
duracion_minutos: 90
nivel: introductorio
prerrequisito: BARCOSMERCAN-10
competencia: "integracion_de_competencias"
resultados_aprendizaje:
  - "Explicar comprensión, aplicación y transferencia a la simulación con vocabulario propio de Barcos mercantes."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Barcos mercantes."
evidencia: "Respuestas justificadas y escenario final resuelto."
criterio_aprobacion: "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🎯 Ejercicios y autoevaluación del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación náutica
> certificada (STCW) ni los manuales del fabricante. Sirve para comprobar si el
> curso se entendió y para detectar que módulo conviene releer.

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Por qué flota un buque mercante de miles de toneladas?

<details>
<summary>Ver respuesta</summary>

Porque desplaza un peso de agua igual al suyo: el empuje vertical del agua
desplazada sostiene el casco. Es el principio de Arquímedes. No depende del
material del casco sino del volumen de agua que desaloja.

Clase 6: [🧪 Principios y operación](../operacion/principios-barco-mercante.md).

</details>

**1.2.** El timón está a tope y el buque casi no responde. ¿Qué está pasando?

<details>
<summary>Ver respuesta</summary>

Falta velocidad. La pala del timón gobierna desviando el flujo de agua en la
popa; si el buque está parado o casi parado no hay flujo que desviar y el timón
no genera fuerza de giro. Intentar gobernar con el buque casi parado es uno de
los errores típicos que la simulación puede enseñar a evitar.

Módulos 3 y 5:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-barco-mercante.md) y
[🧪 Principios](../operacion/principios-barco-mercante.md).

</details>

**1.3.** ¿Qué relación entre el centro de gravedad (G) y el metacentro (M) indica
un buque estable?

<details>
<summary>Ver respuesta</summary>

G por debajo de M: el buque es estable y vuelve a la vertical tras una escora.
Si G queda sobre M hay riesgo de vuelco. La posición de G depende del reparto de
peso, es decir, de la estiba y del lastre.

Módulos 3 y 9:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-barco-mercante.md) y
[🧰 Recursos](../recursos/recursos-barco-mercante.md).

</details>

**1.4.** Nombra la cadena que va del combustible al empuje y di qué hace cada
eslabón.

<details>
<summary>Ver respuesta</summary>

Combustible → **motor principal** (diesel lento, genera potencia) → **línea de
ejes** (transmite el giro y atraviesa el casco por la bocina) → **hélice**
(empuja agua hacia atrás y, por reacción, el buque avanza hacia adelante, tercera
ley de Newton) → **empuje**. Entre motor y eje puede haber un reductor, que no
siempre está presente.

Clase 4:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-barco-mercante.md).

</details>

**1.5.** Ordena las fases de operación de un buque mercante, de la preparación al
cierre.

<details>
<summary>Ver respuesta</summary>

1. **Preparación**: revisión antes de zarpar (máquina, gobierno, cartas,
   combustible).
2. **Desatraque**: salir del muelle con thruster, cabos y remolcadores si aplica.
3. **Salida de puerto**: navegar el canal a baja velocidad, con práctico y
   señales.
4. **Navegación**: travesía en mar abierto, con rumbo, guardias y vigilancia
   radar.
5. **Aproximación**: acercarse al puerto destino reduciendo velocidad con
   anticipación.
6. **Atraque**: amarrar en muelle con maniobra fina, thruster y cabos.
7. **Cierre**: dejar segura la nave, máquina parada, amarre firme y guardias.

Clase 6: [🧪 Principios y operación](../operacion/principios-barco-mercante.md).

</details>

**1.6.** ¿Cuál es la autoridad marítima en Chile, cuál es la ley base y qué
convenio internacional cubre la prevención de abordajes?

<details>
<summary>Ver respuesta</summary>

La autoridad es **DIRECTEMAR** (DGTM y MM). La ley base es el **DL 2.222 de
1978** (Ley de Navegación). La prevención de abordajes la cubre el **COLREG
1972**, con sus reglas de rumbo, luces y señales. El marco internacional lo fija
la OMI, que además aporta SOLAS (seguridad de la vida en el mar), MARPOL
(prevención de la contaminación) y STCW (formación y guardia).

Clase 8: [⚖️ Reglamentos](../reglamentos/reglamentos-barco-mercante.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Vas en travesía y detectas en el radar que la aproximación al puerto
está más cerca de lo previsto. El impulso es ordenar "atrás toda" al llegar.
¿Por qué no funciona así y qué debió pasar antes?

<details>
<summary>Ver respuesta</summary>

Por la **inercia**: con miles de toneladas, la detención es muy progresiva y el
buque sigue avanzando mucho después de la orden. Ordenar atrás toda en el último
momento no cancela esa energía; solo consume distancia que ya no queda.
Subestimar la distancia de frenado por la inercia es uno de los errores típicos.

Lo correcto es reducir la velocidad **mucho antes** de la aproximación: toda
maniobra se anticipa con minutos y millas de margen. La corrección de verdad
ocurre en la fase de aproximación, no en la de atraque.

Clase 6: [🧪 Principios y operación](../operacion/principios-barco-mercante.md).

</details>

**2.2.** Maniobra de atraque en puerto, espacio estrecho y el buque a velocidad
mínima. El timón responde poco. ¿Con qué cuentas?

<details>
<summary>Ver respuesta</summary>

Con el **thruster de proa**, que da movimiento lateral justo a baja velocidad,
que es cuando el timón deja de ser útil; con **remolcadores** y con el
**práctico** en espacios estrechos; y con los **mandos repetidos de las alas del
puente**, que permiten maniobrar con visión directa del costado. Los cabos y
cabrestantes cierran el amarre.

Módulos 3, 4 y 6:
[🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-barco-mercante.md),
[🎛️ Mandos e instrumentos](../mandos/manual-mandos-barco-mercante.md) y
[🌍 Entornos de trabajo](../operacion/entornos-barco-mercante.md).

</details>

**2.3.** Navegación costera con niebla y tráfico denso. ¿Qué cambia respecto del
mar abierto?

<details>
<summary>Ver respuesta</summary>

Cambian tres cosas a la vez. La **visibilidad** cae, así que la vigilancia pasa
del ojo al **radar / ARPA**, y hay que asegurarse de ser visto con las luces de
navegación y las señales acústicas, todo según COLREG. El **tráfico** denso
multiplica las decisiones de prioridad de paso. Y en aguas restringidas aparece
el riesgo de **varada**: hay que vigilar la ecosonda y la profundidad bajo la
quilla frente al calado del buque.

Módulos 6 y 7: [🌍 Entornos de trabajo](../operacion/entornos-barco-mercante.md)
y [⚖️ Reglamentos](../reglamentos/reglamentos-barco-mercante.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la inercia sin explicarla con texto.
¿Qué expondrías y cómo?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: separar visualmente la **orden** del **estado real**. El
telégrafo muestra el régimen ordenado y el indicador de RPM el régimen que la
máquina tiene de verdad; la corredera muestra la velocidad que va cediendo con
retardo. El ciclo básico ya aplica la inercia de la masa del buque al cambio de
velocidad y rumbo, así que basta con dejar ver ese desfase. El usuario ordena
"parado" y **ve** que el buque sigue navegando: la simulación debe reflejar el
retardo entre la orden y la respuesta.

Clase 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-barco-mercante.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías la
estabilidad (GM), el calado y la maniobra de puerto con thruster, y por qué no
antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es rumbo, velocidad y respetar
señales básicas; meter estabilidad y calado ahí añade carga que tapa lo que se
quiere enseñar. El nivel 2 introduce inercia, distancia de frenado y viento, que
son los conceptos centrales del buque. La estabilidad, el calado, las corrientes
y la maniobra de puerto con thruster y remolcadores son el detalle fino y llegan
al final.

Clase 9:
[🎮 Diseño de simulación](../simulacion/diseno-simulador-barco-mercante.md) y
[🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar por qué flota el buque sin decir "porque es hueco".
- [ ] Entiendo por qué el timón necesita velocidad para gobernar.
- [ ] Sé qué relación entre G y M hace estable a un buque.
- [ ] Puedo seguir la cadena motor → eje → hélice → empuje.
- [ ] Sé ordenar las fases de operación y decir por qué la inercia manda.
- [ ] Conozco la autoridad marítima chilena y los convenios OMI aplicables.
- [ ] Puedo nombrar tres variables que un simulador de buque debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Comprueba lo que recuerdas, Aplica: casos de operación, Lleva a la simulación y Guía de estudio aplicada** a **defender una solución integral para entrada a canal angosto con corriente transversal y tráfico**?

### Explicación razonada

La integración no consiste en repetir definiciones. Ante «entrada a canal angosto con corriente transversal y tráfico» hay que reconstruir la cadena motor principal → eje → hélice → casco y timón, aplicar el principio «inercia hidrodinámica: una orden de máquina o timón tarda en cambiar la trayectoria», reconocer el riesgo y defender una decisión verificable: planificar derrota, velocidad y punto de maniobra con margen suficiente.

Esta clase se conecta con el resto del curso mediante **inercia hidrodinámica: una orden de máquina o timón tarda en cambiar la trayectoria**. El hilo de
seguridad consiste en reconocer a tiempo **abordaje o varada por decidir con referencias tardías** y poder justificar la decisión
**planificar derrota, velocidad y punto de maniobra con margen suficiente**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor principal → eje → hélice → casco y timón**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) aporta navegación, SOLAS, COLREG y STCW;
[Collision Regulations](https://www.imo.org/en/about/conventions/pages/colreg.aspx) se usa para prevención de abordajes. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Diagnosticar:** reconstruye **motor principal → eje → hélice → casco y timón** ante **entrada a canal angosto con corriente transversal y tráfico**.
2. **Explicar:** aplica **inercia hidrodinámica: una orden de máquina o timón tarda en cambiar la trayectoria** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **planificar derrota, velocidad y punto de maniobra con margen suficiente** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **portacontenedores frente a granelero**.

### Comprueba tu comprensión

1. ¿Cuál es tu diagnóstico causal de «entrada a canal angosto con corriente transversal y tráfico»?
2. ¿Qué alternativa a **planificar derrota, velocidad y punto de maniobra con margen suficiente** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Resuelve la autoevaluación de Barcos mercantes y defiende una decisión en un escenario integrador sin consultar las respuestas.
- **Evidencia:** Respuestas justificadas y escenario final resuelto.
- **Criterio de aprobación:** Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-barco-mercante.md)
