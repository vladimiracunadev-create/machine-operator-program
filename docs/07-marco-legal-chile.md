# Marco legal y normativo (Chile)

Referencia tecnica del marco legal chileno e internacional aplicable a los
vehiculos del multisimulador. Sirve para disenar reglamentos de simulacion
realistas y para orientar la investigacion de cada vehiculo.

## Aviso importante

Este documento es material educativo y de diseno de simulacion. **No es asesoria
legal ni sustituye las fuentes oficiales vigentes.** Las leyes cambian, se
modifican y se refunden; los numeros de articulo y de decreto pueden variar
entre versiones. Antes de usar cualquier dato para un fin real, verifica el
texto vigente en la fuente oficial (ver enlaces).

Al final hay una seccion de **datos por reconfirmar**: puntos donde las fuentes
secundarias discrepan o donde no se pudo confirmar la cita exacta.

## Fuentes oficiales de referencia

| Ambito | Organismo | Sitio |
| --- | --- | --- |
| Leyes (texto oficial) | Biblioteca del Congreso Nacional (BCN) | <https://www.bcn.cl/leychile> |
| Transito y seguridad vial | CONASET | <https://www.conaset.cl> |
| Transporte | Ministerio de Transportes (MTT) | <https://www.mtt.gob.cl> |
| Registro de vehiculos | Servicio de Registro Civil e Identificacion | <https://www.registrocivil.cl> |
| Maritimo | DIRECTEMAR (Autoridad Maritima) | <https://www.directemar.cl> |
| Aeronautico | Direccion General de Aeronautica Civil (DGAC) | <https://www.dgac.gob.cl> |
| Espacial | Ministerio de Ciencia, Tecnologia, Conocimiento e Innovacion | <https://www.minciencia.gob.cl> |

---

## 1. Vehiculos terrestres

Base legal principal: **Ley 18.290, Ley de Transito** (texto refundido por DFL 1
de 2007). Fuente: <https://www.bcn.cl/leychile/navegar?idNorma=29708>.

### 1.1 Clases de licencia de conducir (Ley 18.290, Art. 12)

Las licencias se agrupan en Profesionales (Clase A), No Profesionales (Clases B
y C) y Especiales (Clases D, E y F).

| Clase | Tipo | Habilita para conducir |
| --- | --- | --- |
| A-1 | Profesional | Taxis (transporte de pasajeros). |
| A-2 | Profesional | Taxis, ambulancias y transporte de pasajeros de 10 a 17 asientos. |
| A-3 | Profesional | Transporte de pasajeros sin limite de asientos (buses, minibuses, trolebuses). Incluye A-1 y A-2. |
| A-4 | Profesional | Vehiculos simples de carga con peso bruto vehicular superior a 3.500 kg. |
| A-5 | Profesional | Todo vehiculo de carga, simple o articulado. Incluye A-4. |
| B | No profesional | Vehiculos de 3 o mas ruedas, particulares, hasta 9 asientos o carga hasta 3.500 kg (automoviles, camionetas). |
| C | No profesional | Vehiculos de dos o tres ruedas: motocicletas, motonetas, bicimotos. |
| D | Especial | Maquinaria automotriz: gruas, tractores, cargadores, retroexcavadoras y similares. |
| E | Especial | Vehiculos a traccion animal. |
| F | Especial | Vehiculos de las Fuerzas Armadas, Carabineros, PDI, Gendarmeria y Bomberos. |

Correspondencia rapida por vehiculo del repositorio:

- Moto: **Clase C**.
- Automovil particular: **Clase B**.
- Bus de transporte publico: **Clase A-3** (o A-2 para 10 a 17 asientos).
- Camion simple de carga (mas de 3.500 kg): **Clase A-4**.
- Camion articulado (tractocamion con acoplado): **Clase A-5**.
- Grua, tractor y maquinaria de construccion (maquinaria automotriz): **Clase D**.

Edad minima general (Art. 13): 18 anos para clases B y C. Las clases
profesionales exigen edad mayor y haber sido titular previo de licencia Clase B
(anos exactos: ver datos por reconfirmar).

### 1.2 Requisitos y elementos de seguridad

