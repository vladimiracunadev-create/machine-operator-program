# Marco legal y normativo (Chile)

Referencia técnica del marco legal chileno e internacional aplicable a los
vehículos del multisimulador. Sirve para diseñar reglamentos de simulación
realistas y para orientar la investigación de cada vehículo.

## Aviso importante

Este documento es material educativo y de diseño de simulación. **No es asesoría
legal ni sustituye las fuentes oficiales vigentes.** Las leyes cambian, se
modifican y se refunden; los números de artículo y de decreto pueden variar
entre versiones. Antes de usar cualquier dato para un fin real, verifica el
texto vigente en la fuente oficial (ver enlaces).

Al final hay una sección de **datos por reconfirmar**: puntos donde las fuentes
secundarias discrepan o donde no se pudo confirmar la cita exacta.

## Fuentes oficiales de referencia

| Ámbito | Organismo | Sitio |
| --- | --- | --- |
| Leyes (texto oficial) | Biblioteca del Congreso Nacional (BCN) | <https://www.bcn.cl/leychile> |
| Tránsito y seguridad vial | CONASET | <https://www.conaset.cl> |
| Transporte | Ministerio de Transportes (MTT) | <https://www.mtt.gob.cl> |
| Registro de vehículos | Servicio de Registro Civil e Identificación | <https://www.registrocivil.cl> |
| Marítimo | DIRECTEMAR (Autoridad Marítima) | <https://www.directemar.cl> |
| Aeronáutico | Dirección General de Aeronáutica Civil (DGAC) | <https://www.dgac.gob.cl> |
| Espacial | Ministerio de Ciencia, Tecnología, Conocimiento e Innovación | <https://www.minciencia.gob.cl> |

---

## 1. Vehículos terrestres

Base legal principal: **Ley 18.290, Ley de Tránsito** (texto refundido por DFL 1
de 2007). Fuente: <https://www.bcn.cl/leychile/navegar?idNorma=29708>.

### 1.1 Clases de licencia de conducir (Ley 18.290, Art. 12)

Las licencias se agrupan en Profesionales (Clase A), No Profesionales (Clases B
y C) y Especiales (Clases D, E y F).

| Clase | Tipo | Habilita para conducir |
| --- | --- | --- |
| A-1 | Profesional | Taxis (transporte de pasajeros). |
| A-2 | Profesional | Taxis, ambulancias y transporte de pasajeros de 10 a 17 asientos. |
| A-3 | Profesional | Transporte de pasajeros sin límite de asientos (buses, minibuses, trolebuses). Incluye A-1 y A-2. |
| A-4 | Profesional | Vehículos simples de carga con peso bruto vehicular superior a 3.500 kg. |
| A-5 | Profesional | Todo vehículo de carga, simple o articulado. Incluye A-4. |
| B | No profesional | Vehículos de 3 o más ruedas, particulares, hasta 9 asientos o carga hasta 3.500 kg (automóviles, camionetas). |
| C | No profesional | Vehículos de dos o tres ruedas: motocicletas, motonetas, bicimotos. |
| D | Especial | Maquinaria automotriz: grúas, tractores, cargadores, retroexcavadoras y similares. |
| E | Especial | Vehículos a tracción animal. |
| F | Especial | Vehículos de las Fuerzas Armadas, Carabineros, PDI, Gendarmería y Bomberos. |

Correspondencia rápida por vehículo del repositorio:

- Moto: **Clase C**.
- Automóvil particular: **Clase B**.
- Bus de transporte público: **Clase A-3** (o A-2 para 10 a 17 asientos).
- Camión simple de carga (más de 3.500 kg): **Clase A-4**.
- Camión articulado (tractocamion con acoplado): **Clase A-5**.
- Grúa, tractor y maquinaria de construcción (maquinaria automotriz): **Clase D**.

Edad mínima general (Art. 13): 18 años para clases B y C. Las clases
profesionales exigen edad mayor y haber sido titular previo de licencia Clase B
(años exactos: ver datos por reconfirmar).

### 1.2 Requisitos y elementos de seguridad

