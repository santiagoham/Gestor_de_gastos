GESTOR DE GASTOS


Descripción

Aplicación de línea de comandos desarrollada en Python para gestionar gastos personales, con almacenamiento persistente y registro de operaciones.
El proyecto está orientado a la organización estructurada de datos y a servir como base para futuros análisis y visualizaciones.


Problema

Gestionar gastos de forma manual o en herramientas simples suele generar datos desordenados y poca visibilidad sobre los hábitos de consumo.


Solución

Esta aplicación centraliza el registro de gastos en un único sistema, permitiendo almacenar, modificar y eliminar registros de forma estructurada, manteniendo además un historial de acciones realizadas.


Funcionalidades principales

Almacenamiento persistente en JSON
Registro de acciones mediante logging (alta, modificación y eliminación)
Interfaz interactiva por consola
Manejo de errores en la entrada de datos


Diseño técnico

Estructura modular para separar lógica, datos e interfaz
Uso de JSON como solución simple y portable de almacenamiento
Implementación de logging para trazabilidad y depuración
Validaciones para mejorar la robustez del sistema


Enfoque en datos

Los datos generados por la aplicación pueden ser utilizados como base para:
Análisis de gastos personales
Clasificación y segmentación por categorías
Integración con herramientas de visualización (Power BI / Looker Studio)


Tecnologías utilizadas

Python
Rich
Tabulate


Ejecución
pip install -r requirements.txt
python main.py
