# 🧰 Recursos del Thunderbird 2

[🏠 Inicio](../../../README.md) · [📦 Curso: Thunderbird 2](../README.md) · 🧰 Recursos

> ⚖️ Material educativo original; los derechos de las obras pertenecen a sus titulares.

Glosario especifico, enlaces y diagramas de apoyo del curso de transporte
pesado modular. Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Carga util | Masa aprovechable que lleva el vehiculo ademas de su peso propio. |
| Fraccion de carga util | Relacion entre la masa util y el peso total del conjunto. |
| Modulo | Contenedor o vaina intercambiable segun la mision. |
| Anclaje | Cierre que fija el modulo al bastidor de forma segura. |
| Bastidor | Estructura portante que sostiene el peso y los anclajes. |
| Empuje | Fuerza que impulsa el vehiculo; debe superar el peso para elevarlo. |
| Margen de empuje | Diferencia entre el empuje disponible y el peso total. |
| Centro de masa | Punto donde se equilibra todo el peso del conjunto. |
| Reparto de peso | Colocacion de la carga para mantener el centro de masa estable. |
| Tren de aterrizaje | Apoyos que reciben el peso del vehiculo al posarse. |

---

## 🗺️ Diagrama: peso frente a carga util

```mermaid
flowchart LR
    Estructura[Mas estructura] --> Peso[Sube el peso propio]
    Peso --> Menos[Queda menos carga util]
    Carga[Anadir modulo] --> Total[Sube el peso total]
    Total --> Empuje[Baja el margen de empuje]
    Menos --> Idea[El diseno busca el equilibrio]
    Empuje --> Idea
```

---

## 🔗 Enlaces y fuentes

- Portada del curso: [📦 Curso: Thunderbird 2](../README.md)
- Catalogo de naves de ficcion: [🌌 Naves de ficcion](../../README.md)
- Glosario general: [📖 docs/05-glosario-general.md](../../../docs/05-glosario-general.md)
- Niveles de realismo: [🎚️ docs/03-niveles-de-realismo.md](../../../docs/03-niveles-de-realismo.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, respetando el aviso de
derechos del catalogo de naves de ficcion.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-thunderbird-2.md)
