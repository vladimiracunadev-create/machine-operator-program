# 📋 Caracteristicas funcionales del helicoptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicopteros](../README.md) · 📋 Caracteristicas

Que es un helicoptero, que tipos existen y para que sirve cada uno. Este modulo
da el contexto antes de abrir la mecanica (Modulo 3).

---

## 🧭 Definicion

Un helicoptero es una aeronave de ala rotatoria que genera sustentacion con un
rotor motorizado en vez de con alas fijas. Gracias a ese rotor puede realizar
vuelo estacionario, ascenso y descenso vertical, y desplazamiento lateral o hacia
atras. No necesita pista: despega y aterriza en vertical.

---

## 🧬 Caracteristicas clave

| Caracteristica | Descripcion |
| --- | --- |
| Vuelo estacionario | Puede mantenerse inmovil en el aire, sobre un punto fijo. |
| Despegue vertical | No requiere pista; opera desde helipuertos y zonas reducidas. |
| Movimiento omnidireccional | Avanza, retrocede y se desplaza de lado. |
| Compensacion del par | Necesita anti-par para no girar sobre si mismo. |
| Autorrotacion | Puede descender de forma segura sin motor. |
| Alto costo operativo | Mantenimiento exigente por la complejidad del rotor. |

---

## 🗂️ Tipos de helicoptero

```mermaid
flowchart TD
    Heli[🚁 Helicoptero] --> Config[Por configuracion]
    Heli --> Motor[Por motorizacion]
    Heli --> Uso[Por uso]
    Config --> Convencional[Rotor principal + rotor de cola]
    Config --> Tandem[Rotores en tandem]
    Motor --> Mono[Ligero monoturbina]
    Motor --> Bi[Biturbina]
    Uso --> Rescate[Rescate y EMS]
    Uso --> Incendio[Extincion de incendios]
    Uso --> Transporte[Transporte y trabajo aereo]
```

| Tipo | Uso tipico | Rasgo destacado |
| --- | --- | --- |
| Rotor principal + rotor de cola | Configuracion general | El rotor de cola compensa el par. |
| Rotores en tandem | Carga pesada y transporte | Dos rotores principales, sin rotor de cola. |
| Ligero monoturbina | Instruccion y trabajo aereo | Sencillo y economico de operar. |
| Biturbina | Transporte y EMS | Dos motores para mayor seguridad. |
| De rescate | Montana y mar | Grua y gran autonomia de vuelo. |
| De extincion | Incendios forestales | Carga externa de agua bajo el fuselaje. |

---

## 🎯 Para que se usa

- Rescate en montana, mar y zonas sin acceso terrestre.
- Evacuacion medica y ambulancia aerea (EMS).
- Extincion de incendios forestales con carga externa.
- Transporte de personas y carga a lugares aislados.
- Trabajo aereo: inspeccion de lineas, fotografia y observacion.

---

[⬅️ Anterior: Historia](../historia/historia-helicoptero.md) · [➡️ Siguiente: Sistemas mecanicos](sistemas-mecanicos-helicoptero.md)
