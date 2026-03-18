# Gestor de Gastos Personales (CLI)

## Descripción
Aplicación de línea de comandos desarrollada en Python para gestionar gastos personales, con almacenamiento persistente y registro de operaciones.

El proyecto está orientado a la organización estructurada de datos, permitiendo registrar información detallada como categorías, montos y fechas.

---

## Problema
Gestionar gastos de forma manual o en herramientas simples suele generar datos desordenados y poca visibilidad sobre los hábitos de consumo.

---

## Solución
Esta aplicación permite centralizar el registro de gastos en un único sistema, almacenando información relevante como descripción, categoría, monto y fechas, y manteniendo un historial de acciones realizadas.

---

## Funcionalidades principales
- Registro de gastos con descripción, categoría, monto y fecha  
- Almacenamiento persistente en formato JSON  
- Visualización de gastos en formato tabular  
- Registro de acciones mediante logging (alta, modificación y eliminación)  
- Validación de fechas y manejo de errores en la entrada de datos  

---

## Diseño técnico
- Estructura modular separando lógica, datos e interfaz  
- Uso de JSON como solución simple y portable de almacenamiento  
- Implementación de logging para trazabilidad y depuración  
- Validación de fechas utilizando `datetime` para garantizar integridad de los datos  
- Manejo de errores para mejorar la robustez del sistema  

---

## Enfoque en datos
La aplicación trabaja con datos estructurados que incluyen categoría, fechas y montos, lo que permite su uso para análisis básicos de gastos personales.

---

## Tecnologías utilizadas
- Python  
- Rich  
- Tabulate  

---

## Ejecución
```bash
pip install -r requirements.txt
python main.py