| Tema | Norma | Detalle |
| --- | --- | --- |
| Casco en moto | Ley 18.290, Art. 84 | Casco protector obligatorio para conductor y acompanante. |
| Cinturon de seguridad | Ley 18.290, Art. 79 | Obligatorio en asientos delanteros y traseros segun ano del vehiculo. |
| Sistema de retencion infantil | Ley 20.904 (modifica Art. 75) | Silla obligatoria para ninos hasta 8 anos; prohibido menores de 12 en asiento delantero. |
| Velocidad urbana | Ley 21.103 (2018) | Limite urbano general de 50 km/h. |
| Convivencia vial | Ley 21.088 (2018) | Reglas para ciclos, ciclovias, distancia de adelantamiento de 1,5 m. |

Referencias: CONASET cinturon <https://www.conaset.cl/normativa-cinturon/>;
CONASET sillas <https://www.conaset.cl/sillas-infantiles/>; CONASET velocidad
<https://www.conaset.cl/normativa-velocidad/>.

### 1.3 Limites de velocidad (Ley 18.290, Art. 150)

| Via | Livianos y motos | Buses y camiones pesados |
| --- | --- | --- |
| Urbana | 50 km/h | 50 km/h |
| Rural, 1 pista por sentido | 100 km/h | 90 km/h (buses interurbanos hasta 100) |
| Rural, 2 o mas pistas por sentido | 120 km/h | 90 a 100 km/h segun tipo |

Municipalidades (zona urbana) y la Direccion de Vialidad (zona rural) pueden
fijar limites distintos con senalizacion reglamentaria.

### 1.4 Documentos obligatorios de circulacion

| Documento | Norma | Organismo |
| --- | --- | --- |
| Inscripcion en el Registro de Vehiculos Motorizados (padron) | Ley 18.290, Titulo III; D.S. 1.111/1984 | Registro Civil |
| Permiso de circulacion (anual, vence 31 de marzo) | Ley 18.290 y normas municipales | Municipalidades |
| Revision tecnica y de gases | Ley 18.290, Titulo VII | Plantas de revision tecnica (MTT) |
| SOAP (Seguro Obligatorio de Accidentes Personales) | Ley 18.490 | Companias de seguros (supervisa CMF) |

El permiso de circulacion exige SOAP vigente, revision tecnica al dia e
inscripcion en el registro. El SOAP cubre lesiones o muerte de personas, no
danos materiales.

### 1.5 Organismos

- **CONASET**: politica de seguridad vial, estadisticas, manuales del conductor.
- **MTT**: transporte publico, revisiones tecnicas, homologacion.
- **Registro Civil**: Registro de Vehiculos Motorizados y padron.
- **Municipalidades**: licencias de conducir y permisos de circulacion.
- **CMF**: supervisa el SOAP.

### 1.6 Ferroviario

El transporte por ferrocarril se rige por la **Ley General de Ferrocarriles** y la
normativa del sector, con la **Empresa de los Ferrocarriles del Estado (EFE)** como
operador estatal historico y el MTT en el rol regulador. La operacion cubre
senalizacion, gestion de la via, pasos a nivel y habilitacion del personal de
conduccion (maquinistas). Los numeros y fechas exactos de la ley y sus reglamentos
se listan en datos por reconfirmar. Fuente institucional: <https://www.efe.cl>.

### 1.7 Maquinaria de izaje fija (grua portuaria y grua torre)

Las gruas fijas (de puerto y de edificio) no circulan por via publica, por lo que
no requieren licencia de conducir. Se rigen por la **seguridad laboral**:

- **Ley 16.744**: seguro social contra riesgos de accidentes del trabajo y
  enfermedades profesionales.
- **D.S. 594 (MINSAL)**: condiciones sanitarias y ambientales basicas en los
  lugares de trabajo.
- Operacion por personal **certificado/competente**, plan de izaje, tablas de
  carga del fabricante, senalero (rigger) y area de exclusion.

En el ambito portuario aplican ademas las normas de la Autoridad Maritima y del
recinto portuario. El detalle de certificacion del operador y montaje de grua
torre se indica en datos por reconfirmar.

### 1.8 Ascensores (transporte vertical)

Los ascensores de edificios se rigen por la **Ley 20.296** (instalacion,
mantencion e inspeccion de ascensores y similares) y por la Ordenanza General de
Urbanismo y Construcciones (OGUC). Exigen mantencion periodica por empresa
competente y certificacion por un organismo autorizado; la fiscalizacion recae
en las municipalidades (Direccion de Obras). Los plazos y detalles exactos se
indican en datos por reconfirmar.

