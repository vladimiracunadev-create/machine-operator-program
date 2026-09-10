---
tipo_documento: clase
clase: 7
codigo: THUNDERBIRD3-07
curso: thunderbird-3
titulo: "Entornos del Thunderbird 3"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: THUNDERBIRD3-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Thunderbird 3."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Thunderbird 3."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos del Thunderbird 3

[🏠 Inicio](../../../README.md) · [🚀 Curso: Thunderbird 3](../README.md) · 🌍 Entornos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Por donde pasa un cohete de rescate durante su vuelo y cómo cambia su
comportamiento en cada tramo. Cada fase implica reglas físicas distintas, y en
simulación se traduce en condiciones diferentes de gravedad, aire y velocidad.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚀 Thunderbird 3))
    Rampa de lanzamiento
      Cohete lleno de propelente
      Peso maximo
      Empuje contra la gravedad
    Atmosfera baja
      Aire denso que frena
      Calor por rozamiento
      Ascenso casi vertical
    Atmosfera alta
      Aire muy fino
      Se puede acelerar mas
      Inclinar hacia la horizontal
    Orbita
      Sin aire util
      Velocidad lateral enorme
      Caida continua alrededor del planeta
```

| Entorno | Características | Riesgos típicos | Ajuste de maniobra |
| --- | --- | --- | --- |
| Rampa de lanzamiento | Cohete lleno y pesado. | Volcar, empuje insuficiente. | Empuje firme y ascenso vertical inicial. |
| Atmósfera baja | Aire denso que frena y calienta. | Recalentar, esfuerzo estructural. | Subir con cuidado sin correr demasiado. |
| Atmósfera alta | Aire fino, menos resistencia. | Inclinar antes o después de tiempo. | Empezar a ganar velocidad lateral. |
| Órbita | Sin aire útil, gran velocidad. | Velocidad lateral insuficiente. | Mantener el rumbo y planificar el regreso. |

---

## 🌡️ Factores del entorno

- **Gravedad**: tira del cohete hacia abajo en todo el ascenso; parte del empuje
  se emplea solo en sostener el peso mientras se sube despacio.
- **Aire**: denso abajo y fino arriba; frena y calienta cerca del suelo, por eso
  no conviene acelerar a fondo en los primeros kilómetros.
- **Velocidad lateral**: es la que decide si se órbita; se gana sobre todo en la
  atmósfera alta y por encima, inclinando la trayectoria.
- **Calor**: aparece con fuerza tanto en el ascenso rápido como, sobre todo, en
  la reentrada, cuando la nave frena contra el aire.

---

## 🎮 Traducción a simulación

Cada tramo es un escenario con su gravedad, densidad de aire y objetivo de
velocidad. El paso del aire denso al vacío de la órbita cambia por completo las
reglas y es una gran lección de física. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-thunderbird-3.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Thunderbird 3 a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [THUNDERBIRDS-OFFICIAL](https://www.thunderbirds.com/): Thunderbirds Vehicles, ITV. Uso: referencia oficial de vehículos de rescate.
- [NASA-ROCKETS](https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf): Rockets Educator Guide, NASA. Uso: propulsión, estabilidad y trayectoria.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-thunderbird-3.md) · [➡️ Siguiente: Reglas del universo](../reglamentos/reglas-universo-thunderbird-3.md)
