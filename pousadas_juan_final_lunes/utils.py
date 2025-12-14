"""
Funciones auxiliares del sistema.
"""

from datetime import datetime, date, time

CANCHAS_DISPONIBLES = {
    "10": 5,
    "12": 2,
    "14": 1
}


def generar_id(reservas: list) -> str:
    if not reservas:
        return "R-001"
    ultimo = reservas[-1]["id"]
    numero = int(ultimo.split("-")[1]) + 1
    return f"R-{numero:03d}"


def obtener_dia(fecha: str) -> str:
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    dias = [
        "LUNES", "MARTES", "MIÉRCOLES",
        "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"
    ]
    return dias[fecha_dt.weekday()]


def validar_hora(hora: str) -> bool:
    try:
        h, m = hora.split(":")
        return m == "00" and 0 <= int(h) <= 23
    except ValueError:
        return False


def validar_fecha_y_hora(fecha: str, hora: str) -> bool:
    """
    No permite fechas pasadas ni horas pasadas del día actual.
    """
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()
    hoy = date.today()

    if fecha_dt < hoy:
        return False

    if fecha_dt == hoy:
        hora_dt = time(int(hora.split(":")[0]))
        ahora = datetime.now().time()
        if hora_dt <= ahora:
            return False

    return True

def validar_fecha_no_pasada(fecha: str) -> bool:
    """
    Valida que la fecha no sea anterior a hoy.
    """
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y").date()
        return fecha_dt >= date.today()
    except ValueError:
        return False
