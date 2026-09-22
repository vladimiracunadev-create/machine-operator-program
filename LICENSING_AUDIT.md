# Auditoría de licencias

**Repositorio:** `vladimiracunadev-create/machine-operator-program`

**Fecha de corte:** 22 de septiembre de 2026

**Resultado:** separación de licencias documentada; no se detectaron activos
binarios ni copias locales de manuales de terceros.

## Objetivo y método

La auditoría revisó el historial Git, autores, ramas, archivos versionados,
licencia original, estructura del corpus, registros de fuentes y automatización
de CI. La verificación se hizo sobre `main` en `1cd6864`, antes de aplicar estos
cambios.

Comandos principales: `git log --all`, `git shortlog -sne --all`,
`git log --follow -- LICENSE`, `git ls-files` y búsquedas de avisos de autoría,
licencia y procedencia.

## Hallazgos

1. El repositorio tenía 597 archivos versionados: 570 Markdown, 4 Python,
   2 PowerShell, 4 workflows YAML y archivos de configuración o marcadores.
2. La licencia MIT entró en el commit `29dd919` del 12 de julio de 2026 y no
   debe borrarse ni reinterpretarse retroactivamente.
3. El historial contiene 27 commits. El único autor humano registrado es
   Vladimir Acuña; `dependabot[bot]` figura como autor de un commit automatizado.
4. El proyecto mezcla infraestructura técnica con un corpus educativo extenso,
   pero el `README.md` describía todo el proyecto simplemente como MIT.
5. Hay 42 registros `manuales/fuentes.md`: uno general y uno por cada uno de
   los 41 cursos. Son catálogos de enlaces; el árbol no contiene PDFs de los
   manuales enlazados.
6. No hay imágenes, audio, video, tipografías, documentos ofimáticos ni otros
   activos binarios versionados.
7. `CODE_OF_CONDUCT.md` declara una adaptación del Contributor Covenant 2.1 y
   requiere conservar atribución y licencia de origen.
8. Los cursos sobre vehículos reales y ficticios mencionan fabricantes,
   organismos, estándares y franquicias; esas menciones no transfieren derechos
   sobre marcas u obras ajenas.

## Decisión aplicada

| Zona | Tratamiento |
| --- | --- |
| `scripts/`, `.github/` y configuración técnica | MIT |
| Currículo y material educativo original | CC BY-NC-SA 4.0 |
| Referencias, manuales, normas y material de fabricantes | Términos originales; no relicenciado |
| Activos futuros | Licencia individual obligatoria |

Se eligió MIT para el código, en vez de Apache-2.0, para preservar la
continuidad del proyecto y evitar un cambio innecesario. La licencia CC se
aplica solo a contenido que el proyecto puede licenciar. El acceso público al
repositorio se mantiene; `NoComercial` limita ciertos usos, no la visibilidad.

## Cambios realizados

- Se conservó `LICENSE` y se normalizó el nombre del titular.
- Se crearon `LICENSE-CONTENT.md`, `THIRD_PARTY_NOTICES.md`,
  `ASSET_LICENSES.md`, `docs/LICENSING_HISTORY.md`, `SAFETY_DISCLAIMER.md` y
  esta auditoría.
- Se sustituyó la declaración global MIT del `README.md` por una matriz de
  alcance y enlaces a los avisos.
- Se aclararon en `CONTRIBUTING.md` las condiciones aplicables a aportes y
  material de terceros.

## Riesgos residuales y mantenimiento

- Los registros de fuentes no siempre declaran una licencia concreta porque
  enlazan recursos externos. Antes de copiar cualquiera de ellos debe
  verificarse y registrarse su permiso exacto.
- La auditoría no decide la situación jurídica de nombres, hechos, extractos o
  posibles similitudes con obras de terceros en cada jurisdicción.
- Un colaborador no visible o mal identificado en Git debe ser atendido antes
  de relicenciar su aporte.
- Cada activo nuevo debe registrarse en `ASSET_LICENSES.md`; cada fuente nueva,
  en el registro del curso; y cada excepción, junto al archivo afectado.

## Criterios de aceptación

- [x] MIT histórico preservado.
- [x] Autoría normalizada solo donde la respalda el historial.
- [x] Código y contenido educativo separados.
- [x] Material externo excluido de la relicencia.
- [x] Aviso de seguridad independiente y explícito.
- [x] Matriz de licencias visible en el `README.md`.
- [x] Validaciones locales documentadas; el estado de CI se comprueba tras el
  push.

## Validación local

- `python scripts/validar_estructura.py`: 29 vehículos, 12 naves de ficción,
  451 clases y 4226 enlaces internos correctos.
- `npx --yes markdownlint-cli2 "**/*.md"`: 576 archivos Markdown, 0 problemas.
- Análisis de sintaxis con `ast.parse`: 4 archivos Python correctos.
- `git diff --check`: sin errores de espacios ni conflictos de parche.

Este documento es un registro técnico de diligencia, no asesoramiento jurídico.
