# **API de Gestión de Reservas Hoteleras**

## **Descripción**

Este proyecto implementa una API RESTful para la gestión de reservas hoteleras, desarrollada con FastAPI. Forma parte de un sistema completo que incluye un frontend independiente.
La API permite registrar y administrar usuarios, clientes, habitaciones y reservas, ofreciendo operaciones CRUD para cada entidad.
Además, incluye un sistema de autenticación JWT y soporte CORS para permitir la comunicación segura con la interfaz web.

## **Tecnologías Usadas**

### Backend
- **FastAPI** – Framework para construir la API RESTful.
- **SQLAlchemy** – ORM para interactuar con la base de datos.
- **Pydantic** – Validación de datos.
- **Uvicorn** – Servidor ASGI para ejecutar la aplicación.
- **JWT** – tokens de autenticación.
- **CORS Middleware** – Para permitir la comunicación con el frontend.

### Frontend
- **HTML, CSS y JavaScript**
- **Axios** – Para consumir la API.

### Autenticación con JWT

Se ha implementado un sistema seguro de autenticación basado en **tokens JWT** . Los endpoints protegidos requieren un token válido en el encabezado Authorization con el siguiente formato:

1. :
   ```bash
   Authorization: Bearer <token>
   
### Autenticación con JWT

- **POST /login :** – Autenticar usuario y obtener un token JWT.

#### Ejemplo de Solicitud:
  ```json
  {
    "username": "juan",
    "password": "mi_contraseña_segura",
  }
  ```
  #### Respuesta Exitosa:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx",
    "token_type": "bearer"
  }
  ```

## **Endpoints Protegidos**

Todos los siguientes endpoints requieren autenticación JWT:

### **Usuarios**
- **GET** `/list`: Lista todos los usuarios.
- **GET** `/userId/{user_id}`: Detalles de un usuario por ID.
- **POST** `/create`: Crear un nuevo usuario.
- **PUT** `/update/{user_id}`: Actualizar usuario por ID.

### **Clientes**
- **GET** `/list`: Lista todos los clientes.
- **GET** `/clienId/{client_id}`: Detalles de un cliente por ID.
- **POST** `/create`: Crear un nuevo client.
- **PUT** `/update/{client_id}`: Actualizar cliente por ID.


### **Habitaciones**
- **GET** `/list`: Lista todos las habitaciones.
- **GET** `/room/{room_id}`: Detalles de un habitacion por ID.
- **POST** `/create`: Crear un nuevo habitacion.
- **PUT** `/room/{room_id}`: Actualizar habitacion por ID.


### **Reservas**
- **GET** `/list`: Lista todas las reservas.
- **GET** `/reservaId/{reserva_id}`: Detalles de una reserva por ID.
- **POST** `/create`: Crear una nueva reserva.
- **PUT** `/update/{cita_id}`: Actualizar una reserva.


### **Login**
- **POST** `/login`: Autenticar usuario.

## **Instrucciones de Instalación**

### **Requisitos**
- Python 3.7+
- Dependencias: FastAPI, SQLAlchemy, Pydantic, Uvicorn, python-jose (para JWT)

### **Pasos para Ejecutar**

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/ThairConstante/API-Reservas-Hotel.git
  cd API-Reservas-Hotel

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

3. Ejecutar el servidor:
   ```bash
   uvicorn main:app --reload

4. Acceder a la documentación interactiva:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

   
### **Ejemplo de Uso**

#### Crear un Usuario
#### **Petición**
- **Método**: POST
- **Endpoint**: `/usuarios`
- **Cuerpo**:
  ```json
  {
    "username": "juan",
    "password": "mi_contraseña_segura",
    "email": "juan@ejemplo.com"
  }
  ```

#### **Respuesta Exitosa**
```json
{
  "username": "juan",
  "email": "juan@ejemplo.com"
}
```
