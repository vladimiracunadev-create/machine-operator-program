---
tipo_documento: clase
clase: 7
codigo: GRUAPORTUARI-07
curso: grua-portuaria
titulo: "Entornos de trabajo de la grúa portuaria"
modalidad: "análisis de escenarios"
duracion_minutos: 60
nivel: introductorio
prerrequisito: GRUAPORTUARI-06
competencia: "adaptacion_al_entorno"
resultados_aprendizaje:
  - "Explicar entornos, factores ambientales, riesgos y respuesta de simulación con vocabulario propio de Grúa portuaria."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Grúa portuaria."
evidencia: "Matriz entorno–cambio–riesgo–respuesta."
criterio_aprobacion: "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🌍 Entornos de trabajo de la grúa portuaria

[🏠 Inicio](../../../README.md) · [⚓ Curso: Grúa portuaria](../README.md) · 🌍 Entornos

Dónde opera una grúa portuaria y cómo cambia la operación según el entorno. El
terminal de contenedores impone reglas, riesgos y ajustes propios, y en
simulación se traduce en escenarios diferentes.

---

## 🗺️ Entornos principales

```mermaid
mindmap
  root((⚓ Grua portuaria))
    Muelle
      Rieles del muelle
      Buque atracado
      Borde de agua
    Clima
      Viento limite
      Lluvia
      Niebla
    Jornada
      Operacion diurna
      Operacion nocturna
      Iluminacion
    Terminal
      Camiones
      Patio de contenedores
      Senaleros
```

| Entorno | Características | Riesgos típicos | Ajuste de operación |
| --- | --- | --- | --- |
| Muelle | Rieles, buque atracado, borde de agua. | Caída al agua, golpe al buque. | Posicionamiento preciso, anti-sway. |
| Viento | Carga colgada expuesta al viento. | Balanceo, deriva de la carga. | Respetar límite del anemómetro. |
| Operación nocturna | Baja visibilidad, jornada continua. | Errores por fatiga y poca luz. | Iluminación, cámaras, ritmo controlado. |
| Coordinación con camiones | Flujo de vehículos bajo la grúa. | Atropello, depósito sobre camión mal ubicado. | Señalero, área de exclusión. |
| Patio de contenedores | Apilado y traslado en tierra. | Choque de contenedores, mal apilado. | Coordinación con grúas de patio. |

---

## 🌦️ Factores del entorno

- **Viento**: es el factor crítico; por encima del límite del anemómetro se
  detiene la operación porque la carga colgada se vuelve incontrolable.
- **Visibilidad**: lluvia, niebla y noche reducen la visión del punto de apoyo;
  la iluminación y las cámaras la complementan.
- **Superficie del muelle**: los rieles deben estar libres y firmes para el
  gantry; el borde de agua exige margen de seguridad.
- **Coordinación humana**: camiones, señaleros y personal de tierra comparten el
  área de trabajo y exigen área de exclusión y comunicación.

---

## 🎮 Traducción a simulación

Cada entorno es un escenario con su clima, jornada y flujo de camiones. Ver como
se modela en el [Módulo 9: Diseño de simulación](../simulacion/diseno-simulador-grua-portuaria.md).

## 🎓 Cierre de clase

- **Actividad:** Contrasta tres entornos de Grúa portuaria a partir de entornos, factores ambientales, riesgos y respuesta de simulación y determina cómo cambian variables, percepción, riesgos y respuesta.
- **Evidencia:** Matriz entorno–cambio–riesgo–respuesta.
- **Criterio de aprobación:** Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [OSHA-CRANES](https://www.osha.gov/cranes-derricks): Crane, Derrick and Hoist Safety, OSHA. Uso: izaje, riesgos y controles.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [CL-DIRECTEMAR](https://www.directemar.cl/directemar/marco-normativo): Marco normativo, DIRECTEMAR. Uso: marco marítimo chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Principios y operación](principios-grua-portuaria.md) · [➡️ Siguiente: Reglamentos](../reglamentos/reglamentos-grua-portuaria.md)
