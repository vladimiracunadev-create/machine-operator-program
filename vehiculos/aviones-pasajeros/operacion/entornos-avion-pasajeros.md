---
tipo_documento: clase
clase: 7
codigo: AVIONESPASAJ-07
curso: aviones-pasajeros
titulo: "Entornos de trabajo del avión de pasajeros"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: AVIONESPASAJ-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Aviones de pasajeros."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones de pasajeros."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo del avión de pasajeros

[🏠 Inicio](../../../README.md) · [🛫 Curso: Aviones de pasajeros](../README.md) · 🌍 Entornos

Dónde opera un avión de pasajeros y cómo cambia el vuelo según el entorno. Cada
entorno implica reglas, riesgos y ajustes distintos, y en simulación se traduce
en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🛫 Avion de pasajeros))
    Aeropuerto
      Plataforma y puertas
      Rodaje y pista
      Torre y control tierra
    Espacio aereo
      Controlado por radar
      Aerovias y niveles
      Aproximaciones instrumentales
    Meteorologia
      Viento y cizalladura
      Nubes y tormentas
      Hielo y turbulencia
    Ruta
      Corto y medio alcance
      Largo alcance
      Zonas remotas
```

| Entorno | Características | Riesgos típicos | Ajuste de vuelo |
| --- | --- | --- | --- |
| Aeropuerto | Plataforma, rodaje, pista. | Tráfico en tierra, incursión de pista. | Seguir autorizaciones, listas y señalización. |
| Espacio aéreo controlado | Radar, aerovias, niveles de vuelo. | Interferir con otros vuelos. | Seguir instrucciones del control, transponder activo. |
| Aproximación instrumental | Guiado por instrumentos a la pista. | Baja visibilidad, cizalladura. | Estabilizar la aproximación, procedimientos definidos. |
| Meteorología adversa | Tormentas, hielo, viento. | Turbulencia, desvío de ruta. | Radar meteorológico, rutas alternativas, antihielo. |
| Largo alcance | Rutas oceánicas o remotas. | Distancia a aeropuertos alternativos. | Planificación, combustible y reglas de desvío. |
| Gran altitud | Aire fino, crucero rápido. | Despresurización, envolvente estrecha. | Presurización, control de velocidad y nivel. |

---

## 🌦️ Factores del entorno

- **Viento y cizalladura**: el viento cruzado y las ráfagas complican despegue y
  aterrizaje; la cizalladura cerca del suelo es un riesgo serio.
- **Meteorología**: tormentas, hielo y baja visibilidad exigen radar, antihielo y
  procedimientos por instrumentos.
- **Densidad del aire**: calor y altitud del aeropuerto afectan el rendimiento.
- **Tráfico y control**: el espacio aéreo controlado ordena rutas, niveles y turnos.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su tipo de espacio aéreo, su clima y su
aeropuerto. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-avion-pasajeros.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Aviones de pasajeros a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-avion-pasajeros.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-avion-pasajeros.md)