### 1.9 Vehiculos de competicion (Formula 1)

Un monoplaza de Formula 1 **no circula por via publica** ni requiere licencia de
conducir comun: es un vehiculo de competicion regido por el **reglamento
deportivo y tecnico de la FIA** (Federacion Internacional del Automovil) y su
serie. En Chile, el automovilismo deportivo se organiza a traves de la
federacion nacional del automovilismo. El enfoque del curso es tecnico y
educativo, no normativo de transito.

### 1.10 Vehiculos militares terrestres (tanques)

Marco institucional publico e historico unicamente. Los carros de combate son
material del **Ejercito de Chile**, dependiente del Ministerio de Defensa
Nacional, en el marco de la **Ley 18.948** (Organica Constitucional de las
Fuerzas Armadas). Se rigen por normativa militar y no por la Ley de Transito.
Este repositorio se limita a historia publica y principios fisicos generales,
sin tactica, sistemas de armas ni procedimientos operativos (ver
`docs/04-seguridad-y-limites.md`).

---

## 2. Vehiculos maritimos

### 2.1 Buques mercantes

Base legal: **DL 2.222 de 1978, Ley de Navegacion** (Ministerio de Defensa).
Fuente: <https://www.bcn.cl/leychile/navegar?idNorma=6855>.

| Tema | Norma | Detalle |
| --- | --- | --- |
| Autoridad Maritima | DL 2.222, Art. 2 | La Direccion (DIRECTEMAR / DGTM y MM) aplica y fiscaliza la ley. |
| Registro de naves | DL 2.222, Art. 10 | Registros de naves mayores, menores, en construccion, artefactos navales e hipotecas. |
| Nacionalidad de la nave | DL 2.222, Art. 11 | Solo se matriculan naves de propietario chileno (con reglas para personas juridicas). |
| Titulo de capitan | DL 2.222, Art. 49 | Se requiere ser chileno y poseer el titulo conferido por el Director. |
| Dotacion minima de seguridad | DL 2.222, Art. 73 | La determina la Direccion (naves mayores) o la Autoridad Maritima (menores). |

Titulos de la Marina Mercante Nacional: los otorga DIRECTEMAR conforme al
Reglamento de Titulos Profesionales y Permisos de Embarco (TM-007A) y al D.S.
127/2019. Escalafon de cubierta: Capitan, Piloto Primero, Segundo, Tercero y
Piloto Costero. Fuente: <https://www.directemar.cl>.

**Cruceros (buques de pasajeros)**: siguen el mismo marco (DL 2.222 y OMI), con
mayor exigencia de seguridad de pasajeros bajo SOLAS, planes de evacuacion, y
personal titulado bajo STCW. La Autoridad Maritima (DIRECTEMAR) fiscaliza el
cumplimiento en aguas de jurisdiccion nacional.

Convenios internacionales que Chile aplica a traves de DIRECTEMAR:

| Convenio | Objeto | Promulgacion en Chile |
| --- | --- | --- |
| SOLAS 1974 | Seguridad de la vida humana en el mar | D.S. (RREE) 328/1980 |
| MARPOL 73/78 | Prevencion de la contaminacion por buques | D.S. (RREE) 1.689/1994 |
| STCW 1978 | Formacion, titulacion y guardia de la gente de mar | D.S. (RREE) 662/1987 (por reconfirmar) |
| COLREG 1972 | Reglamento para prevenir abordajes | D.S. (RREE) 473/1977 |

Organismo internacional: Organizacion Maritima Internacional (OMI / IMO).
Indice oficial de convenios: <https://www.directemar.cl>.

### 2.2 Buques de la Armada (acorazados, portaviones, submarinos)

Marco institucional publico e historico unicamente. Estos buques **no** se rigen
por la Ley de Navegacion mercante sino por normativa militar, en el marco de la
**Ley 18.948, Organica Constitucional de las Fuerzas Armadas**, y dependen del
Ministerio de Defensa. La misma DIRECTEMAR depende de la Armada y ejerce la
funcion civil de Autoridad Maritima.

