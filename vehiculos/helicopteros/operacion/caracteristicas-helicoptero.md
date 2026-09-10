---
tipo_documento: clase
clase: 2
codigo: HELICOPTEROS-02
curso: helicopteros
titulo: "Características funcionales del helicóptero"
modalidad: "teórica aplicada"
duracion_minutos: 45
nivel: introductorio
prerrequisito: HELICOPTEROS-01
competencia: "identificacion_funcional"
resultados_aprendizaje:
  - "Explicar definición, rasgos funcionales, tipos y usos con vocabulario propio de Helicópteros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Helicópteros."
evidencia: "Matriz comparativa y decisión justificada."
criterio_aprobacion: "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 📋 Características funcionales del helicóptero

[🏠 Inicio](../../../README.md) · [🚁 Curso: Helicópteros](../README.md) · 📋 Características

Que es un helicóptero, que tipos existen y para que sirve cada uno. Este módulo
da el contexto antes de abrir la mecánica (Módulo 4).

---

## 🧭 Definición

Un helicóptero es una aeronave de ala rotatoria que genera sustentación con un
rotor motorizado en vez de con alas fijas. Gracias a ese rotor puede realizar
vuelo estacionario, ascenso y descenso vertical, y desplazamiento lateral o hacia
atrás. No necesita pista: despega y aterriza en vertical.

---

## 🧬 Características clave

| Característica | Descripción |
| --- | --- |
| Vuelo estacionario | Puede mantenerse inmóvil en el aire, sobre un punto fijo. |
| Despegue vertical | No requiere pista; opera desde helipuertos y zonas reducidas. |
| Movimiento omnidireccional | Avanza, retrocede y se desplaza de lado. |
| Compensación del par | Necesita anti-par para no girar sobre si mismo. |
| Autorrotación | Puede descender de forma segura sin motor. |
| Alto costo operativo | Mantenimiento exigente por la complejidad del rotor. |

---

## 🗂️ Tipos de helicóptero

```mermaid
flowchart TD
    Heli[🚁 Helicóptero] --> Config[Por configuración]
    Heli --> Motor[Por motorización]
    Heli --> Uso[Por uso]
    Config --> Convencional[Rotor principal + rotor de cola]
    Config --> Tandem[Rotores en tándem]
    Motor --> Mono[Ligero monoturbina]
    Motor --> Bi[Biturbina]
    Uso --> Rescate[Rescate y EMS]
    Uso --> Incendio[Extinción de incendios]
    Uso --> Transporte[Transporte y trabajo aéreo]
```

| Tipo | Uso típico | Rasgo destacado |
| --- | --- | --- |
| Rotor principal + rotor de cola | Configuración general | El rotor de cola compensa el par. |
| Rotores en tándem | Carga pesada y transporte | Dos rotores principales, sin rotor de cola. |
| Ligero monoturbina | Instrucción y trabajo aéreo | Sencillo y económico de operar. |
| Biturbina | Transporte y EMS | Dos motores para mayor seguridad. |
| De rescate | Montaña y mar | Grúa y gran autonomía de vuelo. |
| De extinción | Incendios forestales | Carga externa de agua bajo el fuselaje. |

---

## 🎯 Para qué se usa

- Rescate en montaña, mar y zonas sin acceso terrestre.
- Evacuación médica y ambulancia aérea (EMS).
- Extinción de incendios forestales con carga externa.
- Transporte de personas y carga a lugares aislados.
- Trabajo aéreo: inspección de líneas, fotografía y observación.

## 🎓 Cierre de clase

- **Actividad:** Compara variantes de Helicópteros mediante los ejes «definición, rasgos funcionales, tipos y usos» y elige una para un caso de uso razonado.
- **Evidencia:** Matriz comparativa y decisión justificada.
- **Criterio de aprobación:** La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HELI](https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf): Helicopter Flying Handbook, FAA. Uso: aerodinámica y control de helicópteros.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Historia](../historia/historia-helicoptero.md) · [➡️ Siguiente: Modelos y variantes](../modelos/modelos-helicoptero.md)
