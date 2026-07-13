# 🧪 Principios y operacion del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 🧪 Principios

Documento general, educativo e historico. Trata solo principios fisicos publicos
de flotabilidad, lastre, presion e inmersion. No sustituye formacion nautica ni
describe operacion militar real, tactica o sistemas de armas.

## Principios de funcionamiento

- **Flotacion (Arquimedes)**: el empuje del agua iguala al peso; si el peso sube
  por encima del empuje, el submarino baja.
- **Flotabilidad variable**: inundar los tanques de lastre aumenta el peso
  (sumergirse); vaciarlos con aire lo reduce (emerger).
- **Presion con la profundidad**: la presion crece aproximadamente una atmosfera
  cada 10 metros; por eso existe una cota maxima segura.
- **Gobierno en 3D**: el timon cambia el rumbo y los planos de inmersion ajustan
  la profundidad al avanzar.
- **Propulsion**: la helice empuja agua hacia atras y, por reaccion, el submarino
  avanza (tercera ley de Newton).

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Superficie | Navegar flotando | Ventilar, cargar bateria, vigilar. |
| Preparacion de inmersion | Alistar el buque | Cerrar escotillas, chequear sistemas. |
| Inmersion | Sumergirse | Inundar lastre, planos abajo, control de cota. |
| Navegacion en cota | Navegar sumergido | Flotabilidad neutra, rumbo y velocidad. |
| Emersion | Volver a superficie | Purgar lastre con aire, controlar ascenso. |
| Emergencia | Falla o riesgo | Emersion de emergencia, achique, soporte vital. |

## Control de profundidad: idea general

1. Para **sumergirse**, se inundan los tanques de lastre (peso mayor que empuje).
2. Los **planos de inmersion** ajustan el angulo y afinan la profundidad al
   avanzar.
3. Para **mantener cota**, se busca la **flotabilidad neutra**.
4. Para **emerger**, se **purgan** los tanques con aire comprimido.
5. Nunca superar la **cota maxima segura** por la presion.

## Errores comunes que la simulacion puede ensenar a evitar

- Descender mas alla de la cota segura ignorando la presion.
- Confundir el control de lastre con el de los planos de inmersion.
- Olvidar el nivel de oxigeno y la carga de bateria.
- Emerger de forma brusca perdiendo el control del ascenso.
- No cerrar y verificar sistemas antes de la inmersion.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: sumergir, emerger y mantener una cota simple.
- **Nivel 2 (simplificado)**: agregar flotabilidad neutra, inercia y presion.
- **Nivel 3 (tecnico)**: sumar planos de inmersion, gestion de aire, bateria y
  cota maxima.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-submarino.md) · [➡️ Siguiente: Entornos de trabajo](entornos-submarino.md)
