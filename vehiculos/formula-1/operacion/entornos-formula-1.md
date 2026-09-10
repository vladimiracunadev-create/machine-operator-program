---
tipo_documento: clase
clase: 7
codigo: FORMULA1-07
curso: formula-1
titulo: "Entornos de trabajo de la Fórmula 1"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: FORMULA1-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Fórmula 1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Fórmula 1."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo de la Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🌍 Entornos

Donde compite un monoplaza y cómo cambia el pilotaje según el circuito. Cada
trazado implica reglaje, riesgos y estrategia distintos, y en simulación se
traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🏎️ Monoplaza))
    Circuito urbano
      Muros cercanos
      Curvas lentas
      Baja tolerancia al error
    Circuito permanente
      Escapatorias amplias
      Curvas rapidas
      Alta carga aerodinamica
    Circuito mixto
      Rectas largas
      Zonas tecnicas
      Reglaje de compromiso
    Condiciones
      Lluvia
      Calor extremo
      Altitud
```

| Entorno | Características | Riesgos típicos | Ajuste de pilotaje |
| --- | --- | --- | --- |
| Circuito urbano | Muros cercanos, curvas lentas. | Error mínimo termina en muro. | Precisión, alta carga, cuidar frenos. |
| Circuito permanente | Escapatorias, curvas rápidas. | Sobreexigir gomas y frenos. | Buscar trazada limpia y ritmo. |
| Circuito mixto | Rectas largas y zonas técnicas. | Reglaje de compromiso. | Equilibrar velocidad punta y agarre. |
| Lluvia | Piso mojado, baja adherencia. | Aquaplaning y trompos. | Gomas de lluvia, suavidad, más distancia. |
| Calor / altitud | Menos densidad de aire. | Sobrecalentar unidad y gomas. | Gestión térmica y de energía. |

---

## 🌦️ Factores del entorno

- **Clima**: la lluvia reduce el agarre y cambia el neumático; el calor afecta la
  temperatura de gomas y frenos.
- **Asfalto**: nuevo o gomado, liso o rugoso, cambia el agarre disponible.
- **Trazado**: número y tipo de curvas define la carga aerodinámica ideal.
- **Altitud y temperatura del aire**: afectan la potencia y la refrigeración.

---

## 🎮 Traducción a simulación

Cada circuito es un escenario con su trazado, asfalto, clima y zonas DRS. Ver
como se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-formula-1.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Fórmula 1 a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [FIA-F1-2026](https://www.fia.com/regulations/formula-1): Formula 1 Regulations, FIA. Uso: reglamento, arquitectura y seguridad de Fórmula 1.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-formula-1.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-formula-1.md)
