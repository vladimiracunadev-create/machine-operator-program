# Vehículos

Cada tipo de vehículo tiene su propia carpeta y se documenta como un **curso**
completo (ver [`docs/08-guia-de-estilo-y-curso.md`](../docs/08-guia-de-estilo-y-curso.md)),
conservando la misma estructura interna para facilitar comparación, crecimiento y
futura simulación.

## Estructura común

```text
vehiculo/
  README.md
  mandos/
  manuales/
  historia/
  reglamentos/
  operacion/
  simulacion/
  recursos/
```

## Cursos disponibles

Terrestres:

- 🏍️ [`motos`](motos/README.md)
- 🚗 [`automoviles`](automoviles/README.md)
- 🚌 [`buses`](buses/README.md)
- 🚛 [`camiones`](camiones/README.md)
- 🏗️ [`gruas`](gruas/README.md)
- 🚜 [`tractores`](tractores/README.md)
- 🚧 [`maquinaria-construccion`](maquinaria-construccion/README.md)

Marítimos:

- 🚢 [`barcos-mercantes`](barcos-mercantes/README.md)
- ⛴️ [`cruceros`](cruceros/README.md)
- 🛡️ [`acorazados`](acorazados/README.md)
- 🛳️ [`portaviones`](portaviones/README.md)
- 🌊 [`submarinos`](submarinos/README.md)

Aéreos y espaciales:

- 🛩️ [`aviones-pequenos`](aviones-pequenos/README.md)
- 🛫 [`aviones-pasajeros`](aviones-pasajeros/README.md)
- ✈️ [`aviones-combate`](aviones-combate/README.md)
- 🚀 [`naves-espaciales`](naves-espaciales/README.md)

## Regla de trabajo

Antes de crear un prototipo jugable, cada vehículo debe tener al menos:

- ficha general;
- manual de mandos;
- principios de funcionamiento;
- historia resumida;
- reglamentos principales;
- diseño de simulación;
- fuentes registradas.
