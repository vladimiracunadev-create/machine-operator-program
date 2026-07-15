# Changelog

Todos los cambios relevantes de este repositorio se documentan aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/)
y el proyecto usa [Versionado Semántico](https://semver.org/lang/es/).

## [No publicado]

### Corregido

- Ortografía acentuada en los 443 documentos: el corpus estaba escrito sin tildes
  ni enes ("documentacion", "vehiculo", "diseno"). Las rutas, los identificadores
  y el código quedan intactos; los enlaces internos siguen resolviendo.
- Coherencia del README: el mapa del repositorio decía "11 cursos" cuando hay 29,
  y el estado del proyecto daba por incompletos 40 de los 41 cursos, que sí
  cumplen la checklist. Los badges de CI apuntaban al nombre anterior del
  repositorio (`multi-piloto-navegacion`).
- El validador de estructura solo comprobaba que existieran las carpetas de cada
  sección, de modo que una sección vacía pasaba en verde; además la lista de
  cursos estaba fijada en el código y no detectaba los que sobraban.

### Añadido

- Seis cursos reales más: 🏎️ Fórmula 1 (reglamento FIA), 🪖 tanques (militar, marco público), 🛗 ascensores (Ley 20.296), 🚀 cohetes lanzadores, 🛬 transbordadores y 🛰️ estación espacial ISS. Total: 29 vehículos reales.
- Cuatro naves de ficción más: 🌀 teletransportador (ciencia ficción) y la serie ⚡📦🚀 Thunderbird 1, 2 y 3 (análisis físico educativo, contenido original con aviso de derechos). Total: 12 naves de ficción.
- Curso de 🕹️ drones (RPAS): aeronaves pilotadas a distancia, multirotor y ala fija, con marco DGAC / DAN 151.
- Tres naves de ficción más: 🦅 Halcón Milenario, 🏯 SDF-1 y 🌑 Estrella de la Muerte (análisis físico educativo, contenido original con aviso de derechos). Total: 8 naves de ficción.
- Seis cursos reales más: 🚆 tren de pasajeros, 🚄 tren de alta velocidad y 🚂 tren de carga (ferroviarios); ⚓ grúa portuaria y 🗼 grúa torre (izaje fijo); 🚁 helicópteros (aéreo).
- Nueva sección **naves de ficción** (`vehiculos-fantasticos/`), educativa y separada de los vehículos reales, con 5 cursos (DeLorean, caza estelar, nave de exploración, Nautilus, caza transformable) y aviso de derechos de autor.
- Marco legal ampliado con ferroviario (Ley General de Ferrocarriles, EFE), maquinaria de izaje fija (Ley 16.744, D.S. 594) y helicópteros (DAN 61).
- Cinco cursos nuevos integrados por dominio: 🚛 camiones, 🚜 tractores y 🚧 maquinaria de construcción (terrestres), ⛴️ cruceros (marítimo de pasajeros) y 🛫 aviones de pasajeros (aviación comercial).
- Cada vehículo se documenta ahora como un **curso completo** de 9 módulos: portada con diagramas, historia, características, sistemas mecánicos en profundidad, mandos, principios, entornos de trabajo, reglamentos y diseño de simulación.
- Guía de estilo y estructura de curso `docs/08-guia-de-estilo-y-curso.md`: iconografía, navegación entre módulos y uso de diagramas Mermaid.
- Diagramas Mermaid (flujos, estados, líneas de tiempo, mapas mentales) e iconografía consistente en todos los cursos.
- Navegación interconectada: breadcrumbs y enlaces anterior/siguiente en cada módulo; README raíz rehecho como catálogo de cursos.
- Marco legal técnico `docs/07-marco-legal-chile.md` (normativa chilena e internacional por tipo de vehículo).
- Reglamentos por vehículo con la ley aplicable en los 11 tipos (civiles con licencia y seguridad; militares con marco público e histórico; espacial con tratados).
- Registro de fuentes ampliado en `manuales/fuentes.md` con manuales oficiales (CONASET, DGAC, DIRECTEMAR) y legislación (BCN).
- Endurecimiento de CI: `.gitattributes` (EOL LF), `.editorconfig`, `.github/dependabot.yml`, `SECURITY.md`, `.lycheeignore`.
- Nuevos jobs en CI: auditoría de workflows con `actionlint` y `zizmor`; `persist-credentials: false` y `timeout-minutes` en todos los jobs.
- Workflow `enlaces.yml`: verificación de enlaces internos y externos con lychee (PR, programado y manual).
- Licencia MIT (`LICENSE`).
- Guía de contribución (`CONTRIBUTING.md`) y código de conducta (`CODE_OF_CONDUCT.md`).
- Configuración de `markdownlint-cli2` (`.markdownlint-cli2.jsonc`).
- Plantillas de issues y de Pull Request en `.github/`.
- Guías generales de `operacion/` y `recursos/` para completar la simetría de secciones.
- Documentación completa del vehículo `motos` (ficha, mandos, operación, historia, reglamentos y simulación) como ejemplo de referencia.
- Validador de estructura y enlaces internos (`scripts/validar_estructura.py`).
- Workflow de CI que valida estructura, estilo Markdown y enlaces (`.github/workflows/validar-documentacion.yml`).

## [0.1.0] - 2026-07-12

### Añadido

- Base documental del multisimulador: `docs/`, `plantillas/`, `vehiculos/` y secciones generales.
- Estructura común de 7 secciones por vehículo para 11 tipos de máquina.
- Scripts de PowerShell para publicar y preparar repositorios.
