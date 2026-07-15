# 🎛️ Mandos e instrumentos del Thunderbird 3

[🏠 Inicio](../../../README.md) · [🚀 Curso: Thunderbird 3](../README.md) · 🎛️ Mandos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

## Vista general

El puesto de mando de un cohete de rescate realista se parece más a una sala de
control que a una cabina de avión. Durante el ascenso, gran parte del vuelo la
lleva la computadora de guiado: la tripulación supervisa el empuje, la
inclinación de la trayectoria y el momento de soltar cada etapa. La clave no es
"pilotar" al detalle, sino gestionar bien el propelente y la velocidad.

## Mapa de controles

| Zona | Control | Tipo | Función | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Mano derecha | Palanca de empuje | Palanca lineal | Regular la potencia del motor principal | Alta | Define la aceleración del ascenso. |
| Mano izquierda | Control de inclinación | Mando 2 ejes | Orientar la tobera para inclinar la subida | Alta | Cambia el reparto entre altura y velocidad. |
| Panel central | Secuencia de etapas | Botonera | Preparar y confirmar la separación | Alta | Soltar una etapa vacía es irreversible. |
| Panel derecho | Gestión de propelente | Botonera | Vigilar y repartir el propelente | Alta | El propelente es el recurso crítico. |
| Panel izquierdo | Modo de guiado | Selector | Elegir asistencia de la computadora | Media | Incluye ascenso automático. |
| Consola | Instrumentos | Pantallas | Mostrar estado y sensores | Alta | Ver sección de instrumentos. |

## Instrumentos principales

| Instrumento | Muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Velocidad horizontal | Velocidad lateral ganada | m/s | Alta | Es la que define si se llega a órbita. |
| Altura | Distancia sobre el suelo | km | Media | Subir alto no basta por si solo. |
| Nivel de propelente | Propelente restante | porcentaje | Alta | Sin propelente se acaba el ascenso. |
| Delta-v restante | Cambio de velocidad disponible | m/s | Alta | Mide cuanto queda por acelerar. |
| Aceleración | Empuje frente a masa actual | g | Media | Crece al vaciarse los tanques. |
| Temperatura del escudo | Calor en la reentrada | grados | Alta | Crítica al regresar de órbita. |

## Entradas de simulación

| Acción | Teclado | Controlador | Comentarios |
| --- | --- | --- | --- |
| Aumentar empuje | Flecha arriba | Gatillo derecho | Sube la potencia del motor. |
| Reducir empuje | Flecha abajo | Gatillo izquierdo | Baja la potencia del motor. |
| Inclinar hacia horizontal | D | Stick derecho | Cambia altura por velocidad lateral. |
| Enderezar hacia vertical | A | Stick izquierdo | Prioriza ganar altura. |
| Soltar etapa | Barra espaciadora | Botón central | Suelta la etapa vacía actual. |
| Iniciar reentrada | R | Botón lateral | Frena para salir de órbita. |
| Guiado automático | G | Botón superior | Deja el ascenso a la computadora. |

## Estados del sistema

| Estado | Descripción | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En rampa | Cohete listo, motor apagado | Velocidad cero | Revisar sistemas, iniciar cuenta atrás. |
| Ascenso vertical | Sube recto saliendo del aire denso | Altura creciente | Regular empuje, preparar inclinación. |
| Inclinación | Empuja hacia la horizontal | Velocidad lateral creciente | Ajustar dirección, soltar etapas. |
| En órbita | Velocidad lateral suficiente | Delta-v estable | Planificar el regreso. |
| Reentrada | Regreso a la atmósfera | Escudo caliente | Controlar frenado, desplegar frenos. |

## Observaciones ergonomicas

- La interfaz debe mostrar a la vez la altura y la velocidad horizontal, porque
  es la velocidad lateral la que decide si se alcanza la órbita.
- El nivel de propelente y el delta-v restante son el recurso más valioso: cuando
  se agotan, ya no hay como seguir acelerando.
- La separación de etapas debe pedir confirmación, porque es irreversible.
- Conviene un modo de guiado automático para principiantes que reparta bien el
  empuje entre ganar altura y ganar velocidad lateral.

---

[⬅️ Anterior: Sistemas mecánicos](../operacion/sistemas-mecanicos-thunderbird-3.md) · [➡️ Siguiente: Principios y operación](../operacion/principios-thunderbird-3.md)
