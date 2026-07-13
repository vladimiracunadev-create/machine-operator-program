# 🧪 Principios y operacion del barco mercante

[🏠 Inicio](../../../README.md) · [🚢 Curso: Barcos mercantes](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion nautica certificada
(STCW) ni los manuales del fabricante. Describe como se opera un buque mercante
en simulacion y que principios fisicos conviene representar.

## Principios de funcionamiento

- **Flotacion**: el buque flota porque desplaza un peso de agua igual al suyo
  (principio de Arquimedes). El empuje vertical sostiene el casco.
- **Propulsion**: la helice empuja agua hacia atras y, por reaccion, el buque
  avanza hacia adelante (tercera ley de Newton).
- **Gobierno**: la pala del timon desvia el flujo de agua en popa y genera una
  fuerza que hace rotar el buque; necesita velocidad para responder.
- **Inercia**: por su gran masa, el buque tarda mucho en acelerar, frenar o
  girar; toda maniobra se anticipa con minutos y millas de margen.
- **Estabilidad**: el reparto de peso, la carga y el lastre determinan que el
  buque vuelva a la vertical tras una escora.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Preparacion | Revision antes de zarpar | Maquina, gobierno, cartas, combustible. |
| Desatraque | Salir del muelle | Thruster, cabos, remolcadores si aplica. |
| Salida de puerto | Navegar el canal | Baja velocidad, practico, senales. |
| Navegacion | Travesia en mar abierto | Rumbo, guardias, vigilancia radar. |
| Aproximacion | Acercarse al puerto destino | Reducir velocidad con anticipacion. |
| Atraque | Amarrar en muelle | Maniobra fina, thruster, cabos. |
| Cierre | Dejar segura la nave | Maquina parada, amarre firme, guardias. |

## Maniobras: idea general

1. Anticipar toda maniobra por la **inercia** del buque.
2. Reducir la velocidad **mucho antes** de la aproximacion.
3. Usar el **thruster de proa** y remolcadores en espacios estrechos.
4. Respetar las **reglas de rumbo** COLREG frente a otros buques.
5. Vigilar calado y **profundidad** para no varar.

## Errores comunes que la simulacion puede ensenar a evitar

- Subestimar la distancia de frenado por la inercia.
- Intentar gobernar con el buque casi parado (el timon no responde).
- Ignorar la profundidad bajo la quilla y varar.
- No respetar la prioridad de paso segun COLREG.
- Mala estiba o lastre que compromete la estabilidad.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: rumbo, velocidad y respetar senales basicas.
- **Nivel 2 (simplificado)**: agregar inercia, distancia de frenado y viento.
- **Nivel 3 (tecnico)**: sumar estabilidad, calado, corrientes y maniobra de
  puerto con thruster y remolcadores.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-barco-mercante.md) · [➡️ Siguiente: Entornos de trabajo](entornos-barco-mercante.md)
