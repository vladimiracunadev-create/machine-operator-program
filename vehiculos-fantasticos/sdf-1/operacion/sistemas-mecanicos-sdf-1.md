<!-- clase-meta
tipo_documento: clase
clase: 4
codigo: SDF1-04
curso: sdf-1
titulo: "Sistemas mecánicos del SDF-1"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: SDF1-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Escala: la ley del cubo-cuadrado, Estructura y esfuerzos, Propulsión a escala gigante y Energía y habitabilidad con vocabulario propio de SDF-1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de SDF-1."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# 🔧 Sistemas mecánicos del SDF-1

[🏠 Inicio](../../../README.md) · [🏯 Curso: SDF-1](../README.md) · 🔧 Sistemas mecánicos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Esta clase abre la nave-fortaleza por dentro. Compara la tecnología imaginaria
de la ficción con la física real que la haría funcionar (o que la desmiente). La
regla del curso es clara: describimos conceptos con nuestras palabras, sin
copiar planos ni especificaciones oficiales.

```mermaid
flowchart LR
    subgraph Escala
        Tam[Tamaño gigante] --> Vol[Volumen al cubo]
        Vol --> Masa[Masa enorme]
    end
    subgraph Estructura
        Masa --> Esq[Esqueleto interno]
        Esq --> Esf[Esfuerzos por peso propio]
    end
    subgraph Movimiento
        Energia[Planta de energía] --> Motores[Motores gigantes]
        Motores --> Empuje[Empuje]
        Masa --> Empuje
    end
    Empuje --> Acel[Aceleración muy pequeña]
```

---

## 1. 📏 Escala: la ley del cubo-cuadrado

Aquí está la clave del curso. Cuando agrandas una nave manteniendo su forma, su
superficie crece con el cuadrado del tamaño, pero su volumen (y por tanto su
masa) crece con el cubo. Si duplicas cada dimensión, la superficie se multiplica
por cuatro, pero la masa por ocho. Por eso una nave gigante pesa muchísimo más de
lo que "parece" a simple vista, y toda su estructura tiene que soportar ese peso.

```mermaid
flowchart LR
    Doble[Doblar el tamaño] --> Sup[Superficie x4]
    Doble --> Vol[Volumen x8]
    Vol --> Peso[Masa x8]
    Sup --> Aguante[Lo que aguanta crece menos]
    Peso --> Aguante
    Aguante --> Problema[El peso propio se vuelve el gran problema]
```

| Concepto de ficción | Física real que evoca | Veredicto |
| --- | --- | --- |
| "Es como una nave normal pero enorme" | Escalado geométrico | No: la masa crece al cubo, cambia todo. |
| Estructura que no se dobla | Resistencia de materiales | Muy exigente: el peso propio la castiga. |
| Se mueve como un bloque sólido | Rigidez estructural | A esa escala flexionaria y crujiría. |

---

## 2. 🧱 Estructura y esfuerzos

La superficie de las columnas y vigas es la que aguanta el peso, pero esa
superficie crece con el cuadrado mientras la masa crece con el cubo. Resultado:
cuanto más grande es la nave, más sobrecargada está su estructura por su propio
peso. En un planeta esto sería casi imposible; en el vacío no hay gravedad
externa que la aplaste, pero cualquier maniobra o empuje genera esfuerzos que la
estructura debe repartir sin romperse.

| Idea de la ficción | Que dice la física real |
| --- | --- |
| El casco se mueve rígido y perfecto | A gran escala la estructura flexiona y vibra. |
| Basta con hacer las paredes más gruesas | Más grosor añade más masa; el problema se agrava. |
| Aguanta cualquier maniobra brusca | Las aceleraciones bruscas generarían esfuerzos enormes. |
| El peso propio no importa en el espacio | Sin gravedad no aplasta, pero el empuje si genera cargas. |

---

## 3. 🚀 Propulsión a escala gigante

Mover una masa colosal exige un empuje colosal. Como la aceleración es el empuje
dividido por la masa, una nave gigantesca acelera muy despacio aunque tenga
motores enormes. En la ficción la fortaleza maniobra casi como una nave pequeña;
en la realidad, cambiar su velocidad o su rumbo llevaría mucho tiempo y un gasto
descomunal de propelente.

```mermaid
flowchart TD
    Motores[Motores gigantes] --> Empuje[Empuje enorme]
    Masa[Masa colosal] --> Acel[Aceleración]
    Empuje --> Acel
    Acel --> Lenta[Aun así, aceleración pequeña]
    Lenta --> Tiempo[Maniobrar lleva mucho tiempo]
```

- **Empuje frente a masa**: por muy potentes que sean los motores, la masa manda.
- **Maniobra lenta**: girar o frenar una mole exige tiempo y planificación.
- **Propelente**: mover tanta masa consume cantidades enormes de propelente.

---

