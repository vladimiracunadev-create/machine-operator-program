# 🎛️ Mandos e instrumentos del SDF-1

[🏠 Inicio](../../../README.md) · [🏯 Curso: SDF-1](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puente de mando de una nave-fortaleza realista no se parece a una cabina de
piloto, sino a la sala de control de una gran instalación. Nadie "conduce" una
mole de esta escala con reflejos: se coordinan equipos que vigilan estructura,
energía, propulsión y soporte vital. Como la nave es gigantesca, cada orden de
maniobra tarda en surtir efecto y hay que anticiparse mucho.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Puesto de mando | Ordenes de maniobra | Consola | Pedir cambios de rumbo o velocidad | Alta | La respuesta es lenta por la masa. |
| Estación de propulsión | Gestión de motores | Consola | Repartir empuje entre motores | Alta | Coordina el empuje sobre la mole. |
| Estación de estructura | Vigilancia de esfuerzos | Panel | Controlar tensión del casco | Alta | Evita maniobras que danen la estructura. |
| Estación de energía | Reparto de energía | Consola | Distribuir potencia entre sistemas | Alta | Propulsión, soporte vital, defensa. |
| Estación de soporte vital | Control de habitabilidad | Panel | Aire, agua y temperatura interior | Alta | Mantiene con vida a la tripulación. |
| Estación de sensores | Vigilancia del entorno | Pantallas | Detectar objetos y amenazas | Alta | El entorno se explora a gran distancia. |
| Puesto de coordinación | Comunicación interna | Consola | Enlazar a todas las estaciones | Media | Una nave-ciudad necesita coordinación. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Vector de velocidad | Dirección y módulo del movimiento | m/s | Alta | Cambia muy despacio por la masa. |
| Orientación global | Hacia donde apunta la nave | grados | Alta | Reorientar la mole lleva tiempo. |
| Tensión estructural | Esfuerzo en el casco | porcentaje | Alta | Limita la brusquedad de las maniobras. |
| Masa total | Nave, carga y tripulación | toneladas | Alta | Decide la aceleración posible. |
| Presupuesto de maniobra | Delta-v restante | m/s | Alta | Enorme gasto por la masa. |
| Calor acumulado | Calor interno pendiente de disipar | porcentaje | Alta | La superficie limita su evacuación. |
| Estado de soporte vital | Aire, agua, temperatura | varios | Alta | Vital para la tripulación. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Ordenar empuje adelante | Flecha arriba | Gatillo derecho | La nave tarda en acelerar. |
| Ordenar giro | A y D | Stick horizontal | Reorientar lleva mucho tiempo. |
| Vigilar estructura | E | Botón lateral | Muestra la tensión del casco. |
| Repartir energía | 1 a 5 | Cruceta | Prioriza propulsión, defensa o soporte vital. |
| Control de soporte vital | V | Botón de menu | Ajusta aire, agua y temperatura. |
| Alerta estructural | Barra espaciadora | Botón central | Suaviza una maniobra peligrosa. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En estación | Nave estable, sin maniobra | Velocidad casi constante | Vigilar sistemas, planificar. |
| Maniobra lenta | Cambio de rumbo o velocidad en curso | Tensión estructural visible | Ajustar empuje, cuidar la estructura. |
| Alerta estructural | Esfuerzos cerca del límite | Tensión alta | Reducir la maniobra, estabilizar. |
| Emergencia | Falla de energía o soporte vital | Alertas múltiples | Priorizar la vida de la tripulación. |

## Observaciones ergonomicas

- El puente debe mostrar a la vez el movimiento, la tensión estructural y el
  estado del soporte vital: son las tres cosas que pueden hundir la misión.
- Toda maniobra ha de anticiparse: la masa hace que la respuesta llegue tarde.
- La tensión estructural es tan crítica como el combustible: si se supera, la
  nave se dana.
- Conviene un modo asistido que límite automáticamente las maniobras bruscas
  para proteger la estructura.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-sdf-1.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-sdf-1.md)
