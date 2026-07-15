# 🧪 Principios y operación del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formación náutica certificada
(STCW) ni los manuales del fabricante. Describe cómo se opera un buque mercante
en simulación y que principios físicos conviene representar.

## Principios de funcionamiento

- **Flotación**: el buque flota porque desplaza un peso de agua igual al suyo
  (principio de Arquímedes). El empuje vertical sostiene el casco.
- **Propulsión**: la hélice empuja agua hacia atrás y, por reacción, el buque
  avanza hacia adelante (tercera ley de Newton).
- **Gobierno**: la pala del timón desvia el flujo de agua en popa y genera una
  fuerza que hace rotar el buque; necesita velocidad para responder.
- **Inercia**: por su gran masa, el buque tarda mucho en acelerar, frenar o
  girar; toda maniobra se anticipa con minutos y millas de margen.
- **Estabilidad**: el reparto de peso, la carga y el lastre determinan que el
  buque vuelva a la vertical tras una escora.

## Fases de operación

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Preparación | Revisión antes de zarpar | Máquina, gobierno, cartas, combustible. |
| Desatraque | Salir del muelle | Thruster, cabos, remolcadores si aplica. |
| Salida de puerto | Navegar el canal | Baja velocidad, práctico, señales. |
| Navegación | Travesía en mar abierto | Rumbo, guardias, vigilancia radar. |
| Aproximación | Acercarse al puerto destino | Reducir velocidad con anticipación. |
| Atraque | Amarrar en muelle | Maniobra fina, thruster, cabos. |
| Cierre | Dejar segura la nave | Máquina parada, amarre firme, guardias. |

## Maniobras: idea general

1. Anticipar toda maniobra por la **inercia** del buque.
2. Reducir la velocidad **mucho antes** de la aproximación.
3. Usar el **thruster de proa** y remolcadores en espacios estrechos.
4. Respetar las **reglas de rumbo** COLREG frente a otros buques.
5. Vigilar calado y **profundidad** para no varar.

## Errores comunes que la simulación puede enseñar a evitar

- Subestimar la distancia de frenado por la inercia.
- Intentar gobernar con el buque casi parado (el timón no responde).
- Ignorar la profundidad bajo la quilla y varar.
- No respetar la prioridad de paso según COLREG.
- Mala estiba o lastre que compromete la estabilidad.

## Relación con los niveles de realismo

- **Nivel 1 (educativo)**: rumbo, velocidad y respetar señales básicas.
- **Nivel 2 (simplificado)**: agregar inercia, distancia de frenado y viento.
- **Nivel 3 (técnico)**: sumar estabilidad, calado, corrientes y maniobra de
  puerto con thruster y remolcadores.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-barco-mercante.md) · [➡️ Siguiente: Entornos de trabajo](entornos-barco-mercante.md)
