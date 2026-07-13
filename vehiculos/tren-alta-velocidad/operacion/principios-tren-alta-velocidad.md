# 🧪 Principios y operacion del tren de alta velocidad

[🏠 Inicio](../../../README.md) · [🚄 Curso: Tren de alta velocidad](../README.md) · 🧪 Principios

Documento general y educativo. No sustituye la formacion certificada de un
maquinista ni los manuales del fabricante y del administrador de la
infraestructura. Describe como se opera un tren de alta velocidad en simulacion y
que principios fisicos conviene representar.

## Principios de funcionamiento

- **Propulsion**: los motores electricos, alimentados desde la catenaria, entregan
  esfuerzo de traccion a los ejes. El manipulador regula esa entrega.
- **Energia cinetica enorme**: la gran masa a gran velocidad acumula muchisima
  energia; frenar exige combinar varios sistemas y mucho espacio.
- **Frenado de distancias de kilometros**: no se detiene en metros; la frenada se
  planifica con mucha anticipacion respecto a la senal objetivo.
- **Dominio de la resistencia aerodinamica**: por encima de 250 km/h la resistencia
  del aire es la principal fuerza que se opone al avance.
- **Estabilidad a alta velocidad**: bogies, suspension y via dedicada evitan la
  oscilacion y mantienen el tren centrado sobre el riel.
- **Ruta fija**: el tren no elige direccion; sigue la via y las agujas que le
  asigna el control de trafico.

## Fases de operacion

| Fase | Que ocurre | Puntos clave |
| --- | --- | --- |
| Inspeccion previa | Revision basica | Pantografo, frenos, puertas, senalizacion en cabina. |
| Toma de tension | Subir pantografo | Confirmar tension de linea antes de traccionar. |
| Puesta en marcha | Iniciar movimiento | Confirmar vigilante y aplicar traccion progresiva. |
| Circulacion | Marcha a alta velocidad | Respetar la velocidad objetivo del DMI, anticipar. |
| Frenado planificado | Preparar la parada | Iniciar el frenado con mucha anticipacion. |
| Parada en estacion | Detener con precision | Alinear puertas al anden, abrir con enclavamiento. |
| Cierre | Dejar seguro | Bajar pantografo, freno aplicado, sistemas off. |

## Frenado anticipado: idea general

1. Conocer la **velocidad objetivo** que marca el DMI mucho antes del punto.
2. Iniciar el frenado con **kilometros** de anticipacion, no metros.
3. Usar primero el **freno regenerativo y dinamico**, que no desgastan.
4. Completar con el **freno neumatico** para la detencion final.
5. Detener con precision para alinear las puertas con el anden.

## Errores comunes que la simulacion puede ensenar a evitar

- Frenar tarde, sin respetar la enorme distancia de frenado.
- Ignorar la velocidad objetivo del DMI y provocar el frenado automatico.
- No confirmar el dispositivo de hombre muerto o vigilante.
- Subestimar la resistencia aerodinamica y el consumo a alta velocidad.
- Abrir puertas sin el enclavamiento o con el tren mal alineado al anden.

## Relacion con los niveles de realismo

- **Nivel 1 (educativo)**: traccionar, frenar a tiempo y respetar la senal objetivo.
- **Nivel 2 (simplificado)**: agregar energia cinetica, resistencia aerodinamica
  y distancia de frenado realista.
- **Nivel 3 (tecnico)**: sumar gestion de varios frenos, tension de linea, vigilante
  y supervision ETCS.

Ver [`docs/03-niveles-de-realismo.md`](../../../docs/03-niveles-de-realismo.md) para el detalle de cada nivel.

---

[⬅️ Anterior: Mandos](../mandos/manual-mandos-tren-alta-velocidad.md) · [➡️ Siguiente: Entornos de trabajo](entornos-tren-alta-velocidad.md)
