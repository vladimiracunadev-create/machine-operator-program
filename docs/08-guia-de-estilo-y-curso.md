# 🎓 Guía de estilo y estructura de curso

[⬅️ Volver al índice](00-indice-maestro.md) · [🏠 README](../README.md)

Cada vehículo del repositorio se documenta como un **curso completo**: no es una
ficha suelta, sino un itinerario de aprendizaje conectado que va de la historia a
la simulación, pasando por la mecánica profunda, los mandos, los entornos de
trabajo y los reglamentos. Esta guía define cómo se ve y cómo se conecta ese
curso para que todos sean coherentes.

---

## 🧭 Filosofía: un curso por vehículo

Igual que un piloto estudia un programa completo antes de volar, cada vehículo
tiene su **programa de curso**. El objetivo es que quien lea una carpeta de
vehículo pueda aprenderlo de principio a fin, con material interconectado.

```mermaid
flowchart LR
    H[📜 Historia] --> C[📋 Características]
    C --> S[🔧 Sistemas mecánicos]
    S --> M[🎛️ Mandos e instrumentos]
    M --> P[🧪 Principios y operación]
    P --> E[🌍 Entornos de trabajo]
    E --> R[⚖️ Reglamentos]
    R --> D[🎮 Diseño de simulación]
    D --> X[🧰 Recursos y glosario]
```

---

## 🎨 Iconografía

Iconos fijos para mantener una identidad visual consistente.

### Vehículos

| Vehículo | Icono | Vehículo | Icono |
| --- | :---: | --- | :---: |
| Motos | 🏍️ | Submarinos | 🌊 |
| Automóviles | 🚗 | Aviones pequeños | 🛩️ |
| Buses | 🚌 | Aviones de combate | ✈️ |
| Grúas | 🏗️ | Naves espaciales | 🚀 |
| Barcos mercantes | 🚢 | Acorazados | 🛡️ |
| Portaviones | 🛳️ | | |

### Secciones y módulos

| Módulo | Icono | Módulo | Icono |
| --- | :---: | --- | :---: |
| Historia | 📜 | Entornos de trabajo | 🌍 |
| Características funcionales | 📋 | Reglamentos | ⚖️ |
| Sistemas mecánicos | 🔧 | Diseño de simulación | 🎮 |
| Mandos e instrumentos | 🎛️ | Recursos | 🧰 |
| Principios y operación | 🧪 | Objetivos de aprendizaje | 🎯 |
| Manuales y fuentes | 📚 | Seguridad | 🦺 |

---

## 🗂️ Estructura de archivos de un curso

Dentro de `vehiculos/<vehiculo>/` cada curso usa estos archivos:

```text
<vehiculo>/
  README.md                              # 🎓 Portada del curso (indice + diagrama)
  historia/historia-<v>.md               # 📜 Modulo 1
  operacion/caracteristicas-<v>.md       # 📋 Modulo 2
  operacion/sistemas-mecanicos-<v>.md    # 🔧 Modulo 3
  mandos/manual-mandos-<v>.md            # 🎛️ Modulo 4
  operacion/principios-<v>.md            # 🧪 Modulo 5
  operacion/entornos-<v>.md              # 🌍 Modulo 6
  reglamentos/reglamentos-<v>.md         # ⚖️ Modulo 7
  simulacion/diseno-simulador-<v>.md     # 🎮 Modulo 8
  recursos/recursos-<v>.md               # 🧰 Modulo 9 (glosario + enlaces)
```

---

## 🔗 Navegación e interconexion

La documentación **profesional se conecta**. Reglas:

1. **Breadcrumb superior** en cada archivo, en la primera línea útil:

   ```markdown
   [🏠 Inicio](../../../README.md) · [🏍️ Curso: Motos](../README.md) · 🔧 Sistemas mecanicos
   ```

2. **Portada del curso** (`README.md` del vehículo): tabla de módulos con icono,
   enlace y una línea de descripción, más un diagrama Mermaid del vehículo o su
   itinerario.

3. **Pie "Continuar"** al final de cada módulo, enlazando al anterior y al
   siguiente:

   ```markdown
   ---
   [⬅️ Anterior: Caracteristicas](caracteristicas-motos.md) ·
   [➡️ Siguiente: Mandos](../mandos/manual-mandos-motos.md)
   ```

4. **Enlaces cruzados** hacia el marco legal común
   ([`docs/07-marco-legal-chile.md`](07-marco-legal-chile.md)) y hacia
   [`manuales/fuentes.md`](../manuales/fuentes.md) cuando se cite una norma o
   fuente.

---

## 📊 Diagramas con Mermaid

GitHub renderiza Mermaid de forma nativa. Usalo para explicar sistemas y flujos.

- **Sistemas**: `flowchart` para mostrar cómo se relacionan componentes.
- **Estados**: `stateDiagram-v2` para modos de operación (apagado, en marcha...).
- **Itinerario**: `flowchart LR` para la ruta del curso.
- **Tiempo**: `timeline` para hitos históricos.

Ejemplo de diagrama de sistemas:

```mermaid
flowchart TD
    Energia[Energía / combustible] --> Motor
    Motor --> Transmision
    Transmision --> Ruedas
    Mandos --> Motor
    Mandos --> Frenos
    Frenos --> Ruedas
    Instrumentos -. informan .-> Conductor
    Conductor --> Mandos
```

---

## ✅ Checklist de curso profesional

Un curso de vehículo está "completo" cuando:

- [ ] 🎓 Portada con diagrama y tabla de módulos enlazada.
- [ ] 📜 Historia con línea de tiempo.
- [ ] 📋 Características funcionales y tipos.
- [ ] 🔧 Sistemas mecánicos con al menos un diagrama.
- [ ] 🎛️ Mandos e instrumentos en tablas.
- [ ] 🧪 Principios físicos y operación.
- [ ] 🌍 Entornos de trabajo.
- [ ] ⚖️ Reglamentos enlazados al marco legal.
- [ ] 🎮 Diseño de simulación con variables.
- [ ] 🧰 Recursos, glosario y fuentes registradas.
- [ ] 🔗 Breadcrumb y navegación anterior/siguiente en cada módulo.

---

[⬅️ Volver al índice](00-indice-maestro.md) · [🏍️ Ver el curso de referencia: Motos](../vehiculos/motos/README.md)