Derecho internacional aplicable: **CONVEMAR** (Convencion de las Naciones Unidas
sobre el Derecho del Mar), promulgada por D.S. (RREE) 1.393/1997. Para buques de
guerra son relevantes el derecho de paso inocente (Arts. 17 a 26) y el regimen e
inmunidad de los buques de guerra (Arts. 29 a 32). Este repositorio se limita a
historia publica y principios generales, sin informacion operativa ni de
sistemas de armas (ver `docs/04-seguridad-y-limites.md`).

---

## 3. Vehiculos aereos

### 3.1 Aviones civiles (aviones pequenos)

Base legal: **Ley 18.916, Codigo Aeronautico**. Fuente:
<https://www.bcn.cl/leychile/Navegar?idNorma=30287>.

| Tema | Norma | Detalle |
| --- | --- | --- |
| Soberania del espacio aereo | Codigo Aeronautico, Art. 1 | El Estado tiene soberania exclusiva del espacio aereo sobre su territorio. |
| Jurisdiccion | Codigo Aeronautico, Art. 2 | Aeronaves, personas y cosas a bordo quedan sujetas a la ley chilena. |
| Matricula | Codigo Aeronautico, Art. 32 | La matricula confiere nacionalidad chilena a la aeronave. |
| Registro Nacional de Aeronaves | Codigo Aeronautico, Arts. 44 y 45 | Registro publico de matricula, propiedad y gravamenes. |
| Aeronavegabilidad | Codigo Aeronautico, Art. 52 | Ninguna aeronave vuela sin certificado de aeronavegabilidad. |
| Personal aeronautico | Codigo Aeronautico, Art. 57 | Base del regimen de licencias del personal. |

Licencias y certificados: los otorga la **DGAC** conforme a la reglamentacion
DAR-01 (Licencias al Personal Aeronautico) y las normas DAN complementarias
(por ejemplo DAN 61). Tipos de licencia de vuelo: Alumno Piloto, Piloto Privado
(PPL), Piloto Comercial (CPL), Piloto de Transporte de Linea Aerea (ATP), mas
habilitacion de vuelo por instrumentos.

- PPL (referencia DGAC): edad minima 18 anos, minimo 40 horas de vuelo, examenes
  teorico y practico, certificado medico aeronautico.
- CPL (referencia DGAC): minimo 200 horas de vuelo (o 150 en escuela aprobada) y
  certificado medico correspondiente.

Fuente: <https://www.dgac.gob.cl/licencias/>.

Marco internacional: **Convenio de Chicago 1944** (crea la OACI / ICAO),
promulgado en Chile por D.S. (RREE) 509 bis de 1957. La reglamentacion DAR/DAN
implementa en Chile los estandares y practicas recomendadas de sus Anexos.

**Aviones de pasajeros (aviacion comercial)**: operados por explotadores aereos
certificados (AOC) bajo la fiscalizacion de la DGAC. La tripulacion de vuelo
requiere licencia de **Piloto de Transporte de Linea Aerea (ATP)** ademas de las
habilitaciones de tipo, y la operacion se rige por las normas DAN aplicables al
transporte aereo comercial y por los Anexos del Convenio de Chicago.

### 3.2 Helicopteros

Las aeronaves de ala rotatoria se rigen por el mismo marco que la aviacion civil:
**Codigo Aeronautico (Ley 18.916)** y fiscalizacion de la **DGAC**. La licencia
de piloto de helicoptero y sus habilitaciones estan reguladas por la
reglamentacion **DAN 61** (licencias para pilotos y sus habilitaciones), con
certificado medico aeronautico. Los usos incluyen rescate, transporte, trabajo
aereo (extincion de incendios, carga externa) y servicios medicos.

### 3.3 Drones (RPAS)

Las **aeronaves pilotadas a distancia (RPAS / UAV)** civiles se rigen por la
**DGAC** a traves de la norma **DAN 151** (operaciones de aeronaves pilotadas a
distancia). El marco general cubre el registro del aparato, la responsabilidad
del piloto a distancia, y restricciones de operacion como no volar sobre
aglomeraciones de personas, respetar zonas prohibidas y la cercania de
aeropuertos. Los umbrales exactos (peso, altura maxima, distancias) y la
edicion vigente de la DAN 151 se listan en datos por reconfirmar. Fuente:
<https://www.dgac.gob.cl>.

### 3.4 Aviones de combate

