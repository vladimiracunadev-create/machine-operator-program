---
tipo_documento: clase
clase: 7
codigo: TELETRANSPOR-07
curso: teletransportador
titulo: "Entornos del teletransportador"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TELETRANSPOR-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Teletransportador."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Teletransportador."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos del teletransportador

[🏠 Inicio](../../../README.md) · [🌀 Curso: Teletransportador](../README.md) · 🌍 Entornos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Dónde se usaría un teletransportador y cómo cambia su exigencia según el
entorno. Cada escenario implica límites físicos distintos, y en simulación se
traduce en condiciones diferentes de distancia, energía y materia disponible.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🌀 Teletransportador))
    Corta distancia
      Menos retardo del canal
      Mismo volumen de datos
      Materia local cercana
    Larga distancia
      Retardo por velocidad de la luz
      Canal clasico mas lento
      Sincronizacion dificil
    Enlace cuantico
      Estado, no materia
      Requiere par previo
      Requiere canal clasico
    Sin materia en destino
      No hay con que reconstruir
      Solo sirve transferir estado
      Reconstruccion imposible
```

| Entorno | Características | Riesgos típicos | Ajuste del proceso |
| --- | --- | --- | --- |
| Corta distancia | Poco retardo en el canal. | Igual gasto de datos y energía. | Optimizar escaneo y reserva local. |
| Larga distancia | Retardo grande por la velocidad de la luz. | Pérdida de sincronización. | Planificar el tiempo del canal clásico. |
| Enlace cuántico | Solo transfiere estado, no objetos. | Confundirlo con mover materia. | Preparar el par y el canal clásico. |
| Sin materia en destino | No hay con que reconstruir. | Reconstrucción imposible. | Limitarse a transferir estado. |

---

## 🌡️ Factores del entorno

- **Distancia**: no cambia el volumen de datos, pero si el retardo del canal
  clásico, limitado por la velocidad de la luz.
- **Materia disponible**: sin una reserva de materia en el destino no hay con
  que ensamblar el patrón recibido.
- **Energía accesible**: manipular materia a nivel de partículas exige energía
  colosal; el entorno debe poder aportarla.
- **Ruido e interferencia**: cualquier error en los datos o en el enlace
  cuántico degrada el resultado y puede arruinar el patrón.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su distancia, su reserva de materia y su
presupuesto de energía. El paso de transferir estado a intentar reconstruir un
cuerpo cambia por completo lo que es posible y es una gran lección de física.
Ver cómo se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-teletransportador.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Teletransportador a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [STARTREK-DATABASE](https://www.startrek.com/database): Star Trek Database, Paramount. Uso: canon narrativo y tecnologías de ficción.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-teletransportador.md) · [➡️ Siguiente: Reglas del universo](../reglamentos/reglas-universo-teletransportador.md)
