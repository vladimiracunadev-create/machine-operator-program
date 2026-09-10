---
tipo_documento: clase
clase: 9
codigo: AVIONESCOMBA-09
curso: aviones-combate
titulo: "Diseño de simulación del avión de combate"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: AVIONESCOMBA-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Aviones de combate."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Aviones de combate."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación del avión de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🎮 Simulación

Simulación **educativa** centrada en la física del vuelo a reacción. No modela
sistemas de armas, táctica ni doctrina; su objetivo es enseñar cómo vuela un
reactor.

```mermaid
stateDiagram-v2
    [*] --> EnTierra
    EnTierra --> MotorEnMarcha: encender
    MotorEnMarcha --> EnVuelo: despegar
    EnVuelo --> Maniobra: virar con cargas G
    Maniobra --> EnVuelo: estabilizar
    EnVuelo --> Aproximacion: iniciar descenso
    Aproximacion --> EnTierra: aterrizar
    EnVuelo --> Emergencia: falla o riesgo
    Emergencia --> Aproximacion: estabilizar y desviar
    MotorEnMarcha --> EnTierra: apagar
    EnTierra --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a despegar, ascender, volar a alta velocidad, maniobrar
respetando las cargas G, gestionar la energía y aterrizar un avión a reacción, de
forma educativa y sin contenido sensible.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: agrega el vuelo a alta velocidad y las cargas G, por lo que se
  recomienda tras dominar la aviación general.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-2.0 Mach | Sustentación y resistencia | A alta velocidad se usa Mach. |
| Altitud | numérica | 0-50000 pies | Rendimiento y densidad | Ligada a la presión. |
| Actitud | numérica | -90..90 grados | Trayectoria de vuelo | Referencia del horizonte. |
| Carga G | numérica | -3..9 G | Estructura y piloto | Límite estructural y fisiológico. |
| Empuje del motor | numérica | 0-100% + AB | Aceleración | AB es el posquemador. |
| Energía total | derivada | baja-alta | Capacidad de maniobra | Suma de velocidad y altitud. |
| Combustible | numérica | 0-100% | Autonomía | Incluye reserva. |

## Ciclo básico

1. Leer entrada del usuario (palanca, pedales, empuje, tren, aerofrenos).
2. Actualizar estado del motor y la configuración aerodinámica.
3. Calcular fuerzas: sustentación, peso, empuje y resistencia.
4. Aplicar cargas G, altitud y efectos de alta velocidad.
5. Actualizar velocidad, altitud, actitud y energía.
6. Refrescar instrumentos y alertas (baja velocidad, exceso de G).

## Modos de juego futuros

- Tutorial de cabina y física del vuelo a reacción.
- Práctica de despegue, maniobra y aterrizaje.
- Desafíos de gestión de energía y cargas G.
- Circuitos de navegación a gran altitud.
- Situaciones de emergencia controladas (falla de motor) sin contenido sensible.

## Elementos fuera de alcance

- Sistemas de armas, sensores tacticos o de misión.
- Táctica, doctrina o procedimientos operativos sensibles.
- Datos técnicos que permitan replicar sistemas reales.
- Reproducción de vuelo temerario como objetivo del juego.

## Pendientes

- [ ] Definir valores por defecto de cada variable de vuelo.
- [ ] Prototipar el modelo de cargas G y energía.
- [ ] Ajustar efectos de alta velocidad (Mach) de forma divulgativa.
- [ ] Agregar fuentes públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Aviones de combate basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FAA-HANDBOOKS](https://www.faa.gov/regulations_policies/handbooks_manuals): Aviation Handbooks and Manuals, FAA. Uso: aerodinámica, sistemas y operación.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-avion-combate.md) · [➡️ Siguiente: Recursos](../recursos/recursos-avion-combate.md)
