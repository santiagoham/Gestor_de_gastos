from gastos import (
    agregar_gasto,
    eliminar_gasto,
    modificar_gasto,
    cargar_gastos
)

# Importo las funciones desde gastos.py

from datetime import datetime

from rich import print
from tabulate import tabulate

# Importo "rich" y "tabulate" con la finalidad
# de que el programa sea más estético.


def mostrar_menu():
    # Función para que aparezca el menú, donde se le pide
    # al usuario que elija una opción.
    print("\n[deep_sky_blue2]Menú del Gestor de "
          "Gastos Personales[/deep_sky_blue2]")
    print("1. Agregar gasto")
    print("2. Lista de gastos")
    print("3. Eliminar gasto")
    print("4. Modificar gasto")
    print("5. Salir")


def listar_gastos_tabla():
    gastos = cargar_gastos()
    if not gastos:
        print("[gold1]No hay gastos registrados.[/gold1]")
    else:
        # Función para poner los encabezados de la tabla de tabulate.
        tabla = []
        for g in gastos:
            tabla.append(
                [
                    g["id"],
                    g["descripcion"],
                    g["categoria"],
                    f'$ {g["monto"]}',
                    g["fecha_gasto"],
                    g["fecha_registro"],
                ]
            )
        headers = [
            "ID",
            "Descripción",
            "Categoría",
            "Monto",
            "Fecha del gasto",
            "Fecha de registro",
        ]
        print(tabulate(tabla, headers, tablefmt="fancy_grid"))


def pedir_fecha(prompt):
    while True:
        fecha_str = input(prompt + " (formato YYYY-MM-DD): ")
        try:
            # Función para validar el formato y que sea una fecha real
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha_str
        except ValueError:
            print(
                "[red1]Error: La fecha debe tener el"
                "formato YYYY-MM-DD y ser válida.[/red1]"
            )


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        descripcion = input("Descripción del gasto: ")
        categoria = input("Categoría del gasto: ")
        fecha_gasto = pedir_fecha("Fecha del gasto")
        try:
            monto = float(
                input(
                    "Monto del gasto (solo números, "
                    "en caso de decimales usar '.' como separador): "
                )
            )
            agregar_gasto(descripcion, categoria, monto, fecha_gasto)
        except ValueError:
            print("[red1]Error: Debe ingresar un monto válido.[/red1]")

    elif opcion == "2":
        listar_gastos_tabla()

    elif opcion == "3":
        try:
            id_gasto = int(input("Ingrese el ID del "
                                 "gasto que desea eliminar: "))
            eliminar_gasto(id_gasto)
        except ValueError:
            print("[red1]Error: Debe ingresar un ID válido.[/red1]")

    elif opcion == "4":
        try:
            id_gasto = int(input("Ingrese el ID del "
                                 "gasto que desea modificar: "))

            gastos = cargar_gastos()
            gasto_encontrado = None
            for gasto in gastos:
                if gasto["id"] == id_gasto:
                    gasto_encontrado = gasto
                    break

            if not gasto_encontrado:
                print("[red1]ID de gasto no encontrado.[/red1]")
                continue

            nueva_descripcion = input(
                "Nueva descripción (Presione Enter para no cambiarla): "
            )
            nueva_categoria = input(
                "Nueva categoría (Presione Enter para no cambiarla): "
            )
            nuevo_monto = input("Nuevo monto "
                                "(Presione Enter para no cambiarlo): ")
            nueva_fecha = input(
                "Nueva fecha del gasto (YYYY-MM-DD) (Presione "
                "Enter para no cambiarla): "
            )

            descripcion = nueva_descripcion if nueva_descripcion else None
            categoria = nueva_categoria if nueva_categoria else None

            if nuevo_monto:
                try:
                    monto = float(nuevo_monto)
                except ValueError:
                    print("[red1]Error: Número de monto inválido.[/red1]")
                    continue
            else:
                monto = None

            if nueva_fecha:
                try:
                    datetime.strptime(nueva_fecha, "%Y-%m-%d")
                    fecha_gasto = nueva_fecha
                except ValueError:
                    print(
                        "[red1]Error: La fecha debe tener "
                        "el formato YYYY-MM-DD y ser válida.[/red1]"
                    )
                    continue
            else:
                fecha_gasto = None

            confirmacion = input(
                "¿Está seguro de que desea modificar el "
                "gasto anterior por el nuevo? "
                "Esta acción es irreversible (s/n): "
            ).lower()
            if confirmacion == "s":
                modificar_gasto(
                    id_gasto,
                    descripcion,
                    categoria,
                    monto,
                    fecha_gasto
                    )
            else:
                print("[gold1]Modificación cancelada.[/gold1]")
        except ValueError:
            print("[red1]Error: Ingrese un ID válido.[/red1]")

    elif opcion == "5":
        print("[dark_cyan]Programa finalizado. ¡Hasta luego![/dark_cyan]")
        break

    else:
        print("[red1]Opción inválida. Por favor, "
              "elija una opción del 1 al 5.[/red1]")
