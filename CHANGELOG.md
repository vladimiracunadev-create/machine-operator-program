# Changelog

Todos los cambios relevantes de este repositorio se documentan aqui.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto usa [Versionado Semantico](https://semver.org/lang/es/).

## [No publicado]

### Anadido

- Seis cursos reales mas: 🏎️ Formula 1 (reglamento FIA), 🪖 tanques (militar, marco publico), 🛗 ascensores (Ley 20.296), 🚀 cohetes lanzadores, 🛬 transbordadores y 🛰️ estacion espacial ISS. Total: 29 vehiculos reales.
- Cuatro naves de ficcion mas: 🌀 teletransportador (ciencia ficcion) y la serie ⚡📦🚀 Thunderbird 1, 2 y 3 (analisis fisico educativo, contenido original con aviso de derechos). Total: 12 naves de ficcion.
- Curso de 🕹️ drones (RPAS): aeronaves pilotadas a distancia, multirotor y ala fija, con marco DGAC / DAN 151.
- Tres naves de ficcion mas: 🦅 Halcon Milenario, 🏯 SDF-1 y 🌑 Estrella de la Muerte (analisis fisico educativo, contenido original con aviso de derechos). Total: 8 naves de ficcion.
- Seis cursos reales mas: 🚆 tren de pasajeros, 🚄 tren de alta velocidad y 🚂 tren de carga (ferroviarios); ⚓ grua portuaria y 🗼 grua torre (izaje fijo); 🚁 helicopteros (aereo).
- Nueva seccion **naves de ficcion** (`vehiculos-fantasticos/`), educativa y separada de los vehiculos reales, con 5 cursos (DeLorean, caza estelar, nave de exploracion, Nautilus, caza transformable) y aviso de derechos de autor.
- Marco legal ampliado con ferroviario (Ley General de Ferrocarriles, EFE), maquinaria de izaje fija (Ley 16.744, D.S. 594) y helicopteros (DAN 61).
- Cinco cursos nuevos integrados por dominio: 🚛 camiones, 🚜 tractores y 🚧 maquinaria de construccion (terrestres), ⛴️ cruceros (maritimo de pasajeros) y 🛫 aviones de pasajeros (aviacion comercial).
- Cada vehiculo se documenta ahora como un **curso completo** de 9 modulos: portada con diagramas, historia, caracteristicas, sistemas mecanicos en profundidad, mandos, principios, entornos de trabajo, reglamentos y diseno de simulacion.
- Guia de estilo y estructura de curso `docs/08-guia-de-estilo-y-curso.md`: iconografia, navegacion entre modulos y uso de diagramas Mermaid.
- Diagramas Mermaid (flujos, estados, lineas de tiempo, mapas mentales) e iconografia consistente en todos los cursos.
- Navegacion interconectada: breadcrumbs y enlaces anterior/siguiente en cada modulo; README raiz rehecho como catalogo de cursos.
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
