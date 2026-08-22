import random

from modelos import Solicitud


def generar_tiempo_entre_llegadas(tasa_llegadas):
    return random.expovariate(tasa_llegadas)


def generar_tiempo_servicio(servicio_min, servicio_max):
    return random.uniform(servicio_min, servicio_max)


def registrar_evento(historial, tiempo, evento, cola, servidor_ocupado, solicitud_id):
    historial.append(
        {
            "tiempo": tiempo,
            "evento": evento,
            "cola": len(cola),
            "servidor_ocupado": servidor_ocupado,
            "solicitud": solicitud_id,
        }
    )


def simular(duracion_simulacion, tasa_llegadas, servicio_min, servicio_max):
    reloj = 0.0
    servidor_ocupado = False
    cola = []
    solicitud_actual = None

    proxima_llegada = generar_tiempo_entre_llegadas(tasa_llegadas)
    fin_servicio = float("inf")

    id_solicitud = 0
    solicitudes_atendidas = []
    historial = []

    while reloj < duracion_simulacion or servidor_ocupado or len(cola) > 0:
        if proxima_llegada <= fin_servicio and proxima_llegada <= duracion_simulacion:
            reloj = proxima_llegada
            id_solicitud += 1
            solicitud = Solicitud(id=id_solicitud, tiempo_llegada=reloj)

            if not servidor_ocupado:
                servidor_ocupado = True
                tiempo_servicio = generar_tiempo_servicio(servicio_min, servicio_max)
                solicitud.tiempo_inicio = reloj
                solicitud.tiempo_espera = 0.0
                solicitud.tiempo_servicio = tiempo_servicio
                solicitud_actual = solicitud
                fin_servicio = reloj + tiempo_servicio
            else:
                cola.append(solicitud)

            registrar_evento(
                historial,
                reloj,
                "llegada",
                cola,
                servidor_ocupado,
                solicitud.id,
            )

            proxima_llegada = reloj + generar_tiempo_entre_llegadas(tasa_llegadas)
        else:
            reloj = fin_servicio
            id_finalizada = solicitud_actual.id
            solicitudes_atendidas.append(solicitud_actual)

            if len(cola) > 0:
                solicitud = cola.pop(0)
                tiempo_espera = reloj - solicitud.tiempo_llegada
                solicitud.tiempo_inicio = reloj
                solicitud.tiempo_espera = tiempo_espera
                tiempo_servicio = generar_tiempo_servicio(servicio_min, servicio_max)
                solicitud.tiempo_servicio = tiempo_servicio
                solicitud_actual = solicitud
                fin_servicio = reloj + tiempo_servicio
            else:
                servidor_ocupado = False
                solicitud_actual = None
                fin_servicio = float("inf")

            registrar_evento(
                historial,
                reloj,
                "fin_servicio",
                cola,
                servidor_ocupado,
                id_finalizada,
            )

    return {
        "duracion_simulacion": duracion_simulacion,
        "solicitudes_generadas": id_solicitud,
        "solicitudes_atendidas": solicitudes_atendidas,
        "tiempo_final": reloj,
        "historial": historial,
    }
