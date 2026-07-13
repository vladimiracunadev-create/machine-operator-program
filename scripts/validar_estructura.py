#!/usr/bin/env python3
"""Validador de estructura y enlaces internos del multisimulador.

Verifica, sin dependencias externas, que el repositorio documental mantenga su
forma esperada:

* cada tipo de vehiculo conserva su README y las 7 secciones comunes;
* existen las secciones y documentos generales de referencia;
* todo enlace Markdown interno apunta a un archivo o carpeta que existe.

Se ejecuta en local (antes de commitear) y en CI. Termina con codigo 0 si todo
esta correcto y con codigo 1 si encuentra al menos un problema.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

# Vehiculos esperados y secciones comunes por vehiculo.
VEHICULOS = [
    "motos",
    "automoviles",
    "buses",
    "gruas",
    "barcos-mercantes",
    "acorazados",
    "portaviones",
    "submarinos",
    "aviones-pequenos",
    "aviones-combate",
    "naves-espaciales",
]

SECCIONES_VEHICULO = [
    "mandos",
    "manuales",
    "historia",
    "reglamentos",
    "operacion",
    "simulacion",
    "recursos",
]

# Carpetas generales que deben existir en la raiz.
SECCIONES_GENERALES = [
    "docs",
    "plantillas",
    "vehiculos",
    "mandos",
    "manuales",
    "historia",
    "reglamentos",
    "operacion",
    "recursos",
    "simuladores",
    "scripts",
]

# Documentos generales que no deberian faltar.
DOCUMENTOS_CLAVE = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "docs/00-indice-maestro.md",
    "docs/01-vision-del-proyecto.md",
    "docs/02-metodologia-documental.md",
    "docs/03-niveles-de-realismo.md",
    "docs/04-seguridad-y-limites.md",
    "docs/05-glosario-general.md",
    "docs/06-plan-vehiculos.md",
    "plantillas/ficha-vehiculo.md",
    "plantillas/manual-mandos.md",
    "plantillas/reglamentos.md",
    "plantillas/historia.md",
    "plantillas/diseno-simulacion.md",
    "plantillas/checklist-documentacion.md",
]

# Enlaces Markdown en linea: captura el destino de [texto](destino).
PATRON_ENLACE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")


def existe(rel: str) -> bool:
    return (RAIZ / rel).exists()


def validar_estructura(errores: list[str]) -> None:
    for seccion in SECCIONES_GENERALES:
        if not (RAIZ / seccion).is_dir():
            errores.append(f"Falta la carpeta general: {seccion}/")

    for doc in DOCUMENTOS_CLAVE:
        if not existe(doc):
            errores.append(f"Falta el documento clave: {doc}")

    for vehiculo in VEHICULOS:
        base = RAIZ / "vehiculos" / vehiculo
        if not base.is_dir():
            errores.append(f"Falta el vehiculo: vehiculos/{vehiculo}/")
            continue
        if not (base / "README.md").is_file():
            errores.append(f"Falta README: vehiculos/{vehiculo}/README.md")
        for seccion in SECCIONES_VEHICULO:
            if not (base / seccion).is_dir():
                errores.append(
                    f"Falta la seccion: vehiculos/{vehiculo}/{seccion}/"
                )


def validar_enlaces(errores: list[str]) -> int:
    total = 0
    for md in RAIZ.rglob("*.md"):
        rel_partes = md.relative_to(RAIZ).parts
        if rel_partes and rel_partes[0] in {".git", "node_modules", ".codex-docs-cache"}:
            continue
        texto = md.read_text(encoding="utf-8", errors="replace")
        for destino in PATRON_ENLACE.findall(texto):
            destino = destino.strip()
            # Ignorar externos, anclas puras, correos y protocolos.
            if destino.startswith(("http://", "https://", "mailto:", "#", "//")):
                continue
            # Quitar titulo opcional y ancla.
            destino = destino.split(" ", 1)[0]
            destino = destino.split("#", 1)[0]
            if not destino:
                continue
            if destino.startswith("/"):
                objetivo = RAIZ / destino.lstrip("/")
            else:
                objetivo = (md.parent / destino).resolve()
            total += 1
            if not objetivo.exists():
                rel = md.relative_to(RAIZ).as_posix()
                errores.append(f"Enlace roto en {rel}: {destino}")
    return total


def main() -> int:
    errores: list[str] = []
    validar_estructura(errores)
    enlaces = validar_enlaces(errores)

    vehiculos_ok = sum(
        1 for v in VEHICULOS if (RAIZ / "vehiculos" / v / "README.md").is_file()
    )

    print("Validacion de estructura del multisimulador")
    print(f"  Vehiculos verificados : {vehiculos_ok}/{len(VEHICULOS)}")
    print(f"  Secciones por vehiculo: {len(SECCIONES_VEHICULO)}")
    print(f"  Enlaces internos       : {enlaces}")

    if errores:
        print(f"\nSe encontraron {len(errores)} problema(s):")
        for e in errores:
            print(f"  - {e}")
        return 1

    print("\nTodo correcto: estructura completa y enlaces internos resueltos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
