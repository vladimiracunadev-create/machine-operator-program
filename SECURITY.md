# Política de seguridad

Este es un repositorio documental. No ejecuta servicios ni procesa datos de
usuarios, por lo que su superficie de riesgo es acotada. Aun así, cuidamos dos
aspectos: la integridad de la cadena de suministro del CI y el cumplimiento de
las reglas de contenido del proyecto.

## Reportar un problema

Si encuentras alguno de estos casos, abre un issue (o contacta al responsable
del repositorio si prefieres discreción):

- Contenido que viole `docs/04-seguridad-y-limites.md` (material sensible,
  procedimientos tacticos reales, información restringida).
- Un enlace que apunte a material peligroso o no permitido.
- Un problema en los workflows de GitHub Actions (permisos, acciones no
  pineadas, inyección de comandos).
- Datos personales publicados por error.

## Medidas de seguridad del repositorio

- Todas las acciones de GitHub Actions se fijan por SHA de commit.
- Los workflows usan `permissions: contents: read` por defecto.
- El checkout no persiste credenciales (`persist-credentials: false`).
- Dependabot vigila y actualiza las acciones semanalmente.
- Los workflows se auditan con `actionlint` y `zizmor`.

## Alcance

Este proyecto no ofrece garantias de exactitud legal ni técnica. Ver el aviso de
`docs/04-seguridad-y-limites.md` y `docs/07-marco-legal-chile.md`.
