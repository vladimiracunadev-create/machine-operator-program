# 🎯 Ejercicios y autoevaluación del submarino

[🏠 Inicio](../../../README.md) · [🌊 Curso: Submarinos](../README.md) · 🎯 Ejercicios

Cierre del curso. Las preguntas repasan lo visto en los módulos 1 a 9 y las
respuestas están plegadas a propósito: intenta responder antes de abrirlas,
porque el valor está en el intento, no en la lectura. Todo se mantiene dentro del
marco público del curso: flotabilidad, lastre, presión e inmersión.

> 🦺 **Esto no es un examen.** No acredita nada ni sustituye la formación náutica
> certificada. Sirve para comprobar si el curso se entendió y para detectar qué
> módulo conviene releer. No trata táctica, doctrina ni sistemas de armas: ver
> [🦺 docs/04-seguridad-y-limites.md](../../../docs/04-seguridad-y-limites.md).

---

## 1. 📖 Comprueba lo que recuerdas

**1.1.** ¿Qué hace que un submarino baje, suba o se mantenga a una cota?

<details>
<summary>Ver respuesta</summary>

La relación entre su peso y el empuje del agua que desplaza (Arquímedes). Con
**flotabilidad positiva** (tanques con aire) pesa menos que el agua desplazada y
sube o flota; con **flotabilidad negativa** (tanques con agua) pesa más y baja;
con **flotabilidad neutra** peso y empuje se igualan y se mantiene a la cota.

Módulo 4: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-submarino.md).

</details>

**1.2.** ¿Cuál es la diferencia entre el control de lastre y los planos de
inmersión?

<details>
<summary>Ver respuesta</summary>

El **lastre** fija la flotabilidad general: se inundan los tanques con agua para
sumergirse y se purgan con aire comprimido para emerger. Los **planos de
inmersión**, horizontales, ajustan el ángulo y afinan la profundidad **al
avanzar**, es decir, necesitan flujo de agua para funcionar. Lastre para el
grueso, planos para el ajuste fino en movimiento. Confundirlos es uno de los
errores comunes que la simulación puede enseñar a evitar.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-submarino.md)
y [🧪 Principios y operación](../operacion/principios-submarino.md).

</details>

**1.3.** ¿Por qué existe una cota máxima segura?

<details>
<summary>Ver respuesta</summary>

Porque la presión del agua crece con la profundidad, aproximadamente una
atmósfera cada 10 metros, y el casco resistente está diseñado para soportar
hasta un límite. La cota máxima segura es ese límite de diseño, y superarlo
compromete la integridad estructural.

Módulos 3 y 5: [🔧 Sistemas mecánicos](../operacion/sistemas-mecanicos-submarino.md)
y [🧪 Principios y operación](../operacion/principios-submarino.md).

</details>

**1.4.** Ordena las fases de operación desde superficie hasta volver a
superficie.

<details>
<summary>Ver respuesta</summary>

1. **Superficie**: navegar flotando, ventilar, cargar batería, vigilar.
2. **Preparación de inmersión**: cerrar escotillas y chequear sistemas.
3. **Inmersión**: inundar lastre, planos abajo, control de cota.
4. **Navegación en cota**: flotabilidad neutra, rumbo y velocidad.
5. **Emersión**: purgar lastre con aire y controlar el ascenso.

Y fuera de esa secuencia normal está la **emergencia**: falla o riesgo, con
emersión de emergencia, achique y soporte vital.

Módulo 6: [🧪 Principios y operación](../operacion/principios-submarino.md).

</details>

**1.5.** ¿Qué son las termoclinas y por qué le importan a un submarino?

<details>
<summary>Ver respuesta</summary>

Son cambios de temperatura y densidad del agua con la profundidad. Como la
flotabilidad depende de la densidad del agua desplazada, atravesar una termoclina
produce derivas de cota que hay que corregir ajustando lastre y planos.

Módulos 6 y 9: [🌍 Entornos de trabajo](../operacion/entornos-submarino.md) y
[🧰 Recursos](../recursos/recursos-submarino.md).

</details>

**1.6.** Según CONVEMAR, ¿cómo debe navegar un submarino en el mar territorial?

<details>
<summary>Ver respuesta</summary>

En **superficie** y **enarbolando su pabellón** (Art. 20). El submarino es un
buque de guerra y se rige por normativa militar; en Chile, la Armada de Chile y
la Ley 18.948, no la Ley de Navegación mercante.

Módulo 8: [⚖️ Reglamentos](../reglamentos/reglamentos-submarino.md) y el
[⚖️ marco legal](../../../docs/07-marco-legal-chile.md).

</details>

---

## 2. 🔧 Aplica: casos de operación

