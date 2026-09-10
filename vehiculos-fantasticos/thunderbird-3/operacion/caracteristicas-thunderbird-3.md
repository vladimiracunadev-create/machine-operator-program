<!-- clase-meta
tipo_documento: clase
clase: 2
codigo: THUNDERBIRD3-02
curso: thunderbird-3
titulo: "Características del Thunderbird 3"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: THUNDERBIRD3-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Thunderbird 3."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Thunderbird 3."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 📋 Características del Thunderbird 3

[🏠 Inicio](../../../README.md) · [🚀 Curso: Thunderbird 3](../README.md) · 📋 Características

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Que es un cohete de rescate genérico, que rasgos lo definen en la ficción y cuales
tendrían sentido físico real. Esta clase da el contexto antes de abrir la
tecnología por dentro en el Clase 4.

---

## 🧭 Definición

Un cohete de rescate, en la ficción estilo "Thunderbirds", es un vehículo capaz
de despegar deprisa, llegar al espacio y regresar para socorrer a quien lo
necesite. Lo imaginamos potente, veloz y siempre listo. En este curso lo usamos
como excusa para estudiar como subiría de verdad un vehículo así hasta la órbita.

---

## 🧬 Características clave

| Característica | Como la muestra la ficción | Lectura física real |
| --- | --- | --- |
| Despegue instantáneo | Sube en segundos y sin preparativos | Falso: el ascenso dura minutos y exige mucho propelente. |
| Ascenso vertical | Sube recto como una flecha | Solo al principio; luego debe inclinarse hacia la horizontal. |
| Llegar al espacio | Basta con subir muy alto | Insuficiente: sin velocidad lateral se vuelve a caer. |
| Cohete de una pieza | Sube y baja entero | Conviene soltar etapas vacías para no cargar peso muerto. |
| Combustible discreto | Depósito pequeño y suficiente | Real: el combustible es casi toda la masa del cohete. |
| Regreso suave | Aterriza como si nada | La reentrada libera enorme energía y calor. |

---

## 🗂️ Tipos conceptuales de cohete de rescate

```mermaid
flowchart TD
    Cohete[🚀 Cohete de rescate] --> Ligero[Cohete ligero]
    Cohete --> Pesado[Cohete pesado]
    Cohete --> Reutilizable[Cohete reutilizable]
    Ligero --> Rapido[Poca carga, sube más rápido]
    Pesado --> Carga[Más equipo de rescate y más propelente]
    Reutilizable --> Ahorro[Recupera etapas para volver a volar]
```

| Tipo | Idea de diseño | Compromiso físico |
| --- | --- | --- |
| Cohete ligero | Poca carga útil, estructura mínima | Alcanza órbita antes pero rescata poco. |
| Cohete pesado | Mucho equipo y propelente | Más masa exige más empuje y más combustible. |
| Cohete reutilizable | Etapas que se recuperan | Ahorra a la larga pero añade peso y complejidad. |

---

## 🎯 Para qué sirve en el relato

- Dar espectáculo con despegues potentes y urgentes.
- Representar el rescate rápido como una hazaña heroica.
- Simplificar el viaje al espacio a un simple "subir muy alto".

En cambio, para este curso sirve como laboratorio: cada rasgo llamativo nos
deja preguntar si sería posible y por qué.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Definición, Características clave, Tipos conceptuales de cohete de rescate y Para qué sirve en el relato** a **elegir una configuración adecuada para intercepción de una nave averiada con ventana temporal corta**?

### Explicación razonada

Una característica solo es útil cuando permite anticipar comportamiento. En Thunderbird 3, la relación entre propelentes ficticios, motores, guiado y trayectoria espacial determina capacidad, respuesta y límites. Por eso «ascenso atmosférico frente a encuentro orbital» no se compara por apariencia: se compara por misión, entorno, carga de trabajo y exposición al riesgo «consumir la reserva durante la aproximación y perder capacidad de regreso».

Esta clase se conecta con el resto del curso mediante **una misión de rescate espacial une lanzamiento, encuentro y reserva para retorno**. El hilo de
seguridad consiste en reconocer a tiempo **consumir la reserva durante la aproximación y perder capacidad de regreso** y poder justificar la decisión
**presupuestar combustible y criterios de aborto para cada fase**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **propelentes ficticios → motores → guiado → trayectoria espacial**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Thunderbirds Vehicles](https://www.thunderbirds.com/) aporta referencia oficial de vehículos de rescate;
[Rockets Educator Guide](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf) se usa para propulsión, estabilidad y trayectoria. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Definir la necesidad:** convierte «intercepción de una nave averiada con ventana temporal corta» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **ascenso atmosférico frente a encuentro orbital** usando esos requisitos y la cadena **propelentes ficticios → motores → guiado → trayectoria espacial**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **consumir la reserva durante la aproximación y perder capacidad de regreso**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.

### Comprueba tu comprensión

1. ¿Qué característica de **trayectoria espacial** condiciona primero el caso «intercepción de una nave averiada con ventana temporal corta»?
2. ¿Qué requisito descartaría una de las alternativas **ascenso atmosférico frente a encuentro orbital**?
3. ¿Qué límite debe declararse junto con la variante elegida?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Thunderbird 3 mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [THUNDERBIRDS-OFFICIAL](https://www.thunderbirds.com/): Thunderbirds Vehicles, ITV. Uso: referencia oficial de vehículos de rescate.
- [NASA-ROCKETS](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf): Rockets Educator Guide, NASA. Uso: propulsión, estabilidad y trayectoria.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-thunderbird-3.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-thunderbird-3.md)
