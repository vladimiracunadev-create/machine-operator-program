# Guía de contribución

Gracias por tu interés en el Programa de Operación y Simulación de Máquinas. Este repositorio es
documental: se construye vehículo por vehículo con fuentes públicas y criterios
de seguridad claros. Toda contribución debe respetar esa línea.

## Antes de empezar

1. Lee `README.md` para entender el alcance y la estructura.
2. Lee `docs/04-seguridad-y-limites.md`. Es la regla más importante del repositorio.
3. Revisa `docs/02-metodologia-documental.md` para saber cómo se investiga y redacta.
4. Elige un vehículo o una sección desde `docs/06-plan-vehiculos.md`.

## Que se acepta

- Fichas de vehículo, mandos, historia, reglamentos y diseño de simulación.
- Fuentes públicas, academicas o de fabricante con su procedencia registrada.
- Correcciones de estilo, enlaces rotos, tablas y glosario.
- Mejoras a plantillas, scripts de validación y documentación general.

## Que no se acepta

- Procedimientos tacticos reales, uso de armas o evasión de controles.
- Información clasificada, restringida, filtrada o no pública.
- Manuales presentados como sustituto de entrenamiento certificado.
- Detalles técnicos sensibles de sistemas militares modernos.

Cuando un vehículo tenga uso militar o de alto riesgo, limita el aporte a
historia pública, función general, principios físicos, mandos de simulación no
sensibles, roles generales de tripulación y reglas de seguridad.

## Flujo de trabajo

1. Crea una rama descriptiva, por ejemplo `docs/motos-mandos`.
2. Parte desde `plantillas/clase.md` y adapta objetivos, actividad y evaluación
   a la máquina; cambiar solo su nombre no es una contribución especializada.
3. Escribe en español claro, siguiendo el estilo del repositorio.
4. Registra las fuentes transversales en `manuales/fuentes.md`, las específicas
   en `vehiculos/<curso>/manuales/fuentes.md` y cítalas dentro de la clase.
5. Valida en local antes de abrir el Pull Request (ver siguiente sección).
6. Abre el Pull Request contra `main` y completa la plantilla.

## Validación local

El repositorio incluye un validador de estructura y un linter de Markdown. Ambos
corren también en CI, así que conviene ejecutarlos antes de subir cambios.

```bash
# Estructura del repositorio y enlaces internos
python scripts/validar_estructura.py

# Estilo de Markdown (requiere Node)
npx markdownlint-cli2 "**/*.md"
```

Si `validar_estructura.py` termina con código 0 y markdownlint no reporta
errores, tu cambio debería pasar CI en verde.

## Convenciones de estilo

- Un `# Titulo` único por archivo, al inicio.
- Secciones con `##` y `###`; evita saltar niveles.
- Tablas para mandos, instrumentos y glosarios.
- Bloques de código siempre con lenguaje (` ```text `, ` ```bash `).
- Enlaces internos relativos a la raíz del repositorio.
- Español neutro, claro y correctamente acentuado.

## Código de conducta

Al participar aceptas el `CODE_OF_CONDUCT.md`.
