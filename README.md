# GESTOR DE CANCHAS DE FÚTBOL

## DESCRIPCIÓN

Este programa es un gestor de alquiler de canchas de fútbol por consola, desarrollado en el lenguaje **Python**.

Su función principal es permitir al usuario **crear reservas**, **visualizar un calendario**, **cancelar y eliminar reservas**, teniendo en cuenta **fechas reales**, **horarios en punto**, y la **disponibilidad de canchas según su capacidad**.

El sistema contempla canchas para **10, 12 y 14 personas**, con una cantidad limitada por tipo, y evita superposiciones de horarios o reservas duplicadas.

La información se almacena de manera persistente utilizando un archivo **JSON**, lo que permite conservar los datos entre ejecuciones del programa.

Cuenta con manejo de errores, validaciones de fechas y horarios, registro de eventos mediante logs y el uso de la librería externa **Rich**, que permite mostrar tablas y mensajes con una presentación más clara y visual en la consola.

### El código está dividido en tres módulos principales

- `main.py` (interfaz de usuario y menú interactivo)
- `reservas.py` (lógica de negocio y gestión de reservas)
- `utils.py` (funciones auxiliares y validaciones)

Para el funcionamiento del sistema se requiere crear un entorno virtual (`virtualenv`) que permita aislar las dependencias del sistema operativo.

> Python utiliza el directorio `site-packages` para guardar las dependencias. Mediante el uso de un entorno virtual se genera un `site-packages` aislado, evitando conflictos con otras instalaciones de Python.

## CONFIGURACIÓN DEL ENTORNO VIRTUAL

1. Instalar virtualenv

```bash
py.exe -m pip install virtualenv
```

2. Crear el entorno virtual

```bash
py.exe -m virtualenv .venv
```

3. Activar el entorno virtual

```bash
.\.venv\Scripts\activate
```

4. nstalar las dependencias del proyecto

```bash
py.exe -m pip install -r requirements.txt
```

## ACCIONES QUE SE PUEDEN REALIZAR

Crear una reserva de cancha

Seleccionar fecha real y horario en punto (turnos de una hora)

Asignar canchas según capacidad (10, 12 o 14 personas)

Visualizar calendario de reservas activas

Ver listado completo de reservas con su estado

Cancelar reservas (sin perder el historial)

Eliminar reservas de forma definitiva

Visualizar la disponibilidad de canchas por fecha y horario

El sistema impide:

Reservar fechas pasadas

Reservar horarios ya transcurridos del día actual

Superposición de reservas

Uso de horarios que no sean en punto

Repetición de nombres en reservas activas

## ESTRUCTURA DEL PROYECTO

```text
Copiar código
/gestor_de_canchas
│── data                    # Directorio para datos persistentes
│   │── reservas.json       # Base de datos de reservas
│   │── reservas.log        # Archivo de logs del sistema
│── main.py                 # Interfaz de usuario (menú)
│── reservas.py             # Lógica del programa
│── utils.py                # Funciones auxiliares y validaciones
│── requirements.txt        # Dependencias del proyecto
│── README.md               # Documentación
```
## GENERACIÓN DEL ARCHIVO DE DEPENDENCIAS
Para generar el archivo con las dependencias del proyecto, ejecutar el siguiente comando dentro del entorno virtual:

```bash
py.exe -m pip freeze > requirements.txt
```

## NOTAS FINALES

Este proyecto fue desarrollado aplicando buenas prácticas de programación en Python, siguiendo los lineamientos de PEP8, utilizando docstrings según PEP257 y tomando como guía principios del Zen de Python, priorizando la claridad, simplicidad y mantenibilidad del código.