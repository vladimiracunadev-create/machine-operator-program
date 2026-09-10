---
tipo_documento: clase
clase: 7
codigo: SDF1-07
curso: sdf-1
titulo: "Entornos del SDF-1"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: SDF1-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de SDF-1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de SDF-1."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos del SDF-1

[🏠 Inicio](../../../README.md) · [🏯 Curso: SDF-1](../README.md) · 🌍 Entornos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Dónde opera una nave-fortaleza gigante y cómo cambia su comportamiento según el
entorno. Cada escenario implica reglas físicas distintas, y en simulación se
traduce en condiciones diferentes de gravedad, estructura y disipación de calor.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🏯 Nave-fortaleza))
    Vacio profundo
      Sin aire
      Sin gravedad externa
      Solo radia calor por la superficie
    Orbita planetaria
      Gravedad presente
      Esfuerzos de marea
      Maniobra muy lenta
    Cercania de una atmosfera
      Aparece el aire
      Rozamiento y calor
      Riesgo estructural alto
    Astillero o base
      Construccion y reparacion
      Apoyo estructural externo
      Carga de suministros
```

| Entorno | Características | Riesgos típicos | Ajuste de maniobra |
| --- | --- | --- | --- |
| Vacío profundo | Sin aire ni gravedad externa. | Acumular calor, gastar delta-v. | Maniobras muy lentas y planificadas. |
| Órbita planetaria | Gravedad y posibles esfuerzos de marea. | Deformación, caída o escape. | Respetar mecánica orbital, cuidar la estructura. |
| Cercanía de una atmósfera | Aparece aire, rozamiento y calor. | Esfuerzo estructural grave. | Evitar entrar; la escala no lo favorece. |
| Astillero o base | Apoyo externo para construir o reparar. | Sobrecarga durante el atraque. | Operaciones lentas con soporte externo. |

---

## 🌡️ Factores del entorno

- **Gravedad**: cerca de un planeta la trayectoria se curva y aparecen esfuerzos
  que una mole tan grande sufre de forma desigual en sus extremos.
- **Atmósfera**: una nave de este tamaño no está pensada para volar en el aire;
  el rozamiento y el calor la castigarían, y su peso propio sería un problema
  serio bajo gravedad.
- **Calor**: en el vacío el calor solo sale por radiación; una nave-ciudad
  genera tanto que su superficie apenas basta para disiparlo.
- **Estructura**: cualquier entorno que añada esfuerzos (gravedad, maniobra,
  atraque) pone a prueba el esqueleto interno de la nave.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su gravedad, presencia o ausencia de aire y
nivel de esfuerzos sobre la estructura. Pasar del vacío tranquilo a la cercanía
de un planeta multiplica los retos y es una gran lección sobre escala e
ingeniería. Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-sdf-1.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de SDF-1 a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [ROBOTECH-OFFICIAL](https://robotech.com/): Robotech, Harmony Gold. Uso: referencia oficial del universo ficticio.
- [NASA-SPACECRAFT](https://www.nasa.gov/humans-in-space/spaceships-and-rockets/): Spaceships and Rockets, NASA. Uso: naves, sistemas y misiones.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-sdf-1.md) · [➡️ Siguiente: Reglas del universo](../reglamentos/reglas-universo-sdf-1.md)
