# 🔧 Sistemas mecanicos del avion de combate

[🏠 Inicio](../../../README.md) · [✈️ Curso: Aviones de combate](../README.md) · 🔧 Sistemas mecanicos

Este modulo abre el avion por dentro **solo** en su fisica de vuelo y sus sistemas
generales de aeronave: celula, alas, superficies de control y motor a reaccion a
nivel divulgativo. **No** trata sistemas de armas ni de mision. Es la base tecnica
para entender los mandos (Modulo 4) y la fisica del vuelo (Modulo 5).

```mermaid
flowchart LR
    subgraph Estructura
        Ce[Celula / fuselaje] --- Al[Alas en flecha]
        Al --- Emp[Empenaje]
    end
    subgraph Control
        Ale[Alerones]
        Prof[Estabilizador / profundidad]
        Dir[Timon de direccion]
    end
    subgraph Propulsion
        Toma[Toma de aire] --> Reactor[Motor a reaccion]
        Reactor --> Tobera[Tobera de escape]
    end
    Al --> Ale
    Emp --> Prof
    Emp --> Dir
    Tobera --> Empuje[Empuje]
```

---

## 1. 🧱 Celula y fuselaje

La celula soporta las altas cargas del vuelo rapido y las maniobras.

- **Fuselaje**: cuerpo central; aloja la cabina y une alas y empenaje.
- **Estructura reforzada**: resiste las cargas G de las maniobras.
- **Materiales**: aleaciones ligeras y compuestos avanzados.
- **Empenaje**: superficies de cola que estabilizan y controlan el vuelo.

---

## 2. ✈️ Alas y sustentacion a alta velocidad

El ala genera sustentacion, pero su forma se adapta al vuelo rapido.

```mermaid
flowchart LR
    Aire[Flujo de aire rapido] --> Ala[Ala en flecha]
    Ala --> Retraso[Retrasa efectos del vuelo transonico]
    Ala --> Sust[Genera sustentacion]
    Retraso --> Control[Vuelo estable a alta velocidad]
    Sust --> Control
```

| Elemento del ala | Funcion |
| --- | --- |
| Ala en flecha | Retrasa efectos del vuelo cercano al sonido. |
| Ala delta | Buena para alta velocidad y estructura resistente. |
| Angulo de ataque | Relacion entre ala y aire; define la sustentacion. |
| Dispositivos de borde | Ajustan sustentacion en despegue y aterrizaje. |
| Perfil delgado | Reduce la resistencia a alta velocidad. |

---

## 3. 🎚️ Superficies de control

Controlan la aeronave en sus tres ejes, como en cualquier avion.

| Eje | Movimiento | Superficie | Mando en cabina |
| --- | --- | --- | --- |
| Longitudinal | Alabeo (rolido) | Alerones | Palanca a izquierda / derecha. |
| Lateral | Cabeceo (subir / bajar morro) | Estabilizador / profundidad | Palanca adelante / atras. |
| Vertical | Guinada (nariz izq / der) | Timon de direccion | Pedales. |

- **Mandos electricos (fly-by-wire)**: la palanca envia senales a computadores que
  mueven las superficies, mejorando la estabilidad y suavizando el control.
- **Estabilizador movil**: en muchos reactores la cola horizontal se mueve entera.
- **Compensacion automatica**: el sistema ayuda a mantener la actitud elegida.

---

## 4. ⚙️ Motor a reaccion (divulgativo)

El motor a reaccion impulsa el avion expulsando gases a gran velocidad.

```mermaid
flowchart LR
    Entra[Aire entra] --> Compresor[Compresor]
    Compresor --> Camara[Camara de combustion]
    Camara --> Turbina[Turbina]
    Turbina --> Sale[Gases salen por la tobera]
    Sale --> Empuje[Empuje hacia adelante]
```

| Etapa | Que hace |
| --- | --- |
| Toma de aire | Conduce el aire hacia el motor. |
| Compresor | Comprime el aire para la combustion. |
| Camara de combustion | Mezcla aire y combustible y los quema. |
| Turbina | Los gases mueven la turbina, que gira el compresor. |
| Tobera | Los gases salen a gran velocidad y generan empuje. |
| Posquemador (afterburner) | Empuje extra quemando mas combustible en la tobera. |

El principio es la tercera ley de Newton: expulsar masa hacia atras impulsa el
avion hacia adelante.

---

## 5. 🛞 Tren de aterrizaje y sistemas generales

- **Tren retractil**: se recoge en vuelo para reducir la resistencia.
- **Sistema hidraulico**: mueve tren, frenos y superficies de gran carga.
- **Sistema electrico**: alimenta instrumentos, pantallas y avionica.
- **Sistema de oxigeno y presurizacion**: sostiene al piloto a gran altitud.

---

## 6. 📟 Instrumentos y avionica (nivel general)

Informan al piloto y ayudan al control del vuelo.

| Sistema | Funcion general |
| --- | --- |
| Pantallas de vuelo | Muestran actitud, velocidad y altitud. |
| HUD (display frontal) | Proyecta datos de vuelo en el parabrisas. |
| Instrumentos de motor | Vigilan empuje, temperatura y combustible. |
| Sistemas de navegacion | Ayudan a ubicar la aeronave en el espacio. |
| Alertas de vuelo | Avisan situaciones como baja velocidad. |

> Este modulo no describe sistemas de mision, sensores tacticos ni armamento.

---

## 🔁 Como se conecta todo

1. El **motor a reaccion** produce **empuje** expulsando gases.
2. El empuje da **velocidad**, y las **alas** generan **sustentacion**.
3. Las **superficies de control**, con **mandos electricos**, orientan la aeronave.
4. La **celula reforzada** resiste las cargas del vuelo rapido.
5. Los **sistemas generales** sostienen al piloto y al avion en altitud.
6. Los **instrumentos** informan para volar con seguridad.

Con esto entendido, el [Modulo 4: Mandos](../mandos/manual-mandos-avion-combate.md)
muestra como el piloto opera estos sistemas generales.

---

[⬅️ Anterior: Caracteristicas](caracteristicas-avion-combate.md) · [➡️ Siguiente: Mandos e instrumentos](../mandos/manual-mandos-avion-combate.md)
