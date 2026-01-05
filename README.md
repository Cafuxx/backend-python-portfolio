# Proyecto 01 – API Backend con FastAPI

## 📌 Descripción

Este proyecto es una API backend desarrollada con **Python y FastAPI**, creada como parte de mi proceso de aprendizaje en backend.

La aplicación implementa un **CRUD básico de usuarios**, utilizando validación de datos con Pydantic y almacenamiento en memoria (sin base de datos), con el objetivo de comprender los fundamentos del desarrollo backend y las APIs REST.

---

## 🚀 Tecnologías utilizadas

* Python 3
* FastAPI
* Uvicorn
* Pydantic

---

## ⚙️ Funcionalidades

* Crear usuarios (POST)
* Listar usuarios (GET)
* Obtener un usuario por ID (GET)
* Manejo de errores con códigos HTTP
* Validación automática de datos

---

## 📁 Estructura del proyecto

```
01_hello_api/
│
├── main.py        # Punto de entrada de la aplicación
├── routes.py      # Lógica de las rutas (CRUD)
├── models.py      # Modelos y validación de datos
└── database.py    # Almacenamiento en memoria
```

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Crear y activar un entorno virtual (opcional)
3. Instalar dependencias:

```bash
pip install fastapi uvicorn
```

4. Ejecutar el servidor:

```bash
uvicorn main:api --reload
```

5. Acceder a la documentación interactiva:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Qué aprendí con este proyecto

* Comprender la composición básica de un backend y cómo se organizan sus partes
* Manejo de una API REST con FastAPI
* Validación automática de datos utilizando Pydantic
* Uso de status codes HTTP (200, 201, 404, 422) según el contexto
* Manejo de errores con HTTPException, entendiendo cuándo y por qué utilizarlos
* Separación de responsabilidades en la estructura del proyecto backend
* Diferencias entre GET y POST
* Uso de status codes HTTP (200, 201, 404, 422)
* Manejo de errores con HTTPException
* Validación de datos con Pydantic
* Organización básica de un proyecto backend

---

## 📌 Próximos pasos

* Persistencia con base de datos
* CRUD completo (PUT / DELETE)
* Autenticación
* Separación por routers

---

📌 *Proyecto realizado como parte de mi portafolio de backend en Python.*
