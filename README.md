GESTOR DE GASTOS

Descripción: Con este programa vas a poder gestionar tus gastos.
Podés realizar las siguientes acciones:
* Agregar gastos nuevos
* Ver todos los gastos que agregaste
* Eliminar gastos
* Modificar gastos existentes

Los gastos se guardan automáticamente en el archivo `gastos.json`.  
Además, cada acción que hagas se registra en el archivo `registro.log` (por ejemplo: agregar, eliminar o modificar).

---

Requisitos

* Tener Python 3.10 o superior instalado.

---

¿Qué es un entorno virtual y para qué sirve?

Un entorno virtual es un espacio aislado dentro de tu computadora donde podés instalar y gestionar las librerías que necesita este proyecto, sin afectar otros proyectos o programas que tengas.  
Esto ayuda a mantener tu proyecto ordenado y que funcione igual en cualquier computadora, evitando conflictos de versiones de librerías.

En Python, se suele crear este entorno virtual usando la herramienta llamada `venv`.

---

¿Cómo instalar y correr el programa?

Paso 1: Crear un entorno virtual.
En la terminal, ejecutar:

python -m venv venv

Paso 2: Activar el entorno virtual.
En Windows / PowerShell:

venv\Scripts\activate

En Linux / macOS:

source venv/bin/activate

Paso 3: Instalar dependencias.
Una vez activado el entorno virtual, instalar las librerías necesarias:

pip install -r requirements.txt

Paso 4: Ejecutar el programa.
Estando dentro del entorno virtual, correr el archivo main.py:

python main.py

---

Ejemplo de uso

Cuando ejecutes el programa, vas a ver algo así:

Menú del Gestor de Gastos Personales
1. Agregar gasto
2. Lista de gastos
3. Eliminar gasto
4. Modificar gasto
5. Salir

Solo elegís una opción y seguís los pasos.

---

Archivos importantes:

gastos.json: Archivo donde se guardan todos tus gastos registrados.

registro.log: Archivo que registra las acciones realizadas, como agregar, modificar, o eliminar gastos.

---

Espero que te sirva!