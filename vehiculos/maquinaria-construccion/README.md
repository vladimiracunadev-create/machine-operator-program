# 🚧 Curso: Maquinaria de construcción

[🏠 Inicio](../../README.md) · [🚙 Catálogo de vehículos](../README.md) · [🎓 Guía de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso completo de la maquinaria de construcción.** Documenta las máquinas de
> movimiento de tierra de principio a fin: historia, características, mecánica e
> hidráulica en profundidad, mandos, física de la estabilidad y las cargas,
> entornos, reglamentos chilenos y diseño de simulación. El núcleo del curso es
> la hidráulica de trabajo, el movimiento de tierra y la estabilidad.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Módulos](https://img.shields.io/badge/modulos-9-blue)
![Licencia Chile](https://img.shields.io/badge/licencia-Clase%20D-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar como una máquina de construcción excava, empuja y carga material.
- Identificar sus sistemas, en especial la hidráulica de trabajo.
- Distinguir el trabajo con brazo y cucharón del trabajo con hoja empujadora.
- Comparar orugas y neumáticos y su efecto en agarre y estabilidad.
- Comprender la estabilidad, las cargas y el límite de vuelco.
- Conocer los reglamentos chilenos aplicables (licencia clase D, seguridad).
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehículo

```mermaid
flowchart TD
    Diesel[⛽ Motor diesel] --> Bomba[Bomba hidráulica]
    Bomba --> Valvulas[Válvulas de control]
    Valvulas --> Brazo[Cilindros del brazo]
    Valvulas --> Cucharon[Cilindro del cucharón]
    Valvulas --> Giro[Motor de giro]
    Valvulas --> Traslacion[Motores de traslación]
    Brazo --> Herramienta[Cucharón u hoja]
    Traslacion --> Orugas[Orugas o neumáticos]
    Estabilidad[⚖️ Base y contrapeso] --> Vuelco[Límite de vuelco]
    Mandos[🎛️ Joysticks] --> Valvulas
    Tablero[📊 Tablero] -. informa .-> Operador[🧍 Operador]
    Operador --> Mandos
```

---

## 📚 Módulos del curso

| # | Módulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y evolución de la maquinaria, línea de tiempo. | [Abrir](historia/historia-maquinaria.md) |
| 2 | 📋 Características | Que es, tipos de máquina y para que sirve cada uno. | [Abrir](operacion/caracteristicas-maquinaria.md) |
| 3 | 🔧 Sistemas mecánicos | Hidráulica, movimiento de tierra, brazo, hoja, orugas, estabilidad. | [Abrir](operacion/sistemas-mecanicos-maquinaria.md) |
| 4 | 🎛️ Mandos e instrumentos | Cabina, joysticks, pedales y tablero. | [Abrir](mandos/manual-mandos-maquinaria.md) |
| 5 | 🧪 Principios y operación | Cargas, estabilidad y fases de trabajo. | [Abrir](operacion/principios-maquinaria.md) |
| 6 | 🌍 Entornos de trabajo | Obra, minería, vialidad, demolición y zanjas. | [Abrir](operacion/entornos-maquinaria.md) |
| 7 | ⚖️ Reglamentos | Ley chilena: licencia clase D, seguridad de faena. | [Abrir](reglamentos/reglamentos-maquinaria.md) |
| 8 | 🎮 Diseño de simulación | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-maquinaria.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-maquinaria.md) |

---

## 🧩 Requisitos previos

Se recomienda haber revisado antes el [curso de grúas](../gruas/README.md), que
introduce la hidráulica de trabajo y la estabilidad frente al vuelco. La
maquinaria de construcción comparte esos principios y agrega el movimiento de
tierra con brazo, cucharón y hoja. Marco legal común en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Módulo 1: Historia](historia/historia-maquinaria.md)
