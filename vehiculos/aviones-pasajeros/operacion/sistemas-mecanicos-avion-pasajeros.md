<!-- clase-meta
tipo_documento: clase
clase: 4
codigo: AVIONESPASAJ-04
curso: aviones-pasajeros
titulo: "Sistemas mecánicos del avión de pasajeros"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: AVIONESPASAJ-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Célula y fuselaje presurizado, Alas y dispositivos hipersustentadores, Superficies de control y Motores turbofan con vocabulario propio de Aviones de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones de pasajeros."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🔧 Sistemas mecánicos del avión de pasajeros

[🏠 Inicio](../../../README.md) · [🛫 Curso: Aviones de pasajeros](../README.md) · 🔧 Sistemas mecánicos

Esta clase abre el avión de pasajeros por dentro. Explica cada sistema, como
funciona y cómo se conecta con los demás. Es la base técnica para entender los
mandos (Clase 5) y la física del vuelo (Clase 6). Frente a un avión pequeño,
aquí aparecen la presurización, los motores turbofan y la redundancia de sistemas.

```mermaid
flowchart LR
    subgraph Estructura
        Fu[Fuselaje presurizado] --- Al[Alas]
        Al --- Emp[Empenaje]
    end
    subgraph Control
        Ale[Alerones y spoilers]
        Prof[Timón de profundidad]
        Dir[Timón de dirección]
        Hip[Flaps y slats]
    end
    subgraph Propulsion
        Mot[Motores turbofan] --> Thr[Empuje]
    end
    Al --> Ale
    Al --> Hip
    Emp --> Prof
    Emp --> Dir
    Mot --> Sist[Sistemas hidráulico y eléctrico]
    Sist --> Pres[Presurización]
    Pres --> Fu
```

---

## 1. 🧱 Célula y fuselaje presurizado

La célula es la estructura que sostiene todo. En un avión de pasajeros, el
fuselaje además es una vasija a presión que permite volar cómodo a gran altitud.

- **Fuselaje**: cuerpo central; aloja cabina de pasaje, carga y une alas y empenaje.
- **Cuadernas y larguerillos**: dan rigidez y forma cilíndrica para resistir presión.
- **Revestimiento estructural**: la piel soporta parte de las cargas y contiene la presión.
- **Ciclos de presurización**: cada vuelo presuriza y despresuriza el fuselaje; es
  un factor clave en la fatiga estructural y las inspecciones.

| Elemento | Función | Nota |
| --- | --- | --- |
| Cuadernas | Definen la sección y resisten la presión | Forma casi cilíndrica. |
| Larguerillos | Rigidizan el revestimiento | Reparten cargas longitudinales. |
| Mamparos de presión | Cierran la vasija a presión | En proa y cola. |
| Revestimiento | Piel exterior estructural | Parte de la resistencia. |
| Ventanas y puertas | Aberturas reforzadas | Zonas críticas de la presurización. |

---

## 2. 🛫 Alas y dispositivos hipersustentadores

El ala genera la sustentación. En transporte, se optimiza para crucero rápido y,
con dispositivos móviles, para volar lento y seguro en despegue y aterrizaje.

```mermaid
flowchart LR
    Aire[Flujo de aire] --> Perfil[Perfil alar]
    Perfil --> Arriba[Aire más rápido arriba<br/>menor presión]
    Perfil --> Abajo[Aire más lento abajo<br/>mayor presión]
    Arriba --> Sust[Sustentación]
    Abajo --> Sust
    Flaps[Flaps y slats desplegados] --> Baja[Más sustentación a baja velocidad]
```

| Elemento del ala | Función |
| --- | --- |
| Perfil alar | Crea la diferencia de presión y la sustentación. |
| Flecha (barrido) | Retrasa efectos de compresibilidad a alta velocidad. |
| Flaps | Aumentan sustentación y resistencia para despegue y aterrizaje. |
| Slats / borde de ataque | Retrasan la entrada en pérdida a baja velocidad. |
| Winglets | Reducen la resistencia inducida en las puntas. |
| Cajón de torsión | Estructura interna que aloja combustible. |

---

## 3. 🎚️ Superficies de control

