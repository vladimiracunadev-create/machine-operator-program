---
tipo_documento: clase
clase: 9
codigo: SUBMARINOS-09
curso: submarinos
titulo: "Diseño de simulación del submarino"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: SUBMARINOS-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Submarinos."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Submarinos."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Superficie
    Superficie --> Inmersion: inundar lastre
    Inmersion --> EnCota: alcanzar flotabilidad neutra
    EnCota --> Inmersion: descender
    EnCota --> Emersion: purgar lastre
    Emersion --> Superficie: llegar a superficie
    EnCota --> Emergencia: falla o riesgo
    Emergencia --> Emersion: emersion de emergencia
    Superficie --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a controlar la flotabilidad, sumergir y emerger de forma
segura, mantener una cota, gobernar en profundidad y respetar la cota máxima por
la presión, de forma educativa. **Fuera de alcance**: táctica, doctrina y
sistemas de armas.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el submarino agrega la flotabilidad variable, el lastre y la
  presión, que no aparecen en un buque de superficie.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Profundidad | numérica | 0-cota máxima | Presión y seguridad | Central en inmersión. |
| Flotabilidad | numérica | negativa..positiva | Subir o bajar | Depende del lastre. |
| Lastre | numérica | 0-100% agua | Flotabilidad | Agua o aire en tanques. |
| Velocidad | numérica | 0-25 nudos | Avance y planos | Los planos necesitan flujo. |
| Rumbo | numérica | 0-359 grados | Dirección | Timón vertical. |
| Presión externa | numérica | según profundidad | Integridad | ~1 atm cada 10 m. |
| Oxígeno | numérica | 0-100% | Soporte vital | Limita el tiempo sumergido. |
| Batería | numérica | 0-100% | Autonomía | Energía sumergido. |

## Ciclo básico

1. Leer entrada del usuario (timón, planos, lastre, telégrafo).
2. Actualizar el estado de tanques de lastre y flotabilidad.
3. Calcular fuerzas: empuje, peso, propulsión y presión.
4. Actualizar profundidad, rumbo, ángulo y velocidad.
5. Verificar la cota máxima segura y el soporte vital.
6. Refrescar instrumentos (profundímetro, manómetro, oxígeno) y alarmas.

## Modos de juego futuros

- Tutorial guiado de flotabilidad y lastre.
- Práctica libre de inmersión y emersión.
- Mantener una cota con flotabilidad neutra.
- Desafíos de gestión de aire y batería.
- Exploración educativa del fondo marino, sin contenido sensible.

## Elementos fuera de alcance

- Táctica, doctrina o sistemas de armas de cualquier tipo.
- Detalle operativo sensible de submarinos militares modernos.
- Datos clasificados, restringidos o no públicos.

## Pendientes

- [ ] Definir valores por defecto por tipo de submarino.
- [ ] Prototipar el modelo de flotabilidad y lastre.
- [ ] Ajustar la relación presión-profundidad y la cota máxima.
- [ ] Agregar fuentes públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Submarinos basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-submarino.md) · [➡️ Siguiente: Recursos](../recursos/recursos-submarino.md)
