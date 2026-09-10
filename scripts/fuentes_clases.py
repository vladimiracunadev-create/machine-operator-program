"""Catálogo curado de fuentes públicas por curso.

Las fuentes de ficción identifican el canon; las fuentes técnicas se usan para
contrastar ese canon con física, seguridad y operación reales.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Fuente:
    identificador: str
    titulo: str
    institucion: str
    url: str
    uso: str


def f(identificador: str, titulo: str, institucion: str, url: str, uso: str) -> Fuente:
    return Fuente(identificador, titulo, institucion, url, uso)


CHILE_TRANSITO = f("CL-LEY-18290", "Ley de Tránsito 18.290", "BCN Chile", "https://www.bcn.cl/leychile/navegar?idNorma=29708", "marco legal chileno")
CONASET = f("CL-CONASET", "Manuales para conductores", "CONASET", "https://www.conaset.cl/manuales/", "formación vial y seguridad")
NHTSA_MOTOS = f("US-NHTSA-MOTO", "Motorcycle Safety", "NHTSA", "https://www.nhtsa.gov/road-safety/motorcycles", "riesgos, equipo y conducción segura")
MSF = f("MSF-BRC", "Motorcycle Safety Foundation Library", "MSF", "https://msf-usa.org/library/", "formación inicial y ejercicios")
NHTSA = f("US-NHTSA", "Vehicle Safety", "NHTSA", "https://www.nhtsa.gov/vehicle-safety", "seguridad de vehículos terrestres")
FMCSA = f("US-FMCSA-CDL", "Commercial Driver's License Manual", "FMCSA", "https://www.fmcsa.dot.gov/registration/commercial-drivers-license/cdl-manual", "operación de buses y camiones")
FIA = f("FIA-F1-2026", "Formula 1 Regulations", "FIA", "https://www.fia.com/regulations/formula-1", "reglamento, arquitectura y seguridad de Fórmula 1")
OSHA_GRUAS = f("OSHA-CRANES", "Crane, Derrick and Hoist Safety", "OSHA", "https://www.osha.gov/cranes-derricks", "izaje, riesgos y controles")
OSHA_TORRE = f("OSHA-TOWER", "1926.1435 Tower Cranes", "OSHA", "https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1435", "requisitos específicos de grúas torre")
OSHA_AGRO = f("OSHA-AGRI", "Agricultural Operations: Hazards and Controls", "OSHA", "https://www.osha.gov/agricultural-operations/hazards", "tractores, aperos y riesgos agrícolas")
OSHA_CONSTRUCCION = f("OSHA-CONSTRUCTION", "Construction Industry", "OSHA", "https://www.osha.gov/construction", "maquinaria y seguridad de obra")
OSHA_ASCENSORES = f("OSHA-ELEVATORS", "1917.116 Elevators and Escalators", "OSHA", "https://www.osha.gov/laws-regs/regulations/standardnumber/1917/1917.116", "inspección y riesgos de transporte vertical")
FRA = f("US-FRA-OPS", "Railroad Operating Practices", "Federal Railroad Administration", "https://railroads.fra.dot.gov/railroad-safety/divisions/operating-practices/operating-practices-0", "operación, señalización y competencias ferroviarias")
FRA_HUMAN = f("US-FRA-HF", "Human Factors: Tasks and Demands", "Federal Railroad Administration", "https://railroads.fra.dot.gov/human-factors/elearning-attention/tasks-demands", "factores humanos y carga de trabajo")
IMO_NAV = f("IMO-NAV", "Safety of Navigation", "International Maritime Organization", "https://www.imo.org/en/ourwork/safety/pages/navigationdefault.aspx", "navegación, SOLAS, COLREG y STCW")
IMO_COLREG = f("IMO-COLREG", "Collision Regulations", "International Maritime Organization", "https://www.imo.org/en/about/conventions/pages/colreg.aspx", "prevención de abordajes")
DIRECTEMAR = f("CL-DIRECTEMAR", "Marco normativo", "DIRECTEMAR", "https://www.directemar.cl/directemar/marco-normativo", "marco marítimo chileno")
FAA = f("US-FAA-HANDBOOKS", "Aviation Handbooks and Manuals", "FAA", "https://www.faa.gov/regulations_policies/handbooks_manuals", "aerodinámica, sistemas y operación")
FAA_HELI = f("US-FAA-HELI", "Helicopter Flying Handbook", "FAA", "https://www.faa.gov/sites/faa.gov/files/helicopter_flying_handbook.pdf", "aerodinámica y control de helicópteros")
FAA_UAS = f("US-FAA-UAS", "Unmanned Aircraft Systems", "FAA", "https://www.faa.gov/uas", "operación y normativa RPAS")
DGAC = f("CL-DGAC", "Normativa aeronáutica", "DGAC Chile", "https://www.dgac.gob.cl/normativa/", "marco aeronáutico chileno")
NASA_ROCKETS = f("NASA-ROCKETS", "Rockets Educator Guide", "NASA", "https://www.nasa.gov/wp-content/uploads/2012/07/rockets-educator-guide-20.pdf", "propulsión, estabilidad y trayectoria")
NASA_SHUTTLE = f("NASA-SHUTTLE", "The Space Shuttle", "NASA", "https://www.nasa.gov/reference/the-space-shuttle/", "arquitectura y operación del transbordador")
NASA_ISS = f("NASA-ISS", "International Space Station", "NASA", "https://www.nasa.gov/reference/international-space-station/", "módulos, órbita y soporte vital")
NASA_SPACECRAFT = f("NASA-SPACECRAFT", "Spaceships and Rockets", "NASA", "https://www.nasa.gov/humans-in-space/spaceships-and-rockets/", "naves, sistemas y misiones")
UNOOSA = f("UNOOSA-TREATIES", "Space Law Treaties and Principles", "UNOOSA", "https://www.unoosa.org/oosa/SpaceLaw/treaties.html", "derecho espacial internacional")
TANK_MUSEUM = f("TANK-MUSEUM", "Tank Collection", "The Tank Museum", "https://tankmuseum.org/tank-nuts/tank-collection", "historia pública de vehículos blindados")
NHHC = f("US-NHHC-SHIPS", "Ships", "Naval History and Heritage Command", "https://www.history.navy.mil/browse-by-topic/ships.html", "historia pública de buques militares")
GUTENBERG_NAUTILUS = f("GUTENBERG-20000", "Twenty Thousand Leagues under the Sea", "Project Gutenberg", "https://www.gutenberg.org/ebooks/164", "obra primaria en dominio público")
STARWARS = f("STARWARS-DATABANK", "Star Wars Databank", "Lucasfilm", "https://www.starwars.com/databank", "canon narrativo y diseño visual")
STARWARS_FALCON = f("STARWARS-FALCON", "Millennium Falcon", "Lucasfilm", "https://www.starwars.com/databank/millennium-falcon", "canon narrativo del vehículo")
STARWARS_DEATHSTAR = f("STARWARS-DEATHSTAR", "Death Star", "Lucasfilm", "https://www.starwars.com/databank/death-star", "canon narrativo de la estación")
STARTREK = f("STARTREK-DATABASE", "Star Trek Database", "Paramount", "https://www.startrek.com/database", "canon narrativo y tecnologías de ficción")
ROBOTECH = f("ROBOTECH-OFFICIAL", "Robotech", "Harmony Gold", "https://robotech.com/", "referencia oficial del universo ficticio")
THUNDERBIRDS = f("THUNDERBIRDS-OFFICIAL", "Thunderbirds Vehicles", "ITV", "https://www.thunderbirds.com/", "referencia oficial de vehículos de rescate")
BACK_FUTURE = f("UNIVERSAL-BTTF", "Back to the Future", "Universal Pictures At Home", "https://www.universalpicturesathome.com/movies/back-to-the-future", "obra audiovisual primaria")
NASA_PHYSICS = f("NASA-FLIGHT", "Beginner's Guide to Aeronautics", "NASA", "https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/", "contraste con física y vuelo reales")
IBM_TELEPORT = f("IBM-QUANTUM-TELEPORT", "Quantum Teleportation", "IBM Quantum Learning", "https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/quantum-teleportation", "información cuántica, entrelazamiento y teorema de no clonación")


FUENTES_POR_CURSO: dict[str, tuple[Fuente, ...]] = {
    "motos": (CHILE_TRANSITO, CONASET, NHTSA_MOTOS, MSF),
    "automoviles": (CHILE_TRANSITO, CONASET, NHTSA),
    "formula-1": (FIA, NHTSA, NASA_PHYSICS),
    "buses": (CHILE_TRANSITO, FMCSA, NHTSA),
    "camiones": (CHILE_TRANSITO, FMCSA, NHTSA),
    "tanques": (TANK_MUSEUM, NHTSA, NASA_PHYSICS),
    "ascensores": (OSHA_ASCENSORES, NHTSA),
    "tren-pasajeros": (FRA, FRA_HUMAN),
    "tren-alta-velocidad": (FRA, FRA_HUMAN, NASA_PHYSICS),
    "tren-carga": (FRA, FRA_HUMAN),
    "gruas": (OSHA_GRUAS, CHILE_TRANSITO),
    "grua-portuaria": (OSHA_GRUAS, IMO_NAV, DIRECTEMAR),
    "grua-torre": (OSHA_GRUAS, OSHA_TORRE),
    "tractores": (OSHA_AGRO, CHILE_TRANSITO),
    "maquinaria-construccion": (OSHA_CONSTRUCCION, OSHA_GRUAS),
    "barcos-mercantes": (IMO_NAV, IMO_COLREG, DIRECTEMAR),
    "cruceros": (IMO_NAV, IMO_COLREG, DIRECTEMAR),
    "acorazados": (NHHC, IMO_NAV),
    "portaviones": (NHHC, IMO_NAV, FAA),
    "submarinos": (NHHC, IMO_NAV, NASA_PHYSICS),
    "aviones-pequenos": (FAA, DGAC),
    "aviones-pasajeros": (FAA, DGAC),
    "aviones-combate": (FAA, NASA_PHYSICS),
    "helicopteros": (FAA_HELI, FAA, DGAC),
    "drones": (FAA_UAS, DGAC),
    "cohetes": (NASA_ROCKETS, UNOOSA),
    "transbordadores": (NASA_SHUTTLE, FAA, UNOOSA),
    "estacion-espacial": (NASA_ISS, UNOOSA),
    "naves-espaciales": (NASA_SPACECRAFT, UNOOSA),
    "delorean": (BACK_FUTURE, NHTSA, NASA_PHYSICS),
    "caza-estelar": (STARWARS, NASA_PHYSICS),
    "nave-exploracion": (STARTREK, NASA_SPACECRAFT, NASA_PHYSICS),
    "nautilus": (GUTENBERG_NAUTILUS, IMO_NAV, NASA_PHYSICS),
    "caza-transformable": (ROBOTECH, FAA, NASA_PHYSICS),
    "halcon-milenario": (STARWARS_FALCON, NASA_SPACECRAFT, NASA_PHYSICS),
    "sdf-1": (ROBOTECH, NASA_SPACECRAFT, NASA_PHYSICS),
    "estrella-de-la-muerte": (STARWARS_DEATHSTAR, NASA_SPACECRAFT, NASA_PHYSICS),
    "teletransportador": (STARTREK, IBM_TELEPORT, NASA_PHYSICS),
    "thunderbird-1": (THUNDERBIRDS, FAA, NASA_PHYSICS),
    "thunderbird-2": (THUNDERBIRDS, FAA, NASA_PHYSICS),
    "thunderbird-3": (THUNDERBIRDS, NASA_ROCKETS, NASA_PHYSICS),
}
