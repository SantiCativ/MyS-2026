# Simulación de un servidor

## Objetivo

Simular un sistema de atención con un único servidor para analizar la evolución de la cola y obtener indicadores de desempeño.

## Descripción del sistema

Las solicitudes llegan al sistema, son atendidas por un único servidor y, si el servidor está ocupado, esperan en una cola. Cuando termina una atención, el servidor toma la primera solicitud de la cola.

## Parámetros

- Duración del período de generación de llegadas: 480 minutos.
- Tasa de llegadas: 10 solicitudes por hora, expresada como `10 / 60` solicitudes por minuto.
- Tiempo mínimo de servicio: 2 minutos.
- Tiempo máximo de servicio: 6 minutos.
- Semilla aleatoria: 42.

## Distribuciones utilizadas

- Tiempo entre llegadas: distribución exponencial.
- Tiempo de servicio: distribución uniforme entre 2 y 6 minutos.

## Regla de atención

La cola usa la regla FIFO: la primera solicitud que entra a la cola es la primera en ser atendida.

## Criterio de finalización

Las nuevas llegadas se generan solamente hasta el minuto 480. Después de ese momento no se generan nuevas solicitudes, pero la simulación continúa hasta que el servidor termina de atender todas las solicitudes pendientes y la cola queda vacía.

## Indicadores obtenidos

- Solicitudes generadas.
- Solicitudes atendidas.
- Tiempo de espera promedio.
- Tiempo de espera máximo.
- Tiempo promedio en sistema.
- Cola máxima.
- Tiempo total de servidor ocupado.
- Utilización del servidor.

La utilización se calcula respecto del período de generación de llegadas:

```text
utilización = tiempo_ocupado / 480 * 100
```

## Estructura de archivos

- `main.py`: define parámetros, ejecuta la simulación, imprime resultados y muestra la gráfica.
- `simulacion.py`: contiene la lógica de eventos discretos, llegadas, servicios, cola FIFO y reloj de simulación.
- `modelos.py`: define la estructura de una solicitud.
- `estadisticas.py`: calcula los indicadores a partir del resultado de la simulación.
- `graficos.py`: contiene funciones para graficar el historial de eventos.
- `requirements.txt`: lista las dependencias necesarias para ejecutar el proyecto.
- `README.md`: documenta el modelo y la organización del proyecto.

## Puesta en marcha

### Requisitos

- Python 3.10 o superior.
- `pip`, el gestor de paquetes de Python.
- Las dependencias listadas en `requirements.txt`.

### 1. Ubicarse en la carpeta del proyecto

Desde la raíz del repositorio, ingresar a la carpeta donde se encuentra la simulación:

```bash
cd TP1/Servidor
```

### 2. Crear un entorno virtual

Se recomienda crear un entorno virtual para instalar las dependencias del proyecto sin afectar la instalación global de Python:

```bash
python3 -m venv .venv
```

En Linux o macOS, activar el entorno con:

```bash
source .venv/bin/activate
```

En Windows, activar el entorno con:

```bash
.venv\Scripts\activate
```

### 3. Instalar todas las dependencias

Con el entorno virtual activado, instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la simulación

Ejecutar el archivo principal:

```bash
python main.py
```

El programa imprime en consola los indicadores de la simulación y genera el archivo `cola_vs_tiempo.png` en la misma carpeta. Además, intenta abrir una ventana con la gráfica usando Matplotlib.

### 5. Resultado esperado

Con los parámetros definidos en `main.py` y la semilla aleatoria `42`, la ejecución debe mostrar un resumen similar al siguiente:

```text
===================================
      RESULTADOS DE SIMULACIÓN
===================================
Período de llegadas:         480 min
Tiempo final de simulación:  485.24 min
Solicitudes generadas:       86
Solicitudes atendidas:       86
Tiempo espera promedio:      7.54 min
Tiempo espera máximo:        25.72 min
Tiempo sistema promedio:     11.60 min
Cola máxima:                 7 solicitudes
Tiempo servidor ocupado:     348.93 min
Utilización del servidor:    72.69%
```

Los valores numéricos se mantienen reproducibles mientras no se modifiquen los parámetros ni la semilla.

### 6. Problemas frecuentes

Si aparece el error `ModuleNotFoundError: No module named 'matplotlib'`, significa que falta instalar las dependencias. Se soluciona ejecutando:

```bash
pip install -r requirements.txt
```

Si se ejecuta el programa en un entorno sin interfaz gráfica, puede generarse correctamente el archivo `cola_vs_tiempo.png`, aunque la ventana de Matplotlib no llegue a mostrarse.
