<!-- clase-meta
tipo_documento: clase
clase: 8
codigo: TRENALTAVELO-08
curso: tren-alta-velocidad
titulo: "Reglamentos del tren de alta velocidad (Chile)"
modalidad: "estudio de casos"
duracion_minutos: 60
nivel: introductorio
prerrequisito: TRENALTAVELO-07
competencia: "cumplimiento_y_seguridad"
resultados_aprendizaje:
  - "Explicar ámbito, requisitos, seguridad, restricciones y aplicación en simulación con vocabulario propio de Tren de alta velocidad."
  - "Aplicar esos conceptos a una decisión segura o a un escenario de simulación de Tren de alta velocidad."
evidencia: "Ficha normativa con decisión y fuente trazable."
criterio_aprobacion: "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
fuentes: manuales/fuentes.md
ultima_revision: 2026-09-10
-->

# ⚖️ Reglamentos del tren de alta velocidad (Chile)

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · ⚖️ Reglamentos

Referencia educativa y de diseño de simulación. Las normas reales cambian; para
operar se deben consultar la autoridad ferroviaria y la ley vigente. Chile aún no
cuenta con alta velocidad comercial, por lo que este módulo trata el marco
ferroviario general y usa estandares internacionales como referencia. Marco
general en [`docs/07-marco-legal-chile.md`](../../../docs/07-marco-legal-chile.md),
sección 1.6 (Ferroviario).

## Ámbito

- País: Chile.
- Ley base: Ley General de Ferrocarriles (número y fecha por confirmar).
- Autoridad: MTT como regulador y EFE (Empresa de los Ferrocarriles del Estado)
  como operador estatal histórico.
- Tipo de vehículo: tren de alta velocidad sobre vía dedicada.
- No aplica licencia de vía pública: la conducción exige habilitación o
  certificación de maquinista (por confirmar).

## Habilitación y certificación del maquinista

- No existe una licencia de vía pública como en los vehículos de carretera.
- La conducción requiere **habilitación o certificación de maquinista**, con
  formación específica del sistema; los requisitos exactos en Chile quedan por
  confirmar.
- Como referencia se usan los **estandares internacionales de alta velocidad**,
  incluida la señalización embarcada ETCS/ERTMS.

## Requisitos y elementos de seguridad

| Tema | Norma | Requisito | Aplicación en simulación |
| --- | --- | --- | --- |
| Habilitación de maquinista | Marco ferroviario (por confirmar) | Certificación específica del sistema. | Modo habilitación antes de conducir. |
| Señalización en cabina | Estandar ETCS/ERTMS (referencia) | Respetar la velocidad objetivo del DMI. | Supervisión y frenado automático. |
| Vigilante / hombre muerto | Reglamento de operación (por confirmar) | Confirmar atención de forma periódica. | Frenado si no se confirma. |
| Vía dedicada | Estandar de alta velocidad (referencia) | Sin pasos a nivel, curvas amplias. | Trazado del escenario sin cruces. |
| Ancho de vía | Trocha internacional (referencia) | Valor exacto para Chile por confirmar. | Parámetro del escenario. |
| Documentos de operación | Marco ferroviario (por confirmar) | Autorización de circulación del tren. | Chequeo previo simulado. |

## Reglas de seguridad

- Respetar siempre la velocidad objetivo que muestra la señalización en cabina.
- Confirmar el dispositivo de hombre muerto o vigilante de forma periódica.
- Iniciar el frenado con la anticipación que exige la enorme distancia de frenado.
- Reducir la velocidad ante viento fuerte en viaductos o clima adverso.
- No abrir puertas sin el enclavamiento y con el tren alineado al andén.

## Restricciones

- Conducción solo por personal habilitado o certificado (por confirmar).
- Circulación sujeta a la asignación de vía y agujas del control de tráfico.
- Límites de velocidad según el tramo, el clima y el estado de la catenaria.

## Notas para simulación

- El núcleo educativo es la gestión de la energía cinética: distancia de frenado,
  aerodinámica y respeto de la señal objetivo.
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Modelar la supervisión ETCS como frenado automático al exceder el límite.
- Marcar como por confirmar los datos legales locales que aún no existen en Chile.
- Registrar cada norma usada en
  [`manuales/fuentes.md`](../../../manuales/fuentes.md). Fuente institucional:
  <https://www.efe.cl>.

## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **Ámbito, Habilitación y certificación del maquinista, Requisitos y elementos de seguridad y Reglas de seguridad** a **interrumpir la cadena que podría producir perder margen por interpretar tarde una restricción a velocidad elevada**?

### Explicación razonada

La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «perder margen por interpretar tarde una restricción a velocidad elevada» se controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de Tren de alta velocidad.

Esta clase se conecta con el resto del curso mediante **estabilidad dinámica y crecimiento de la energía con el cuadrado de la velocidad**. El hilo de
seguridad consiste en reconocer a tiempo **perder margen por interpretar tarde una restricción a velocidad elevada** y poder justificar la decisión
**cumplir la curva de frenado con anticipación y sin correcciones bruscas**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **catenaria → electrónica de potencia → motores distribuidos → rueda-carril**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [Railroad Operating Practices](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0) aporta operación, señalización y competencias ferroviarias;
[Human Factors: Tasks and Demands](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands) se usa para factores humanos y carga de trabajo. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

1. **Describir el daño:** explica cómo se llegaría a **perder margen por interpretar tarde una restricción a velocidad elevada** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **cumplir la curva de frenado con anticipación y sin correcciones bruscas** es una decisión preventiva y verificable.

### Comprueba tu comprensión

1. ¿Qué mecanismo concreto conduce a **perder margen por interpretar tarde una restricción a velocidad elevada**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>

## 🎓 Cierre de clase

- **Actividad:** Analiza dos casos de Tren de alta velocidad; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación.
- **Evidencia:** Ficha normativa con decisión y fuente trazable.
- **Criterio de aprobación:** Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional.
- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.

### Fuentes de esta clase

- [US-FRA-OPS](https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0): Railroad Operating Practices, Federal Railroad Administration. Uso: operación, señalización y competencias ferroviarias.
- [US-FRA-HF](https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands): Human Factors: Tasks and Demands, Federal Railroad Administration. Uso: factores humanos y carga de trabajo.
- [NASA-FLIGHT](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/): Beginner's Guide to Aeronautics, NASA. Uso: contraste con física y vuelo reales.

> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual
> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.

---

[⬅️ Anterior: Entornos de trabajo](../operacion/entornos-tren-alta-velocidad.md) · [➡️ Siguiente: Diseño de simulación](../simulacion/diseno-simulador-tren-alta-velocidad.md)
