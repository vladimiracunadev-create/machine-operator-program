---
tipo_documento: clase
clase: 7
codigo: TRANSBORDADO-07
curso: transbordadores
titulo: "Entornos de trabajo del transbordador"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRANSBORDADO-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Transbordadores."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Transbordadores."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo del transbordador

[🏠 Inicio](../../../README.md) · [🛬 Curso: Transbordadores](../README.md) · 🌍 Entornos

Dónde opera un transbordador y cómo cambian las condiciones a lo largo de la
misión. Cada fase implica un entorno distinto, con riesgos y ajustes propios, y en
simulación se traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🛬 Transbordador))
    Plataforma
      Carga de propelente
      Torre de servicio
      Cuenta atras
    Ascenso
      Aire denso
      Separacion de propulsores
      Separacion del tanque
    Orbita
      Microgravedad
      Bahia de carga abierta
      Brazo robotico
    Reentrada y planeo
      Calor extremo
      Escudo por delante
      Aterrizaje en pista
```

| Entorno | Características | Riesgos típicos | Ajuste de operación |
| --- | --- | --- | --- |
| Plataforma | Vehículo cargado y sujeto. | Fuga de propelente, clima. | Checklist, ventana de lanzamiento. |
| Ascenso | Aire denso y gran empuje. | Separaciones a destiempo. | Guiar, separar propulsores y tanque. |
| Órbita | Microgravedad, sin aire. | Colisiones, basura orbital. | Control de actitud, operar la carga. |
| Reentrada | Calor y frenado por el aire. | Mala orientación del escudo. | Escudo por delante, ángulo correcto. |
| Planeo y pista | Descenso sin motor. | Quedar corto o largo, viento. | Administrar energía, un solo intento. |

---

## 🌦️ Factores del entorno

- **Clima**: viento y visibilidad afectan tanto el despegue como el aterrizaje.
- **Ventana de lanzamiento**: momento preciso para alcanzar la órbita objetivo.
- **Calor de reentrada**: depende del ángulo y de la velocidad de reingreso.
- **Estado de la pista**: viento cruzado y longitud influyen en el aterrizaje.

---

## 🎮 Traducción a simulación

Cada fase es un escenario con su densidad de aire, su gravedad efectiva y su
régimen de vuelo o planeo. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-transbordador.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Transbordadores a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [NASA-SHUTTLE](https://www.nasa.gov/reference/the-space-shuttle/): The Space Shuttle, NASA. Uso: arquitectura y operación del transbordador.
- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [UNOOSA-TREATIES](https://www.unoosa.org/oosa/SpaceLaw/treaties.html): Space Law Treaties and Principles, UNOOSA. Uso: derecho espacial internacional.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-transbordador.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-transbordador.md)
