---
tipo_documento: clase
clase: 4
codigo: ACORAZADOS-04
curso: acorazados
titulo: "Sistemas mecánicos del acorazado"
modalidad: "teórica aplicada"
duracion_minutos: 90
nivel: introductorio
prerrequisito: ACORAZADOS-03
competencia: "comprension_de_sistemas"
resultados_aprendizaje:
  - "Explicar Casco y flotación, Blindaje (concepto físico), Propulsión y Gobierno y timón con vocabulario propio de Acorazados."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Acorazados."
evidencia: "Esquema con flujos de energía, materia o información anotados."
criterio_aprobacion: "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
---

# 🔧 Sistemas mecánicos del acorazado

[🏠 Inicio](../../../README.md) · [🛡️ Curso: Acorazados](../README.md) · 🔧 Sistemas mecánicos

Este módulo describe, **solo con física pública**, como flota, avanza, gobierna y
se mantiene estable un gran buque blindado. No incluye sistemas de armas,
táctica ni datos sensibles. Es la base para entender los mandos (Módulo 5) y la
física de la navegación (Módulo 6).

```mermaid
flowchart LR
    subgraph Propulsion
        M[Planta propulsora] --> Ej[Línea de ejes] --> H[Hélices]
    end
    subgraph Gobierno
        Ti[Timón] --> Pa[Pala del timón]
    end
    subgraph Estructura
        Ca[Casco] --- Bl[Blindaje]
        Ca --- Ma[Mamparos estancos]
    end
    H --> Empuje[Empuje]
    Pa --> Rumbo[Rumbo]
    Ma --> Estabilidad[Estabilidad y flotabilidad]
```

---

## 1. 🚢 Casco y flotación

El casco es la estructura estanca que sostiene el buque por flotación. En un
acorazado es especialmente robusto por el peso del blindaje.

- **Obra viva y obra muerta**: parte sumergida y parte emergida del casco.
- **Reserva de flotabilidad**: volumen estanco por encima de la flotación.
- **Compartimentación**: mamparos que dividen el casco para limitar inundaciones.

| Parte | Función | Efecto en el buque |
| --- | --- | --- |
| Quilla | Eje estructural inferior | Rigidez y estabilidad. |
| Mamparos | Dividen el casco | Contienen inundaciones. |
| Doble fondo | Espacio inferior estanco | Protección y lastre. |
| Francobordo | Altura hasta cubierta | Reserva de flotabilidad. |

---

## 2. 🛡️ Blindaje (concepto físico)

El blindaje es acero de protección distribuido en el casco. Tratado aquí solo
como masa estructural y su efecto en la física del buque, no como sistema de
combate.

- **Peso**: el blindaje añade mucha masa, aumentando la inercia y el calado.
- **Distribución**: concentrar peso alto sube el centro de gravedad y reduce
  estabilidad; por eso el diseño cuida donde va cada tonelada.
- **Compromiso**: más protección implica más peso y menor velocidad o autonomía.

| Aspecto físico | Efecto |
| --- | --- |
| Masa del blindaje | Mayor inercia y calado. |
| Altura del peso | Afecta el centro de gravedad. |
| Reparto | Condiciona la estabilidad. |

---

## 3. 🔧 Propulsión

Convierte energía en empuje para mover una gran masa.

```mermaid
flowchart LR
    Caldera[Energía / calderas] --> Turbina[Turbinas o máquinas]
    Turbina --> Eje[Línea de ejes]
    Eje --> Helice[Hélices]
    Helice -->|empuja agua atrás| Empuje[Empuje adelante]
```

- **Planta propulsora**: históricamente máquinas de vapor o turbinas.
- **Línea de ejes**: transmite el giro a varias hélices.
- **Hélices**: empujan agua hacia atrás y, por reacción, mueven el buque.

---

## 4. ⚙️ Gobierno y timón

El gobierno cambia el rumbo desviando el flujo de agua en la popa.

- **Pala del timón**: al girar desvia el agua y hace rotar el buque.
- **Servomotor**: mueve la pala con la fuerza necesaria para la gran masa.
- **Inercia**: por su tamaño, el giro es amplio y lento.

---

## 5. ⚖️ Estabilidad y control de flotabilidad

La estabilidad depende del equilibrio entre peso, blindaje y lastre.

| Concepto | Definición | Riesgo si falla |
| --- | --- | --- |
| Centro de gravedad (G) | Punto donde actua el peso total. | Muy alto: inestable. |
| Metacentro (M) | Referencia de estabilidad al escorar. | G sobre M: riesgo de vuelco. |
| Escora | Inclinación transversal. | Excesiva por inundación asimétrica. |
| Contrainundación | Igualar peso entre costados. | Concepto de seguridad de flotabilidad. |
| Lastre | Agua de ajuste de peso. | Mal manejo: inestabilidad. |

---

## 🔁 Cómo se conecta todo

1. El **casco** aporta flotación y aloja el **blindaje**.
2. La **planta propulsora** genera potencia para las **hélices**.
3. El **timón** desvia el agua para cambiar el rumbo.
4. La **compartimentación** y el **lastre** cuidan la estabilidad.
5. Todo se opera de forma coordinada por la tripulación.

Con esto entendido, el
[Módulo 5: Mandos](../mandos/manual-mandos-acorazado.md) describe, a nivel
educativo, como se navega el buque desde el puente.

## 🎓 Cierre de clase

- **Actividad:** Dibuja un esquema funcional de Acorazados que conecte Casco y flotación, Blindaje (concepto físico), Propulsión y Gobierno y timón; después predice el efecto de una falla simulada.
- **Evidencia:** Esquema con flujos de energía, materia o información anotados.
- **Criterio de aprobación:** Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-NHHC-SHIPS](https://www.history.navy.mil/browse-by-topic/ships.html): Ships, Naval History and Heritage Command. Uso: historia pública de buques militares.
- [IMO-NAV](https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx): Safety of Navigation, International Maritime Organization. Uso: navegación, SOLAS, COLREG y STCW.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Modelos y variantes](../modelos/modelos-acorazado.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-acorazado.md)