| Tema | Norma | Detalle |
| --- | --- | --- |
| Casco en moto | Ley 18.290, Art. 84 | Casco protector obligatorio para conductor y acompañante. |
| Cinturón de seguridad | Ley 18.290, Art. 79 | Obligatorio en asientos delanteros y traseros según año del vehículo. |
| Sistema de retención infantil | Ley 20.904 (modifica Art. 75) | Silla obligatoria para ninos hasta 8 años; prohibido menores de 12 en asiento delantero. |
| Velocidad urbana | Ley 21.103 (2018) | Límite urbano general de 50 km/h. |
| Convivencia vial | Ley 21.088 (2018) | Reglas para ciclos, ciclovias, distancia de adelantamiento de 1,5 m. |

Referencias: CONASET cinturón <https://www.conaset.cl/normativa-cinturon/>;
CONASET sillas <https://www.conaset.cl/sillas-infantiles/>; CONASET velocidad
<https://www.conaset.cl/normativa-velocidad/>.

### 1.3 Límites de velocidad (Ley 18.290, Art. 150)

| Vía | Livianos y motos | Buses y camiones pesados |
| --- | --- | --- |
| Urbana | 50 km/h | 50 km/h |
| Rural, 1 pista por sentido | 100 km/h | 90 km/h (buses interurbanos hasta 100) |
| Rural, 2 o más pistas por sentido | 120 km/h | 90 a 100 km/h según tipo |

Municipalidades (zona urbana) y la Dirección de Vialidad (zona rural) pueden
fijar límites distintos con señalización reglamentaria.

### 1.4 Documentos obligatorios de circulación

| Documento | Norma | Organismo |
| --- | --- | --- |
| Inscripción en el Registro de Vehículos Motorizados (padrón) | Ley 18.290, Título III; D.S. 1.111/1984 | Registro Civil |
| Permiso de circulación (anual, vence 31 de marzo) | Ley 18.290 y normas municipales | Municipalidades |
| Revisión técnica y de gases | Ley 18.290, Título VII | Plantas de revisión técnica (MTT) |
| SOAP (Seguro Obligatorio de Accidentes Personales) | Ley 18.490 | Companias de seguros (supervisa CMF) |

El permiso de circulación exige SOAP vigente, revisión técnica al día e
inscripción en el registro. El SOAP cubre lesiones o muerte de personas, no
daños materiales.

### 1.5 Organismos

- **CONASET**: política de seguridad vial, estadisticas, manuales del conductor.
- **MTT**: transporte público, revisiones técnicas, homologación.
- **Registro Civil**: Registro de Vehículos Motorizados y padrón.
- **Municipalidades**: licencias de conducir y permisos de circulación.
- **CMF**: supervisa el SOAP.

### 1.6 Ferroviario

El transporte por ferrocarril se rige por la **Ley General de Ferrocarriles** y la
normativa del sector, con la **Empresa de los Ferrocarriles del Estado (EFE)** como
operador estatal histórico y el MTT en el rol regulador. La operación cubre
señalización, gestión de la vía, pasos a nivel y habilitación del personal de
conducción (maquinistas). Los números y fechas exactos de la ley y sus reglamentos
se listan en datos por reconfirmar. Fuente institucional: <https://www.efe.cl>.

### 1.7 Maquinaria de izaje fija (grúa portuaria y grúa torre)

Las grúas fijas (de puerto y de edificio) no circulan por vía pública, por lo que
no requieren licencia de conducir. Se rigen por la **seguridad laboral**:

- **Ley 16.744**: seguro social contra riesgos de accidentes del trabajo y
  enfermedades profesionales.
- **D.S. 594 (MINSAL)**: condiciones sanitarias y ambientales básicas en los
  lugares de trabajo.
- Operación por personal **certificado/competente**, plan de izaje, tablas de
  carga del fabricante, señalero (rigger) y área de exclusión.

En el ámbito portuario aplican además las normas de la Autoridad Marítima y del
recinto portuario. El detalle de certificación del operador y montaje de grúa
torre se indica en datos por reconfirmar.

### 1.8 Ascensores (transporte vertical)

Los ascensores de edificios se rigen por la **Ley 20.296** (instalación,
mantención e inspección de ascensores y similares) y por la Ordenanza General de
Urbanismo y Construcciones (OGUC). Exigen mantención periódica por empresa
competente y certificación por un organismo autorizado; la fiscalización recae
en las municipalidades (Dirección de Obras). Los plazos y detalles exactos se
indican en datos por reconfirmar.

