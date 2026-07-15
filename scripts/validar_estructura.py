#!/usr/bin/env python3
"""Validador de estructura y enlaces internos del programa.

Verifica, sin dependencias externas, que el repositorio documental mantenga su
forma esperada:

* la lista de cursos del disco coincide con la esperada, en ambos sentidos: se
  detecta tanto el curso que falta como el que sobra (un curso nuevo que nadie
  anadio aqui quedaria fuera de toda validacion sin que el CI se entere);
* cada curso conserva su README y las 7 secciones comunes, y cada seccion tiene
  contenido: comprobar solo que exista la carpeta dejaba pasar en verde una
  seccion vacia;
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
    "formula-1",
    "buses",
    "camiones",
    "tanques",
    "ascensores",
    "tren-pasajeros",
    "tren-alta-velocidad",
    "tren-carga",
    "gruas",
    "grua-portuaria",
    "grua-torre",
    "tractores",
    "maquinaria-construccion",
    "barcos-mercantes",
    "cruceros",
    "acorazados",
    "portaviones",
    "submarinos",
    "aviones-pequenos",
    "aviones-pasajeros",
    "aviones-combate",
    "helicopteros",
    "drones",
    "cohetes",
    "transbordadores",
    "estacion-espacial",
    "naves-espaciales",
]

# Naves de ficcion (seccion educativa aparte, en vehiculos-fantasticos/).
FANTASTICOS = [
    "delorean",
    "caza-estelar",
    "nave-exploracion",
    "nautilus",
    "caza-transformable",
    "halcon-milenario",
    "sdf-1",
    "estrella-de-la-muerte",
    "teletransportador",
    "thunderbird-1",
    "thunderbird-2",
    "thunderbird-3",
]

SECCIONES_VEHICULO = [
    "mandos",
    "manuales",
    "historia",
    "reglamentos",
    "operacion",
    "modelos",
    "simulacion",
    "recursos",
    "ejercicios",
]

# Secciones que todavia no se exige poblar. 'manuales/' guarda las fuentes
# publicas de cada curso y esta pendiente en todos: si se exigiera aqui, el CI
# quedaria rojo de forma permanente y dejaria de avisar de nada.
SECCIONES_EN_ESPERA = {"manuales"}

# Carpetas generales que deben existir en la raiz.
SECCIONES_GENERALES = [
    "docs",
    "plantillas",
    "vehiculos",
    "vehiculos-fantasticos",
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
    "docs/07-marco-legal-chile.md",
    "docs/08-guia-de-estilo-y-curso.md",
    "docs/09-carga-y-manejo.md",
    "plantillas/ficha-vehiculo.md",
    "plantillas/manual-mandos.md",
    "plantillas/reglamentos.md",
    "plantillas/historia.md",
    "plantillas/diseno-simulacion.md",
    "plantillas/checklist-documentacion.md",
]

# Enlaces Markdown en linea: captura el destino de [texto](destino).
PATRON_ENLACE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")

# Bloques de codigo cercados: sus enlaces son ejemplos, no se verifican.
PATRON_CODIGO = re.compile(r"```.*?```", re.DOTALL)


def existe(rel: str) -> bool:
    return (RAIZ / rel).exists()


def cursos_en_disco(raiz_rel: str) -> set[str]:
    base = RAIZ / raiz_rel
    if not base.is_dir():
        return set()
    return {d.name for d in base.iterdir() if d.is_dir()}


def seccion_tiene_contenido(seccion: Path) -> bool:
    """Una seccion cuenta como poblada si trae algun documento o material.

    El .gitkeep no basta: es justo el marcador de que la seccion sigue vacia.
    """
    return any(
        f.is_file() and f.name != ".gitkeep" for f in seccion.rglob("*")
    )


def validar_estructura(errores: list[str]) -> None:
    for seccion in SECCIONES_GENERALES:
        if not (RAIZ / seccion).is_dir():
            errores.append(f"Falta la carpeta general: {seccion}/")

    for doc in DOCUMENTOS_CLAVE:
        if not existe(doc):
            errores.append(f"Falta el documento clave: {doc}")

    for raiz_rel, lista in (("vehiculos", VEHICULOS), ("vehiculos-fantasticos", FANTASTICOS)):
        esperados = set(lista)
        en_disco = cursos_en_disco(raiz_rel)

        for sobrante in sorted(en_disco - esperados):
            errores.append(
                f"Curso sin registrar en {Path(__file__).name}: "
                f"{raiz_rel}/{sobrante}/ (anadelo a la lista para que se valide)"
            )

        for vehiculo in lista:
            base = RAIZ / raiz_rel / vehiculo
            if not base.is_dir():
                errores.append(f"Falta el vehiculo: {raiz_rel}/{vehiculo}/")
                continue
            if not (base / "README.md").is_file():
                errores.append(f"Falta README: {raiz_rel}/{vehiculo}/README.md")
            for seccion in SECCIONES_VEHICULO:
                ruta = base / seccion
                if not ruta.is_dir():
                    errores.append(
                        f"Falta la seccion: {raiz_rel}/{vehiculo}/{seccion}/"
                    )
                elif seccion not in SECCIONES_EN_ESPERA and not seccion_tiene_contenido(ruta):
                    errores.append(
                        f"Seccion vacia: {raiz_rel}/{vehiculo}/{seccion}/"
                    )


def validar_caracteres(errores: list[str]) -> None:
    """Busca caracteres de control sueltos en los documentos.

    Un .md no tiene ningun motivo para llevar un NUL ni un byte de control: si
    aparece uno, lo ha dejado un procesado automatico. Ni markdownlint ni el
    resto de comprobaciones los miran, asi que pasarian en verde con el fichero
    corrupto. Solo se admiten el salto de linea y el tabulador.
    """
    permitidos = {"\n", "\t"}
    for md in RAIZ.rglob("*.md"):
        rel_partes = md.relative_to(RAIZ).parts
        if rel_partes and rel_partes[0] in {".git", "node_modules", ".codex-docs-cache"}:
            continue
        texto = md.read_text(encoding="utf-8", errors="replace")
        for i, ch in enumerate(texto):
            if ch < " " and ch not in permitidos:
                rel = md.relative_to(RAIZ).as_posix()
                linea = texto.count("\n", 0, i) + 1
                errores.append(
                    f"Caracter de control U+{ord(ch):04X} en {rel}, linea {linea}"
                )
                break


def validar_enlaces(errores: list[str]) -> int:
    total = 0
    for md in RAIZ.rglob("*.md"):
        rel_partes = md.relative_to(RAIZ).parts
        if rel_partes and rel_partes[0] in {".git", "node_modules", ".codex-docs-cache"}:
            continue
        texto = md.read_text(encoding="utf-8", errors="replace")
        # Ignorar enlaces dentro de bloques de codigo (son ejemplos).
        texto = PATRON_CODIGO.sub("", texto)
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
    validar_caracteres(errores)
    enlaces = validar_enlaces(errores)

    vehiculos_ok = sum(
        1 for v in VEHICULOS if (RAIZ / "vehiculos" / v / "README.md").is_file()
    )
    fantasticos_ok = sum(
        1 for v in FANTASTICOS
        if (RAIZ / "vehiculos-fantasticos" / v / "README.md").is_file()
    )

    exigidas = len(SECCIONES_VEHICULO) - len(SECCIONES_EN_ESPERA)

    print("Validacion de estructura del Programa de Operacion y Simulacion de Maquinas")
    print(f"  Vehiculos verificados  : {vehiculos_ok}/{len(VEHICULOS)}")
    print(f"  Naves de ficcion       : {fantasticos_ok}/{len(FANTASTICOS)}")
    print(f"  Secciones por vehiculo : {len(SECCIONES_VEHICULO)}"
          f" ({exigidas} con contenido exigido,"
          f" {len(SECCIONES_EN_ESPERA)} en espera)")
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
