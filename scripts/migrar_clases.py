#!/usr/bin/env python3
"""Migra los documentos lectivos existentes al contrato pedagogico de clase.

El script es deliberadamente determinista e idempotente: conserva el contenido
tecnico de cada maquina y solo agrega metadatos y un cierre evaluable. Tambien
actualiza las portadas de curso para hablar de clases en lugar de modulos.
"""

from __future__ import annotations

import re
import os
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from fuentes_clases import FUENTES_POR_CURSO, Fuente


RAIZ = Path(__file__).resolve().parent.parent
RAICES_CURSOS = (RAIZ / "vehiculos", RAIZ / "vehiculos-fantasticos")
RESTAURAR_DESDE_HEAD = "--from-head" in sys.argv


@dataclass(frozen=True)
class TipoClase:
    numero: int
    patron: str
    nombre: str
    duracion: int
    modalidad: str
    competencia: str
    actividad: str
    evidencia: str
    criterio: str


TIPOS = (
    TipoClase(1, "historia/*.md", "Historia y evolución", 45, "teórica dialogada",
              "contexto_historico",
              "Construir una linea de tiempo razonada y relacionar dos hitos con cambios en la maquina.",
              "Linea de tiempo comentada con al menos cuatro hitos.",
              "Ordena los hitos y explica correctamente dos relaciones de causa y efecto."),
    TipoClase(2, "operacion/caracteristicas-*.md", "Características y usos", 45, "teórica aplicada",
              "identificacion_funcional",
              "Clasificar variantes a partir de necesidades de uso planteadas en tres casos breves.",
              "Tabla de clasificacion con justificacion tecnica.",
              "Distingue funciones y selecciona una variante coherente en al menos dos de tres casos."),
    TipoClase(3, "modelos/*.md", "Modelos y variantes", 60, "comparativa guiada",
              "seleccion_de_configuracion",
              "Comparar dos variantes y justificar como cambian el mando, el comportamiento y la simulacion.",
              "Matriz comparativa de variantes.",
              "Identifica al menos tres diferencias relevantes y sus consecuencias operativas."),
    TipoClase(4, "operacion/sistemas-mecanicos-*.md", "Sistemas principales", 90, "teórica aplicada",
              "comprension_de_sistemas",
              "Trazar el flujo de energia e informacion entre los sistemas principales sobre un esquema incompleto.",
              "Diagrama funcional anotado.",
              "Conecta correctamente los sistemas esenciales y explica el efecto de una falla simulada."),
    TipoClase(5, "mandos/*.md", "Mandos e instrumentos", 60, "taller de simulación",
              "lectura_y_mando",
              "Resolver un recorrido guiado de identificacion de controles, indicadores y estados del sistema.",
              "Mapa de mandos e instrumentos completado.",
              "Reconoce los controles criticos y relaciona cada indicacion con una decision segura."),
    TipoClase(6, "operacion/principios-*.md", "Principios y operación", 90, "resolución de problemas",
              "razonamiento_operacional",
              "Explicar y resolver un escenario de simulación usando los principios físicos que gobiernan la máquina.",
              "Resolucion argumentada de un escenario operacional.",
              "Aplica los principios correctos, anticipa consecuencias y mantiene los limites de seguridad."),
    TipoClase(7, "operacion/entornos-*.md", "Entornos de trabajo", 60, "análisis de escenarios",
              "adaptacion_al_entorno",
              "Comparar tres entornos y decidir qué variables, riesgos y límites cambian en cada uno.",
              "Matriz entorno-riesgo-respuesta para simulacion.",
              "Adapta las decisiones a cada entorno y reconoce sus riesgos diferenciales."),
    TipoClase(8, "reglamentos/*.md", "Reglamentos y seguridad", 60, "estudio de casos",
              "cumplimiento_y_seguridad",
              "Analizar casos simulados e identificar la norma, autoridad o regla de universo aplicable.",
              "Ficha de resolucion normativa con fuentes.",
              "Fundamenta las decisiones en las referencias del curso y distingue formacion de habilitacion real."),
    TipoClase(9, "simulacion/*.md", "Diseño de simulación", 90, "laboratorio de diseño",
              "modelado_de_simulacion",
              "Definir un escenario educativo con entradas, estados, variables, retroalimentacion y condicion de cierre.",
              "Ficha de escenario de simulacion.",
              "El modelo es coherente con la maquina, medible, seguro y trazable a contenidos anteriores."),
    TipoClase(10, "recursos/*.md", "Taller de recursos", 45, "taller documental",
              "alfabetizacion_tecnica",
              "Construir un glosario minimo y verificar la procedencia de las fuentes empleadas en el curso.",
              "Glosario aplicado y ficha de trazabilidad de fuentes.",
              "Define los terminos en contexto y diferencia una fuente primaria de una referencia de apoyo."),
    TipoClase(11, "ejercicios/*.md", "Evaluación integradora", 90, "evaluación auténtica",
              "integracion_de_competencias",
              "Resolver la autoevaluacion y defender una decision en un escenario integrador de simulacion.",
              "Respuestas justificadas y escenario final resuelto.",
              "Alcanza al menos 80 % de los indicadores y no incurre en errores criticos de seguridad."),
)