### 1.9 Vehículos de competición (Fórmula 1)

Un monoplaza de Fórmula 1 **no circula por vía pública** ni requiere licencia de
conducir común: es un vehículo de competición regido por el **reglamento
deportivo y técnico de la FIA** (Federación Internacional del Automóvil) y su
serie. En Chile, el automovilismo deportivo se organiza a través de la
federación nacional del automovilismo. El enfoque del curso es técnico y
educativo, no normativo de tránsito.

### 1.10 Vehículos militares terrestres (tanques)

Marco institucional público e histórico únicamente. Los carros de combate son
material del **Ejército de Chile**, dependiente del Ministerio de Defensa
Nacional, en el marco de la **Ley 18.948** (Orgánica Constitucional de las
Fuerzas Armadas). Se rigen por normativa militar y no por la Ley de Tránsito.
Este repositorio se limita a historia pública y principios físicos generales,
sin táctica, sistemas de armas ni procedimientos operativos (ver
`docs/04-seguridad-y-limites.md`).

---

## 2. Vehículos marítimos

### 2.1 Buques mercantes

Base legal: **DL 2.222 de 1978, Ley de Navegación** (Ministerio de Defensa).
Fuente: <https://www.bcn.cl/leychile/navegar?idNorma=6855>.

| Tema | Norma | Detalle |
| --- | --- | --- |
| Autoridad Marítima | DL 2.222, Art. 2 | La Dirección (DIRECTEMAR / DGTM y MM) aplica y fiscaliza la ley. |
| Registro de naves | DL 2.222, Art. 10 | Registros de naves mayores, menores, en construcción, artefactos navales e hipotecas. |
| Nacionalidad de la nave | DL 2.222, Art. 11 | Solo se matriculan naves de propietario chileno (con reglas para personas juridicas). |
| Título de capitán | DL 2.222, Art. 49 | Se requiere ser chileno y poseer el título conferido por el Director. |
| Dotación mínima de seguridad | DL 2.222, Art. 73 | La determina la Dirección (naves mayores) o la Autoridad Marítima (menores). |

Títulos de la Marina Mercante Nacional: los otorga DIRECTEMAR conforme al
Reglamento de Títulos Profesionales y Permisos de Embarco (TM-007A) y al D.S.
127/2019. Escalafón de cubierta: Capitán, Piloto Primero, Segundo, Tercero y
Piloto Costero. Fuente: <https://www.directemar.cl>.

**Cruceros (buques de pasajeros)**: siguen el mismo marco (DL 2.222 y OMI), con
mayor exigencia de seguridad de pasajeros bajo SOLAS, planes de evacuación, y
personal titulado bajo STCW. La Autoridad Marítima (DIRECTEMAR) fiscaliza el
cumplimiento en aguas de jurisdicción nacional.

Convenios internacionales que Chile aplica a través de DIRECTEMAR:

| Convenio | Objeto | Promulgación en Chile |
| --- | --- | --- |
| SOLAS 1974 | Seguridad de la vida humana en el mar | D.S. (RREE) 328/1980 |
| MARPOL 73/78 | Prevención de la contaminación por buques | D.S. (RREE) 1.689/1994 |
| STCW 1978 | Formación, titulación y guardia de la gente de mar | D.S. (RREE) 662/1987 (por reconfirmar) |
| COLREG 1972 | Reglamento para prevenir abordajes | D.S. (RREE) 473/1977 |

Organismo internacional: Organización Marítima Internacional (OMI / IMO).
Índice oficial de convenios: <https://www.directemar.cl>.

### 2.2 Buques de la Armada (acorazados, portaviones, submarinos)

Marco institucional público e histórico únicamente. Estos buques **no** se rigen
por la Ley de Navegación mercante sino por normativa militar, en el marco de la
**Ley 18.948, Orgánica Constitucional de las Fuerzas Armadas**, y dependen del
Ministerio de Defensa. La misma DIRECTEMAR depende de la Armada y ejerce la
función civil de Autoridad Marítima.

