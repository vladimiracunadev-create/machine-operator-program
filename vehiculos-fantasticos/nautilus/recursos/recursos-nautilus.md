# 🧰 Recursos del Nautilus

[🏠 Inicio](../../../README.md) · [🐙 Curso: Nautilus](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; el Nautilus de Julio Verne (1870) es de dominio publico; otros derechos pertenecen a sus titulares.

Glosario especifico, enlaces y diagramas de apoyo del curso del Nautilus. Amplia
el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Flotabilidad | Tendencia de un cuerpo a subir o bajar segun su peso frente al empuje del agua. |
| Principio de Arquimedes | Todo cuerpo sumergido recibe un empuje igual al peso del agua que desplaza. |
| Tanque de lastre | Deposito que se llena de agua o aire para variar el peso de la nave. |
| Flotabilidad neutra | Estado en que peso y empuje se igualan y la nave se mantiene a media agua. |
| Casco de presion | Estructura resistente que soporta la presion del agua a profundidad. |
| Profundidad limite | Profundidad maxima antes de que la presion aplaste el casco. |
| Timon de profundidad | Aleta horizontal que inclina la nave hacia arriba o hacia abajo. |
| Soporte vital | Conjunto de sistemas que mantienen el aire respirable a bordo. |

---

## 🗺️ Diagrama de flotabilidad

```mermaid
flowchart LR
    Peso[Peso de la nave] --> Balance[Comparacion]
    Empuje[Empuje de Arquimedes] --> Balance
    Balance -->|peso mayor| Baja[La nave baja]
    Balance -->|peso menor| Sube[La nave sube]
    Balance -->|iguales| Neutra[Flotabilidad neutra]
```

---

## 🔗 Enlaces y fuentes

- Glosario general: [📚 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Portada del curso: [🐙 README del Nautilus](../README.md)
- Catalogo de naves de ficcion: [🌌 README de ficcion](../../README.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-nautilus.md)
