#!/usr/bin/env python3
"""Validador de estructura y enlaces internos del programa.

Verifica, sin dependencias externas, que el repositorio documental mantenga su
forma esperada:

* la lista de cursos del disco coincide con la esperada, en ambos sentidos: se
  detecta tanto el curso que falta como el que sobra (un curso nuevo que nadie
  anadio aqui quedaria fuera de toda validacion sin que el CI se entere);
* cada curso conserva su README, sus secciones comunes y sus 11 clases, y cada seccion tiene
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

from perfiles_pedagogicos import PERFILES

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

# Todas las secciones, incluida `manuales/`, deben estar pobladas.
SECCIONES_EN_ESPERA: set[str] = set()

# Las once clases son artefactos concretos, no solo carpetas con cualquier
# contenido. Los comodines absorben las diferencias de singular entre cursos.
PATRONES_CLASE = [
    "historia/*.md",
    "operacion/caracteristicas-*.md",
    "modelos/*.md",
    "operacion/sistemas-mecanicos-*.md",
    "mandos/*.md",
    "operacion/principios-*.md",
    "operacion/entornos-*.md",
    "reglamentos/*.md",
    "simulacion/*.md",
    "recursos/*.md",
    "ejercicios/*.md",
]

TOTAL_CLASES_ESPERADO = (len(VEHICULOS) + len(FANTASTICOS)) * len(PATRONES_CLASE)

CAMPOS_CLASE = {
    "tipo_documento",
    "clase",
    "codigo",
    "curso",
    "titulo",
    "modalidad",
    "duracion_minutos",
    "nivel",
    "prerrequisito",
    "competencia",
    "resultados_aprendizaje",
    "evidencia",
    "criterio_aprobacion",
    "fuentes",
    "ultima_revision",
}

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
    "docs/10-modelo-pedagogico.md",
    "plantillas/ficha-vehiculo.md",
    "plantillas/manual-mandos.md",
    "plantillas/reglamentos.md",
    "plantillas/historia.md",
    "plantillas/diseno-simulacion.md",
    "plantillas/checklist-documentacion.md",
    "plantillas/clase.md",
    "plantillas/rubrica-clase.md",
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


def leer_front_matter(ruta: Path) -> tuple[dict[str, str], str]:
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    if texto.startswith("<!-- clase-meta\n"):
        inicio = len("<!-- clase-meta\n")
        fin = texto.find("\n-->\n", inicio)
        separador = 5
    elif texto.startswith("---\n"):
        inicio = 4
        fin = texto.find("\n---\n", inicio)
        separador = 5
    else:
        return {}, texto
    if fin == -1:
        return {}, texto
    cabecera = texto[inicio:fin]
    campos: dict[str, str] = {}
    resultados = 0
    for linea in cabecera.splitlines():
        if linea.startswith("  - "):
            resultados += 1
        if linea and not linea.startswith((" ", "-")) and ":" in linea:
            clave, valor = linea.split(":", 1)
            campos[clave.strip()] = valor.strip()
    campos["_resultados"] = str(resultados)
    return campos, texto[fin + separador:]


def validar_clases(
    base: Path,
    curso: str,
    errores: list[str],
    codigos: set[str],
    preguntas: set[str],
) -> tuple[int, int]:
    total = 0
    minutos = 0
    numeros: set[int] = set()
    perfil = PERFILES.get(curso)
    if perfil is None:
        errores.append(f"Falta perfil pedagógico específico para {curso}")
        return total, minutos
    for esperado, patron in enumerate(PATRONES_CLASE, 1):
        rutas = list(base.glob(patron))
        if len(rutas) != 1:
            errores.append(
                f"{base.relative_to(RAIZ).as_posix()}: {patron} debe identificar una clase y encontró {len(rutas)}"
            )
            continue
        ruta = rutas[0]
        campos, texto = leer_front_matter(ruta)
        faltantes = CAMPOS_CLASE - campos.keys()
        if faltantes:
            errores.append(
                f"Metadatos incompletos en {ruta.relative_to(RAIZ).as_posix()}: {', '.join(sorted(faltantes))}"
            )
            continue
        try:
            numero = int(campos["clase"])
            duracion = int(campos["duracion_minutos"])
        except ValueError:
            errores.append(f"Número o duración inválida en {ruta.relative_to(RAIZ).as_posix()}")
            continue
        if numero != esperado:
            errores.append(
                f"Clase fuera de secuencia en {ruta.relative_to(RAIZ).as_posix()}: {numero}, esperada {esperado}"
            )
        if numero in numeros:
            errores.append(f"Clase duplicada {numero} en {base.relative_to(RAIZ).as_posix()}")
        numeros.add(numero)
        if duracion <= 0:
            errores.append(f"Duración no positiva en {ruta.relative_to(RAIZ).as_posix()}")
        if campos["tipo_documento"] != "clase" or campos["curso"] != curso:
            errores.append(f"Identidad de clase incoherente en {ruta.relative_to(RAIZ).as_posix()}")
        codigo = campos["codigo"]
        if codigo in codigos:
            errores.append(f"Código de clase duplicado: {codigo}")
        codigos.add(codigo)
        if int(campos["_resultados"]) < 2:
            errores.append(f"Faltan dos resultados de aprendizaje en {ruta.relative_to(RAIZ).as_posix()}")
        if ruta.read_text(encoding="utf-8", errors="replace").startswith("---\n"):
            errores.append(f"Los metadatos se muestran al lector en {ruta.relative_to(RAIZ).as_posix()}")
        apartados_pedagogicos = (
            "## 🧭 Guía de estudio aplicada",
            "### Pregunta guía",
            "### Explicación razonada",
            "### Caso resuelto: de la observación a la decisión",
            "### Comprueba tu comprensión",
        )
        for apartado in apartados_pedagogicos:
            if apartado not in texto:
                errores.append(f"Falta '{apartado}' en {ruta.relative_to(RAIZ).as_posix()}")
        pregunta = re.search(r"### Pregunta guía\n\n(.+)", texto)
        if pregunta:
            if pregunta.group(1) in preguntas:
                errores.append(f"Pregunta guía repetida en {ruta.relative_to(RAIZ).as_posix()}")
            preguntas.add(pregunta.group(1))
        fundamentos = (perfil.principio, perfil.riesgo, perfil.decision)
        cadena_presente = sum(componente in texto for componente in perfil.cadena)
        if any(huella not in texto for huella in fundamentos) or cadena_presente < 2:
            errores.append(
                f"La guía no desarrolla el perfil propio de {curso} en {ruta.relative_to(RAIZ).as_posix()}"
            )
        if "## 🎓 Cierre de clase" not in texto or "### Fuentes de esta clase" not in texto:
            errores.append(f"Falta cierre pedagógico o fuentes en {ruta.relative_to(RAIZ).as_posix()}")
        else:
            bloque_fuentes = texto.split("### Fuentes de esta clase", 1)[1]
            if len(re.findall(r"^- \[[^]]+\]\(https?://", bloque_fuentes, re.MULTILINE)) < 2:
                errores.append(f"Hay menos de dos fuentes visibles en {ruta.relative_to(RAIZ).as_posix()}")
        total += 1
        minutos += duracion
    fuente_curso = base / "manuales" / "fuentes.md"
    if not fuente_curso.is_file() or "| ID | Fuente |" not in fuente_curso.read_text(encoding="utf-8", errors="replace"):
        errores.append(f"Falta registro de fuentes del curso: {base.relative_to(RAIZ).as_posix()}")
    elif len(re.findall(r"^\| `[^`]+` \| \[[^]]+\]\(https?://", fuente_curso.read_text(encoding="utf-8"), re.MULTILINE)) < 2:
        errores.append(f"El registro tiene menos de dos fuentes: {base.relative_to(RAIZ).as_posix()}")
    return total, minutos


def validar_estructura(errores: list[str]) -> tuple[int, int]:
    total_clases = 0
    total_minutos = 0
    codigos: set[str] = set()
    preguntas: set[str] = set()
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
            clases, minutos = validar_clases(base, vehiculo, errores, codigos, preguntas)
            total_clases += clases
            total_minutos += minutos
    return total_clases, total_minutos


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
    clases, minutos = validar_estructura(errores)
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
    print(f"  Clases verificadas     : {clases}/{TOTAL_CLASES_ESPERADO}")
    print(f"  Duracion nominal       : {minutos / 60:.2f} horas")

    if errores:
        print(f"\nSe encontraron {len(errores)} problema(s):")
        for e in errores:
            print(f"  - {e}")
        return 1

    print("\nTodo correcto: estructura completa y enlaces internos resueltos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
