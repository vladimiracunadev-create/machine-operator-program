---
tipo_documento: clase
clase: 9
codigo: FORMULA1-09
curso: formula-1
titulo: "Diseño de simulación de la Fórmula 1"
modalidad: "laboratorio de diseño"
duracion_minutos: 90
nivel: introductorio
prerrequisito: FORMULA1-08
competencia: "modelado_de_simulacion"
resultados_aprendizaje:
  - "Explicar objetivo, variables, estados, ciclo y escenarios de simulación con vocabulario propio de Fórmula 1."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Fórmula 1."
evidencia: "Ficha de escenario y diagrama de estados."
criterio_aprobacion: "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🎮 Diseño de simulación de la Fórmula 1

[🏠 Inicio](../../../README.md) · [🏎️ Curso: Fórmula 1](../README.md) · 🎮 Simulación

```mermaid
stateDiagram-v2
    [*] --> Garaje
    Garaje --> EnPista: salir de boxes
    EnPista --> VueltaRapida: buscar tiempo
    VueltaRapida --> EnPista: rodar normal
    EnPista --> Boxes: entrar a boxes
    Boxes --> EnPista: salir de nuevo
    EnPista --> Bandera: incidente en pista
    Bandera --> EnPista: pista despejada
    EnPista --> Garaje: fin de tanda
    Garaje --> [*]
```

## Objetivo de la simulación

Que el usuario aprenda a frenar tarde y recto, seguir la trazada, gestionar la
energía ERS, cuidar los neumáticos y respetar las banderas, de forma segura y
progresiva.

## Nivel de realismo

- Nivel elegido: se ofrece del 1 al 3 (ver `docs/03-niveles-de-realismo.md`).
- Justificación: el monoplaza es el vehículo terrestre más exigente del
  repositorio; se recomienda dominar antes el curso de automóviles.

## Variables principales

| Variable | Tipo | Rango | Afecta a | Comentarios |
| --- | --- | --- | --- | --- |
| Velocidad | numérica | 0-350 km/h | Movimiento y aerodinámica | Central para todo. |
| Marcha | discreta | N,1..8 | Aceleración y freno motor | Caja secuencial. |
| Carga aerodinámica | numérica | baja-alta | Agarre en curva | Depende del reglaje. |
| Energía ERS | numérica | 0-100% | Impulso disponible | Se gasta y recupera por vuelta. |
| Adherencia | numérica | 0-1 | Freno, giro, aceleración | Baja con lluvia y goma fría. |
| Temperatura de gomas | numérica | rango en grados | Agarre | Ventana estrecha óptima. |
| Desgaste de gomas | numérica | 0-100% | Rendimiento y estrategia | Obliga a parar en boxes. |
| Combustible | numérica | 0-100% | Peso y autonomía | Menos combustible, más rápido. |

## Ciclo básico

1. Leer entrada del usuario (acelerador, freno, marcha, dirección, DRS, ERS).
2. Actualizar unidad de potencia y estado de energía.
3. Calcular fuerzas: propulsión, frenada, carga aerodinámica y adherencia.
4. Aplicar restricciones del entorno (asfalto, clima, zonas DRS).
5. Actualizar velocidad, posición, temperatura y desgaste.
6. Refrescar pantalla del volante y retroalimentación (sonido, vibración).

## Modos de juego futuros

- Tutorial guiado del volante y los pedales.
- Práctica libre para aprender la trazada.
- Vuelta cronometrada con delta de referencia.
- Gestión de energía y neumáticos en tandas largas.
- Escenarios de lluvia y coche de seguridad, sin contenido sensible.

## Elementos fuera de alcance

- Presentar conducción temeraria como objetivo del juego.
- Datos que permitan alterar sistemas reales de un monoplaza.
- Reproducir accidentes de forma gratuita o sensacionalista.

## Pendientes

- [ ] Definir valores por defecto de cada variable por tipo de circuito.
- [ ] Prototipar el ciclo básico en un motor simple.
- [ ] Ajustar el modelo de degradación de neumáticos.
- [ ] Agregar fuentes técnicas públicas a [`manuales/fuentes.md`](../../../manuales/fuentes.md).

## 🎓 Cierre de clase

- **Actividad:** Diseña un escenario educativo de Fórmula 1 basado en objetivo, variables, estados, ciclo y escenarios de simulación, con entradas, estados, variables y criterio de cierre.
- **Evidencia:** Ficha de escenario y diagrama de estados.
- **Criterio de aprobación:** El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [FIA-F1-2026](https://www.fia.com/regulations/formula-1): Formula 1 Regulations, FIA. Uso: reglamento, arquitectura y seguridad de Fórmula 1.
- [US-NHTSA](https://www.nhtsa.gov/vehicle-safety): Vehicle Safety, NHTSA. Uso: seguridad de vehículos terrestres.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Reglamentos](../reglamentos/reglamentos-formula-1.md) · [➡️ Siguiente: Recursos](../recursos/recursos-formula-1.md)