Derecho internacional aplicable: **CONVEMAR** (Convención de las Naciones Unidas
sobre el Derecho del Mar), promulgada por D.S. (RREE) 1.393/1997. Para buques de
guerra son relevantes el derecho de paso inocente (Arts. 17 a 26) y el régimen e
inmunidad de los buques de guerra (Arts. 29 a 32). Este repositorio se limita a
historia pública y principios generales, sin información operativa ni de
sistemas de armas (ver `docs/04-seguridad-y-limites.md`).

---

## 3. Vehículos aéreos

### 3.1 Aviones civiles (aviones pequeños)

Base legal: **Ley 18.916, Código Aeronáutico**. Fuente:
<https://www.bcn.cl/leychile/Navegar?idNorma=30287>.

| Tema | Norma | Detalle |
| --- | --- | --- |
| Soberanía del espacio aéreo | Código Aeronáutico, Art. 1 | El Estado tiene soberanía exclusiva del espacio aéreo sobre su territorio. |
| Jurisdicción | Código Aeronáutico, Art. 2 | Aeronaves, personas y cosas a bordo quedan sujetas a la ley chilena. |
| Matrícula | Código Aeronáutico, Art. 32 | La matrícula confiere nacionalidad chilena a la aeronave. |
| Registro Nacional de Aeronaves | Código Aeronáutico, Arts. 44 y 45 | Registro público de matrícula, propiedad y gravamenes. |
| Aeronavegabilidad | Código Aeronáutico, Art. 52 | Ninguna aeronave vuela sin certificado de aeronavegabilidad. |
| Personal aeronáutico | Código Aeronáutico, Art. 57 | Base del régimen de licencias del personal. |

Licencias y certificados: los otorga la **DGAC** conforme a la reglamentación
DAR-01 (Licencias al Personal Aeronáutico) y las normas DAN complementarias
(por ejemplo DAN 61). Tipos de licencia de vuelo: Alumno Piloto, Piloto Privado
(PPL), Piloto Comercial (CPL), Piloto de Transporte de Línea Aérea (ATP), más
habilitación de vuelo por instrumentos.

- PPL (referencia DGAC): edad mínima 18 años, mínimo 40 horas de vuelo, examenes
  teórico y práctico, certificado médico aeronáutico.
- CPL (referencia DGAC): mínimo 200 horas de vuelo (o 150 en escuela aprobada) y
  certificado médico correspondiente.

Fuente: <https://www.dgac.gob.cl/licencias/>.

Marco internacional: **Convenio de Chicago 1944** (crea la OACI / ICAO),
promulgado en Chile por D.S. (RREE) 509 bis de 1957. La reglamentación DAR/DAN
implementa en Chile los estandares y prácticas recomendadas de sus Anexos.

**Aviones de pasajeros (aviación comercial)**: operados por explotadores aéreos
certificados (AOC) bajo la fiscalización de la DGAC. La tripulación de vuelo
requiere licencia de **Piloto de Transporte de Línea Aérea (ATP)** además de las
habilitaciones de tipo, y la operación se rige por las normas DAN aplicables al
transporte aéreo comercial y por los Anexos del Convenio de Chicago.

### 3.2 Helicópteros

Las aeronaves de ala rotatoria se rigen por el mismo marco que la aviación civil:
**Código Aeronáutico (Ley 18.916)** y fiscalización de la **DGAC**. La licencia
de piloto de helicóptero y sus habilitaciones están reguladas por la
reglamentación **DAN 61** (licencias para pilotos y sus habilitaciones), con
certificado médico aeronáutico. Los usos incluyen rescate, transporte, trabajo
aéreo (extinción de incendios, carga externa) y servicios médicos.

### 3.3 Drones (RPAS)

Las **aeronaves pilotadas a distancia (RPAS / UAV)** civiles se rigen por la
**DGAC** a través de la norma **DAN 151** (operaciones de aeronaves pilotadas a
distancia). El marco general cubre el registro del aparato, la responsabilidad
del piloto a distancia, y restricciones de operación como no volar sobre
aglomeraciones de personas, respetar zonas prohibidas y la cercanía de
aeropuertos. Los umbrales exactos (peso, altura máxima, distancias) y la
edición vigente de la DAN 151 se listan en datos por reconfirmar. Fuente:
<https://www.dgac.gob.cl>.

### 3.4 Aviones de combate

