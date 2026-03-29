# Monografico Tarea 2

**Participantes:**

| Nombre                         | Matrícula |
| ------------------------------ | --------- |
| Henry Edilio Ramirez Chevalier | 100498807 |
| Miguel Angel Mendez            | 100281535 |
| Roslyn Cruz                    | AA-7473   |

## Requerimientos de tarea:

Tarea2:

Crear una aplicación web con Django que permita capturar datos de un empleado (id,nombre,salario).

Este aplicativo debe mostrar una página inicial cuando entre, que muestre un listado de empleado almacenados, como se hizo en clases. Pero también debe permitir capturar esos datos.

Por ahora, no tienes guadar nada en la base datos o en memoria. Solo capturar los datos y mostrar un mensaje "Registro almacenado" al usuario.

Para esa captura debes investigar como se usa la etiqueta formulario en html y la acción de aceptar datos en Django. Tambien lo puedes revisar en el pdf llamado "jdjango3 - forms.pdf".

Fecha de entrega: **2026/03/29**

## deployment

Para probar la aplicacion Funcionando en linea [aga click aqui](https://monograficodemo.avantkeel.com) o de forma local una vez configurado postgresql, las dependencias de python de el projecto y el archivo .env ir a http://localhost:8000/app/ 


## Repositorio

(monografico-tareas)[https://github.com/avantkeel/monograficodemo]

## Instrucciones para ejecutar projecto

### 1. clonar el projecto

```bash
git clone git@github.com:avantkeel/monograficodemo.git
cd tarea2
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

- **Windows (Git Bash / CMD / PowerShell):**

```bash
.venv\Scripts\activate
```

- **macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Verificar instalación

```bash
pip freeze
```

Deberías ver algo como:

```text
asgiref==3.11.1
Django==6.0.3
sqlparse==0.5.5
tzdata==2025.3
```

## 5. Configurar postgres

Configurar postgress y poner la configuracion de postgress en archivo env como el que esta como ejemplo en `source/django/core/.env.example`

## Ejecutar el servidor de desarrollo

Ejecutar:

```bash
python manage.py runserver
```

Abrir el navegador en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver la página de Inicio

## Deployment

Para hacer deployment de este projecto le presentamos las siguientes guias para varias plataformas:

- [Vercel](https://github.com/avantkeel/monograficodemo/blob/main/documentation/deployment/vercel.md)

---

## Notas

- Todas las dependencias se manejan dentro del **entorno virtual** (`.venv`).
- Para instalar dependencias en otra máquina:
- para colaborar crear un fork de el projecto, hacer commit de los cambios y crear una pull request o hablar con uno de los colaboradores de este projecto.

- no se ve el css en local: poner el archivo .env en entorno de desarrollo para probar en local.