## 4. 🔋 Energía y habitabilidad

Una nave-ciudad necesita energía no solo para moverse, sino para mantener con
vida a miles de personas: aire, agua, temperatura, luz y reciclaje. En la ficción
todo funciona sin explicación. En la realidad, ese soporte vital a gran escala
es un sistema tan complejo como la propia propulsión, y cada parte añade más masa
que a su vez exige más estructura y más empuje.

| Sistema | En la ficción | En la realidad |
| --- | --- | --- |
| Energía | Fuente casi infinita | Planta enorme y con límites de calor. |
| Soporte vital | Funciona sin más | Aire, agua y temperatura para miles de personas. |
| Reciclaje | Invisible | Imprescindible para la autonomía real. |

---

## 5. 🌡️ Calor a gran escala

Cuanto más grande y poblada es la nave, más calor genera por dentro. Y en el
vacío el calor solo se puede expulsar por radiación, a través de la superficie.
Pero la superficie crece con el cuadrado y el volumen con el cubo: una nave
gigante genera mucho más calor del que su superficie puede disipar con facilidad.
Refrigerar un gigante es, otra vez, un problema de escala.

| Elemento | Función en la ficción | Función útil real |
| --- | --- | --- |
| Paneles del casco | Estética y blindaje | Radiadores para expulsar calor. |
| Interior gigante | Espacio habitable | Fuente de mucho calor que hay que evacuar. |
| Superficie externa | Aspecto imponente | Única vía de disipación en el vacío. |

---

## 🔁 Cómo se conecta todo

1. La **escala** dispara la masa según la ley del cubo-cuadrado.
2. La **estructura** debe soportar el peso propio y los esfuerzos de maniobra.
3. La **propulsión** lucha contra una masa colosal: acelera despacio.
4. La **energía y el soporte vital** mantienen viva a la nave-ciudad.
5. El **calor** interno cuesta cada vez más de disipar al crecer la nave.

Con esto claro, el [Clase 5: Mandos](../mandos/manual-mandos-sdf-1.md)
muestra cómo se operaría una nave de este tamaño.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Escala: la ley del cubo-cuadrado, Estructura y esfuerzos, Propulsión a escala gigante y Energía y habitabilidad** a **seguir una alteración desde energía ficticia hasta nave y población durante transformación simulada mientras algunos sistemas están degradados**?

### Explicación razonada

El funcionamiento puede leerse como una cadena causal: energía ficticia entrega o transforma energía; propulsión la adapta; transformación estructural la transmite o gobierna; y nave y población produce el efecto observable. La cadena no es lineal en sentido estricto: sensores, estructura y operador cierran el lazo. Si un eslabón se degrada, la señal importante es cómo cambia el estado de nave y población y qué margen queda.

```mermaid
flowchart LR
    A["energía ficticia"] --> B["propulsión"] --> C["transformación estructural"] --> D["nave y población"]
    D -. respuesta observable .-> O["operador o control"]
    O -. orden y verificación .-> A
```

Esta clase se conecta con el resto del curso mediante **una nave-ciudad combina movilidad, transformación y continuidad de servicios**. El hilo de
seguridad consiste en reconocer a tiempo **tratar la transformación como efecto visual sin impactos en energía, estructura y habitabilidad** y poder justificar la decisión
**secuenciar transición, aislar servicios y representar costos operativos**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **energía ficticia → propulsión → transformación estructural → nave y población**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Robotech](https://robotech.com/) aporta referencia oficial del universo ficticio;
[Spaceships and Rockets](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/) se usa para naves, sistemas y misiones. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Entrada:** identifica el estado inicial de **energía ficticia** durante **transformación simulada mientras algunos sistemas están degradados**.
2. **Transformación:** explica qué hacen **propulsión** y **transformación estructural**, y qué magnitud cambia en cada paso.
3. **Salida:** comprueba el efecto esperado en **nave y población** y busca una desviación temprana.
4. **Falla razonada:** si aparece **tratar la transformación como efecto visual sin impactos en energía, estructura y habitabilidad**, retrocede por la cadena antes de ordenar otra acción.

### Comprueba tu comprensión

1. Si se degrada **propulsión**, ¿qué efecto esperarías primero en **transformación estructural** y después en **nave y población**?
2. ¿Qué observación ayudaría a diferenciar una falla de **energía ficticia** de una falla de **transformación estructural**?
3. ¿Por qué una segunda orden podría agravar **tratar la transformación como efecto visual sin impactos en energía, estructura y habitabilidad**?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de SDF-1 que conecte Escala: la ley del cubo-cuadrado, Estructura y esfuerzos, Propulsión a escala gigante y Energía y habitabilidad; después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [ROBOTECH-OFFICIAL](https://robotech.com/): Robotech, Harmony Gold. Uso: referencia oficial del universo ficticio.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-sdf-1.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-sdf-1.md)
