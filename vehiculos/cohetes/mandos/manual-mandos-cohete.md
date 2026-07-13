# 🎛️ Mandos e instrumentos del cohete

[🏠 Inicio](../../../README.md) · [🚀 Curso: Cohetes](../README.md) · 🎛️ Mandos

## Vista general

Un cohete moderno no se "pilota" desde una cabina como una moto: lo dirige un
**computador de vuelo** a bordo, mientras un **control de mision** en tierra lo
vigila y toma decisiones de alto nivel. El puesto de mando es, por tanto, una
sala con consolas de telemetria y una cuenta atras coordinada. La tripulacion,
cuando la hay, viaja en una capsula sobre el cohete y supervisa el ascenso.

## Mapa de controles

| Zona | Control | Tipo | Funcion | Prioridad | Comentarios |
| --- | --- | --- | --- | --- | --- |
| Tierra | Cuenta atras | Secuenciador | Coordinar el lanzamiento | Alta | Sincroniza cada sistema. |
| Tierra | Autorizacion de lanzamiento | Consola | Dar o negar el si final | Alta | Requiere todos los sistemas en verde. |
| Tierra | Corte de emergencia | Boton | Abortar el lanzamiento | Alta | Detiene la secuencia con seguridad. |
| Tierra | Seguimiento de trayectoria | Radar y telemetria | Vigilar el rumbo | Alta | Base de la seguridad de rango. |
| A bordo | Computador de vuelo | Automatico | Guiar y controlar el empuje | Alta | Corrige el rumbo en tiempo real. |
| A bordo | Control de motores | Automatico | Regular empuje y apagado | Alta | Ordena separacion de etapas. |
| Capsula | Panel de tripulacion | Pantallas | Supervisar el ascenso | Media | Permite abortar si hay tripulacion. |
| Capsula | Palanca de aborto | Manual | Escapar del cohete | Alta | Solo en vuelos tripulados. |

## Instrumentos y telemetria

| Instrumento | Mide o muestra | Unidad | Importancia | Notas |
| --- | --- | --- | --- | --- |
| Altitud | Altura sobre el suelo | km | Alta | Sigue el ascenso. |
| Velocidad | Rapidez respecto al suelo | m/s | Alta | Debe llegar a velocidad orbital. |
| Empuje de motores | Fuerza entregada | kN | Alta | Comparado con el peso actual. |
| Presion de tanques | Presion del propelente | bar | Alta | Evita fallas de las bombas. |
| Nivel de propelente | Propelente restante | porcentaje | Alta | Define cuando separar etapas. |
| Aceleracion | Fuerza g sobre la estructura | g | Media | Limita el esfuerzo estructural. |
| Estado de etapas | Conectada o separada | discreto | Alta | Marca cada separacion. |

## Entradas de simulacion

| Accion | Teclado | Controlador | Panel tactil | Comentarios |
| --- | --- | --- | --- | --- |
| Iniciar cuenta atras | Tecla C | Boton | Boton de cuenta | Arranca la secuencia. |
| Encender motores | Tecla espacio | Gatillo | Boton de ignicion | Solo con sistemas en verde. |
| Regular empuje | Shift y Ctrl | Gatillos | Barra de empuje | Ajusta la potencia. |
| Separar etapa | Tecla S | Boton | Boton de separacion | Al agotar el propelente. |
| Orientar el cohete | Teclas WASD | Stick | Zona de actitud | Mueve el motor orientable. |
| Retornar propulsor | Tecla R | Boton | Modo aterrizaje | Encendidos de reentrada y aterrizaje. |
| Abortar | Tecla A | Boton rojo | Boton de aborto | Detiene o escapa con seguridad. |

## Estados del sistema

| Estado | Descripcion | Indicadores | Acciones disponibles |
| --- | --- | --- | --- |
| En plataforma | Cohete cargado y listo | Checklist en verde | Cargar propelente, iniciar cuenta. |
| Cuenta atras | Secuencia previa al despegue | Reloj y estados | Continuar o abortar. |
| Ascenso | Subiendo con motores encendidos | Empuje y velocidad activos | Guiar, regular empuje, separar etapas. |
| Separacion | Se suelta una etapa | Estado de etapas | Encender etapa superior. |
| Retorno del propulsor | Primera etapa vuelve | Altitud y velocidad | Reentrada, guiado, aterrizaje. |
| Emergencia | Falla o riesgo | Alarmas activas | Abortar, cortar motores. |

## Observaciones ergonomicas

- La cuenta atras y el estado de cada sistema deben verse de un vistazo.
- El corte de emergencia y el aborto deben ser inconfundibles y accesibles.
- La telemetria clave (altitud, velocidad, empuje) debe estar siempre visible.
- En vuelos tripulados, la palanca de aborto tiene prioridad sobre todo lo demas.
- La interfaz debe dejar claro que casi todo el guiado es automatico.

---

[⬅️ Anterior: Sistemas mecanicos](../operacion/sistemas-mecanicos-cohete.md) · [➡️ Siguiente: Principios y operacion](../operacion/principios-cohete.md)
