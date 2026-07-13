<div align="center">

# 🎮 Multisimulador de Mandos y Navegacion

**Una biblioteca de cursos tecnicos para pilotar, conducir y navegar cualquier maquina.**

[![Validar documentacion](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/validar-documentacion.yml/badge.svg)](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/validar-documentacion.yml)
[![Verificar enlaces](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/enlaces.yml/badge.svg)](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/enlaces.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Vehiculos](https://img.shields.io/badge/vehiculos-11-blue)
![Enfoque](https://img.shields.io/badge/enfoque-educativo%20y%20seguro-green)

</div>

---

Cada tipo de maquina se documenta como un **curso completo e interconectado**:
historia, caracteristicas funcionales, mecanica en profundidad, mandos,
principios fisicos, entornos de trabajo, reglamentos (con foco en la ley chilena)
y diseno de simulacion. La meta no es todavia crear juegos, sino ordenar el
conocimiento para que cada vehiculo pueda convertirse en una simulacion
coherente, educativa y segura.

> 🎓 **Empieza por el curso de referencia:** [🏍️ Motocicletas](vehiculos/motos/README.md)
> · o revisa la [guia de estilo y estructura de curso](docs/08-guia-de-estilo-y-curso.md).

---

## 🗺️ Mapa del repositorio

```mermaid
flowchart TD
    Repo[🎮 Multisimulador] --> Docs[📖 docs/<br/>vision, metodologia, marco legal]
    Repo --> Plant[🧩 plantillas/<br/>modelos reutilizables]
    Repo --> Veh[🚙 vehiculos/<br/>11 cursos]
    Repo --> Man[📚 manuales/<br/>fuentes publicas]
    Veh --> Tierra[🛞 Terrestres]
    Veh --> Mar[⚓ Maritimos]
    Veh --> Aire[✈️ Aereos]
    Veh --> Espacio[🚀 Espaciales]
    Tierra --> T1[🏍️ Motos · 🚗 Autos · 🚌 Buses · 🏗️ Gruas]
    Mar --> M1[🚢 Mercantes · 🛡️ Acorazados · 🛳️ Portaviones · 🌊 Submarinos]
    Aire --> A1[🛩️ Avionetas · ✈️ Combate]
    Espacio --> E1[🚀 Naves espaciales]
```

---

## 📚 Catalogo de cursos

Cada vehiculo es un curso con 9 modulos (ver
[guia de curso](docs/08-guia-de-estilo-y-curso.md)).

### 🛞 Terrestres

| Curso | Descripcion | Licencia (Chile) |
| --- | --- | --- |
| [🏍️ Motocicletas](vehiculos/motos/README.md) | Equilibrio, transmision y dinamica de dos ruedas. | Clase C |
| [🚗 Automoviles](vehiculos/automoviles/README.md) | Direccion, motor, seguridad y transito. | Clase B |
| [🚌 Buses](vehiculos/buses/README.md) | Transporte de pasajeros y operacion profesional. | Clase A-3 |
| [🏗️ Gruas](vehiculos/gruas/README.md) | Maquinaria automotriz, izaje y estabilidad. | Clase D |

### ⚓ Maritimos

| Curso | Descripcion | Marco |
| --- | --- | --- |
| [🚢 Barcos mercantes](vehiculos/barcos-mercantes/README.md) | Propulsion naval, gobierno y navegacion. | DIRECTEMAR / OMI |
| [🛡️ Acorazados](vehiculos/acorazados/README.md) | Historia y principios (marco publico). | Armada / CONVEMAR |
| [🛳️ Portaviones](vehiculos/portaviones/README.md) | Aviacion naval e historia (marco publico). | Armada / CONVEMAR |
| [🌊 Submarinos](vehiculos/submarinos/README.md) | Flotabilidad e inmersion (marco publico). | Armada / CONVEMAR |

### ✈️ Aereos y 🚀 espaciales

| Curso | Descripcion | Marco |
| --- | --- | --- |
| [🛩️ Aviones pequenos](vehiculos/aviones-pequenos/README.md) | Sustentacion, instrumentos y navegacion aerea. | DGAC / OACI |
| [✈️ Aviones de combate](vehiculos/aviones-combate/README.md) | Fisica del vuelo e historia (marco publico). | FACH |
| [🚀 Naves espaciales](vehiculos/naves-espaciales/README.md) | Orbitas, propulsion y soporte vital. | Tratados UNOOSA |

---

## 🧭 Ruta de aprendizaje sugerida

```mermaid
flowchart LR
    F1[🛞 Fase 1<br/>Tierra] --> F2[⚓ Fase 2<br/>Mar]
    F2 --> F3[✈️ Fase 3<br/>Aire]
    F3 --> F4[🚀 Fase 4<br/>Espacio]
```

De lo cotidiano a lo complejo. Detalle en
[`docs/06-plan-vehiculos.md`](docs/06-plan-vehiculos.md).

---

## 📖 Documentacion general

| Documento | Contenido |
| --- | --- |
| [📌 Indice maestro](docs/00-indice-maestro.md) | Mapa de todo el repositorio. |
| [🎯 Vision del proyecto](docs/01-vision-del-proyecto.md) | Alcance y filosofia. |
| [🔬 Metodologia documental](docs/02-metodologia-documental.md) | Como investigar y redactar. |
| [🎚️ Niveles de realismo](docs/03-niveles-de-realismo.md) | De arcade educativo a simulacion tecnica. |
| [🦺 Seguridad y limites](docs/04-seguridad-y-limites.md) | Reglas de contenido responsable. |
| [📖 Glosario general](docs/05-glosario-general.md) | Vocabulario comun. |
| [🗓️ Plan de vehiculos](docs/06-plan-vehiculos.md) | Orden recomendado. |
| [⚖️ Marco legal (Chile)](docs/07-marco-legal-chile.md) | Normativa por tipo de vehiculo. |
| [🎓 Guia de estilo y curso](docs/08-guia-de-estilo-y-curso.md) | Iconografia, modulos y navegacion. |

---

## 🦺 Principio de seguridad

Documentacion orientada a **simulacion, formacion general e investigacion
historica**. No sustituye entrenamiento certificado, licencias ni manuales
oficiales vigentes. Para maquinas militares o de alto riesgo, el repositorio se
limita a informacion publica, principios generales, historia e interfaz de
simulacion. Ver [`docs/04-seguridad-y-limites.md`](docs/04-seguridad-y-limites.md).

---

## ✅ Validacion y calidad

Cada cambio se valida en CI (estructura, enlaces internos, estilo Markdown y
seguridad de los workflows). Para validar en local:

```bash
# Estructura del repositorio y enlaces internos
python scripts/validar_estructura.py

# Estilo de Markdown (requiere Node)
npx markdownlint-cli2 "**/*.md"
```

---

## 🤝 Como contribuir

Lee la [guia de contribucion](CONTRIBUTING.md) y el
[codigo de conducta](CODE_OF_CONDUCT.md). El historial esta en
[`CHANGELOG.md`](CHANGELOG.md); la seguridad, en [`SECURITY.md`](SECURITY.md). El
proyecto se distribuye bajo licencia [MIT](LICENSE).

## 📊 Estado del proyecto

- ✅ Base documental, marco legal y CI en verde.
- ✅ [🏍️ Motos](vehiculos/motos/README.md): **curso completo** de referencia (9 modulos con diagramas).
- 🚧 Resto de vehiculos: portada de curso, reglamentos y modulos base; en ampliacion progresiva.