Marco publico unicamente. Las aeronaves militares de la **Fuerza Aerea de Chile
(FACH)** se rigen por normativa militar (marco de la Ley 18.948) y no por las
licencias civiles de la DGAC ni por la matricula civil del Codigo Aeronautico.
El repositorio se limita a historia publica y principios generales, sin
sistemas de armas ni tactica.

---

## 4. Vehiculos espaciales

Chile **no** cuenta a la fecha con una ley espacial nacional integral; el marco
interno es de politica publica mas los tratados internacionales.

- **Politica Nacional Espacial**: Decreto 30 del Ministerio de Ciencia,
  Tecnologia, Conocimiento e Innovacion (aprobada 2024, publicada 2025). Fuente:
  <https://www.bcn.cl/leychile/navegar?idNorma=1215119>.
- **Sistema Nacional Satelital (SNSat)**: programa liderado por la FACH para
  dotar a Chile de capacidades satelitales.

El material espacial real (cohetes lanzadores, transbordadores y estaciones como
la ISS) opera bajo la jurisdiccion del **Estado de lanzamiento** y su agencia
espacial (por ejemplo NASA, ESA, Roscosmos, JAXA, CSA), dentro del marco de los
tratados internacionales. La ISS se rige ademas por un **Acuerdo
Intergubernamental** entre los paises socios.

Tratados internacionales del espacio ultraterrestre ratificados por Chile
(marco de UNOOSA):

| Tratado | Objeto | Promulgacion en Chile |
| --- | --- | --- |
| Tratado del Espacio Ultraterrestre (1967) | Principios de la actividad espacial de los Estados | D.S. (RREE) 77/1982 |
| Acuerdo de Salvamento y Devolucion (1968) | Rescate de astronautas y objetos | D.S. (RREE) 76/1982 |
| Convenio de Responsabilidad (1972) | Responsabilidad por danos de objetos espaciales | D.S. (RREE) 818 (ano por reconfirmar) |
| Convenio de Registro (1975) | Registro de objetos lanzados al espacio | Decreto por reconfirmar |

Compilacion oficial de la ONU (UNOOSA):
<https://www.unoosa.org/pdf/publications/STSPACE11S.pdf>.

---

## 5. Datos por reconfirmar

Puntos donde las fuentes secundarias discrepan o donde no se confirmo la cita
exacta. Verificar en el texto vigente antes de tomarlos como definitivos.

- **Ley 18.290, Art. 13**: anos exactos de edad y prerrequisitos de las clases
  profesionales.
- **Casco**: numeros de decreto del MTT que fijan el tipo de casco y montos de
  multa.
- **Velocidad urbana**: la reduccion a 50 km/h la establecio la Ley 21.103 de
  2018; conviene reconfirmar el numero de articulo modificado (145 o 150) en el
  texto refundido vigente.
- **DL 2.222**: numeracion vigente de los articulos 29 y 102.
- **STCW**: numero y fecha exactos del decreto promulgatorio en Chile.
- **Reglamento del Registro de Naves**: numero y fecha del reglamento especifico.
- **Convenio de Responsabilidad (1972)**: ano exacto del D.S. 818 (1976 o 1977).
- **Convenio de Registro (1975)**: numero y fecha del decreto promulgatorio.
- **Ley espacial / Agencia Espacial**: estado de tramitacion del proyecto de ley.
- **Ferroviario**: numero y fecha exactos de la Ley General de Ferrocarriles y sus reglamentos; regimen de habilitacion de maquinistas.
- **Maquinaria de izaje fija**: normas especificas de certificacion del operador de grua y de montaje de grua torre.
- **Helicopteros**: confirmar edicion vigente de la DAN 61 aplicable a la licencia de helicoptero.
- **Drones (RPAS)**: confirmar edicion vigente de la DAN 151 y los umbrales exactos de peso, altura y distancias.
- **Ascensores**: plazos exactos de mantencion e inspeccion y organismos certificadores de la Ley 20.296.
- **Formula 1 / competicion**: version vigente del reglamento FIA y organizacion nacional del automovilismo.

## 6. Como usar este marco en la simulacion

- Traducir cada requisito legal en una regla del simulador (por ejemplo, exigir
  casco antes de arrancar una moto, o certificado medico antes de un vuelo).
- Usar sanciones educativas (avisos) en vez de castigos frustrantes.
- Mantener el enfoque publico y general en los vehiculos militares.
- Enlazar cada dato usado a su fuente en `manuales/fuentes.md`.
