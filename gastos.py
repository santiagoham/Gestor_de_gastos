from datetime import datetime
import json
import os
from rich import print

# Importo "rich" con la finalidad de que el programa sea más estético

ARCHIVO_GASTOS = "gastos.json"  # Acá vamos a guardar los gastos
ARCHIVO_LOG = "registro.log"  # Acá vamos a guardar los registros


def registrar_log(mensaje):
    """
    Función para escribir los logs con fecha y hora
    para registrar las acciones que se realizan.
    """
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
            f.write(f"{ahora} - {mensaje}\n")
    except Exception as e:
        print(f"[red1]Error al registrar log: {e}[/red1]")


def cargar_gastos():
    """
    Función que carga la lista de gastos guardados en el archivo .json.
    En caso de que no exista el archivo, retorna una lista vacía.
    Notifica si ocurre algún problema.
    """
    if not os.path.exists(ARCHIVO_GASTOS):
        return []
    try:
        with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[red1]Error al cargar gastos: {e}[/red1]")
        return []


def guardar_gastos(gastos):
    """
    Función para sobreescribir la lista de gastos en el archivo .json.
    Notifica si ocurre algún problema.
    """
    try:
        with open(ARCHIVO_GASTOS, "w", encoding="utf-8") as f:
            json.dump(gastos, f, indent=4, ensure_ascii=False)
            # De esta manera es mejor visualmente
    except Exception as e:
        print(f"[red1]Error al guardar gastos: {e}[/red1]")


def generar_id(gastos):
    """
    Función para generar un ID único para un gasto nuevo.
    En caso de no haber gastos, empieza por el 1.
    En caso de que ya haya gastos, agarra el ID más alto y
    le suma 1 para que no se repitan.
    """
    if not gastos:
        return 1
    return max(g["id"] for g in gastos) + 1


def agregar_gasto(descripcion, categoria, monto, fecha_gasto):
    """
    Función para agregar un gasto nuevo a la lista y guardarlo.
    Registra la acción en el log.
    Notifica al usuario cuando se agrega.
    """
    gastos = cargar_gastos()
    nuevo_gasto = {
        "id": generar_id(gastos),
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto,
        "fecha_gasto": fecha_gasto,
        "fecha_registro": datetime.now().strftime("%Y-%m-%d"),
    }
    gastos.append(nuevo_gasto)
    guardar_gastos(gastos)
    registrar_log(f"Gasto agregado: {nuevo_gasto}")
    print("[green3]Gasto agregado con éxito.[/green3]")


def listar_gastos():
    """
    Función para mostrar en pantalla todos los gastos cargados.
    En caso de no haber gastos, avisa que la lista está vacía.
    """
    gastos = cargar_gastos()
    if not gastos:
        print("[gold1]No hay gastos registrados.[/gold1]")
    else:
        print("\nLista de gastos registrados:")
        for g in gastos:
            print(
                f'ID: {g["id"]} | {g["descripcion"]} | '
                f'{g["categoria"]} | $ {g["monto"]} | '
                f'Gasto: {g["fecha_gasto"]} | Registro: {g["fecha_registro"]}'
            )


def eliminar_gasto(id_gasto):
    """
    Función para eliminar el gasto que coincide con el ID proporcionado.
    Si el ID no existe, se lo informa al usuario.
    Guarda los cambios y registra la acción en el log.
    """
    gastos = cargar_gastos()
    gastos_nuevos = [g for g in gastos if g["id"] != id_gasto]
    if len(gastos_nuevos) == len(gastos):
        print("[red1]ID de gasto no encontrado.[/red1]")
    else:
        guardar_gastos(gastos_nuevos)
        registrar_log(f"Gasto eliminado: ID {id_gasto}")
        print("[green3]Gasto eliminado con éxito.[/green3]")


def modificar_gasto(
    id_gasto, descripcion=None, categoria=None, monto=None, fecha_gasto=None
):
    """
    Función para modificar los datos de un gasto dado su ID.
    Si el ID no existe, se lo informa al usuario.
    Guarda los cambios y registra la acción en el log.
    """
    gastos = cargar_gastos()
    for gasto in gastos:
        if gasto["id"] == id_gasto:
            if descripcion is not None:
                gasto["descripcion"] = descripcion
            if categoria is not None:
                gasto["categoria"] = categoria
            if monto is not None:
                gasto["monto"] = monto
            if fecha_gasto is not None:
                gasto["fecha_gasto"] = fecha_gasto
            guardar_gastos(gastos)
            registrar_log(f"Gasto modificado: ID {id_gasto}")
            print("[green3]Gasto modificado con éxito.[/green3]")
            return
    print("[red1]ID de gasto no encontrado.[/red1]")
