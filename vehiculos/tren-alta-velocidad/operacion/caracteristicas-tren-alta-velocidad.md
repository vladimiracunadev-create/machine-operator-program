# 📋 Caracteristicas funcionales del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 📋 Caracteristicas

Que es un tren de alta velocidad, que configuraciones existen y para que sirve
cada una. Este modulo da el contexto antes de abrir la mecanica (Modulo 3).

---

## 🧭 Definicion

Un tren de alta velocidad es un tren disenado para circular por encima de unos
250 km/h sobre una via dedicada, sin cruces a nivel y con curvas amplias. A esa
velocidad la resistencia del aire domina, por lo que la aerodinamica y una via
especial son tan importantes como la potencia. Guia sobre rieles, de modo que no
tiene direccion libre: su ruta esta fijada por la via.

---

## 🧬 Caracteristicas clave

| Caracteristica | Descripcion |
| --- | --- |
| Velocidad de servicio | Por encima de 250 km/h en via dedicada. |
| Via dedicada | Sin pasos a nivel, con curvas amplias y peralte. |
| Aerodinamica | Nariz alargada; la resistencia del aire domina a alta velocidad. |
| Traccion distribuida | Motores repartidos en varios coches (EMU) en muchos disenos. |
| Energia cinetica enorme | Gran masa por gran velocidad; distancias de frenado de kilometros. |
| Senalizacion en cabina | ETCS/ERTMS; no hay senales laterales legibles a esa velocidad. |
| Alimentacion electrica | Pantografo unico sobre catenaria de alta tension. |

---

## 🗂️ Tipos de configuracion

```mermaid
flowchart TD
    Tren[🚄 Tren de alta velocidad] --> Traccion[Por traccion]
    Tren --> Contacto[Por contacto con la via]
    Traccion --> Distribuida[Distribuida EMU]
    Traccion --> Concentrada[Concentrada con locomotora]
    Contacto --> Rueda[Rueda-riel clasico]
    Contacto --> Maglev[Levitacion magnetica]
    Distribuida --> Shinkansen[Estilo Shinkansen]
    Concentrada --> TGV[Estilo TGV]
```

| Tipo | Como se distingue | Rasgo destacado |
| --- | --- | --- |
| Traccion distribuida (EMU) | Motores en varios coches | Mejor adherencia y aceleracion repartida. |
| Traccion concentrada | Locomotora en cabeza (y cola) | Coches remolcados sin motor. |
| Rueda-riel | Contacto clasico rueda de pestana | Compatible con red convencional. |
| Levitacion magnetica | Sin contacto fisico | Muy alta velocidad, via propia exclusiva. |
| Ancho internacional | Trocha estandar | Referencia comun; valor para Chile por confirmar. |

---

## 🎯 Para que se usa

- Unir grandes ciudades separadas por distancias medias de forma rapida.
- Competir con el avion en trayectos de algunos cientos de kilometros.
- Descongestionar corredores de transporte muy demandados.
- Ofrecer transporte publico masivo con alta frecuencia y puntualidad.
- Reducir el uso del automovil entre ciudades conectadas.

---

[⬅️ Anterior: Historia](../historia/historia-tren-alta-velocidad.md) · [➡️ Siguiente: Sistemas mecanicos](sistemas-mecanicos-tren-alta-velocidad.md)
