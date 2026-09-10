---
tipo_documento: clase
clase: 7
codigo: CAMIONES-07
curso: camiones
titulo: "Entornos de trabajo del camión"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: CAMIONES-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Camiones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Camiones."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo del camión

[🏠 Inicio](../../../README.md) · [🚛 Curso: Camiones](../README.md) · 🌍 Entornos

Dónde opera un camión y cómo cambia la conducción según el entorno. Cada entorno
implica reglas, riesgos y ajustes distintos, y en simulación se traduce en
escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((🚛 Camion))
    Ruta
      Larga distancia
      Velocidad sostenida
      Fatiga y jornada
    Ciudad
      Reparto
      Puntos ciegos
      Peatones y ciclos
    Montana
      Pendientes largas
      Freno de motor
      Curvas cerradas
    Faena
      Mineria y obra
      Aridos y volquete
      Caminos de tierra
```

| Entorno | Características | Riesgos típicos | Ajuste de conducción |
| --- | --- | --- | --- |
| Ruta interurbana | Velocidad sostenida, largas distancias. | Fatiga, viento lateral, adelantar. | Distancia amplia, jornada controlada. |
| Ciudad | Reparto, cruces, tráfico denso. | Puntos ciegos, peatones, ciclos. | Baja velocidad, maniobras lentas. |
| Montaña | Pendientes largas y curvas. | Sobrecalentamiento de frenos. | Marcha corta, freno de motor y retarder. |
| Faena minera / obra | Caminos de tierra, áridos. | Polvo, volcamiento, otros equipos. | Velocidad baja, respeto de señalización interna. |
| Lluvia / noche | Baja visibilidad y agarre. | Aquaplaning, deslumbramiento. | Más distancia, luces, velocidad prudente. |

---

## 🌦️ Factores del entorno

- **Pendiente**: define el uso del freno de motor y del retarder, y la marcha.
- **Superficie**: asfalto, tierra, ripio o barro cambian el agarre y el frenado.
- **Clima**: lluvia, hielo o viento reducen adherencia y estabilidad.
- **Tráfico**: más vehículos y usuarios vulnerables exigen anticipar y ceder.
- **Carga**: su peso, altura y si es líquida o suelta cambian la dinámica.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su pendiente, superficie, clima y carga. Ver
como se modela en el
[Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-camion.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Camiones a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [CL-LEY-18290](https://www.bcn.cl/leychile/navegar?idNorma=29708): Ley de Tránsito 18.290, BCN Chile. Uso: marco legal chileno.
- [US-FMCSA-CDL](https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual): Commercial Driver's License Manual, FMCSA. Uso: operación de buses y camiones.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-camion.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-camion.md)