Controlan la aeronave en sus tres ejes. En transporte se agregan superficies
como los spoilers para frenar y descender.

| Eje | Movimiento | Superficie | Mando en cabina |
| --- | --- | --- | --- |
| Longitudinal | Alabeo (rolido) | Alerones y spoilers de rolido | Yugo o sidestick a izquierda / derecha. |
| Lateral | Cabeceo | Timón de profundidad / estabilizador | Yugo o sidestick adelante / atrás. |
| Vertical | Guiñada | Timón de dirección | Pedales. |

- **Alerones**: en los bordes exteriores de las alas; suben un ala y bajan la otra.
- **Spoilers**: se levantan para reducir sustentación, frenar en el aire y en pista.
- **Timón de profundidad y estabilizador**: controlan y compensan el cabeceo.
- **Timón de dirección**: orienta la nariz y coordina el vuelo.
- **Fly-by-wire**: en muchos aviones, las ordenes van por señal eléctrica a los
  actuadores, con protecciones que evitan salir de la envolvente segura.

---

## 4. ⚙️ Motores turbofan

Convierten combustible en empuje. El turbofan mueve una gran masa de aire con un
ventilador frontal, lo que lo hace eficiente y más silencioso.

```mermaid
flowchart LR
    Aire[Aire de entrada] --> Fan[Ventilador / fan]
    Fan --> Deriv[Flujo de derivación frío]
    Fan --> Comp[Compresor]
    Comp --> Camara[Cámara de combustión]
    Camara --> Turb[Turbina]
    Turb --> Tobera[Tobera de gases]
    Deriv --> Empuje[Empuje]
    Tobera --> Empuje
```

| Componente | Función |
| --- | --- |
| Ventilador (fan) | Mueve gran masa de aire; da la mayor parte del empuje. |
| Compresor | Comprime el aire antes de la combustión. |
| Cámara de combustión | Quema combustible y libera energía. |
| Turbina | Extrae energía para mover fan y compresor. |
| Reversa de empuje | Redirige el flujo para frenar en pista. |
| FADEC | Control electrónico que regula el motor con precisión. |

---

## 5. 🛞 Tren de aterrizaje

Sostiene el avión en tierra y absorbe el impacto del aterrizaje; en transporte es
retráctil y con varias ruedas por su peso.

- **Configuración triciclo**: tren de nariz más dos o más patas principales.
- **Retráctil**: se recoge en vuelo para reducir la resistencia.
- **Amortiguadores oleoneumaticos**: absorben la energía del contacto.
- **Frenos y antideslizante (antiskid)**: detienen el avión sin bloquear ruedas.
- **Dirección de rueda de nariz**: para maniobrar en tierra.

---

## 6. 🔩 Sistemas hidráulico, eléctrico y de presurización

Los grandes aviones dependen de sistemas potentes y redundantes que mueven
superficies, tren y frenos, y mantienen habitable la cabina.

```mermaid
flowchart TD
    Motores[Motores turbofan] --> Bombas[Bombas hidráulicas]
    Motores --> Genera[Generadores eléctricos]
    Motores --> Sangrado[Aire de sangrado]
    Bombas --> Hidra[Sistemas hidráulicos redundantes]
    Hidra --> Mueve[Superficies, tren y frenos]
    Genera --> Electrico[Red eléctrica]
    Electrico --> Avion[Avionica e iluminación]
    Sangrado --> Aire[Acondicionamiento de aire]
    Aire --> Presur[Presurización de cabina]
    APU[APU] -. respalda .-> Electrico
    APU -. respalda .-> Aire
```

| Sistema | Función | Nota de seguridad |
| --- | --- | --- |
| Hidráulico | Mueve superficies, tren y frenos | Varios circuitos independientes. |
| Eléctrico | Alimenta avionica, luces y equipos | Generadores más baterías y RAT. |
| Neumático (sangrado) | Aire caliente del motor | Acondicionamiento y antihielo. |
| Presurización | Mantiene presión de cabina cómoda | Controla la altitud de cabina. |
| APU | Turbina auxiliar en tierra y respaldo | Energía sin motores en marcha. |
| Combustible | Depósitos en alas y centro | Bombas y trasvase entre tanques. |

---

