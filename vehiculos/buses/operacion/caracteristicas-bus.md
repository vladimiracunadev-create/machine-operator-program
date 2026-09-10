<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: BUSES-02
curso: buses
titulo: "Características funcionales del bus"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: BUSES-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Buses."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Buses."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características funcionales del bus

[🏠 Inicio](../../../README.md) · [🚌 Curso: Buses](../README.md) · 📋 Características

Que es un bus, que tipos existen y para que sirve cada uno. Esta clase da el
contexto antes de abrir la mecánica (Clase 4).

---

## 🧭 Definición

Un bus es un vehículo motorizado de gran tamaño disenado para transportar muchos
pasajeros por carretera de forma colectiva. A diferencia de un automóvil, el
conductor gestiona no solo la marcha sino también la seguridad y comodidad de
decenas de personas, muchas de ellas de pie, y el ascenso y descenso en paradas.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Gran masa | Entre 10 y 30 toneladas cargado; alta inercia al acelerar y frenar. |
| Capacidad | Desde 20 hasta más de 250 pasajeros en biarticulados. |
| Pasajeros de pie | El frenado brusco los desestabiliza; exige suavidad. |
| Accesibilidad | Piso bajo, rampa y arrodillamiento para movilidad reducida. |
| Radio de giro amplio | El barrido trasero invade el carril contiguo al girar. |
| Puntos ciegos extensos | Gran carrocería y muchos espejos y cámaras. |
| Sistema neumático | Aire comprimido para frenos, puertas y suspensión. |
| Frenado asistido | Frenos de aire, ABS/EBS, freno motor y retardador. |

---

## 🗂️ Tipos de bus

```mermaid
flowchart TD
    Bus[🚌 Bus] --> Urbano[Uso urbano]
    Bus --> Interurbano[Uso interurbano]
    Bus --> Especial[Uso especial]
    Urbano --> Estandar[Urbano piso bajo]
    Urbano --> Articulado[Articulado]
    Urbano --> Biarticulado[Biarticulado]
    Urbano --> Mini[Minibus]
    Interurbano --> Ruta[Interurbano de ruta]
    Especial --> Escolar[Escolar]
    Especial --> Electrico[Eléctrico]
```

| Tipo | Uso típico | Rasgo destacado |
| --- | --- | --- |
| Urbano piso bajo | Ciudad, paradas frecuentes | Acceso a nivel de acera, accesible. |
| Articulado | Corredores de alta demanda | Sección flexible, gran aforo. |
| Biarticulado | BRT de muy alta demanda | Dos secciones flexibles, máxima capacidad. |
| Interurbano | Rutas entre ciudades | Butacas reclinables, bodega, mayor velocidad. |
| Minibus | Baja y media demanda | Menor tamaño, más maniobrable. |
| Escolar | Transporte de estudiantes | Señalización y seguridad reforzadas. |
| Eléctrico | Ciudad y BRT | Cero emisiones locales, bajo ruido. |

---

## 🎯 Para qué se usa

- Transporte público urbano masivo en ciudades.
- Corredores segregados de alta demanda (BRT).
- Conexión interurbana entre ciudades y regiones.
- Transporte escolar y de personal de empresas.
- Servicios turísticos y de acercamiento.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Tipos de bus y Para qué se usa** a **elegir una configuración adecuada para descenso prolongado con el vehículo cargado y una parada próxima**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Buses, la relación entre motor, transmisión, freno de servicio y retardador y ejes determina capacidad, respuesta y límites. Por eso «bus urbano frente a autocar interurbano» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «sobrecalentar los frenos o provocar caídas de pasajeros con acciones bruscas».

Esta clase se conecta con el resto del curso mediante **gestión de inercia, distancia de detención y transferencia de peso con pasajeros**. El hilo de
seguridad consiste en reconocer a tiempo **sobrecalentar los frenos o provocar caídas de pasajeros con acciones bruscas** y poder justificar la decisión
**seleccionar marcha y retardador antes de que la velocidad obligue a abusar del freno**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **motor → transmisión → freno de servicio y retardador → ejes**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Ley de Tránsito 18.290](https://www.bcn.cl/leychile/navegar?idNorma=29708) aporta marco legal chileno;
[Commercial Driver's License Manual](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual) se usa para operación de buses y camiones. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «descenso prolongado con el vehículo cargado y una parada próxima» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **bus urbano frente a autocar interurbano** usando esos requisitos y la cadena **motor → transmisión → freno de servicio y retardador → ejes**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **sobrecalentar los frenos o provocar caídas de pasajeros con acciones bruscas**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **ejes** condiciona primero el caso «descenso prolongado con el vehículo cargado y una parada próxima»?
2. ¿Qué requisito descartaría una de las alternativas **bus urbano frente a autocar interurbano**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Buses mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-bus.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-bus.md)