def curso_codigo(curso: Path) -> str:
    return curso.name.upper().replace("-", "")[:12]


def quitar_icono(texto: str) -> str:
    return re.sub(r"^[^\wÁÉÍÓÚÜÑáéíóúüñ]+", "", texto).strip()


def titulo_documento(texto: str) -> str:
    coincidencia = re.search(r"^#\s+(.+)$", texto, re.MULTILINE)
    if not coincidencia:
        raise ValueError("documento sin titulo H1")
    return quitar_icono(coincidencia.group(1))


def nombre_curso(curso: Path) -> str:
    texto = leer_texto(curso / "README.md")
    titulo = titulo_documento(texto)
    return re.sub(r"^Curso:\s*", "", titulo, flags=re.IGNORECASE).strip()


def leer_texto(ruta: Path) -> str:
    """Lee la versión limpia de Git durante la primera migración, si se solicita."""
    if RESTAURAR_DESDE_HEAD:
        relativa = ruta.relative_to(RAIZ).as_posix()
        proceso = subprocess.run(
            ["git", "show", f"HEAD:{relativa}"],
            cwd=RAIZ,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        if proceso.returncode == 0:
            return proceso.stdout.decode("utf-8")
    return ruta.read_text(encoding="utf-8")


def escribir_texto(ruta: Path, texto: str) -> None:
    """Reemplazo atómico con reintentos para bloqueos breves de Windows."""
    temporal = ruta.with_name(ruta.name + ".codex-tmp")
    datos = texto.encode("utf-8")
    ultimo_error: OSError | None = None
    for intento in range(12):
        try:
            temporal.write_bytes(datos)
            os.replace(temporal, ruta)
            return
        except OSError as error:
            ultimo_error = error
            if temporal.exists():
                temporal.unlink(missing_ok=True)
            time.sleep(0.05 * (intento + 1))
    assert ultimo_error is not None
    raise ultimo_error


def apartados(texto: str) -> list[str]:
    """Extrae el foco real de la clase en vez de inyectar objetivos genéricos."""
    titulos = []
    for valor in re.findall(r"^##\s+(?:\d+\.\s+)?(.+)$", texto, re.MULTILINE):
        limpio = quitar_icono(valor)
        if limpio not in {"Fuentes", "Cierre de clase", "Pendientes", "Autochequeo"}:
            titulos.append(limpio)
    return titulos[:4]


def enumerar_natural(elementos: list[str], respaldo: str) -> str:
    if not elementos:
        return respaldo
    if len(elementos) == 1:
        return elementos[0]
    return ", ".join(elementos[:-1]) + " y " + elementos[-1]


def pedagogia(
    tipo: TipoClase, nombre: str, temas: list[str]
) -> tuple[list[str], str, str, str]:
    """Crea una consigna humana a partir de los temas propios del documento."""
    focos_base = {
        1: "origen, evolución tecnológica, variantes representativas e impacto",
        2: "definición, rasgos funcionales, tipos y usos",
        3: "manejo, arquitectura de mandos y variables de simulación",
        5: "controles, instrumentos, entradas y estados del sistema",
        6: "principios físicos, fases de operación, decisiones y errores frecuentes",
        7: "entornos, factores ambientales, riesgos y respuesta de simulación",
        8: "ámbito, requisitos, seguridad, restricciones y aplicación en simulación",
        9: "objetivo, variables, estados, ciclo y escenarios de simulación",
        10: "glosario, esquemas y trazabilidad de fuentes",
        11: "comprensión, aplicación y transferencia a la simulación",
    }
    tema = (
        enumerar_natural(temas[:6], tipo.nombre.lower())
        if tipo.numero == 4
        else focos_base[tipo.numero]
    )
    resultados = [
        f"Explicar {tema} con vocabulario propio de {nombre}.",
        f"Aplicar esos conceptos a una decisión segura o a un escenario de simulación de {nombre}.",
    ]
    if tipo.numero == 1:
        return resultados, (
            f"Construye una línea de tiempo de {nombre} y explica cómo dos cambios históricos "
            "transformaron su función o su puesto de mando."
        ), "Línea de tiempo comentada con cuatro hitos o más.", (
            "Los hitos están ordenados, son pertinentes y dos relaciones de causa y efecto quedan justificadas."
        )
    if tipo.numero in (2, 3):
        return resultados, (
            f"Compara variantes de {nombre} mediante los ejes «{tema}» y elige una para un caso de uso razonado."
        ), "Matriz comparativa y decisión justificada.", (
            "La elección considera función, límites, mando y efecto en la simulación; no se apoya solo en preferencias."
        )
    if tipo.numero == 4:
        return resultados, (
            f"Dibuja un esquema funcional de {nombre} que conecte {tema}; después predice el efecto de una falla simulada."
        ), "Esquema con flujos de energía, materia o información anotados.", (
            "Las conexiones esenciales son correctas y la consecuencia de la falla se propaga de manera coherente."
        )
    if tipo.numero == 5:
        return resultados, (
            f"Recorre el puesto de mando simulado de {nombre}: localiza los controles de {tema} y asocia cada indicación con una decisión."
        ), "Mapa de mandos y resolución de dos estados del tablero.", (
            "Reconoce los controles críticos y responde a los estados sin introducir acciones inseguras."
        )
    if tipo.numero == 6:
        return resultados, (
            f"Resuelve un escenario de {nombre} explicando, paso a paso, cómo intervienen {tema}."
        ), "Resolución argumentada de un escenario operacional.", (
            "Aplica los principios correctos, anticipa consecuencias y respeta los límites del curso."
        )
    if tipo.numero == 7:
        return resultados, (
            f"Contrasta tres entornos de {nombre} a partir de {tema} y determina cómo cambian variables, percepción, riesgos y respuesta."
        ), "Matriz entorno–cambio–riesgo–respuesta.", (
            "Cada respuesta se adapta al entorno y distingue riesgos que no son intercambiables entre escenarios."
        )
    if tipo.numero == 8:
        return resultados, (
            f"Analiza dos casos de {nombre}; localiza la fuente aplicable y separa obligación real, buena práctica y regla de simulación."
        ), "Ficha normativa con decisión y fuente trazable.", (
            "Las decisiones citan la autoridad adecuada y no presentan el curso como habilitación profesional."
        )
    if tipo.numero == 9:
        return resultados, (
            f"Diseña un escenario educativo de {nombre} basado en {tema}, con entradas, estados, variables y criterio de cierre."
        ), "Ficha de escenario y diagrama de estados.", (
            "El modelo es específico de la máquina, medible, seguro y trazable a clases anteriores."
        )
    if tipo.numero == 10:
        return resultados, (
            f"Selecciona términos de {tema}, explícalos en contexto de {nombre} y verifica la procedencia de las fuentes utilizadas."
        ), "Glosario aplicado y ficha breve de trazabilidad.", (
            "Los términos permiten interpretar el curso y las fuentes se distinguen por autoridad, alcance y vigencia."
        )
    return resultados, (
        f"Resuelve la autoevaluación de {nombre} y defiende una decisión en un escenario integrador sin consultar las respuestas."
    ), "Respuestas justificadas y escenario final resuelto.", (
        "Alcanza al menos 80 % de los indicadores y no incurre en errores críticos de seguridad."
    )


def metadatos(
    tipo: TipoClase,
    curso: Path,
    titulo: str,
    resultados: list[str],
    evidencia: str,
    criterio: str,
) -> str:
    codigo = f"{curso_codigo(curso)}-{tipo.numero:02d}"
    prerrequisito = "ninguno" if tipo.numero == 1 else f"{curso_codigo(curso)}-{tipo.numero - 1:02d}"
    citar = lambda valor: json.dumps(valor, ensure_ascii=False)
    return (
        "---\n"
        "tipo_documento: clase\n"
        f"clase: {tipo.numero}\n"
        f"codigo: {codigo}\n"
        f"curso: {curso.name}\n"
        f"titulo: {citar(titulo)}\n"
        f"modalidad: {citar(tipo.modalidad)}\n"
        f"duracion_minutos: {tipo.duracion}\n"
        "nivel: introductorio\n"
        f"prerrequisito: {prerrequisito}\n"
        f"competencia: {citar(tipo.competencia)}\n"
        "resultados_aprendizaje:\n"
        + "".join(f"  - {citar(resultado)}\n" for resultado in resultados)
        + f"evidencia: {citar(evidencia)}\n"
        f"criterio_aprobacion: {citar(criterio)}\n"
        "fuentes: manuales/fuentes.md\n"
        "ultima_revision: 2026-09-10\n"
        "---\n\n"
    )


def cierre(
    actividad: str,
    evidencia: str,
    criterio: str,
    fuentes: tuple[Fuente, ...],
) -> str:
    lista_fuentes = "\n".join(
        f"- [{fuente.identificador}]({fuente.url}): {fuente.titulo}, "
        f"{fuente.institucion}. Uso: {fuente.uso}."
        for fuente in fuentes
    )
    return (
        "\n\n## 🎓 Cierre de clase\n\n"
        f"- **Actividad:** {actividad}\n"
        f"- **Evidencia:** {evidencia}\n"
        f"- **Criterio de aprobación:** {criterio}\n"
        "- **Transferencia:** explica qué cambiaría al pasar a otra variante de esta máquina.\n\n"
        "### Fuentes de esta clase\n\n"
        f"{lista_fuentes}\n\n"
        "> Las fuentes sostienen el marco conceptual y normativo; esta clase no reemplaza el manual\n"
        "> del fabricante, la formación certificada ni la habilitación exigida para operar equipos reales.\n"
    )


def insertar_cierre(texto: str, bloque: str) -> str:
    inicio = texto.find("\n## 🎓 Cierre de clase\n")
    if inicio != -1:
        pie = texto.find("\n---\n", inicio)
        texto = texto[:inicio].rstrip() + (texto[pie:] if pie != -1 else "")
    pos = texto.rfind("\n---\n")
    if pos == -1:
        return texto.rstrip() + bloque + "\n"
    return texto[:pos].rstrip() + bloque + texto[pos:]


def migrar_documento(ruta: Path, tipo: TipoClase, curso: Path, nombre: str) -> None:
    texto = leer_texto(ruta)
    if texto.startswith("---\n"):
        fin = texto.find("\n---\n", 4)
        if fin == -1:
            raise ValueError(f"front matter incompleto: {ruta}")
        cuerpo = texto[fin + 5:].lstrip("\n")
    else:
        cuerpo = texto
    titulo = titulo_documento(cuerpo)
    temas = apartados(cuerpo)
    resultados, actividad, evidencia, criterio = pedagogia(tipo, nombre, temas)
    cuerpo = insertar_cierre(
        cuerpo,
        cierre(actividad, evidencia, criterio, FUENTES_POR_CURSO[curso.name]),
    )
    escribir_texto(
        ruta, metadatos(tipo, curso, titulo, resultados, evidencia, criterio) + cuerpo
    )


def registrar_fuentes(curso: Path, nombre: str, fuentes: tuple[Fuente, ...]) -> None:
    filas = "\n".join(
        f"| `{fuente.identificador}` | [{fuente.titulo}]({fuente.url}) | "
        f"{fuente.institucion} | {fuente.uso} | Verificada 2026-09-10 |"
        for fuente in fuentes
    )
    texto = f"""# Fuentes del curso: {nombre}

[🏠 Inicio](../../../README.md) · [🎓 Curso](../README.md)

Este registro identifica las fuentes públicas que respaldan las once clases. Las
referencias se seleccionan por autoridad y utilidad pedagógica; los documentos
vigentes del fabricante u operador prevalecen siempre en una formación real.

| ID | Fuente | Institución | Uso en el curso | Estado |
| --- | --- | --- | --- | --- |
{filas}

## Criterio de uso

- Las clases citan estas fuentes junto a su actividad de cierre.
- Una fuente de otro país aporta principios técnicos, no sustituye la normativa chilena.
- En vehículos ficticios, la fuente de canon se contrasta con referencias de física real.
- Toda revisión futura debe comprobar vigencia, alcance y posibles cambios de URL.
"""
    escribir_texto(curso / "manuales" / "fuentes.md", texto)


def migrar_portada(curso: Path) -> None:
    ruta = curso / "README.md"
    texto = leer_texto(ruta)
    texto = texto.replace("badge/modulos-11", "badge/clases-11")
    texto = texto.replace("badge/m%C3%B3dulos-11", "badge/clases-11")
    texto = texto.replace("![Módulos]", "![Clases]")
    if "![Duración del curso]" not in texto:
        texto = re.sub(
            r"(!\[Clases\]\(https://img\.shields\.io/badge/clases-11-blue\)\n)",
            r"\1![Duración del curso](https://img.shields.io/badge/duracion-12h15-5f3dc4)\n",
            texto,
            count=1,
        )
    texto = texto.replace("## 📚 Módulos del curso", "## 📚 Clases del curso")
    texto = texto.replace("| # | Módulo |", "| # | Clase |")
    texto = texto.replace("[➡️ Empezar por el Módulo 1:", "[➡️ Empezar por la Clase 1:")
    escribir_texto(ruta, texto)


def main() -> int:
    cursos = sorted(c for raiz in RAICES_CURSOS for c in raiz.iterdir() if c.is_dir())
    faltantes = {curso.name for curso in cursos} - FUENTES_POR_CURSO.keys()
    if faltantes:
        raise RuntimeError(f"cursos sin fuentes: {sorted(faltantes)}")
    migrados = 0
    for curso in cursos:
        nombre = nombre_curso(curso)
        for tipo in TIPOS:
            rutas = list(curso.glob(tipo.patron))
            if len(rutas) != 1:
                raise RuntimeError(
                    f"{curso.relative_to(RAIZ)}: se esperaba un archivo para {tipo.patron}, encontrados {len(rutas)}"
                )
            migrar_documento(rutas[0], tipo, curso, nombre)
            migrados += 1
        registrar_fuentes(curso, nombre, FUENTES_POR_CURSO[curso.name])
        migrar_portada(curso)
    print(f"Cursos migrados: {len(cursos)}")
    print(f"Clases migradas: {migrados}")
    print(f"Horas nominales: {sum(t.duracion for t in TIPOS) * len(cursos) / 60:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
