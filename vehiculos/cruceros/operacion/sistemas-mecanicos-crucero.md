<!-- clase-meta
tipo_documento: clase
clase: 4
codigo: CRUCEROS-04
curso: cruceros
titulo: "Sistemas mecánicos del crucero"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: CRUCEROS-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Casco y compartimentado, Propulsión diesel-eléctrica y pods, Gobierno y estabilizadores y Generación y distribución eléctrica con vocabulario propio de Cruceros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Cruceros."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🔧 Sistemas mecánicos del crucero

[🏠 Inicio](../../../README.md) · [⛴️ Curso: Cruceros](../README.md) · 🔧 Sistemas mecánicos

Esta clase abre el crucero por dentro. Explica cada sistema, como funciona y como
se conecta con los demás. Es la base técnica para entender los mandos (Clase 5)
y la física de la navegación (Clase 6). En un buque de pasaje, la cadena de
energía alimenta por igual a la propulsión y a la ciudad flotante que vive a bordo.

```mermaid
flowchart LR
    subgraph Energia
        G[Generadores diesel] --> Cu[Cuadro eléctrico principal]
    end
    subgraph Propulsion
        Cu --> Me[Motores eléctricos] --> Po[Pods azimutales]
    end
    subgraph Estructura
        Ca[Casco compartimentado] --- La[Lastre]
        Ca --- Es[Estabilizadores]
    end
    subgraph Hotel
        Cu --> Se[Servicios de hotel]
    end
    Po --> Empuje[Empuje y gobierno]
    Es --> Confort[Confort]
    Se --> Pasaje[Pasajeros]
```

---

## 1. 🚢 Casco y compartimentado

El casco es la estructura estanca que da flotación, resistencia y forma
hidrodinámica. En un buque de pasaje, su división interna es tan importante como
su resistencia: debe seguir a flote aun con varios compartimentos inundados.

- **Obra viva**: parte sumergida; su forma define la resistencia al avance.
- **Obra muerta**: parte sobre la flotación, muy alta por las cubiertas de pasaje.
- **Mamparos estancos transversales**: dividen el casco para limitar inundaciones.
- **Estabilidad tras avería (damage stability)**: SOLAS exige que el buque flote
  y se mantenga con una escora tolerable tras una vía de agua definida.

| Parte | Función | Efecto en el buque |
| --- | --- | --- |
| Proa | Corta el agua | Menor resistencia al avance. |
| Popa | Aloja pods y timones | Gobierno y propulsión. |
| Quilla | Eje estructural inferior | Rigidez y estabilidad. |
| Francobordo | Altura hasta la cubierta | Reserva de flotabilidad. |
| Cubierta de cierre | Límite superior de mamparos | Referencia de compartimentado. |
| Calado | Profundidad sumergida | Limita puertos y canales. |

---

## 2. ⚡ Propulsión diesel-eléctrica y pods

El crucero moderno separa la generación de energía de la propulsión. Los
generadores diesel producen electricidad, que alimenta motores eléctricos
acoplados a los pods; no hay ejes largos que atraviesen todo el buque.

```mermaid
flowchart LR
    Comb[Combustible] --> Gen[Grupos generadores diesel]
    Gen --> Cuadro[Cuadro eléctrico principal]
    Cuadro --> Convert[Convertidores de frecuencia]
    Convert --> Motor[Motores eléctricos de propulsión]
    Motor --> Pod[Pod azimutal]
    Pod -->|empuja agua atrás| Empuje[Empuje adelante]
    Pod -->|gira 360 grados| Gobierno[Gobierno]
```

- **Grupos generadores**: varios motores diesel mueven alternadores; se conectan
  y desconectan según la demanda de propulsión y de hotel.
- **Cuadro eléctrico principal**: reparte la energía entre propulsión y servicios;
  es el corazón de la planta diesel-eléctrica.
- **Motores eléctricos**: convierten la electricidad en giro para los pods.
- **Pods azimutales**: unidades bajo el casco que giran 360 grados; propulsan y
  gobiernan a la vez, y mejoran mucho la maniobra en puerto.
- **Propulsores de proa (bow thrusters)**: dan movimiento lateral a baja velocidad.

| Componente | Función | Nota |
| --- | --- | --- |
| Grupo generador | Produce electricidad | Se acopla según demanda. |
| Cuadro principal | Reparte energía | Propulsión más hotel. |
| Convertidor de frecuencia | Regula revoluciones del motor | Control fino de empuje. |
| Motor de propulsión | Mueve el pod | Eléctrico, sin caja larga. |
| Pod azimutal | Empuja y gobierna | Giro de 360 grados. |
| Thruster de proa | Maniobra en puerto | Movimiento lateral. |

