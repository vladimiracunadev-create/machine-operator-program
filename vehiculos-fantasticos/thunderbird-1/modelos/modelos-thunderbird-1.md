<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: THUNDERBIRD1-03
curso: thunderbird-1
titulo: "Modelos y variantes del Thunderbird 1"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: THUNDERBIRD1-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Thunderbird 1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Thunderbird 1."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes del Thunderbird 1

[🏠 Inicio](../../../README.md) · [⚡ Curso: Thunderbird 1](../README.md) · 🧩 Modelos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

El [Clase 2](../operacion/caracteristicas-thunderbird-1.md) ya dijo qué tipos
conceptuales de vehículo de respuesta rápida existen —explorador ligero,
transporte pesado, nave de transición— y qué compromiso físico acepta cada uno.
Esta clase responde a otra cosa, y conviene decirlo sin rodeos: en esta nave el
eje que decide el simulador **no es el modelo, es el modo de vuelo**. Los tres
tipos del Clase 2 se distinguen por masa y empuje disponible, es decir, por
rangos. Los modos de vuelo se distinguen por qué mandos tienen sentido, que es
otra categoría de diferencia.

> 🎯 **La idea que sostiene el módulo.** "Un Thunderbird 1" no es una sola
> máquina desde el punto de vista del mando. En vertical el piloto sostiene el
> peso con el motor; en crucero lo sostienen las alas y el motor solo empuja
> hacia adelante. La misma palanca de potencia manda cosas distintas en cada
> modo. Un simulador que presente un único esquema de control está
> representando un modo concreto aunque diga representar la nave entera.

---

## 🧭 Por qué el modo decide el simulador

El [Clase 5](../mandos/manual-mandos-thunderbird-1.md) no deja lugar a dudas:
entre sus controles hay un **selector de modo de vuelo** —vertical, transición o
crucero— cuya función declarada es "cambia como responden los mandos". No cambia
la dificultad ni los rangos: cambia la respuesta. Ese selector es la confesión de
que hay tres máquinas debajo.

La razón física está en el [Clase 4](../operacion/sistemas-mecanicos-thunderbird-1.md)
y en el [Clase 6](../operacion/principios-thunderbird-1.md). En vertical, la nave
se sostiene por empuje directo: la palanca de potencia decide si sube, flota o
baja, y la relación empuje/peso es la variable que manda. En crucero, las alas
sostienen y el motor rebaja el empuje: esa misma palanca ya no decide la altura
sino la velocidad. Las alas, dice el Clase 4, "casi no sirven al despegar". La
transición es el único momento en que ambos regímenes conviven, y por eso es el
más difícil de modelar: el empuje se reparte entre sostener y avanzar.

---

## 🗂️ Qué cambia en el manejo

| Modo | Qué cambia al pilotarlo |
| --- | --- |
| Despegue y vuelo vertical | Toda la carga recae en el motor. El piloto vigila el empuje frente al peso: por encima sube, igualado flota, por debajo no despega. Las alas no aportan nada. |
| Vuelo estacionario | El caso extremo del vertical: empuje igual al peso, avance nulo y consumo continuo sin ganar nada. Un desajuste pequeño hace subir, bajar o volcar. |
| Transición | El régimen inestable. Al inclinar el chorro, parte del empuje deja de sostener antes de que las alas releven: hacerlo de golpe cuesta altura antes de dar velocidad. |
| Crucero horizontal | Las alas sostienen y el motor solo empuja hacia adelante. Se parece a pilotar un avión: la velocidad se vuelve condición para no caer, no un lujo. |
| Emergencia | No es un modo de vuelo sino una restricción sobre el activo: poco combustible o falla obligan a ahorrar potencia y aterrizar. |

Los tipos conceptuales del Clase 2 sí caben en un mismo esquema: el transporte
pesado necesita más empuje para el mismo despegue y el explorador ligero acelera
antes, pero ambos usan los mismos mandos. Es una diferencia de rango.

---

## 🎛️ Qué cambia en el mando

Contrastado con el mapa de controles del
[Clase 5](../mandos/manual-mandos-thunderbird-1.md):

| Modo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Despegue y vuelo vertical | El **mando de toberas** existe pero se mantiene a cero: inclinarlo es dejar el modo. La palanca de potencia **manda la altura**. | El eje vertical del stick derecho está de hecho inhabilitado mientras se sube recto. |
| Vuelo estacionario | **Aparece** la asistencia de estabilización como mando de pleno derecho: su función descrita es "mantiene el vuelo estacionario". | Con asistencia activa, la palanca de actitud pasa a corregir, no a mandar. |
| Transición | Ningún mando desaparece: **todos actúan a la vez**. El ángulo de toberas es el mando protagonista y la potencia debe acompañarlo. | Es el único modo que exige coordinar potencia y toberas de forma continua. |
| Crucero horizontal | El **mando de toberas** deja de ser el control de transición: quedan enderezadas. La palanca de potencia **deja de mandar la altura y manda la velocidad**. | El mismo control físico gobierna otra magnitud. La altura pasa a depender del cabeceo y de la velocidad. |
| Emergencia | **Aparece** la gestión de energía del panel central como decisión real: repartir entre motor, sensores y servicios. | En vuelo normal es un mando de prioridad media; aquí decide si la misión termina bien. |

