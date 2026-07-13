# ⚡ Curso: Thunderbird 1

[🏠 Inicio](../../README.md) · [🌌 Naves de ficcion](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

---

> Curso de analisis educativo de ciencia ficcion inspirado en el estilo
> "Thunderbirds". Estudiamos un vehiculo de respuesta rapida generico para
> entender la fisica real del despegue y aterrizaje vertical (VTOL), el empuje
> vectorizado y el compromiso entre velocidad y autonomia.

![Tipo](https://img.shields.io/badge/tipo-ficcion-purple)
![Modulos](https://img.shields.io/badge/modulos-9-blue)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar el despegue y aterrizaje vertical por empuje directo hacia abajo.
- Distinguir la sustentacion por empuje directo de la sustentacion aerodinamica.
- Describir el empuje vectorizado y la transicion de vuelo vertical a horizontal.
- Razonar sobre la relacion empuje/peso mayor que uno como condicion del VTOL.
- Entender el compromiso entre velocidad, empuje, consumo y autonomia.
- Traducir todo lo anterior a variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Energia[🔋 Fuente de energia] --> Motor[🚀 Motor de empuje]
    Motor --> Vertical[Empuje directo hacia abajo]
    Motor --> Toberas[🎯 Toberas vectorizadas]
    Vertical --> Despegue[Despegue y aterrizaje vertical]
    Toberas --> Transicion[Transicion a vuelo horizontal]
    Piloto[🧑 Piloto] --> Mandos[🎛️ Mandos]
    Mandos --> Motor
    Mandos --> Toberas
    Sensores[📡 Sensores] -. informan .-> Piloto
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Contexto de la nave de ficcion y su idea de vuelo. | [Abrir](historia/historia-thunderbird-1.md) |
| 2 | 📋 Caracteristicas | Que es un vehiculo de respuesta rapida y para que sirve. | [Abrir](operacion/caracteristicas-thunderbird-1.md) |
| 3 | 🔧 Sistemas mecanicos | Tecnologia imaginaria frente a la fisica real. | [Abrir](operacion/sistemas-mecanicos-thunderbird-1.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de mando conceptual y controles. | [Abrir](mandos/manual-mandos-thunderbird-1.md) |
| 5 | 🧪 Principios y operacion | VTOL y empuje vectorizado: que si, que no y por que. | [Abrir](operacion/principios-thunderbird-1.md) |
| 6 | 🌍 Entornos | Base, atmosfera y escenarios de respuesta rapida. | [Abrir](operacion/entornos-thunderbird-1.md) |
| 7 | ⚖️ Reglas del universo | Las leyes internas de la ficcion frente a la fisica. | [Abrir](reglamentos/reglas-universo-thunderbird-1.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modo ciencia o ficcion. | [Abrir](simulacion/diseno-simulador-thunderbird-1.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-thunderbird-1.md) |

---

## 🧩 Requisitos previos

Ninguno formal. Ayuda tener nociones basicas de fuerzas y peso, pero el curso
las explica desde cero. La idea central es simple y potente: para elevarse en
vertical una nave debe empujar hacia abajo con mas fuerza que su propio peso, y
esa forma de volar es muy distinta de la de un avion que se apoya en sus alas.

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-thunderbird-1.md)
