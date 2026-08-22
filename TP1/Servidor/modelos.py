from dataclasses import dataclass


@dataclass
class Solicitud:
    id: int
    tiempo_llegada: float
    tiempo_inicio: float | None = None
    tiempo_espera: float = 0.0
    tiempo_servicio: float = 0.0
