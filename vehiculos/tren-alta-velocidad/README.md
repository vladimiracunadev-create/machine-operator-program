# 🚄 Curso: Tren de alta velocidad

[🏠 Inicio](../../README.md) · [🚙 Catalogo de vehiculos](../README.md) · [🎓 Guia de curso](../../docs/08-guia-de-estilo-y-curso.md)

> **Curso del tren de alta velocidad.** Documenta el tren de gran velocidad de
> principio a fin: historia mundial (Shinkansen, TGV, AVE), caracteristicas,
> mecanica en profundidad, mandos de cabina, fisica, entornos, marco ferroviario
> y diseno de simulacion. Enfoque general e internacional; Chile aun no cuenta
> con alta velocidad comercial.

![Nivel](https://img.shields.io/badge/nivel-avanzado-red)
![Modulos](https://img.shields.io/badge/modulos-9-blue)
![Marco legal](https://img.shields.io/badge/marco-ferroviario-orange)

---

## 🎯 Objetivos de aprendizaje

Al terminar este curso deberias poder:

- Explicar que es un tren de alta velocidad y como acelera, frena y se mantiene estable a mas de 250 km/h.
- Distinguir la traccion distribuida (EMU) de la concentrada (locomotora en cabeza).
- Identificar sus sistemas mecanicos y como se conectan.
- Comprender el dominio de la resistencia aerodinamica y la enorme energia cinetica.
- Reconocer los mandos de cabina y la senalizacion embarcada ETCS/ERTMS.
- Conocer el marco ferroviario de referencia y marcar lo no confirmado en Chile.
- Traducir todo lo anterior en variables de un simulador educativo.

---

## 🗺️ Mapa del vehiculo

```mermaid
flowchart TD
    Catenaria[⚡ Catenaria alta tension] --> Pantografo[Pantografo]
    Pantografo --> Transformador[Transformador y traccion]
    Transformador --> Motores[Motores repartidos EMU]
    Motores --> Bogies[Bogies motores]
    Bogies --> Ruedas[Ruedas de pestana]
    Ruedas --> Riel[Riel de via dedicada]
    Manipulador[🎛️ Manipulador] --> Traccion[Traccion / freno]
    Traccion --> Motores
    Traccion --> Frenos[Frenos de gran masa]
    Frenos --> Ruedas
    DMI[📊 DMI ETCS] -. informa .-> Maquinista[🧍 Maquinista]
    Maquinista --> Manipulador
```

---

## 📚 Modulos del curso

| # | Modulo | Contenido | Enlace |
| :-: | --- | --- | --- |
| 1 | 📜 Historia | Origen y expansion mundial de la alta velocidad, linea de tiempo. | [Abrir](historia/historia-tren-alta-velocidad.md) |
| 2 | 📋 Caracteristicas | Que es, traccion distribuida vs concentrada, tipos y usos. | [Abrir](operacion/caracteristicas-tren-alta-velocidad.md) |
| 3 | 🔧 Sistemas mecanicos | Traccion electrica, bogies, frenado, aerodinamica, via dedicada, senalizacion. | [Abrir](operacion/sistemas-mecanicos-tren-alta-velocidad.md) |
| 4 | 🎛️ Mandos e instrumentos | Puesto del maquinista, manipulador y pantalla de senalizacion. | [Abrir](mandos/manual-mandos-tren-alta-velocidad.md) |
| 5 | 🧪 Principios y operacion | Energia cinetica, frenado en km y estabilidad a alta velocidad. | [Abrir](operacion/principios-tren-alta-velocidad.md) |
| 6 | 🌍 Entornos de trabajo | Corredores de alta velocidad, tuneles, viaductos, estaciones. | [Abrir](operacion/entornos-tren-alta-velocidad.md) |
| 7 | ⚖️ Reglamentos | Marco ferroviario: Ley General de Ferrocarriles, EFE, MTT. | [Abrir](reglamentos/reglamentos-tren-alta-velocidad.md) |
| 8 | 🎮 Diseno de simulacion | Variables, ciclo y modos de juego. | [Abrir](simulacion/diseno-simulador-tren-alta-velocidad.md) |
| 9 | 🧰 Recursos | Glosario, enlaces y diagramas. | [Abrir](recursos/recursos-tren-alta-velocidad.md) |

---

## 🧩 Requisitos previos

Se recomienda haber revisado antes el curso de motos como base de aceleracion,
frenado y transmision, y conviene entender la gestion de gran masa vista en el
curso de camiones o buses. El tren de alta velocidad es un vehiculo avanzado
porque suma la energia cinetica enorme, el dominio de la aerodinamica y una via
dedicada. Marco legal comun en
[⚖️ docs/07-marco-legal-chile.md](../../docs/07-marco-legal-chile.md).

---

[➡️ Empezar por el Modulo 1: Historia](historia/historia-tren-alta-velocidad.md)
