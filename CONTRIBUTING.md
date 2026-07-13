# Guia de contribucion

Gracias por tu interes en el multisimulador de mandos. Este repositorio es
documental: se construye vehiculo por vehiculo con fuentes publicas y criterios
de seguridad claros. Toda contribucion debe respetar esa linea.

## Antes de empezar

1. Lee `README.md` para entender el alcance y la estructura.
2. Lee `docs/04-seguridad-y-limites.md`. Es la regla mas importante del repositorio.
3. Revisa `docs/02-metodologia-documental.md` para saber como se investiga y redacta.
4. Elige un vehiculo o una seccion desde `docs/06-plan-vehiculos.md`.

## Que se acepta

- Fichas de vehiculo, mandos, historia, reglamentos y diseno de simulacion.
- Fuentes publicas, academicas o de fabricante con su procedencia registrada.
- Correcciones de estilo, enlaces rotos, tablas y glosario.
- Mejoras a plantillas, scripts de validacion y documentacion general.

## Que no se acepta

- Procedimientos tacticos reales, uso de armas o evasion de controles.
- Informacion clasificada, restringida, filtrada o no publica.
- Manuales presentados como sustituto de entrenamiento certificado.
- Detalles tecnicos sensibles de sistemas militares modernos.

Cuando un vehiculo tenga uso militar o de alto riesgo, limita el aporte a
historia publica, funcion general, principios fisicos, mandos de simulacion no
sensibles, roles generales de tripulacion y reglas de seguridad.

## Flujo de trabajo

1. Crea una rama descriptiva, por ejemplo `docs/motos-mandos`.
2. Parte siempre desde una plantilla de `plantillas/`.
3. Escribe en espanol claro, siguiendo el estilo del repositorio.
4. Registra las fuentes que uses en `manuales/fuentes.md`.
5. Valida en local antes de abrir el Pull Request (ver siguiente seccion).
6. Abre el Pull Request contra `main` y completa la plantilla.

## Validacion local

El repositorio incluye un validador de estructura y un linter de Markdown. Ambos
corren tambien en CI, asi que conviene ejecutarlos antes de subir cambios.

```bash
# Estructura del repositorio y enlaces internos
python scripts/validar_estructura.py

# Estilo de Markdown (requiere Node)
npx markdownlint-cli2 "**/*.md"
```

Si `validar_estructura.py` termina con codigo 0 y markdownlint no reporta
errores, tu cambio deberia pasar CI en verde.

## Convenciones de estilo

- Un `# Titulo` unico por archivo, al inicio.
- Secciones con `##` y `###`; evita saltar niveles.
- Tablas para mandos, instrumentos y glosarios.
- Bloques de codigo siempre con lenguaje (` ```text `, ` ```bash `).
- Enlaces internos relativos a la raiz del repositorio.
- Espanol neutro; el repositorio usa texto sin tildes por consistencia.

## Codigo de conducta

Al participar aceptas el `CODE_OF_CONDUCT.md`.
