# Repositorio Multisimulador de Mandos

[![Validar documentacion](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/validar-documentacion.yml/badge.svg)](https://github.com/vladimiracunadev-create/multi-piloto-navegacion/actions/workflows/validar-documentacion.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Repositorio documental para construir, paso a paso, una biblioteca de mandos, principios de funcionamiento, historia, reglamentos, manuales y criterios de simulacion para distintos tipos de maquinas.

El objetivo inicial no es crear juegos todavia. La prioridad es ordenar el conocimiento necesario para que, mas adelante, cada vehiculo pueda convertirse en una experiencia de simulacion coherente, educativa y segura.

## Alcance inicial

- Motos
- Automoviles
- Buses
- Gruas
- Barcos mercantes
- Acorazados
- Portaviones
- Submarinos
- Aviones pequenos
- Aviones de combate
- Naves espaciales
- Otros vehiculos futuros

## Principio de seguridad

Esta documentacion esta orientada a simulacion, formacion general e investigacion historica. No debe usarse como sustituto de entrenamiento certificado, licencias, manuales oficiales vigentes ni procedimientos reales de operacion. Para maquinas militares o de alto riesgo, el repositorio se limita a informacion publica, principios generales, historia, interfaz de simulacion y reglas de seguridad.

## Estructura

```text
multisimulador-mandos/
  README.md
  docs/
  plantillas/
  vehiculos/
    motos/
    automoviles/
    buses/
    gruas/
    barcos-mercantes/
    acorazados/
    portaviones/
    submarinos/
    aviones-pequenos/
    aviones-combate/
    naves-espaciales/
```

Cada tipo de vehiculo tiene las mismas secciones:

- `mandos`: controles, instrumentos, paneles y ergonomia.
- `manuales`: referencias publicas, resumenes y bibliografia.
- `historia`: evolucion historica y generaciones tecnologicas.
- `reglamentos`: normas, licencias, seguridad y restricciones.
- `operacion`: procedimientos generales de uso en simulacion.
- `simulacion`: modelo de juego/simulador, variables y niveles de realismo.
- `recursos`: imagenes, esquemas, enlaces, tablas y glosarios.

## Flujo de trabajo recomendado

1. Elegir un vehiculo.
2. Completar la ficha base desde `plantillas/ficha-vehiculo.md`.
3. Documentar los mandos principales.
4. Documentar principios fisicos y mecanicos.
5. Reunir fuentes publicas y manuales permitidos.
6. Resumir reglamentos y requisitos de seguridad.
7. Definir que debe simularse y que debe omitirse.
8. Crear una version educativa inicial.
9. Revisar con fuentes confiables.
10. Preparar el material para un futuro juego o simulador.

## Validacion y calidad

El repositorio se valida de forma automatica en cada cambio con el workflow
[`validar-documentacion.yml`](.github/workflows/validar-documentacion.yml), que
comprueba la estructura, los enlaces internos y el estilo de Markdown.

Para validar en local antes de subir cambios:

```bash
# Estructura del repositorio y enlaces internos
python scripts/validar_estructura.py

# Estilo de Markdown (requiere Node)
npx markdownlint-cli2 "**/*.md"
```

## Marco legal

El repositorio incluye un marco legal tecnico por tipo de vehiculo, centrado en
la normativa chilena e internacional, en
[`docs/07-marco-legal-chile.md`](docs/07-marco-legal-chile.md). Cada vehiculo
civil tiene ademas su propio archivo de reglamentos con la ley aplicable
(licencias, seguridad, documentos). Es material educativo, no asesoria legal.

## Como contribuir

Lee la [guia de contribucion](CONTRIBUTING.md) y el
[codigo de conducta](CODE_OF_CONDUCT.md). El historial de cambios esta en
[`CHANGELOG.md`](CHANGELOG.md) y el proyecto se distribuye bajo licencia
[MIT](LICENSE).

## Estado del proyecto

Estado actual: base documental creada y validada en CI. El vehiculo
[`motos`](vehiculos/motos/README.md) esta documentado como ejemplo de referencia
del formato esperado (mandos, operacion, historia, reglamentos y simulacion).

Siguiente paso sugerido: replicar ese nivel de detalle en `automoviles`, `buses`
y `gruas`, siguiendo el orden de [`docs/06-plan-vehiculos.md`](docs/06-plan-vehiculos.md).
