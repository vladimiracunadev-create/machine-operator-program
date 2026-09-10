---
tipo_documento: clase
clase: 8
codigo: DRONES-08
curso: drones
titulo: "Reglamentos de los drones (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: DRONES-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Drones."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Drones."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# ⚖️ Reglamentos de los drones (Chile)

[🏠 Inicio](../../../README.md) · [🕹️ Curso: Drones](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad aeronáutica y la ley vigente. Marco general
en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md), sección
3.3 (Drones / RPAS).

## Ámbito

- País: Chile.
- Marco base: reglamentación aeronáutica de la DGAC para RPAS.
- Autoridad: Dirección General de Aeronáutica Civil (DGAC).
- Norma específica: **DAN 151** (operaciones de aeronaves pilotadas a distancia).
- Tipo de aeronave: dron civil (RPAS / UAV), foco en multirotor.

## Autoridad y norma DAN 151

- La operación civil de aeronaves pilotadas a distancia se rige por la **DGAC** a
  través de la norma **DAN 151**, edición vigente por confirmar.
- La DAN 151 cubre el registro del aparato, la responsabilidad del piloto a
  distancia y las condiciones de operación.
- Se enmarca en el Código Aeronáutico y en la fiscalización de la DGAC, igual que
  el resto de la aviación civil.

## Registro y piloto a distancia

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Registro del aparato | DAN 151 (edición por confirmar) | Inscripción del RPAS ante la DGAC. | Estado documental del dron. |
| Piloto a distancia | DAN 151 (edición por confirmar) | Responsabilidad y aptitud del operador. | Requisito de piloto habilitado. |
| Operación | DAN 151 (edición por confirmar) | Reglas de vuelo y límites de operación. | Reglas del escenario. |
| Cercanía de aeropuertos | Reglamentación DGAC | Prohibido operar cerca de aeródromos. | Zona prohibida en el mapa. |

## Restricciones de operación

- **No volar sobre aglomeraciones de personas**: prohibido sobrevolar público.
- **No volar cerca de aeropuertos ni aeródromos**: zona crítica para la aviación.
- **Respetar zonas prohibidas y restringidas** definidas por la autoridad.
- **Altura máxima de operación**: umbral exacto por confirmar en la DAN 151.
- **Peso y categoría del aparato**: umbrales exactos por confirmar en la DAN 151.

Los umbrales concretos de peso, altura máxima y distancias no se citan con cifra
porque dependen de la edición vigente de la DAN 151; se marcan como
"(por confirmar)". Fuente: <https://www.dgac.gob.cl>.

## Reglas de seguridad

- Completar el chequeo previo antes de armar los motores.
- Mantener el dron a la vista y dentro del alcance del enlace de radio.
- No sobrevolar personas ni operar cerca de aeropuertos.
- Vigilar batería, viento y calidad del GPS durante todo el vuelo.
- Respetar la privacidad al usar la cámara.

## Notas para simulación

- El núcleo educativo son el vuelo estable, la gestión de batería y el respeto de
  las zonas prohibidas.
- Modelar chequeos previos, avisos de batería y activación del retorno a casa.
- Marcar como "(por confirmar)" la edición vigente de la DAN 151 y sus umbrales.
  Fuente: <https://www.dgac.gob.cl>.
- Registrar cada norma usada en [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Drones; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-UAS](https://www.faa.gov/uas): Unmanned Aircraft Systems, FAA. Uso: operación y normativa RPAS.
- [CL-DGAC](https://www.dgac.gob.cl/normativa/): Normativa aeronáutica, DGAC Chile. Uso: marco aeronáutico chileno.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-dron.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-dron.md)
