---
tipo_documento: clase
clase: 7
codigo: NAVEEXPLORAC-07
curso: nave-exploracion
titulo: "Entornos de la nave de exploración"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: NAVEEXPLORAC-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Nave de exploración."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Nave de exploración."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de la nave de exploración

[🏠 Inicio](../../../README.md) · [🌌 Curso: Nave de exploración](../README.md) · 🌍 Entornos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Dónde opera una nave de exploración y cómo cambia su misión según el entorno.
Cada región del espacio impone riesgos y ajustes distintos, y en simulación se
traduce en escenarios diferentes. Describimos entornos genéricos y reales del
cosmos, no lugares concretos de ninguna obra.

## 🗺️ Entornos principales

```mermaid
mindmap
  root((Nave de exploracion))
    El vacio
      Sin aire
      Sin friccion
      Radiacion
    Sistema estelar
      Estrella central
      Planetas y orbitas
      Asteroides
    Espacio profundo
      Enormes distancias
      Frio extremo
      Aislamiento
    Fenomenos extremos
      Estrellas de neutrones
      Nubes de gas
      Campos gravitatorios fuertes
```

## Comparación de entornos

| Entorno | Características | Riesgos típicos | Ajuste de misión |
| --- | --- | --- | --- |
| El vacío | Sin aire ni fricción | Radiación, micrometeoritos | Blindaje y soporte vital constante. |
| Sistema estelar | Estrella, planetas, órbitas | Gravedad, calor de la estrella | Navegación orbital cuidadosa. |
| Espacio profundo | Distancias inmensas, frío | Aislamiento, viajes largos | Autonomía total y gestión de energía. |
| Cerca de una estrella masiva | Gravedad intensa | Mareas y radiación fuertes | Distancia segura y mediciones. |
| Nube de gas o polvo | Materia dispersa | Erosión del casco | Velocidad reducida y protección. |

## 🌌 Factores del entorno

- **Vacío**: no hay aire que frene ni transmita sonido; moverse depende solo de
  la reacción del motor.
- **Radiación**: estrellas y espacio emiten partículas daninas; el blindaje es
  vital para la tripulación.
- **Gravedad**: cerca de cuerpos masivos, las órbitas y las mareas condicionan la
  ruta.
- **Distancia**: en el espacio profundo, cualquier ayuda está a años luz, así que
  la nave debe bastarse a si misma.
- **Temperatura**: el vacío es muy frío, pero cerca de una estrella el calor es
  un problema tan grave como el frío.

## 🎮 Traducción a simulación

Cada entorno es un escenario con su nivel de radiación, gravedad y distancia a la
ayuda más cercana. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-nave-exploracion.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Nave de exploración a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARTREK-DATABASE](https://www.startrek.com/database): Star Trek Database, Paramount. Uso: canon narrativo y tecnologías de ficción.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-nave-exploracion.md) · [➡️ Siguiente: Reglas del universo](../reglamentos/reglas-universo-nave-exploracion.md)
