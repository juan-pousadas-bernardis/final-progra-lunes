"""
Gestor de alquiler de canchas de fútbol.
"""

from rich.console import Console
from rich.prompt import Prompt
from reservas import (
    crear_reserva,
    listar_calendario,
    listar_reservas_completas,
    eliminar_reserva
)

console = Console()


def mostrar_menu() -> None:
    console.print("\n[bold cyan]GESTOR DE CANCHAS[/bold cyan]")
    console.print("1 - Crear reserva")
    console.print("2 - Ver calendario")
    console.print("3 - Ver todas las reservas")
    console.print("4 - Eliminar reserva")
    console.print("5 - Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = Prompt.ask("Seleccione una opción")

        if opcion == "1":
            crear_reserva()
        elif opcion == "2":
            listar_calendario()
        elif opcion == "3":
            listar_reservas_completas()
        elif opcion == "4":
            eliminar_reserva()
        elif opcion == "5":
            console.print("[green]Hasta luego[/green]")
            break
        else:
            console.print("[red]Opción inválida[/red]")


if __name__ == "__main__":
    main()