# 🎛️ Mandos e instrumentos de la DeLorean temporal

[🏠 Inicio](../../../README.md) · [🕰️ Curso: DeLorean temporal](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Este modulo describe un puesto de mando conceptual y original para la nave. No
reproduce ningun tablero ni arte de la obra: propone controles utiles para
ensenar los conceptos de fisica del curso y para alimentar un simulador.

---

## 🧭 Vista general del puesto de mando

El puesto conceptual se divide en dos zonas. La **zona de conduccion** es la de
cualquier coche: acelerador, freno y direccion. La **zona temporal** es
ficticia y sirve para ilustrar los conceptos: un selector de fecha, un medidor
de energia y un indicador de velocidad umbral.

---

## 🎚️ Mapa de controles

```mermaid
flowchart TD
    Puesto[🎛️ Puesto de mando] --> Conduccion[Zona de conduccion]
    Puesto --> Temporal[Zona temporal ficticia]
    Conduccion --> Acel[Acelerador]
    Conduccion --> Freno[Freno]
    Conduccion --> Dir[Direccion]
    Temporal --> Fecha[Selector de fecha]
    Temporal --> Carga[Carga de energia]
    Temporal --> Activar[Boton de salto]
```

---

## 🕹️ Controles y su funcion

| Zona | Control | Funcion | Base |
| --- | --- | --- | --- |
| Conduccion | Acelerador | Aumentar la velocidad del vehiculo | Real |
| Conduccion | Freno | Reducir la velocidad | Real |
| Conduccion | Direccion | Cambiar el rumbo | Real |
| Temporal | Selector de fecha | Elegir la fecha objetivo del salto | Ficticio |
| Temporal | Carga de energia | Acumular la energia narrativa del salto | Ficticio |
| Temporal | Boton de salto | Ejecutar el salto al llegar al umbral | Ficticio |
| Temporal | Interruptor ciencia/ficcion | Alternar entre reglas reales y de guion | Educativo |

---

## 📟 Instrumentos principales

| Instrumento | Muestra | Unidad | Base |
| --- | --- | --- | --- |
| Velocimetro | Velocidad actual | km/h | Real |
| Medidor de energia | Energia acumulada para el salto | fraccion | Ficticio |
| Indicador de umbral | Cercania a la velocidad umbral | porcentaje | Ficticio |
| Pantalla de fecha | Fecha objetivo elegida | fecha | Ficticio |
| Aviso de causalidad | Riesgo de paradoja en el destino | nivel | Educativo |

---

## 🎮 Entradas de simulacion

| Accion | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Progresivo, sube la velocidad. |
| Frenar | Flecha abajo | Gatillo izquierdo | Reduce la velocidad. |
| Girar | Flechas izq/der | Stick izquierdo | Cambia el rumbo. |
| Cargar energia | Tecla C | Boton superior | Solo activo en modo ficcion. |
| Elegir fecha | Teclas mas/menos | Cruceta | Ajusta la fecha objetivo. |
| Ejecutar salto | Barra espaciadora | Boton central | Requiere umbral y energia llena. |
| Cambiar modo | Tecla M | Boton lateral | Alterna ciencia y ficcion. |

---

## 🧠 Observaciones de diseno

- El velocimetro y el indicador de umbral deben verse siempre juntos, para que
  el usuario relacione velocidad con la condicion del salto.
- El interruptor ciencia/ficcion es la pieza educativa central: en modo ciencia
  el boton de salto queda deshabilitado y se explica por que.
- El aviso de causalidad no castiga; informa y abre la discusion sobre
  paradojas, que se detalla en el Modulo 7.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-delorean.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-delorean.md)
