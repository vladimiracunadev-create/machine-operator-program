# 🧰 Recursos de la maquinaria de construcción

[🏠 Inicio](../../../README.md) · [🚧 Curso: Maquinaria de construcción](../README.md) · 🧰 Recursos

Glosario específico, enlaces y diagramas de apoyo del curso de maquinaria de
construcción. Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario específico

| Término | Definición |
| --- | --- |
| Hidráulica de trabajo | Sistema de aceite a presión que mueve brazos, cucharones y hojas. |
| Pluma (boom) | Primer tramo del brazo de una excavadora. |
| Balancín (arm) | Segundo tramo del brazo que acerca y aleja el cucharón. |
| Cucharón | Herramienta que recoge, corta y descarga material. |
| Hoja empujadora | Placa que empuja y nivela el terreno. |
| Escarificador (ripper) | Diente que rompe suelo duro antes de empujarlo. |
| Traslación | Movimiento de la máquina por giro de orugas o ruedas. |
| Giro diferencial | Virar moviendo una oruga más que la otra. |
| Momento de vuelco | Peso de la carga por su distancia al punto de vuelco. |
| Zona de exclusión | Radio de trabajo que debe estar libre de personas. |
| ROPS / FOPS | Estructuras que protegen del vuelco y de la caída de objetos. |

---

## 🗺️ Diagrama del ciclo de excavación

```mermaid
flowchart LR
    Penetrar[Penetrar el terreno] --> Arrastrar[Arrastrar cerrando el balancín]
    Arrastrar --> Llenar[Cerrar el cucharón]
    Llenar --> Levantar[Levantar la pluma]
    Levantar --> Girar[Girar al camión]
    Girar --> Descargar[Abrir el cucharón]
    Descargar --> Penetrar
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)
- Manuales oficiales del conductor (CONASET): ver el registro de fuentes.

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseño de simulación](../simulacion/diseno-simulador-maquinaria.md) · [➡️ Siguiente: Ejercicios](../ejercicios/ejercicios-maquinaria.md)
