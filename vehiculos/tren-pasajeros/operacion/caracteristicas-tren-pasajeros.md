---
tipo_documento: clase
clase: 2
codigo: TRENPASAJERO-02
curso: tren-pasajeros
titulo: "Características funcionales del tren de pasajeros"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: TRENPASAJERO-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Tren de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de pasajeros."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 📋 Características funcionales del tren de pasajeros

[🏠 Inicio](../../../README.md) · [🚆 Curso: Tren de pasajeros](../README.md) · 📋 Características

Que es un tren de pasajeros, que tipos existen y para que sirve cada uno. Este
módulo da el contexto antes de abrir la mecánica (Módulo 4).

---

## 🧭 Definición

Un tren de pasajeros es una composición guiada que circula sobre rieles de acero,
formada por uno o varios vehículos unidos, con gran capacidad de transporte y
alta eficiencia energética. A diferencia de un vehículo de carretera, no elige su
trayectoria: la vía lo guía, y su seguridad depende de la señalización y de las
distancias de frenado.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Guía sobre rieles | La rueda de pestaña sigue el riel; no se conduce girando. |
| Gran capacidad | Transporta cientos o miles de pasajeros por composición. |
| Alta eficiencia | La rueda de acero sobre riel tiene muy baja resistencia. |
| Gran masa | Mucha inercia; acelera y frena lentamente. |
| Distancias largas | La frenada exige cientos de metros a alta velocidad. |
| Ruta fija | Circula por una vía predefinida controlada por señales. |

---

## 🗂️ Tipos de tren de pasajeros

```mermaid
flowchart TD
    Tren[🚆 Tren de pasajeros] --> Urbano[Servicio urbano]
    Tren --> Media[Media distancia]
    Tren --> Larga[Larga distancia]
    Urbano --> Metro[Metro / subterráneo]
    Urbano --> Suburbano[Suburbano / cercanías]
    Urbano --> TrenTram[Tren-tram]
    Media --> Regional[Regional EMU]
    Larga --> Interurbano[Locomotora más coches]
```

| Tipo | Uso típico | Rasgo destacado |
| --- | --- | --- |
| Metro / subterráneo | Ciudad, alta frecuencia | Tracción eléctrica, gran capacidad. |
| Suburbano / cercanías | Periferia urbana | Paradas frecuentes, unidad múltiple. |
| Tren-tram | Ciudad y vía férrea | Circula en calle y en línea de tren. |
| Regional | Ciudades intermedias | EMU eléctrica o diesel-eléctrica. |
| Interurbano | Larga distancia | Locomotora que remolca coches. |

---

## 🎯 Para qué se usa

- Movilidad urbana masiva de alta frecuencia (metro).
- Transporte de cercanías entre la ciudad y su periferia.
- Conexión regional entre ciudades intermedias.
- Servicios interurbanos de larga distancia.
- Transporte eficiente con bajo consumo de energía por pasajero.

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Tren de pasajeros mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-tren-pasajeros.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-tren-pasajeros.md)