**2.1.** Navegas en cota con flotabilidad neutra y la profundidad empieza a
aumentar sola, sin que hayas tocado nada. ¿Qué puede estar pasando?

<details>
<summary>Ver respuesta</summary>

La flotabilidad neutra es un equilibrio entre peso y empuje, y el empuje depende
de la densidad del agua. Si se atraviesa una **termoclina** o un cambio de
salinidad, esa densidad cambia y el equilibrio se rompe: lo que era neutro pasa a
ser ligeramente negativo y el submarino deriva hacia abajo.

Lo razonable es corregir con los planos de inmersión mientras se ajusta el lastre
para recuperar la neutralidad en la nueva densidad, vigilando el profundímetro y
el manómetro para no acercarse a la cota máxima segura.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-submarino.md).

</details>

**2.2.** Un operador novato en el simulador purga todos los tanques de golpe para
subir rápido. ¿Qué problema tiene esa maniobra?

<details>
<summary>Ver respuesta</summary>

Purgar todo el lastre deja el submarino con flotabilidad muy positiva, y el
ascenso deja de estar controlado: se emerge de forma brusca. Es uno de los
errores comunes que el curso identifica, junto con no controlar el ascenso al
volver a superficie.

Además, en superficie la maniobra no termina: el mar y el tráfico exigen
vigilancia y COLREG. La purga total con aire comprimido es el concepto de
**emersión de emergencia**, no la forma normal de emerger.

Módulos 4 y 5: [🎛️ Mandos e instrumentos](../mandos/manual-mandos-submarino.md)
y [🧪 Principios y operación](../operacion/principios-submarino.md).

</details>

**2.3.** Escenario de aguas costeras, poca profundidad. ¿Qué cambia respecto de
navegar en cota media en mar abierto?

<details>
<summary>Ver respuesta</summary>

El límite deja de venir solo de la presión y pasa a venir del **fondo**: en aguas
someras el riesgo típico es tocar fondo o chocar con obstáculos, no superar la
cota máxima segura. El margen vertical disponible se estrecha por abajo.

El ajuste es navegar con sonda y mantener un margen de seguridad respecto del
fondo, con la profundidad siempre visible.

Módulo 7: [🌍 Entornos de trabajo](../operacion/entornos-submarino.md).

</details>

---

## 3. 🎮 Lleva a la simulación

**3.1.** Quieres que el simulador enseñe la flotabilidad sin explicarla con
texto. ¿Qué variables expondrías y cómo las mostrarías?

<details>
<summary>Ver respuesta</summary>

Una idea razonable: mostrar juntos el **lastre** (0-100% de agua en tanques) y la
**flotabilidad** resultante (de negativa a positiva), de modo que el usuario vea
que al inundar tanques la barra de lastre sube y la flotabilidad cruza hacia
negativa, y que la profundidad empieza a crecer como consecuencia. Junto a eso, el
profundímetro y la presión externa (~1 atm cada 10 m) hacen visible por qué existe
una cota máxima.

Así el usuario entiende solo la cadena lastre → peso vs empuje → inmersión, que es
la que resume el diagrama de flotabilidad del curso.

Módulo 9: [🎮 Diseño de simulación](../simulacion/diseno-simulador-submarino.md).

</details>

**3.2.** El curso define tres niveles de realismo. ¿En cuál introducirías los
planos de inmersión y la gestión de aire y batería, y por qué no antes?

<details>
<summary>Ver respuesta</summary>

En el **nivel 3 (técnico)**. En el nivel 1 la meta es sumergir, emerger y
mantener una cota simple; añadir planos, oxígeno y batería ahí tapa lo que se
quiere enseñar. El nivel 2 introduce flotabilidad neutra, inercia y presión, que
son los conceptos físicos centrales. Los planos de inmersión, la gestión de aire
y batería y la cota máxima son detalle técnico y llegan al final.

Ver [🎚️ niveles de realismo](../../../docs/03-niveles-de-realismo.md).

</details>

---

## ✅ Autochequeo

- [ ] Puedo explicar la flotabilidad positiva, negativa y neutra.
- [ ] Distingo el control de lastre de los planos de inmersión.
- [ ] Sé por qué existe una cota máxima segura y cómo crece la presión.
- [ ] Puedo ordenar las fases de operación y decir qué ocurre en cada una.
- [ ] Conozco el marco público aplicable y qué exige CONVEMAR en mar territorial.
- [ ] Puedo nombrar tres variables que un simulador debería exponer.

Si alguna casilla queda vacía, el módulo que la cubre está enlazado en su
respuesta.

---

[🎓 Portada del curso](../README.md) · [⬅️ Anterior: Recursos](../recursos/recursos-submarino.md)
