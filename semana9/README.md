🩺 Aplicación de Escritorio: Registro de Pacientes – SaludTotal
📌 Descripción General
SaludTotal es una aplicación de escritorio desarrollada en Python con Tkinter, diseñada para gestionar el registro clínico de pacientes. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar), generar informes en PDF, y mantener una base de datos estructurada mediante MySQL.

🧰 Tecnologías Utilizadas
Python 3.13+

Tkinter – Interfaz gráfica

MySQL – Base de datos relacional

ReportLab – Generación de informes PDF

ttk.Treeview – Visualización tabular de pacientes

OS / Platform – Apertura automática de archivos según sistema operativo

🧩 Estructura del Proyecto
EJERCICIOS_P.AVANZADA/
│
├── semana9/
│   ├── gui/
│   │   └── interfaz.py
│   ├── controllers/
│   │   └── pacientes_controller.py
│   ├── models/
│   │   └── paciente_model.py
│   ├── services/
│   │   └── informes.py
│   └── database/
│       └── conexion.py


🚀 Funcionalidades
📝 Registro de Pacientes
Campos: Nombre, Edad, Género, Historial Médico, Contacto

Validación de datos antes de guardar

🔄 Actualización y Eliminación
Selección desde tabla

Modificación directa desde el formulario

📊 Visualización
Tabla con todos los pacientes registrados

Ordenado por columnas

📄 Generación de Informes
Exportación a PDF con cabeceras y datos

Apertura automática del archivo generado

Nombre del archivo incluye fecha y hora

📂 Base de Datos
Tabla: pacientes

Campo	Tipo
id	INT (PK)
nombre	VARCHAR(100)
edad	INT
genero	VARCHAR(20)
historial	TEXT
contacto	VARCHAR(50)
📦 Instalación y Ejecución
Clonar el repositorio

Instalar dependencias:

bash
pip install mysql-connector-python reportlab
Configurar conexión en database/conexion.py

Ejecutar la interfaz:
bash
python semana9/gui/interfaz.py

🛡️ Derechos de Autor
© 2025 Franco Sigm – Todos los derechos reservados. Esta aplicación fue desarrollada como parte del curso Programación Avanzada en IACC. Su uso está destinado a fines educativos y profesionales.