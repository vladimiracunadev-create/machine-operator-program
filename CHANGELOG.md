# Changelog

Todos los cambios relevantes de este repositorio se documentan aqui.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto usa [Versionado Semantico](https://semver.org/lang/es/).

## [No publicado]

### Anadido

- Marco legal tecnico `docs/07-marco-legal-chile.md` (normativa chilena e internacional por tipo de vehiculo).
- Reglamentos por vehiculo con la ley aplicable en los 11 tipos (civiles con licencia y seguridad; militares con marco publico e historico; espacial con tratados).
- Registro de fuentes ampliado en `manuales/fuentes.md` con manuales oficiales (CONASET, DGAC, DIRECTEMAR) y legislacion (BCN).
- Endurecimiento de CI: `.gitattributes` (EOL LF), `.editorconfig`, `.github/dependabot.yml`, `SECURITY.md`, `.lycheeignore`.
- Nuevos jobs en CI: auditoria de workflows con `actionlint` y `zizmor`; `persist-credentials: false` y `timeout-minutes` en todos los jobs.
- Workflow `enlaces.yml`: verificacion de enlaces internos y externos con lychee (PR, programado y manual).
- Licencia MIT (`LICENSE`).
- Guia de contribucion (`CONTRIBUTING.md`) y codigo de conducta (`CODE_OF_CONDUCT.md`).
- Configuracion de `markdownlint-cli2` (`.markdownlint-cli2.jsonc`).
- Plantillas de issues y de Pull Request en `.github/`.
- Guias generales de `operacion/` y `recursos/` para completar la simetria de secciones.
- Documentacion completa del vehiculo `motos` (ficha, mandos, operacion, historia, reglamentos y simulacion) como ejemplo de referencia.
- Validador de estructura y enlaces internos (`scripts/validar_estructura.py`).
- Workflow de CI que valida estructura, estilo Markdown y enlaces (`.github/workflows/validar-documentacion.yml`).

## [0.1.0] - 2026-07-12

### Anadido

- Base documental del multisimulador: `docs/`, `plantillas/`, `vehiculos/` y secciones generales.
- Estructura comun de 7 secciones por vehiculo para 11 tipos de maquina.
- Scripts de PowerShell para publicar y preparar repositorios.
