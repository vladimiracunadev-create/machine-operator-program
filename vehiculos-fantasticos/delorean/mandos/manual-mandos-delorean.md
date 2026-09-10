---
tipo_documento: clase
clase: 5
codigo: DELOREAN-05
curso: delorean
titulo: "Mandos e instrumentos de la DeLorean temporal"
modalidad: "taller de simulación"
duracion_minutos: 60
nivel: introductorio
prerrequisito: DELOREAN-04
competencia: "lectura_y_mando"
resultados_aprendizaje:
  - "Explicar controles, instrumentos, entradas y estados del sistema con vocabulario propio de DeLorean temporal."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de DeLorean temporal."
evidencia: "Mapa de mandos y resolución de dos estados del tablero."
criterio_aprobacion: "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎛️ Mandos e instrumentos de la DeLorean temporal

[🏠 Inicio](../../../README.md) · [🕰️ Curso: DeLorean temporal](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Este módulo describe un puesto de mando conceptual y original para la nave. No
reproduce ningún tablero ni arte de la obra: propone controles útiles para
enseñar los conceptos de física del curso y para alimentar un simulador.

---

## 🧭 Vista general del puesto de mando

El puesto conceptual se divide en dos zonas. La **zona de conducción** es la de
cualquier coche: acelerador, freno y dirección. La **zona temporal** es
ficticia y sirve para ilustrar los conceptos: un selector de fecha, un medidor
de energía y un indicador de velocidad umbral.

---

## 🎚️ Mapa de controles

```mermaid
flowchart TD
    Puesto[🎛️ Puesto de mando] --> Conduccion[Zona de conducción]
    Puesto --> Temporal[Zona temporal ficticia]
    Conduccion --> Acel[Acelerador]
    Conduccion --> Freno[Freno]
    Conduccion --> Dir[Dirección]
    Temporal --> Fecha[Selector de fecha]
    Temporal --> Carga[Carga de energía]
    Temporal --> Activar[Botón de salto]
```

---

## 🕹️ Controles y su función

| Zona | Control | Función | Base |
| --- | --- | --- | --- |
| Conducción | Acelerador | Aumentar la velocidad del vehículo | Real |
| Conducción | Freno | Reducir la velocidad | Real |
| Conducción | Dirección | Cambiar el rumbo | Real |
| Temporal | Selector de fecha | Elegir la fecha objetivo del salto | Ficticio |
| Temporal | Carga de energía | Acumular la energía narrativa del salto | Ficticio |
| Temporal | Botón de salto | Ejecutar el salto al llegar al umbral | Ficticio |
| Temporal | Interruptor ciencia/ficción | Alternar entre reglas reales y de guion | Educativo |

---

## 📟 Instrumentos principales

| Instrumento | Muestra | Unidad | Base |
| --- | --- | --- | --- |
| Velocímetro | Velocidad actual | km/h | Real |
| Medidor de energía | Energía acumulada para el salto | fracción | Ficticio |
| Indicador de umbral | Cercanía a la velocidad umbral | porcentaje | Ficticio |
| Pantalla de fecha | Fecha objetivo elegida | fecha | Ficticio |
| Aviso de causalidad | Riesgo de paradoja en el destino | nivel | Educativo |

---

## 🎮 Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Acelerar | Flecha arriba | Gatillo derecho | Progresivo, sube la velocidad. |
| Frenar | Flecha abajo | Gatillo izquierdo | Reduce la velocidad. |
| Girar | Flechas izq/der | Stick izquierdo | Cambia el rumbo. |
| Cargar energía | Tecla C | Botón superior | Solo activo en modo ficción. |
| Elegir fecha | Teclas más/menos | Cruceta | Ajusta la fecha objetivo. |
| Ejecutar salto | Barra espaciadora | Botón central | Requiere umbral y energía llena. |
| Cambiar modo | Tecla M | Botón lateral | Alterna ciencia y ficción. |

---

## 🧠 Observaciones de diseño

- El velocímetro y el indicador de umbral deben verse siempre juntos, para que
  el usuario relacione velocidad con la condición del salto.
- El interruptor ciencia/ficción es la pieza educativa central: en modo ciencia
  el botón de salto queda deshabilitado y se explica por qué.
- El aviso de causalidad no castiga; informa y abre la discusión sobre
  paradojas, que se detalla en el Módulo 8.

## 🎓 Cierre de clase

- **Actividad:** Recorre el puesto de mando simulado de DeLorean temporal: localiza los controles de controles, instrumentos, entradas y estados del sistema y asocia cada indicación con una decisión.
- **Evidencia:** Mapa de mandos y resolución de dos estados del tablero.
- **Criterio de aprobación:** Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [UNIVERSAL-BTTF](https://www.universalpicturesathome.com/movies/back-to-the-future): Back to the Future, Universal Pictures At Home. Uso: obra audiovisual primaria.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-delorean.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-delorean.md)
