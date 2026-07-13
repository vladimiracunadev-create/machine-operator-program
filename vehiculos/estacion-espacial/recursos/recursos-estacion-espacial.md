# 🧰 Recursos de la estacion espacial

[🏠 Inicio](../../../README.md) · [🛰️ Curso: Estacion espacial (ISS)](../README.md) · 🧰 Recursos

Glosario especifico, enlaces y diagramas de apoyo del curso de estacion espacial.
Amplia el [glosario general](../../../docs/05-glosario-general.md).

---

## 📖 Glosario especifico

| Termino | Definicion |
| --- | --- |
| Estacion espacial | Habitat permanente en orbita donde vive y trabaja una tripulacion. |
| Modulo | Cada seccion presurizada que se une a otras para formar la estacion. |
| Nodo de union | Modulo que conecta otros modulos y reparte el paso interno. |
| Microgravedad | Estado de caida libre en que los objetos parecen flotar. |
| Soporte vital de ciclo cerrado | Sistema que recicla aire y agua para durar mas. |
| Acoplamiento | Union hermetica de una nave con la estacion. |
| EVA | Actividad extravehicular o caminata espacial en el exterior. |
| Esclusa de aire | Cierre que permite salir al vacio sin despresurizar toda la estacion. |
| Reimpulso | Maniobra para elevar la orbita que baja por el rozamiento. |
| Radiador | Panel que expulsa el calor sobrante al espacio. |

---

## 🗺️ Diagrama del soporte vital de ciclo cerrado

```mermaid
flowchart LR
    Aire[Aire usado] --> RetiraCO2[Retirar CO2]
    RetiraCO2 --> GeneraO2[Generar oxigeno]
    GeneraO2 --> AireLimpio[Aire respirable]
    AguaUsada[Agua usada] --> Recicla[Reciclar]
    Recicla --> AguaLimpia[Agua limpia]
    AguaLimpia --> Tripulacion[Tripulacion]
    AireLimpio --> Tripulacion
```

---

## 🔗 Enlaces y fuentes

- Marco legal: [⚖️ docs/07-marco-legal-chile.md](../../../docs/07-marco-legal-chile.md)
- Seguridad y limites: [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md)
- Registro de fuentes: [📚 manuales/fuentes.md](../../../manuales/fuentes.md)

Registrar cada recurso nuevo con su origen y licencia, siguiendo
[`recursos/README.md`](../../../recursos/README.md).

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Diseno de simulacion](../simulacion/diseno-simulador-estacion-espacial.md)
