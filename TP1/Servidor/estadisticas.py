def calcular_indicadores(resultado_simulacion):
    solicitudes_atendidas = resultado_simulacion["solicitudes_atendidas"]
    historial = resultado_simulacion["historial"]
    duracion_simulacion = resultado_simulacion["duracion_simulacion"]

    cantidad_atendidas = len(solicitudes_atendidas)
    tiempo_espera_total = sum(s.tiempo_espera for s in solicitudes_atendidas)
    tiempo_sistema_total = sum(
        s.tiempo_inicio + s.tiempo_servicio - s.tiempo_llegada
        for s in solicitudes_atendidas
    )
    tiempo_ocupado = sum(s.tiempo_servicio for s in solicitudes_atendidas)

    if cantidad_atendidas > 0:
        tiempo_espera_promedio = tiempo_espera_total / cantidad_atendidas
        tiempo_sistema_promedio = tiempo_sistema_total / cantidad_atendidas
        tiempo_espera_maximo = max(s.tiempo_espera for s in solicitudes_atendidas)
    else:
        tiempo_espera_promedio = 0.0
        tiempo_sistema_promedio = 0.0
        tiempo_espera_maximo = 0.0

    cola_maxima = max((evento["cola"] for evento in historial), default=0)
    utilizacion = (tiempo_ocupado / duracion_simulacion) * 100

    return {
        "solicitudes_generadas": resultado_simulacion["solicitudes_generadas"],
        "solicitudes_atendidas": cantidad_atendidas,
        "tiempo_espera_promedio": tiempo_espera_promedio,
        "tiempo_espera_maximo": tiempo_espera_maximo,
        "tiempo_sistema_promedio": tiempo_sistema_promedio,
        "cola_maxima": cola_maxima,
        "tiempo_ocupado": tiempo_ocupado,
        "utilizacion": utilizacion,
        "tiempo_final": resultado_simulacion["tiempo_final"],
    }