La reasignación de la palanca de potencia es el cambio más fuerte del curso, y no
tiene equivalente en el mapa de controles: el Clase 5 describe un solo puesto de
mando porque físicamente hay uno solo. Lo que cambia es su significado.

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-thunderbird-1.md):

| Modo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Despegue y vuelo vertical | `Relación empuje/peso` es la variable que decide todo. `Ángulo de toberas` queda fijo en 0. `Velocidad horizontal` vale 0 y no aporta. | Potencia como control de altura; toberas sin uso. |
| Vuelo estacionario | `Relación empuje/peso` clavada en uno. `Combustible` cae sin que ninguna otra variable progrese. `Calor del motor` marca el límite del modo. | El anterior, más la asistencia activa. |
| Transición | `Ángulo de toberas` recorre su rango de 0 a 90 grados y reparte el empuje. `Velocidad horizontal` crece y empieza a alimentar la sustentación de alas. | Potencia y toberas acopladas; es el único modo donde ambas se mandan a la vez. |
| Crucero horizontal | `Relación empuje/peso` **deja de gobernar la altura**: la sostienen las alas vía `Velocidad horizontal`. `Densidad del aire` pasa de detalle a variable central. `Empuje del motor` puede bajar sin caer. | Esquema aerodinámico: potencia como velocidad. |
| Emergencia | `Combustible` y `Calor del motor` dejan de ser límites de fondo y pasan a ser la restricción activa. | El del modo en curso, con la potencia acotada. |

Una advertencia de nomenclatura: el Clase 9 ya usa la variable `Modo` para el
interruptor **ciencia / ficción**, que es otro eje distinto. El modo de vuelo de
este módulo necesita su propia variable; confundir ambas rompería las dos.

---

## 🗺️ Del modo al esquema de control

```mermaid
flowchart TD
    Modo[🧩 Modo de vuelo activo] --> Sost{¿Qué sostiene la nave?}
    Sost -- El motor --> Vert[Esquema vertical:<br/>potencia manda altura,<br/>toberas a cero]
    Sost -- Las alas --> Cru[Esquema de crucero:<br/>potencia manda velocidad,<br/>toberas enderezadas]
    Sost -- Ambos a la vez --> Tran[Esquema de transición:<br/>potencia y toberas<br/>acopladas]
    Vert --> V1[Simulador con relación empuje/peso como variable central]
    Cru --> V2[Simulador con velocidad horizontal y densidad del aire]
    Tran --> V3[Simulador con ángulo de toberas repartiendo el empuje]
    Modo --> Recurso{¿Combustible o calor al límite?}
    Recurso -- No --> Normal[Gestión de energía en segundo plano]
    Recurso -- Sí --> Emer[Modo emergencia:<br/>potencia acotada,<br/>reparto de energía activo]
```

---

## ⚠️ Qué modos no comparten simulador

Dos separaciones no se resuelven ajustando parámetros, porque el esquema de
control es otro:

- **El vertical frente al crucero**: no es que uno sea más difícil. Es que la
  palanca de potencia gobierna magnitudes distintas y la sustentación viene de
  fuentes distintas. Son dos modelos de vuelo, no dos niveles del mismo.
- **La transición frente a los dos anteriores**: es el único régimen donde el
  empuje se reparte entre sostener y avanzar, con las alas entrando a medias.
  No es un punto intermedio entre los otros dos: tiene su propia física, y el
  Clase 6 insiste en que es gradual, nunca instantánea.

Los tipos conceptuales del Clase 2 sí caben en un mismo simulador ajustando
rangos, igual que el interruptor ciencia / ficción del Clase 9 actúa sobre las
reglas sin tocar los mandos. La escala está en los
[niveles de realismo](../../../docs/03-niveles-de-realismo.md) que recoge el
Clase 6: en el nivel 1 basta despegar y notar que hace falta empuje, y solo al
subir de nivel la transición y el crucero exigen su propio esquema.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar vuelo supersónico ficticio frente a jet ligero real frente al mismo encargo**?

### Explicación razonada

Las variantes «vuelo supersónico ficticio frente a jet ligero real» resuelven prioridades distintas. Una comparación profesional sigue la cadena energía ficticia → propulsión → superficies de control → trayectoria de respuesta: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **una aeronave de alerta rápida prioriza tiempo de llegada sin abandonar energía ni margen de aterrizaje**. El hilo de
seguridad consiste en reconocer a tiempo **convertir velocidad narrativa en llegada segura sin plan de aproximación** y poder justificar la decisión
**separar crucero rápido de aproximación estabilizada y mantener alternativa**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **energía ficticia → propulsión → superficies de control → trayectoria de respuesta**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Thunderbirds Vehicles](https://www.thunderbirds.com/) aporta referencia oficial de vehículos de rescate;
[Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) se usa para aerodinámica, sistemas y operación. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **despliegue de rescate a una pista corta con meteorología cambiante**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **energía ficticia** hasta **trayectoria de respuesta**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **energía ficticia → propulsión → superficies de control → trayectoria de respuesta** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «despliegue de rescate a una pista corta con meteorología cambiante» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Thunderbird 1 mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [THUNDERBIRDS-OFFICIAL](https://www.thunderbirds.com/): Thunderbirds Vehicles, ITV. Uso: referencia oficial de vehículos de rescate.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-thunderbird-1.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-thunderbird-1.md)
