<!-- clase-meta
tipo_documento: clase
clase: 3
codigo: MOTOS-03
curso: motos
titulo: "Modelos y variantes de la moto"
modalidad: "comparativa guiada"
duracion_minutos: 60
nivel: introductorio
prerrequisito: MOTOS-02
competencia: "seleccion_de_configuracion"
resultados_aprendizaje:
  - "Explicar manejo, arquitectura de mandos y variables de simulación con vocabulario propio de Motocicletas."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Motocicletas."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🧩 Modelos y variantes de la moto

[🏠 Inicio](../../../README.md) · [🏍️ Curso: Motos](../README.md) · 🧩 Modelos

El [Clase 2](../operacion/caracteristicas-moto.md) ya dijo qué tipos de moto
existen y para qué sirve cada uno. Esta clase responde a lo siguiente: **no
todas se pilotan igual**, y esa diferencia no es de matiz. Cambia qué mandos
tiene la máquina y, por tanto, qué debe modelar el simulador.

> 🎯 **La idea que sostiene el módulo.** "Una moto" no es una sola máquina desde
> el punto de vista del mando. Un scooter no tiene embrague ni palanca de cambio:
> no es que los tenga más fáciles, es que **no existen**. Un simulador que
> presente un solo esquema de control está representando una moto concreta
> aunque diga representarlas todas.

---

## 🧭 Por qué el modelo decide el simulador

El [Clase 5](../mandos/manual-mandos-moto.md) describe un puesto de mando con
embrague en la maneta izquierda y cambio en el pie izquierdo. El
[Clase 9](../simulacion/diseno-simulador-moto.md) expone una variable `Marcha`
con rango `N,1..6`. Ambos describen una moto **de transmisión manual**.

En un scooter esa maneta izquierda no es el embrague: es el freno trasero. Y la
variable `Marcha` sencillamente no tiene valores que tomar. Si el simulador se
construye sobre el esquema manual y luego se le "añade" un scooter, el resultado
es un scooter con embrague, que no existe.

---

## 🗂️ Qué cambia en el manejo

| Modelo | Qué cambia al pilotarla |
| --- | --- |
| Urbana / naked | La referencia del curso: posición erguida, peso contenido, comportamiento neutro. |
| Scooter | Sin gestión de marchas, la atención se libera hacia el tráfico. Ruedas pequeñas: más nervioso ante baches y juntas. |
| Deportiva | Peso adelantado sobre las muñecas y mucha potencia: la transferencia de peso es más brusca y el margen de error se acorta. |
| Crucero / custom | Centro de gravedad bajo y par a bajas vueltas: estable y cómoda en recta, pero toca antes en las curvas cerradas. |
| Trail / adventure | Suspensión larga y rueda delantera grande: absorbe el terreno irregular y se hunde más al frenar. |
| Eléctrica | Entrega de par inmediata desde parado y sin ruido de motor: se pierde la referencia sonora del régimen. |
| Reparto / trabajo | La carga cambia durante la jornada: el mismo vehículo se comporta distinto al principio y al final del reparto. |

---

## 🎛️ Qué cambia en el mando

| Modelo | Qué mando aparece o desaparece | Consecuencia |
| --- | --- | --- |
| Urbana / naked, Deportiva, Crucero, Trail | Ninguno: el mapa de controles del Clase 5 aplica tal cual. | Cambian los rangos, no los controles. |
| Scooter | **Desaparecen** el embrague y la palanca de cambio. El freno trasero **se muda** del pedal a la maneta izquierda. | El pie izquierdo deja de tener función y ambos frenos se accionan con las manos. |
| Eléctrica | **Desaparecen** el embrague y el cambio en la mayoría. El acelerador pasa a mandar par directo. | El tacómetro pierde sentido; el freno regenerativo se solapa con el freno trasero. |
| Reparto / trabajo | **Aparece** el portaequipajes o el baúl como masa que el piloto gestiona. | No es un mando, pero altera el resultado de todos los demás. |

---

## 🎮 Qué cambia en el simulador

Contrastado con las variables del
[Clase 9](../simulacion/diseno-simulador-moto.md):

