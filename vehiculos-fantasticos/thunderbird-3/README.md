# 🚀 Curso: Thunderbird 3

[🏠 Inicio](../../README.md) · [🌌 Naves de ficcion](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

---

> Curso de analisis educativo de ciencia ficcion inspirado en el estilo
> "Thunderbirds". Estudiamos un cohete de rescate generico para entender la
> fisica real del ascenso al espacio: por que llegar a orbita no es solo subir,
> sino alcanzar una enorme velocidad lateral, y por que el combustible manda.

![Tipo](https://img.shields.io/badge/tipo-ficcion-purple)
![Modulos](https://img.shields.io/badge/modulos-9-blue)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar por que llegar al espacio exige velocidad orbital lateral, no solo altura.
- Entender el papel de la gravedad y del aire durante el ascenso de un cohete.
- Describir por que conviene soltar masa vacia con cohetes de varias etapas.
- Razonar sobre la ecuacion del cohete y el crecimiento exponencial del combustible.
- Distinguir que evoca la ficcion que seria real y que rompe la fisica.
- Traducir todo lo anterior a variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Combustible[⛽ Deposito de propelente] --> Motor[🚀 Motor principal]
    Motor --> Empuje[Empuje hacia arriba]
    Empuje --> Ascenso[Ascenso contra la gravedad]
    Ascenso --> Giro[Inclinar hacia la horizontal]
    Giro --> Orbita[Ganar velocidad lateral]
    Etapas[🪜 Etapas] --> Suelta[Soltar masa vacia]
    Suelta --> Motor
    Piloto[🧑 Tripulacion] --> Guiado[🎛️ Guiado del ascenso]
    Guiado --> Motor
    Guiado --> Etapas
    Sensores[📡 Sensores] -. informan .-> Piloto
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Contexto de la nave de ficcion y su idea de vuelo. | [Abrir](historia/historia-thunderbird-3.md) |
| 2 | 📋 Caracteristicas | Que es un cohete de rescate generico y para que sirve. | [Abrir](operacion/caracteristicas-thunderbird-3.md) |
| 3 | 🔧 Sistemas mecanicos | Tecnologia imaginaria frente a la fisica real. | [Abrir](operacion/sistemas-mecanicos-thunderbird-3.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto de mando conceptual y controles. | [Abrir](mandos/manual-mandos-thunderbird-3.md) |
| 5 | 🧪 Principios y operacion | Ascenso, etapas y ecuacion del cohete: que si y que no. | [Abrir](operacion/principios-thunderbird-3.md) |
| 6 | 🌍 Entornos | Rampa, atmosfera baja, atmosfera alta y orbita. | [Abrir](operacion/entornos-thunderbird-3.md) |
| 7 | ⚖️ Reglas del universo | Las leyes internas de la ficcion frente a la fisica. | [Abrir](reglamentos/reglas-universo-thunderbird-3.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modo ciencia o ficcion. | [Abrir](simulacion/diseno-simulador-thunderbird-3.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-thunderbird-3.md) |

---

## 🧩 Requisitos previos

Ninguno formal. Ayuda tener nociones basicas de las leyes de Newton, pero el
curso las explica desde cero. La idea central es simple y potente: para quedarse
en el espacio no basta con subir muy alto, hay que moverse tan rapido de lado
que la caida hacia el planeta se convierta en una orbita estable.

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-thunderbird-3.md)
