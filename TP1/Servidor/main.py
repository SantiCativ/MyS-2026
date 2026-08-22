import random
from pathlib import Path

from estadisticas import calcular_indicadores
from graficos import graficar_cola
from simulacion import simular

DURACION_SIMULACION = 480
TASA_LLEGADAS = 10 / 60
SERVICIO_MIN = 2
SERVICIO_MAX = 6
SEMILLA = 42


def imprimir_resultados(indicadores):
    print("\n===================================")
    print("      RESULTADOS DE SIMULACIÓN")
    print("===================================")
    print(f"Período de llegadas:         {DURACION_SIMULACION} min")
    print(f"Tiempo final de simulación:  {indicadores['tiempo_final']:.2f} min")
    print(f"Solicitudes generadas:       {indicadores['solicitudes_generadas']}")
    print(f"Solicitudes atendidas:       {indicadores['solicitudes_atendidas']}")
    print(
        f"Tiempo espera promedio:      {indicadores['tiempo_espera_promedio']:.2f} min"
    )
    print(f"Tiempo espera máximo:        {indicadores['tiempo_espera_maximo']:.2f} min")
    print(
        f"Tiempo sistema promedio:     {indicadores['tiempo_sistema_promedio']:.2f} min"
    )
    print(f"Cola máxima:                 {indicadores['cola_maxima']} solicitudes")
    print(f"Tiempo servidor ocupado:     {indicadores['tiempo_ocupado']:.2f} min")
    print(f"Utilización del servidor:    {indicadores['utilizacion']:.2f}%")


def main():
    random.seed(SEMILLA)

    resultado_simulacion = simular(
        DURACION_SIMULACION,
        TASA_LLEGADAS,
        SERVICIO_MIN,
        SERVICIO_MAX,
    )
    indicadores = calcular_indicadores(resultado_simulacion)

    imprimir_resultados(indicadores)

    archivo_grafica = Path(__file__).with_name("cola_vs_tiempo.png")
    graficar_cola(resultado_simulacion["historial"], archivo_grafica)


if __name__ == "__main__":
    main()