| Modelo | Variables que cambian | Esquema de control |
| --- | --- | --- |
| Urbana / naked | Ninguna: es el caso base. | El del Clase 5. |
| Scooter | `Marcha` **se elimina**. `Régimen del motor` se desacopla de la marcha y pasa a depender solo del acelerador. | Sin entrada de embrague ni de cambio; dos frenos en las manos. |
| Deportiva | `Régimen` e `Inclinación` amplían rango; la transferencia de peso pesa más en el cálculo. | El mismo, con respuesta más sensible. |
| Crucero / custom | `Inclinación` **reduce** su rango útil: toca suelo antes. | El mismo. |
| Trail / adventure | `Adherencia` deja de ser un valor de asfalto y depende del terreno. | El mismo. |
| Eléctrica | `Régimen del motor` **desaparece** o se sustituye por par disponible. `Combustible/energía` pasa a ser carga de batería, y se degrada con la temperatura. | Sin embrague ni cambio; frenada regenerativa. |
| Reparto / trabajo | `Peso del conjunto` deja de ser fijo y pasa a variar durante la partida. | El mismo. |

---

## 🗺️ Del modelo al esquema de control

```mermaid
flowchart TD
    Modelo[🧩 Modelo elegido] --> Trans{¿Tiene marchas?}
    Trans -- Sí --> Manual[Esquema manual:<br/>embrague, cambio,<br/>freno trasero al pie]
    Trans -- No --> Auto[Esquema automático:<br/>sin embrague ni cambio,<br/>ambos frenos a mano]
    Manual --> Var1[Simulador con variable Marcha]
    Auto --> Var2[Simulador sin variable Marcha]
    Modelo --> Energia{¿Combustión o eléctrica?}
    Energia -- Combustión --> Reg[Régimen en rpm<br/>y sonido como referencia]
    Energia -- Eléctrica --> Par[Par inmediato,<br/>sin referencia sonora]
```

---

## ⚠️ Qué modelos no comparten simulador

Dos familias no se resuelven con un ajuste de parámetros, porque su esquema de
control es otro:

- **El scooter y la eléctrica sin marchas** frente al resto: faltan dos entradas
  y una tercera cambia de sitio. Es un modo de control distinto, no una
  dificultad distinta.
- **El reparto con carga variable** frente a los demás: obliga a que el peso sea
  una variable viva durante la partida, no una constante que se fija al empezar.

El resto de modelos sí caben en un mismo simulador ajustando rangos, tal como
plantean los [niveles de realismo](../../../docs/03-niveles-de-realismo.md): en
el nivel 1 casi todos se comportan igual, y las diferencias emergen a medida que
el nivel sube.

> ⚖️ **El principio detrás de todo esto.** Cuánto pesa la carga y dónde va no cambia
> solo los números: cambia qué puede hacer el operador. La física común a todas las
> máquinas del catálogo —sostener, girar, equilibrar y la masa que cambia en
> marcha— está en [⚖️ carga y manejo](../../../docs/09-carga-y-manejo.md).

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Por qué el modelo decide el simulador, Qué cambia en el manejo, Qué cambia en el mando y Qué cambia en el simulador** a **comparar scooter urbano frente a motocicleta trail frente al mismo encargo**?

### Explicación razonada

Las variantes «scooter urbano frente a motocicleta trail» resuelven prioridades distintas. Una comparación profesional sigue la cadena motor → embrague y caja → transmisión final → neumático trasero: cada cambio de arquitectura modifica mandos, respuesta, mantenimiento y variables que una simulación debe representar. Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito.

Esta clase se conecta con el resto del curso mediante **equilibrio entre inclinación, velocidad, radio y adherencia disponible**. El hilo de
seguridad consiste en reconocer a tiempo **agotar adherencia por frenar o acelerar bruscamente con la moto inclinada** y poder justificar la decisión
**ajustar velocidad, trayectoria y suavidad de los mandos antes de inclinar**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → embrague y caja → transmisión final → neumático trasero**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Manuales para conductores](https://www.conaset.cl/manuales/) se usa para formación vial y seguridad. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **aproximación a una curva urbana mojada con visibilidad parcial**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **motor** hasta **neumático trasero**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.

### Comprueba tu comprensión

1. ¿Qué cambia en la cadena **motor → embrague y caja → transmisión final → neumático trasero** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «aproximación a una curva urbana mojada con visibilidad parcial» y qué desventaja aceptarías?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Motocicletas mediante los ejes «manejo, arquitectura de mandos y variables de simulación» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [CL-CONASET](https://www.conaset.cl/manuales/): Manuales para conductores, CONASET. Uso: formación vial y seguridad.
- [US-NHTSA-MOTO](https://www.nhtsa.gov/road-safety/motorcycles): Motorcycle Safety, NHTSA. Uso: riesgos, equipo y conducción segura.
- [MSF-BRC](https://msf-usa.org/library/): Motorcycle Safety Foundation Library, MSF. Uso: formación inicial y ejercicios.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Características](../operacion/caracteristicas-moto.md) · [➡️ Siguiente: Sistemas mecánicos](../operacion/sistemas-mecanicos-moto.md)
