---
tipo_documento: clase
clase: 2
codigo: TRENALTAVELO-02
curso: tren-alta-velocidad
titulo: "Características funcionales del tren de alta velocidad"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: TRENALTAVELO-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Tren de alta velocidad."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de alta velocidad."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 📋 Características funcionales del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 📋 Características

Que es un tren de alta velocidad, que configuraciones existen y para que sirve
cada una. Este módulo da el contexto antes de abrir la mecánica (Módulo 4).

---

## 🧭 Definición

Un tren de alta velocidad es un tren disenado para circular por encima de unos
250 km/h sobre una vía dedicada, sin cruces a nivel y con curvas amplias. A esa
velocidad la resistencia del aire domina, por lo que la aerodinámica y una vía
especial son tan importantes como la potencia. Guía sobre rieles, de modo que no
tiene dirección libre: su ruta está fijada por la vía.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Velocidad de servicio | Por encima de 250 km/h en vía dedicada. |
| Vía dedicada | Sin pasos a nivel, con curvas amplias y peralte. |
| Aerodinámica | Nariz alargada; la resistencia del aire domina a alta velocidad. |
| Tracción distribuida | Motores repartidos en varios coches (EMU) en muchos diseños. |
| Energía cinética enorme | Gran masa por gran velocidad; distancias de frenado de kilómetros. |
| Señalización en cabina | ETCS/ERTMS; no hay señales laterales legibles a esa velocidad. |
| Alimentación eléctrica | Pantógrafo único sobre catenaria de alta tensión. |

---

## 🗂️ Tipos de configuración

```mermaid
flowchart TD
    Tren[🚄 Tren de alta velocidad] --> Traccion[Por tracción]
    Tren --> Contacto[Por contacto con la vía]
    Traccion --> Distribuida[Distribuida EMU]
    Traccion --> Concentrada[Concentrada con locomotora]
    Contacto --> Rueda[Rueda-riel clásico]
    Contacto --> Maglev[Levitación magnética]
    Distribuida --> Shinkansen[Estilo Shinkansen]
    Concentrada --> TGV[Estilo TGV]
```

| Tipo | Como se distingue | Rasgo destacado |
| --- | --- | --- |
| Tracción distribuida (EMU) | Motores en varios coches | Mejor adherencia y aceleración repartida. |
| Tracción concentrada | Locomotora en cabeza (y cola) | Coches remolcados sin motor. |
| Rueda-riel | Contacto clásico rueda de pestaña | Compatible con red convencional. |
| Levitación magnética | Sin contacto físico | Muy alta velocidad, vía propia exclusiva. |
| Ancho internacional | Trocha estandar | Referencia común; valor para Chile por confirmar. |

---

## 🎯 Para qué se usa

- Unir grandes ciudades separadas por distancias medias de forma rápida.
- Competir con el avión en trayectos de algunos cientos de kilómetros.
- Descongestionar corredores de transporte muy demandados.
- Ofrecer transporte público masivo con alta frecuencia y puntualidad.
- Reducir el uso del automóvil entre ciudades conectadas.

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Tren de alta velocidad mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-tren-alta-velocidad.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-tren-alta-velocidad.md)
