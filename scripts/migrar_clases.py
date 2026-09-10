#!/usr/bin/env python3
"""Convierte los documentos en clases legibles y pedagógicamente aplicadas.

El script conserva la explicación técnica específica de cada máquina, oculta
los metadatos administrativos al lector y agrega una guía de razonamiento con
caso, explicación, esquema cuando aporta y comprobación con respuestas.
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
from perfiles_pedagogicos import PERFILES, Perfil


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
        "<!-- clase-meta\n"
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
        "-->\n\n"
    )


def guia_aplicada(
    tipo: TipoClase,
    nombre: str,
    temas: list[str],
    perfil: Perfil,
    fuentes: tuple[Fuente, ...],
) -> str:
    """Produce contenido de estudio ligado a la arquitectura de la máquina."""
    foco = enumerar_natural(temas[:4], tipo.nombre.lower())
    a, b, c, d = perfil.cadena
    casos = {
        1: f"explicar cómo la evolución hizo posibles alternativas como {perfil.contraste}",
        2: f"elegir una configuración adecuada para {perfil.caso}",
        3: f"comparar {perfil.contraste} frente al mismo encargo",
        4: f"seguir una alteración desde {a} hasta {d} durante {perfil.caso}",
        5: f"interpretar mandos e indicaciones durante {perfil.caso}",
        6: f"resolver {perfil.caso} sin agotar el margen operacional",
        7: f"adaptar {perfil.caso} a tres condiciones ambientales distintas",
        8: f"interrumpir la cadena que podría producir {perfil.riesgo}",
        9: f"modelar {perfil.caso} como estados, variables y decisiones observables",
        10: f"explicar con fuentes los términos {a}, {b}, {c} y {d}",
        11: f"defender una solución integral para {perfil.caso}",
    }
    caso_clase = casos[tipo.numero]
    explicaciones = {
        1: (
            f"La evolución de {nombre} se comprende mejor como una sucesión de respuestas "
            f"a problemas, no como una lista de fechas. Los cambios en {a}, {b}, {c} y {d} "
            f"alteraron qué podía hacer la máquina, quién podía usarla y qué riesgos debían controlarse. "
            f"El contraste «{perfil.contraste}» permite observar qué decisiones de diseño permanecieron "
            "y cuáles cambiaron con la tecnología y el propósito."
        ),
        2: (
            f"Una característica solo es útil cuando permite anticipar comportamiento. En {nombre}, "
            f"la relación entre {a}, {b}, {c} y {d} determina capacidad, respuesta y límites. "
            f"Por eso «{perfil.contraste}» no se compara por apariencia: se compara por misión, "
            f"entorno, carga de trabajo y exposición al riesgo «{perfil.riesgo}»."
        ),
        3: (
            f"Las variantes «{perfil.contraste}» resuelven prioridades distintas. Una comparación "
            f"profesional sigue la cadena {a} → {b} → {c} → {d}: cada cambio de arquitectura modifica "
            "mandos, respuesta, mantenimiento y variables que una simulación debe representar. "
            "Elegir un modelo significa justificar qué compromiso sirve mejor al caso, no declarar un favorito."
        ),
        4: (
            f"El funcionamiento puede leerse como una cadena causal: {a} entrega o transforma energía; "
            f"{b} la adapta; {c} la transmite o gobierna; y {d} produce el efecto observable. "
            f"La cadena no es lineal en sentido estricto: sensores, estructura y operador cierran el lazo. "
            f"Si un eslabón se degrada, la señal importante es cómo cambia el estado de {d} y qué margen queda."
        ),
        5: (
            f"Un mando no se aprende memorizando su nombre, sino recorriendo el ciclo intención → acción → "
            f"indicación → verificación. En {nombre}, el operador actúa sobre {a} o {b}, observa la respuesta "
            f"en {c} y confirma el efecto en {d}. Una indicación inesperada exige detener la secuencia mental, "
            "identificar el modo activo y evitar una segunda orden que agrave el estado."
        ),
        6: (
            f"El principio rector puede resumirse así: {perfil.principio}. Esto explica por qué una misma orden produce resultados "
            "distintos cuando cambian velocidad, carga, configuración o entorno. Operar bien consiste en leer "
            f"la tendencia antes de agotar el margen y tomar esta decisión: {perfil.decision}."
        ),
        7: (
            f"El entorno no es decoración: modifica las fuerzas, la percepción y el tiempo disponible. En el caso "
            f"«{perfil.caso}», cambia el comportamiento de {d} y aumenta la probabilidad de {perfil.riesgo}. "
            "La respuesta correcta empieza por reconocer qué variable cambió y después adaptar límites, ruta o misión."
        ),
        8: (
            f"La regla de seguridad debe conectarse con un mecanismo de daño. El riesgo «{perfil.riesgo}» se "
            "controla mediante límites, inspección, competencia y coordinación; cada medida corta una parte de la "
            f"cadena causal. En una situación real prevalecen la autoridad aplicable y el manual vigente de {nombre}."
        ),
        9: (
            f"Una simulación de {nombre} es educativa si representa decisiones y consecuencias. Como mínimo debe "
            f"modelar el estado de {a}, la respuesta de {b}, la transición en {c} y el resultado en {d}. "
            f"El escenario «{perfil.caso}» es valioso porque obliga a observar, formular una hipótesis, actuar y comprobar."
        ),
        10: (
            f"El vocabulario técnico organiza relaciones: {a}, {b}, {c} y {d} nombran partes distintas de una "
            "misma cadena funcional. Una fuente se usa para sostener una afirmación concreta —principio, límite, "
            "procedimiento o contexto— y debe distinguirse del manual particular de un fabricante o de una regla narrativa."
        ),
        11: (
            f"La integración no consiste en repetir definiciones. Ante «{perfil.caso}» hay que reconstruir la cadena "
            f"{a} → {b} → {c} → {d}, aplicar el principio «{perfil.principio}», reconocer el riesgo y defender "
            f"una decisión verificable: {perfil.decision}."
        ),
    }
    diagramas = {
        4: f'''\n```mermaid
flowchart LR
    A["{a}"] --> B["{b}"] --> C["{c}"] --> D["{d}"]
    D -. respuesta observable .-> O["operador o control"]
    O -. orden y verificación .-> A
```\n''',
        5: f'''\n```mermaid
flowchart LR
    I["intención"] --> M["mando sobre {a} o {b}"]
    M --> R["respuesta de {c}"] --> E["efecto en {d}"]
    E --> V["verificar indicación"] --> I
```\n''',
        6: f'''\n```mermaid
flowchart LR
    C["condición inicial"] --> P["{perfil.principio}"]
    P --> R["riesgo: {perfil.riesgo}"]
    R --> D["decisión: {perfil.decision}"]
```\n''',
        9: f'''\n```mermaid
stateDiagram-v2
    [*] --> Preparado
    Preparado --> Operando: orden válida
    Operando --> Degradado: límite o falla
    Degradado --> Seguro: decisión correctiva
    Operando --> Completado: criterio logrado
    Seguro --> [*]
    Completado --> [*]
```\n''',
    }
    pasos = {
        1: f'''1. **Situar:** ordena los hitos que explican cómo se llegó a **{perfil.contraste}** y describe la necesidad que impulsó cada cambio.
2. **Relacionar:** explica qué se modificó en **{a}**, **{b}**, **{c}** o **{d}**; una fecha sin mecanismo no basta.
3. **Interpretar:** vincula el cambio con una capacidad nueva y también con el riesgo **{perfil.riesgo}**.
4. **Transferir:** usa la evolución para justificar por qué hoy conviene **{perfil.decision}**.''',
        2: f'''1. **Definir la necesidad:** convierte «{perfil.caso}» en requisitos de capacidad, entorno y respuesta.
2. **Comparar:** contrasta **{perfil.contraste}** usando esos requisitos y la cadena **{a} → {b} → {c} → {d}**.
3. **Descartar:** elimina la alternativa que deja menos margen frente a **{perfil.riesgo}**.
4. **Elegir:** declara la variante escogida, la evidencia usada y una limitación que todavía debe respetarse.''',
        3: f'''1. **Mantener el encargo constante:** ambas variantes deben evaluarse ante **{perfil.caso}**.
2. **Trazar consecuencias:** para cada variante sigue el efecto desde **{a}** hasta **{d}**.
3. **Comparar el puesto de mando:** determina qué debe percibir y controlar el operador en cada arquitectura.
4. **Justificar:** elige una variante y explica qué sacrifica; toda selección técnica contiene un compromiso.''',
        4: f'''1. **Entrada:** identifica el estado inicial de **{a}** durante **{perfil.caso}**.
2. **Transformación:** explica qué hacen **{b}** y **{c}**, y qué magnitud cambia en cada paso.
3. **Salida:** comprueba el efecto esperado en **{d}** y busca una desviación temprana.
4. **Falla razonada:** si aparece **{perfil.riesgo}**, retrocede por la cadena antes de ordenar otra acción.''',
        5: f'''1. **Intención:** formula qué cambio se necesita durante **{perfil.caso}**.
2. **Mando:** identifica el control que actúa sobre **{a}** o **{b}** y el modo que debe estar activo.
3. **Lectura:** localiza la indicación que confirma la respuesta de **{c}** y el efecto en **{d}**.
4. **Verificación:** si la lectura no coincide, no acumules órdenes; estabiliza e investiga el estado.''',
        6: f'''1. **Datos:** reconoce condiciones, configuración y margen disponibles en **{perfil.caso}**.
2. **Modelo:** aplica **{perfil.principio}** para predecir una tendencia antes de actuar.
3. **Riesgo:** explica mediante qué cadena de causas podría ocurrir **{perfil.riesgo}**.
4. **Decisión:** ejecuta mentalmente **{perfil.decision}** y define qué observación confirmaría que funcionó.''',
        7: f'''1. **Escenario base:** conserva la misión «{perfil.caso}» para poder comparar.
2. **Cambiar una condición:** modifica sucesivamente superficie o medio, visibilidad y perturbación externa.
3. **Recalcular margen:** explica cómo cada cambio afecta **{d}** y acerca o aleja **{perfil.riesgo}**.
4. **Adaptar:** cambia límite, ruta, configuración o incluso cancela; no mantengas la misma respuesta por hábito.''',
        8: f'''1. **Describir el daño:** explica cómo se llegaría a **{perfil.riesgo}** sin usar solo la palabra “peligro”.
2. **Localizar controles:** asocia inspección, límite, competencia o coordinación con un punto de la cadena causal.
3. **Consultar:** distingue qué afirma la fuente pública y qué debe verificarse en normativa y manual vigentes.
4. **Resolver:** documenta por qué **{perfil.decision}** es una decisión preventiva y verificable.''',
        9: f'''1. **Estado inicial:** representa {perfil.caso} con valores observables para **{a}**, **{b}**, **{c}** y **{d}**.
2. **Decisión del estudiante:** ofrece una elección que cambie el estado, no una animación automática.
3. **Consecuencia:** modela la tendencia hacia **{perfil.riesgo}** y una señal previa que permita corregir.
4. **Cierre:** evalúa la explicación de la decisión, además de si el estudiante “ganó” el escenario.''',
        10: f'''1. **Definir en contexto:** explica **{a}**, **{b}**, **{c}** y **{d}** por su función y relación.
2. **Respaldar:** enlaza cada afirmación importante con una fuente identificable y declara su alcance.
3. **Contrastar:** separa principios generales, requisitos locales, manual de fabricante y —si aplica— canon ficticio.
4. **Reformular:** convierte una definición copiada en una explicación propia con un ejemplo de **{nombre}**.''',
        11: f'''1. **Diagnosticar:** reconstruye **{a} → {b} → {c} → {d}** ante **{perfil.caso}**.
2. **Explicar:** aplica **{perfil.principio}** y cita el dato que sostiene la interpretación.
3. **Decidir:** propone **{perfil.decision}** y compara una alternativa que sería menos segura o menos eficaz.
4. **Verificar:** define evidencia de éxito, condición de abandono y aprendizaje transferible a **{perfil.contraste}**.''',
    }
    fuente_principal = fuentes[0]
    fuente_contraste = fuentes[1]
    preguntas = {
        1: f'''1. ¿Qué necesidad histórica impulsó un cambio en **{a}** o **{b}**?
2. ¿Qué hito modificó la relación entre capacidad y **{perfil.riesgo}**?
3. ¿Por qué **{perfil.contraste}** no puede explicarse como una simple diferencia estética?''',
        2: f'''1. ¿Qué característica de **{d}** condiciona primero el caso «{perfil.caso}»?
2. ¿Qué requisito descartaría una de las alternativas **{perfil.contraste}**?
3. ¿Qué límite debe declararse junto con la variante elegida?''',
        3: f'''1. ¿Qué cambia en la cadena **{a} → {b} → {c} → {d}** entre las dos variantes?
2. ¿Qué indicación o mando adicional necesitaría una de ellas?
3. ¿Cuál elegirías para «{perfil.caso}» y qué desventaja aceptarías?''',
        4: f'''1. Si se degrada **{b}**, ¿qué efecto esperarías primero en **{c}** y después en **{d}**?
2. ¿Qué observación ayudaría a diferenciar una falla de **{a}** de una falla de **{c}**?
3. ¿Por qué una segunda orden podría agravar **{perfil.riesgo}**?''',
        5: f'''1. ¿Qué mando inicia la respuesta y qué instrumento confirma que el modo correcto está activo?
2. ¿Qué indicación temprana advertiría **{perfil.riesgo}**?
3. ¿Qué secuencia usarías si la respuesta de **{d}** no coincide con la orden?''',
        6: f'''1. ¿Qué variable del principio «{perfil.principio}» cambia primero en el caso?
2. ¿Cómo se propaga ese cambio hasta **{d}**?
3. ¿Qué evidencia confirmaría que **{perfil.decision}** conservó margen operacional?''',
        7: f'''1. ¿Cómo cambiaría **{d}** si empeora la perturbación externa?
2. ¿Qué condición ambiental acerca más el escenario a **{perfil.riesgo}**?
3. ¿Cuándo adaptarías la maniobra y cuándo la cancelarías?''',
        8: f'''1. ¿Qué mecanismo concreto conduce a **{perfil.riesgo}**?
2. ¿Qué barrera preventiva actúa antes del movimiento y cuál durante la operación?
3. ¿Qué parte de la respuesta requiere consultar normativa o manual vigente?''',
        9: f'''1. ¿Qué cuatro estados mínimos necesita el escenario «{perfil.caso}»?
2. ¿Qué variable anticipa **{perfil.riesgo}** antes de llegar al estado de falla?
3. ¿Cómo evaluarías la explicación del estudiante y no solo el resultado final?''',
        10: f'''1. Explica la diferencia funcional entre **{b}** y **{c}** sin copiar una definición.
2. ¿Qué fuente respalda el principio «{perfil.principio}» y cuál es su alcance?
3. ¿Qué dato exigiría un manual de fabricante en vez de una fuente general?''',
        11: f'''1. ¿Cuál es tu diagnóstico causal de «{perfil.caso}»?
2. ¿Qué alternativa a **{perfil.decision}** considerarías y por qué ofrece menos margen?
3. ¿Qué criterio observable usarías para continuar, corregir o abandonar?''',
    }
    return f'''\n\n## 🧭 Guía de estudio aplicada

### Pregunta guía

¿Cómo ayuda **{foco}** a **{caso_clase}**?

### Explicación razonada

{explicaciones[tipo.numero]}
{diagramas.get(tipo.numero, "")}
Esta clase se conecta con el resto del curso mediante **{perfil.principio}**. El hilo de
seguridad consiste en reconocer a tiempo **{perfil.riesgo}** y poder justificar la decisión
**{perfil.decision}**; en clases posteriores cambiará el ángulo de análisis, no esa relación causal.
La lectura funcional común sigue **{a} → {b} → {c} → {d}**, de modo que cada concepto pueda
ubicarse dentro del funcionamiento completo y no quede como un dato aislado.

**Apoyo documental:** [{fuente_principal.titulo}]({fuente_principal.url}) aporta {fuente_principal.uso};
[{fuente_contraste.titulo}]({fuente_contraste.url}) se usa para {fuente_contraste.uso}. Estas fuentes
se contrastan con el alcance de la clase y no sustituyen un manual de equipo concreto.

### Caso resuelto: de la observación a la decisión

{pasos[tipo.numero]}

### Comprueba tu comprensión

{preguntas[tipo.numero]}

<details>
<summary>Orientación para revisar tus respuestas</summary>

- La primera respuesta debe relacionar el eslabón elegido con un efecto posterior, no solo nombrarlo.
- La segunda debe proponer una señal medible u observable y explicar qué tendencia sería preocupante.
- La tercera debe cambiar al menos una variable de capacidad, mando, entorno o margen de seguridad.

</details>
'''


def insertar_guia(texto: str, bloque: str) -> str:
    inicio = texto.find("\n## 🧭 Guía de estudio aplicada\n")
    if inicio != -1:
        fin = texto.find("\n## 🎓 Cierre de clase\n", inicio)
        texto = texto[:inicio].rstrip() + (texto[fin:] if fin != -1 else "")
    pos = texto.find("\n## 🎓 Cierre de clase\n")
    if pos == -1:
        pos = texto.rfind("\n---\n")
    if pos == -1:
        return texto.rstrip() + bloque + "\n"
    return texto[:pos].rstrip() + bloque + texto[pos:]


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
    elif texto.startswith("<!-- clase-meta\n"):
        fin = texto.find("\n-->\n")
        if fin == -1:
            raise ValueError(f"metadatos ocultos incompletos: {ruta}")
        cuerpo = texto[fin + 5:].lstrip("\n")
    else:
        cuerpo = texto
    cuerpo = re.sub(r"\bEste módulo\b", "Esta clase", cuerpo)
    cuerpo = re.sub(r"\bMódulo (\d+)\b", r"Clase \1", cuerpo)
    cuerpo = re.sub(
        r"\n## Fuentes\n\n- Registrar aquí las fuentes públicas consultadas\.\n"
        r"- Enlazar cada fuente también en \[`manuales/fuentes\.md`\]\([^\n]+\)\.\n",
        "",
        cuerpo,
    )
    titulo = titulo_documento(cuerpo)
    temas = apartados(cuerpo)
    resultados, actividad, evidencia, criterio = pedagogia(tipo, nombre, temas)
    cuerpo = insertar_guia(
        cuerpo,
        guia_aplicada(
            tipo,
            nombre,
            temas,
            PERFILES[curso.name],
            FUENTES_POR_CURSO[curso.name],
        ),
    )
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
