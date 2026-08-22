import matplotlib.pyplot as plt


def graficar_cola(historial, archivo_salida=None):
    tiempos = [evento["tiempo"] for evento in historial]
    cantidad_cola = [evento["cola"] for evento in historial]

    plt.figure(figsize=(12, 5))
    plt.step(tiempos, cantidad_cola, where="post")
    plt.xlabel("Tiempo (minutos)")
    plt.ylabel("Solicitudes en cola")
    plt.title("Evolución de la cantidad de solicitudes en cola")
    plt.grid(True)
    plt.tight_layout()

    if archivo_salida is not None:
        plt.savefig(archivo_salida, dpi=150)

    plt.show()