Marco público únicamente. Las aeronaves militares de la **Fuerza Aérea de Chile
(FACH)** se rigen por normativa militar (marco de la Ley 18.948) y no por las
licencias civiles de la DGAC ni por la matrícula civil del Código Aeronáutico.
El repositorio se limita a historia pública y principios generales, sin
sistemas de armas ni táctica.

---

## 4. Vehículos espaciales

Chile **no** cuenta a la fecha con una ley espacial nacional integral; el marco
interno es de política pública más los tratados internacionales.

- **Política Nacional Espacial**: Decreto 30 del Ministerio de Ciencia,
  Tecnología, Conocimiento e Innovación (aprobada 2024, publicada 2025). Fuente:
  <https://www.bcn.cl/leychile/navegar?idNorma=1215119>.
- **Sistema Nacional Satelital (SNSat)**: programa liderado por la FACH para
  dotar a Chile de capacidades satelitales.

El material espacial real (cohetes lanzadores, transbordadores y estaciones como
la ISS) opera bajo la jurisdicción del **Estado de lanzamiento** y su agencia
espacial (por ejemplo NASA, ESA, Roscosmos, JAXA, CSA), dentro del marco de los
tratados internacionales. La ISS se rige además por un **Acuerdo
Intergubernamental** entre los países socios.

Tratados internacionales del espacio ultraterrestre ratificados por Chile
(marco de UNOOSA):

| Tratado | Objeto | Promulgación en Chile |
| --- | --- | --- |
| Tratado del Espacio Ultraterrestre (1967) | Principios de la actividad espacial de los Estados | D.S. (RREE) 77/1982 |
| Acuerdo de Salvamento y Devolución (1968) | Rescate de astronautas y objetos | D.S. (RREE) 76/1982 |
| Convenio de Responsabilidad (1972) | Responsabilidad por daños de objetos espaciales | D.S. (RREE) 818 (año por reconfirmar) |
| Convenio de Registro (1975) | Registro de objetos lanzados al espacio | Decreto por reconfirmar |

Compilación oficial de la ONU (UNOOSA):
<https://www.unoosa.org/pdf/publications/STSPACE11S.pdf>.

---

## 5. Datos por reconfirmar

Puntos donde las fuentes secundarias discrepan o donde no se confirmó la cita
exacta. Verificar en el texto vigente antes de tomarlos como definitivos.

- **Ley 18.290, Art. 13**: años exactos de edad y prerrequisitos de las clases
  profesionales.
- **Casco**: números de decreto del MTT que fijan el tipo de casco y montos de
  multa.
- **Velocidad urbana**: la reducción a 50 km/h la establecio la Ley 21.103 de
  2018; conviene reconfirmar el número de artículo modificado (145 o 150) en el
  texto refundido vigente.
- **DL 2.222**: numeración vigente de los artículos 29 y 102.
- **STCW**: número y fecha exactos del decreto promulgatorio en Chile.
- **Reglamento del Registro de Naves**: número y fecha del reglamento específico.
- **Convenio de Responsabilidad (1972)**: año exacto del D.S. 818 (1976 o 1977).
- **Convenio de Registro (1975)**: número y fecha del decreto promulgatorio.
- **Ley espacial / Agencia Espacial**: estado de tramitación del proyecto de ley.
- **Ferroviario**: número y fecha exactos de la Ley General de Ferrocarriles y sus reglamentos; régimen de habilitación de maquinistas.
- **Maquinaria de izaje fija**: normas específicas de certificación del operador de grúa y de montaje de grúa torre.
- **Helicópteros**: confirmar edición vigente de la DAN 61 aplicable a la licencia de helicóptero.
- **Drones (RPAS)**: confirmar edición vigente de la DAN 151 y los umbrales exactos de peso, altura y distancias.
- **Ascensores**: plazos exactos de mantención e inspección y organismos certificadores de la Ley 20.296.
- **Fórmula 1 / competición**: versión vigente del reglamento FIA y organización nacional del automovilismo.

## 6. Cómo usar este marco en la simulación

- Traducir cada requisito legal en una regla del simulador (por ejemplo, exigir
  casco antes de arrancar una moto, o certificado médico antes de un vuelo).
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Mantener el enfoque público y general en los vehículos militares.
- Enlazar cada dato usado a su fuente en `manuales/fuentes.md`.