## 7. 📟 Avionica y sistemas de navegación

Informan a la tripulación y gestionan el vuelo cuando no hay referencias visuales.

| Sistema | Función |
| --- | --- |
| Pantallas primarias de vuelo (PFD) | Actitud, velocidad, altitud y rumbo integrados. |
| Pantalla multifunción (ND / MFD) | Navegación, ruta y meteorología. |
| Sistema de gestión de vuelo (FMS) | Planifica y sigue la ruta, optimiza el vuelo. |
| Piloto automático y autothrottle | Mantienen rumbo, altitud, velocidad y senda. |
| Radios y transponder | Comunicación y respuesta al control de tráfico. |
| Sistemas de alerta (TCAS, GPWS) | Previenen colisión y vuelo contra el terreno. |

---

## 🔁 Cómo se conecta todo

1. Los **motores turbofan** generan **empuje** y alimentan los sistemas.
2. El empuje da **velocidad**, y las **alas** la convierten en **sustentación**.
3. Las **superficies de control** orientan el avión en los tres ejes.
4. El **fuselaje presurizado** aloja al pasaje y contiene la presión en altitud.
5. Los **sistemas hidráulico, eléctrico y neumático** mueven todo y mantienen la cabina.
6. La **avionica** informa y asiste a la tripulación para volar con seguridad.

Con esto entendido, el [Clase 5: Mandos](../mandos/manual-mandos-avion-pasajeros.md)
muestra cómo la tripulación opera cada uno de estos sistemas desde la cabina de vuelo.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Célula y fuselaje presurizado, Alas y dispositivos hipersustentadores, Superficies de control y Motores turbofan** a **seguir una alteración desde motor hasta alas y controles durante aproximación con cambio tardío de viento y una alerta de configuración**?

### Explicación razonada

El funcionamiento puede leerse como una cadena causal: motor entrega o transforma energía; empuje la adapta; flujo de aire la transmite o gobierna; y alas y controles produce el efecto observable. La cadena no es lineal en sentido estricto: sensores, estructura y operador cierran el lazo. Si un eslabón se degrada, la señal importante es cómo cambia el estado de alas y controles y qué margen queda.

```mermaid
flowchart LR
    A["motor"] --> B["empuje"] --> C["flujo de aire"] --> D["alas y controles"]
    D -. respuesta observable .-> O["operador o control"]
    O -. orden y verificación .-> A
```

Esta clase se conecta con el resto del curso mediante **gestión de energía vertical y horizontal mediante actitud, empuje y configuración**. El hilo de
seguridad consiste en reconocer a tiempo **continuar una aproximación inestable o automatizar sin comprender el modo activo** y poder justificar la decisión
**confirmar modo, energía y configuración; frustrar si la estabilidad no se recupera**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → empuje → flujo de aire → alas y controles**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Aviation Handbooks and Manuals](https://www.faa.gov/regulations_policies/handbooks_manuals) aporta aerodinámica, sistemas y operación;
[Normativa aeronáutica](https://www.dgac.gob.cl/normativa/) se usa para marco aeronáutico chileno. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Entrada:** identifica el estado inicial de **motor** durante **aproximación con cambio tardío de viento y una alerta de configuración**.
2. **Transformación:** explica qué hacen **empuje** y **flujo de aire**, y qué magnitud cambia en cada paso.
3. **Salida:** comprueba el efecto esperado en **alas y controles** y busca una desviación temprana.
4. **Falla razonada:** si aparece **continuar una aproximación inestable o automatizar sin comprender el modo activo**, retrocede por la cadena antes de ordenar otra acción.

### Comprueba tu comprensión

1. Si se degrada **empuje**, ¿qué efecto esperarías primero en **flujo de aire** y después en **alas y controles**?
2. ¿Qué observación ayudaría a diferenciar una falla de **motor** de una falla de **flujo de aire**?
3. ¿Por qué una segunda orden podría agravar **continuar una aproximación inestable o automatizar sin comprender el modo activo**?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de Aviones de pasajeros que conecte Célula y fuselaje presurizado, Alas y dispositivos hipersustentadores, Superficies de control y Motores turbofan; después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-avion-pasajeros.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-avion-pasajeros.md)