---

## 3. ⚙️ Gobierno y estabilizadores

En un buque con pods, el gobierno se logra orientando las unidades; en buques con
línea de ejes clásica, con timones. El confort del pasaje agrega los
estabilizadores.

```mermaid
flowchart TD
    Puente[Puente de mando] --> Orden[Orden de rumbo]
    Orden --> Pod[Pods orientables]
    Orden --> Timon[Timones si hay ejes]
    Pod -->|vector de empuje| Giro[Cambio de rumbo]
    Timon -->|desvia el agua| Giro
    Sensor[Sensor de balance] --> Aletas[Aletas estabilizadoras]
    Aletas -->|contrarrestan| Balance[Reduce el balance]
```

- **Gobierno por pods**: se cambia el rumbo orientando el vector de empuje; muy
  eficaz incluso a baja velocidad.
- **Timones (buques con ejes)**: la pala desvia el flujo de agua en popa.
- **Aletas estabilizadoras**: superficies retráctiles a los costados que se
  inclinan para contrarrestar el balance transversal y dar confort al pasaje.
- **Efecto de la velocidad**: el gobierno por pod mantiene autoridad a menor
  velocidad que un timón clásico.

---

## 4. 🔌 Generación y distribución eléctrica

La electricidad es el sistema central de un crucero: mueve la propulsión y toda
la hoteleria. Su fiabilidad es una cuestión de seguridad.

| Elemento | Función | Nota de seguridad |
| --- | --- | --- |
| Grupos generadores principales | Producen la energía de a bordo | Redundancia entre varios grupos. |
| Cuadro principal | Distribuye a propulsión y hotel | Puede dividirse en secciones. |
| Generador de emergencia | Alimenta cargas vitales si falla lo principal | Arranque automático exigido por SOLAS. |
| Baterías y SAI | Respaldan luces y sistemas críticos | Transición sin corte. |
| Blackout recovery | Reconexion tras apagón general | Procedimiento y automatismo definidos. |

- **Cargas de propulsión**: motores de los pods y thrusters.
- **Cargas de hotel**: iluminación, climatización, cocinas, ascensores, ocio.
- **Cargas de seguridad**: alumbrado de emergencia, bombas contraincendios,
  comunicaciones, control de botes.

---

## 5. 🏨 Servicios de hotel

El crucero es una ciudad flotante. Además de navegar, debe dar agua, aire
acondicionado, energía y saneamiento a miles de personas.

```mermaid
flowchart LR
    Mar[Agua de mar] --> Potable[Plantas de agua potable]
    Potable --> Red[Red de agua dulce]
    Red --> Camarotes[Camarotes y cocinas]
    HVAC[Plantas HVAC] --> Clima[Climatización de cubiertas]
    Camarotes --> Aguas[Aguas residuales]
    Aguas --> Depura[Planta de tratamiento]
    Depura --> Descarga[Descarga según MARPOL]
```

- **Agua potable**: se produce a bordo por evaporadores u ósmosis inversa desde
  agua de mar, y se almacena en tanques dedicados.
- **Climatización (HVAC)**: mantiene temperatura y ventilación en camarotes y
  espacios públicos; es un gran consumidor de energía.
- **Aguas residuales**: plantas de tratamiento procesan aguas negras y grises
  antes de descargar, según MARPOL.
- **Cocinas, lavandería y ocio**: servicios que definen la vida del pasaje y su
  demanda de energía y agua.

---

## 6. 🛟 Seguridad de pasajeros y evacuación

Es el sistema que distingue a un buque de pasaje. Debe permitir evacuar a todos
los que van a bordo en un tiempo definido.

```mermaid
flowchart TD
    Alarma[Alarma general] --> Reunion[Puntos de reunión / muster]
    Reunion --> Chalecos[Chalecos salvavidas]
    Chalecos --> Botes[Botes salvavidas]
    Chalecos --> Balsas[Balsas inflables]
    Botes --> Arriado[Pescantes de arriado]
    Balsas --> Arriado
    Arriado --> Agua[Embarcaciones al agua]
    Deteccion[Detección de incendios] --> Zonas[Zonas contraincendios]
    Zonas --> Rociadores[Rociadores y puertas estancas]
```

