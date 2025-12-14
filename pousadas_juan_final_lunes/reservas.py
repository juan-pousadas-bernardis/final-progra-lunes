"""
Gestión de reservas de canchas de fútbol.
"""

import json
import logging
from pathlib import Path
from rich.console import Console
from rich.table import Table
from utils import (
    generar_id,
    obtener_dia,
    validar_hora,
    CANCHAS_DISPONIBLES
)
from utils import validar_fecha_no_pasada

console = Console()

_root = Path(__file__).parent
data_path = _root / "data"
data_path.mkdir(exist_ok=True)

data_json = data_path / "reservas.json"
data_log = data_path / "reservas.log"

logging.basicConfig(
    filename=data_log,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def cargar_reservas() -> list:
    if not data_json.exists():
        return []
    with open(data_json, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_reservas(reservas: list) -> None:
    with open(data_json, "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=4, ensure_ascii=False)


def calcular_disponibilidad(reservas: list, fecha: str, hora: str) -> dict:
    """
    Calcula cuántas canchas quedan disponibles por tipo
    para una fecha y hora determinadas.
    """
    disponibles = {}

    for tipo, total in CANCHAS_DISPONIBLES.items():
        usadas = sum(
            1
            for r in reservas
            if (
                r["activa"]
                and r["fecha"] == fecha
                and r["hora"] == hora
                and r["cancha"] == tipo
            )
        )
        disponibles[tipo] = total - usadas

    return disponibles



def crear_reserva() -> None:
    reservas = cargar_reservas()

    # NOMBRE
    while True:
        nombre = input("Nombre del cliente: ").strip()
        if any(
            r["nombre"].lower() == nombre.lower()
            and r["activa"]
            for r in reservas
        ):
            console.print("[red]Nombre ya utilizado[/red]")
        else:
            break

    # FECHA
    while True:
        fecha = input("Fecha (DD/MM/YYYY): ")

        if not validar_fecha_no_pasada(fecha):
         console.print(
              "[red]No se puede reservar una fecha anterior a hoy[/red]"
          )
         continue

        try:
            dia = obtener_dia(fecha)
            break
        except ValueError:
          console.print("[red]Formato de fecha inválido[/red]")

    # HORA
    while True:
        hora = input("Hora de inicio (XX:00): ")
        if not validar_hora(hora):
            console.print("[red]Horario inválido[/red]")
            continue

        from utils import validar_fecha_y_hora
        if not validar_fecha_y_hora(fecha, hora):
            console.print("[red]No se puede reservar en el pasado[/red]")
            continue

        break

    # DISPONIBILIDAD (DEPENDIENTE DEL DÍA)
    while True:
        disponibles = calcular_disponibilidad(reservas, fecha, hora)

        console.print(
            f"\nCanchas disponibles para {dia} {fecha} a las {hora}:"
        )
        for tipo, cantidad in disponibles.items():
            console.print(f"{tipo} personas: {cantidad}")

        if all(c == 0 for c in disponibles.values()):
            console.print(
                "[red]No hay canchas disponibles para ese día y horario[/red]"
            )
            return

        cancha = input("Elegir cancha (10 / 12 / 14): ")

        if cancha not in disponibles:
            console.print("[red]Tipo inválido[/red]")
        elif disponibles[cancha] <= 0:
            console.print("[red]No quedan canchas de ese tipo[/red]")
        else:
            break

    reserva = {
        "id": generar_id(reservas),
        "nombre": nombre,
        "fecha": fecha,
        "dia": dia,
        "hora": hora,
        "cancha": cancha,
        "activa": True
    }

    reservas.append(reserva)
    guardar_reservas(reservas)

    logging.info("Reserva creada %s", reserva["id"])
    console.print(
        f"[green]Reserva {reserva['id']} creada "
        f"{dia} {fecha} {hora}[/green]"
    )



def listar_calendario() -> None:
    reservas = cargar_reservas()

    table = Table(title="Calendario (Reservas Activas)")
    table.add_column("Fecha")
    table.add_column("Día")
    table.add_column("Hora")
    table.add_column("Cancha")

    for r in reservas:
        if r["activa"]:
            table.add_row(
                r["fecha"],
                r["dia"],
                r["hora"],
                f"{r['cancha']} personas"
            )

    console.print(table)


def listar_reservas_completas() -> None:
    reservas = cargar_reservas()

    table = Table(title="Listado Completo de Reservas")
    table.add_column("ID")
    table.add_column("Nombre")
    table.add_column("Fecha")
    table.add_column("Día")
    table.add_column("Hora")
    table.add_column("Cancha")
    table.add_column("Estado")

    for r in reservas:
        estado = "Activa" if r["activa"] else "Cancelada"
        table.add_row(
            r["id"],
            r["nombre"],
            r["fecha"],
            r["dia"],
            r["hora"],
            r["cancha"],
            estado
        )

    console.print(table)


def eliminar_reserva() -> None:
    reservas = cargar_reservas()
    reserva_id = input("ID a eliminar: ")

    nuevas = [r for r in reservas if r["id"] != reserva_id]

    if len(nuevas) == len(reservas):
        console.print("[red]Reserva no encontrada[/red]")
        return

    guardar_reservas(nuevas)
    logging.info("Reserva eliminada %s", reserva_id)
    console.print("[green]Reserva eliminada definitivamente[/green]")