| Elemento | Función | Referencia |
| --- | --- | --- |
| Botes salvavidas | Evacuación ordenada del pasaje | Capacidad para todos a bordo, SOLAS. |
| Balsas inflables | Complemento de evacuación | Se arrian y se inflan al agua. |
| Chalecos salvavidas | Flotabilidad individual | En camarotes y puntos de reunión. |
| Ejercicio de muster | Reunión y conteo del pasaje | Antes de zarpar, obligatorio. |
| Zonas contraincendios | Limitan la propagación | Mamparos y puertas estancas. |
| Detección y rociadores | Detectan y extinguen fuego | Cubren camarotes y espacios públicos. |

- **Compartimentado activo**: puertas estancas que se cierran para contener vías
  de agua o incendios.
- **Rutas de evacuación**: senalizadas y con alumbrado de emergencia hacia los
  puntos de reunión.
- **Dotación de seguridad**: la tripulación tiene roles asignados para guiar y
  contar a los pasajeros.

---

## 🔁 Cómo se conecta todo

1. Los **generadores diesel** producen la electricidad del buque.
2. El **cuadro principal** la reparte entre **propulsión** y **hotel**.
3. Los **motores eléctricos** mueven los **pods**, que empujan y gobiernan.
4. El **casco compartimentado** y los **estabilizadores** dan flotación y confort.
5. Los **servicios de hotel** sostienen la vida del pasaje.
6. Los **sistemas de seguridad** permiten contener averías y evacuar a todos.

Con esto entendido, el [Clase 5: Mandos](../mandos/manual-mandos-crucero.md)
muestra cómo la tripulación opera cada uno de estos sistemas desde el puente.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Casco y compartimentado, Propulsión diesel-eléctrica y pods, Gobierno y estabilizadores y Generación y distribución eléctrica** a **seguir una alteración desde generación eléctrica hasta casco y gobierno durante atraque con viento sobre una superestructura de gran superficie**?

### Explicación razonada

El funcionamiento puede leerse como una cadena causal: generación eléctrica entrega o transforma energía; propulsión la adapta; hélices o pods la transmite o gobierna; y casco y gobierno produce el efecto observable. La cadena no es lineal en sentido estricto: sensores, estructura y operador cierran el lazo. Si un eslabón se degrada, la señal importante es cómo cambia el estado de casco y gobierno y qué margen queda.

```mermaid
flowchart LR
    A["generación eléctrica"] --> B["propulsión"] --> C["hélices o pods"] --> D["casco y gobierno"]
    D -. respuesta observable .-> O["operador o control"]
    O -. orden y verificación .-> A
```

Esta clase se conecta con el resto del curso mediante **maniobrabilidad de gran masa combinada con viento lateral y efecto de aguas restringidas**. El hilo de
seguridad consiste en reconocer a tiempo **contacto con muelle o pérdida de separación por subestimar abatimiento** y poder justificar la decisión
**coordinar propulsión, remolcadores y límites de viento antes de aproximar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **generación eléctrica → propulsión → hélices o pods → casco y gobierno**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Safety of Navigation](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx) aporta navegación, SOLAS, COLREG y STCW;
[Collision Regulations](https://www.imo.org/en/about/conventions/pages/colreg.aspx) se usa para prevención de abordajes. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Entrada:** identifica el estado inicial de **generación eléctrica** durante **atraque con viento sobre una superestructura de gran superficie**.
2. **Transformación:** explica qué hacen **propulsión** y **hélices o pods**, y qué magnitud cambia en cada paso.
3. **Salida:** comprueba el efecto esperado en **casco y gobierno** y busca una desviación temprana.
4. **Falla razonada:** si aparece **contacto con muelle o pérdida de separación por subestimar abatimiento**, retrocede por la cadena antes de ordenar otra acción.

### Comprueba tu comprensión

1. Si se degrada **propulsión**, ¿qué efecto esperarías primero en **hélices o pods** y después en **casco y gobierno**?
2. ¿Qué observación ayudaría a diferenciar una falla de **generación eléctrica** de una falla de **hélices o pods**?
3. ¿Por qué una segunda orden podría agravar **contacto con muelle o pérdida de separación por subestimar abatimiento**?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de Cruceros que conecte Casco y compartimentado, Propulsión diesel-eléctrica y pods, Gobierno y estabilizadores y Generación y distribución eléctrica; después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [IMO-COLREG](https://www.imo.org/en/about/conventions/pages/colreg.aspx): Collision Regulations, International Maritime Organization. Uso: prevención de abordajes.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-crucero.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-crucero.md)
