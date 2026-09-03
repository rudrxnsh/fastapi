# 🚀 FastAPI Learning Hub

> A hands-on FastAPI learning repository covering REST APIs, Pydantic,
> CRUD operations, validation, dependency injection, databases,
> authentication, async programming, testing, and production-ready
> backend architecture.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern%20Python%20API-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Data%20Validation-E92063)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-222222)
![Status](https://img.shields.io/badge/Status-Learning%20%26%20Building-orange)

------------------------------------------------------------------------

## 📌 About This Repository

This repository documents my journey of learning **FastAPI from
fundamentals to production-level backend development**.

The goal is not just to learn how to write endpoints, but to understand
the complete backend stack:

``` text
HTTP
  ↓
ASGI
  ↓
Uvicorn
  ↓
FastAPI
  ↓
Pydantic
  ↓
Business Logic
  ↓
SQLAlchemy
  ↓
PostgreSQL
  ↓
Authentication / Authorization
  ↓
Testing / Docker / Deployment
```

The repository will evolve as I build increasingly complex APIs and
backend systems.

------------------------------------------------------------------------

# 🧠 What is FastAPI?

**FastAPI** is a modern Python web framework for building APIs and
backend services.

It is built around:

-   Python type hints
-   Starlette for web/ASGI functionality
-   Pydantic for validation and serialization
-   OpenAPI for API schemas and documentation
-   Uvicorn or another ASGI server for serving the application

A minimal FastAPI application looks like this:

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

Run it with:

``` bash
fastapi dev main.py
```

The development server is then available at:

``` text
http://127.0.0.1:8000
```

Interactive API documentation:

``` text
http://127.0.0.1:8000/docs
```

Alternative documentation:

``` text
http://127.0.0.1:8000/redoc
```

------------------------------------------------------------------------

# ⚡ Why FastAPI?

FastAPI is designed around a very productive combination:

``` text
Python Type Hints
       +
Pydantic Validation
       +
ASGI / Async Support
       +
OpenAPI
       +
Automatic Documentation
```

This allows a relatively small amount of Python code to provide:

-   routing
-   request parsing
-   validation
-   serialization
-   API documentation
-   dependency injection
-   automatic OpenAPI schemas

------------------------------------------------------------------------

# 🏗️ FastAPI Architecture

``` mermaid
flowchart TD
    A[Client / Browser / Mobile App] -->|HTTP Request| B[Uvicorn]
    B -->|ASGI| C[FastAPI]
    C --> D[Routing]
    D --> E[Dependency Injection]
    E --> F[Pydantic Validation]
    F --> G[Business Logic]
    G --> H[Service Layer]
    H --> I[SQLAlchemy / Database Layer]
    I --> J[(PostgreSQL)]
    G --> K[External APIs / Services]
    G --> L[Pydantic Response Model]
    L --> B
    B -->|HTTP Response| A
```

### The request lifecycle

``` text
Client
  │
  │ HTTP Request
  ▼
Uvicorn
  │
  │ ASGI
  ▼
FastAPI
  │
  ├── Routing
  ├── Middleware
  ├── Dependencies
  ├── Validation
  │
  ▼
Endpoint
  │
  ▼
Business Logic
  │
  ▼
Database / External Service
  │
  ▼
Response Model
  │
  ▼
HTTP Response
  │
  ▼
Client
```

------------------------------------------------------------------------

# 🌐 FastAPI and ASGI

FastAPI itself is **not the server**.

The relationship is:

``` text
                ┌──────────────────┐
                │      Client      │
                └────────┬─────────┘
                         │ HTTP
                         ▼
                ┌──────────────────┐
                │     Uvicorn      │
                │    ASGI Server   │
                └────────┬─────────┘
                         │ ASGI
                         ▼
                ┌──────────────────┐
                │     FastAPI      │
                │   Web Framework  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Application Code │
                └──────────────────┘
```

### What is ASGI?

**ASGI --- Asynchronous Server Gateway Interface** --- defines how an
asynchronous Python web server communicates with a Python web
application.

FastAPI is an **ASGI framework**.

Uvicorn is an **ASGI server**.

This is one of the fundamental concepts behind FastAPI.

------------------------------------------------------------------------

# 🆚 FastAPI vs Other Python Web Frameworks

> **Important:** FastAPI is not universally "better" than every other
> framework. Different frameworks optimize for different use cases. The
> comparison below focuses mainly on API/backend development.

  ------------------------------------------------------------------------------------
  Feature             FastAPI        Flask          Django              Django Ninja
  ------------------- -------------- -------------- ------------------- --------------
  Primary focus       APIs / modern  Minimal web    Full-stack web      APIs inside
                      web backends   framework      framework           Django

  Architecture        ASGI           WSGI + ASGI    Full framework      Django + API
                                     support                            layer

  Async support       ⭐ Excellent   Improving      Good                Good

  Type hints          ⭐ Core        Optional       Optional            ⭐ Strong
                      feature                                           

  Automatic           ⭐ Pydantic    Usually        Forms/serializers   Pydantic
  validation                         extensions     depending on stack  

  OpenAPI docs        ⭐ Automatic   Usually        Usually extensions  ⭐ Automatic
                                     extensions                         

  Dependency          ⭐ Built-in    Not core       Not core            Available
  Injection                                                             

  ORM included        No             No             ⭐ Django ORM       ⭐ Django ORM

  Admin panel         No             No             ⭐ Excellent        Uses Django
                                                                        admin

  Microservices/API   ⭐ Excellent   Excellent      Can be heavy        Good
  services                                                              

  Large monolithic    Good           Good           ⭐ Excellent        Excellent
  web apps                                                              

  Learning curve      Moderate       ⭐ Easy        Higher              Moderate

  Performance         ⭐ High        Good           Good                High
  potential                                                             

  Best for            APIs, ML       Small/simple   Full web platforms  Django-based
                      backends,      web apps                           APIs
                      services                                          
  ------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 🥊 FastAPI vs Flask

### Flask

Flask follows a **minimal and flexible** philosophy.

``` python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello"}
```

Flask gives you a small core and lets you choose additional libraries.

### FastAPI

``` python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}
```

FastAPI goes further by integrating:

``` text
Type Hints
   ↓
Validation
   ↓
Serialization
   ↓
OpenAPI
   ↓
Interactive Docs
```

### FastAPI's advantage

For API-heavy applications, FastAPI provides many features out of the
box that Flask commonly handles through additional extensions or manual
patterns.

### Flask's advantage

Flask's minimalism can be an advantage when:

-   the application is small
-   you want maximum architectural freedom
-   you already have a Flask ecosystem
-   you don't need FastAPI's automatic validation/documentation features

**Verdict:** FastAPI is often more productive for modern API-first
services, while Flask remains excellent for small and highly
customizable applications.

------------------------------------------------------------------------

# 🏢 FastAPI vs Django

Django is much more than an API framework.

It is a **full-stack web framework** containing major components such
as:

``` text
Django
 ├── ORM
 ├── Admin
 ├── Authentication
 ├── Templates
 ├── Forms
 ├── Middleware
 ├── Routing
 └── Security utilities
```

FastAPI is intentionally more focused:

``` text
FastAPI
 ├── Routing
 ├── Validation
 ├── Serialization
 ├── Dependency Injection
 ├── OpenAPI
 └── ASGI ecosystem
```

### Django wins when:

-   you need a large server-rendered web application
-   Django ORM is central to your architecture
-   you need the built-in admin
-   you want a batteries-included framework

### FastAPI wins when:

-   the backend is primarily an API
-   you are building microservices
-   you need an API for an ML/AI system
-   async I/O is important
-   automatic OpenAPI documentation is valuable
-   you want a lightweight framework with composable components

**Verdict:** Django is broader; FastAPI is more focused on API/backend
services.

------------------------------------------------------------------------

# 🥋 FastAPI vs Django Ninja

Django Ninja is specifically designed for building APIs on top of
Django.

It combines:

``` text
Django
  +
Pydantic
  +
Type Hints
  +
OpenAPI
```

This makes Django Ninja a very strong choice when you already want the
Django ecosystem.

### Choose Django Ninja when:

``` text
You need Django ORM
        +
Django Admin
        +
Django authentication
        +
Django ecosystem
```

### Choose FastAPI when:

``` text
You primarily need an API/backend service
        +
ASGI-first architecture
        +
Pydantic
        +
Dependency Injection
        +
Automatic OpenAPI
```

**The key difference:** Django Ninja is an API layer for the Django
ecosystem, while FastAPI is an independent API-focused framework.

------------------------------------------------------------------------

# 🧩 Core FastAPI Concepts

## 1. Routes

Routes connect HTTP requests to Python functions.

``` python
@app.get("/products")
def get_products():
    return {"products": []}
```

The route consists of:

``` text
GET
 ↓
/products
 ↓
Python function
```

------------------------------------------------------------------------

## 2. HTTP Methods

FastAPI supports the standard HTTP methods:

``` text
GET       → Retrieve data
POST      → Create data
PUT       → Replace/update data
PATCH     → Partially update data
DELETE    → Delete data
```

------------------------------------------------------------------------

# 🛠️ CRUD Operations

CRUD means:

``` text
C → Create
R → Read
U → Update
D → Delete
```

A typical REST API can look like:

``` text
                Products API
                     │
       ┌─────────────┼─────────────┐
       │             │             │
      POST          GET           DELETE
       │             │             │
       ▼             ▼             ▼
    Create         Read          Delete
       │             │             │
       └─────────────┼─────────────┘
                     │
                    PUT
                     │
                     ▼
                   Update
```

------------------------------------------------------------------------

# 📦 CRUD Example

## Data model

``` python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    product_name: str
    price: float
    description: str
```

------------------------------------------------------------------------

## CREATE --- POST

``` python
@app.post("/products")
def create_product(product: Product):
    return {
        "message": "Product created",
        "product": product
    }
```

Request:

``` http
POST /products
Content-Type: application/json
```

``` json
{
    "id": 1,
    "product_name": "Laptop",
    "price": 75000,
    "description": "Gaming laptop"
}
```

------------------------------------------------------------------------

## READ --- GET

``` python
@app.get("/products")
def get_products():
    return products
```

Get a single product:

``` python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    ...
```

Request:

``` http
GET /products/1
```

The `product_id: int` is validated automatically.

------------------------------------------------------------------------

## UPDATE --- PUT

``` python
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    ...
```

Request:

``` http
PUT /products/1
```

------------------------------------------------------------------------

## DELETE --- DELETE

``` python
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    ...
```

Request:

``` http
DELETE /products/1
```

------------------------------------------------------------------------

# 🔄 CRUD Request Flow

``` mermaid
flowchart LR
    A[Client] --> B{HTTP Method}

    B -->|POST| C[Create Product]
    B -->|GET| D[Read Product]
    B -->|PUT/PATCH| E[Update Product]
    B -->|DELETE| F[Delete Product]

    C --> G[(Database)]
    D --> G
    E --> G
    F --> G

    G --> H[Pydantic Response Model]
    H --> A
```

------------------------------------------------------------------------

# 🧪 Pydantic and Data Validation

One of FastAPI's most important components is **Pydantic**.

Example:

``` python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
```

FastAPI can use this model to validate incoming JSON.

Valid:

``` json
{
    "name": "Rudransh",
    "age": 22,
    "email": "user@example.com"
}
```

Invalid:

``` json
{
    "name": "Rudransh",
    "age": "hello",
    "email": "user@example.com"
}
```

Instead of manually checking every field, Pydantic performs structured
validation.

------------------------------------------------------------------------

# 🔍 Path Parameters

``` python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}
```

Request:

``` text
/products/10
```

FastAPI extracts:

``` text
product_id = 10
```

and validates it as an integer.

------------------------------------------------------------------------

# 🔎 Query Parameters

``` python
@app.get("/products")
def search_products(
    limit: int = 10,
    category: str | None = None
):
    ...
```

Request:

``` text
/products?limit=20&category=laptops
```

Conceptually:

``` text
Path parameter
/products/{id}

Query parameter
/products?limit=20
```

------------------------------------------------------------------------

# 📥 Request Body

``` python
@app.post("/products")
def create_product(product: Product):
    return product
```

The `Product` Pydantic model describes the expected request body.

------------------------------------------------------------------------

# 📤 Response Models

FastAPI can also validate and serialize outgoing responses.

``` python
@app.get(
    "/products/{product_id}",
    response_model=Product
)
def get_product(product_id: int):
    ...
```

This creates a clear contract:

``` text
Client
  ↓
Request schema
  ↓
Validation
  ↓
Endpoint
  ↓
Response schema
  ↓
Client
```

------------------------------------------------------------------------

# 💉 Dependency Injection

FastAPI provides a powerful dependency injection system.

``` python
from fastapi import Depends

def get_database():
    ...

@app.get("/products")
def get_products(db = Depends(get_database)):
    ...
```

Conceptually:

``` text
Request
  ↓
FastAPI
  ↓
Resolve dependencies
  ↓
get_database()
  ↓
Endpoint
  ↓
Response
```

Dependencies are useful for:

-   database sessions
-   authentication
-   authorization
-   reusable query parameters
-   shared services
-   configuration
-   permission checks

------------------------------------------------------------------------

# 🗂️ APIRouter

As applications grow, putting everything in `main.py` becomes difficult.

A better structure:

``` text
app/
│
├── main.py
│
├── routers/
│   ├── users.py
│   ├── products.py
│   └── auth.py
│
├── schemas/
│   ├── user.py
│   └── product.py
│
├── models/
│   ├── user.py
│   └── product.py
│
├── services/
│   ├── user_service.py
│   └── product_service.py
│
├── database/
│   └── connection.py
│
└── core/
    └── config.py
```

Example:

``` python
from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_products():
    return []
```

Then register it:

``` python
app.include_router(router)
```

------------------------------------------------------------------------

# 🗄️ FastAPI + PostgreSQL

A common production stack:

``` mermaid
flowchart TD
    A[Client] --> B[FastAPI]
    B --> C[Pydantic]
    B --> D[Service Layer]
    D --> E[SQLAlchemy]
    E --> F[(PostgreSQL)]
    F --> E
    E --> D
    D --> B
    B --> A
```

Typical technologies:

``` text
FastAPI
   ↓
Pydantic
   ↓
SQLAlchemy
   ↓
Alembic
   ↓
PostgreSQL
```

------------------------------------------------------------------------

# 🔐 Authentication & Authorization

FastAPI provides security utilities that can be used to build systems
involving:

``` text
Authentication
Authorization
JWT
OAuth2
API Keys
Roles
Permissions
```

Typical flow:

``` mermaid
sequenceDiagram
    participant C as Client
    participant A as FastAPI
    participant DB as Database

    C->>A: Login credentials
    A->>DB: Verify user
    DB-->>A: User found
    A-->>C: Access Token

    C->>A: API request + token
    A->>A: Validate token
    A->>DB: Check permissions
    DB-->>A: Authorized
    A-->>C: Protected resource
```

------------------------------------------------------------------------

# ⚡ Async Programming

FastAPI supports asynchronous endpoints:

``` python
@app.get("/products")
async def get_products():
    ...
```

The important concepts are:

``` text
async
await
coroutines
event loop
concurrency
I/O-bound operations
blocking operations
```

Async programming is especially useful when your application spends
significant time waiting for:

-   databases
-   HTTP APIs
-   files
-   network operations
-   other I/O

> `async` does not automatically make CPU-heavy Python code faster.
> CPU-bound workloads often require different strategies such as
> multiprocessing, task queues, or specialized compute systems.

------------------------------------------------------------------------

# 📚 Automatic API Documentation

FastAPI automatically exposes OpenAPI documentation.

``` text
/docs
   ↓
Swagger UI

/redoc
   ↓
ReDoc

/openapi.json
   ↓
OpenAPI specification
```

``` mermaid
flowchart LR
    A[FastAPI Routes] --> B[Pydantic Models]
    B --> C[OpenAPI Schema]
    C --> D[Swagger UI]
    C --> E[ReDoc]
```

This is particularly useful when frontend and backend teams need a
shared API contract.

------------------------------------------------------------------------

# 🧪 Testing

FastAPI applications can be tested using Python testing tools such as
`pytest` and FastAPI's testing utilities.

Example concept:

``` python
def test_root():
    response = client.get("/")
    assert response.status_code == 200
```

Testing areas I intend to cover:

``` text
Unit Tests
Integration Tests
API Tests
Database Tests
Authentication Tests
Dependency Overrides
Error Cases
```

------------------------------------------------------------------------

# 📈 Production Architecture

A more complete backend can eventually look like:

``` mermaid
flowchart TD
    A[Web / Mobile Client] --> B[Reverse Proxy]
    B --> C[FastAPI Application]
    C --> D[Authentication]
    C --> E[API Routers]
    E --> F[Service Layer]
    F --> G[Repository / Data Layer]
    G --> H[(PostgreSQL)]
    F --> I[(Redis)]
    F --> J[External APIs]
    C --> K[Background Workers]
    K --> L[Message Queue]
```

Possible production components:

``` text
FastAPI
Uvicorn
Nginx / Reverse Proxy
PostgreSQL
Redis
SQLAlchemy
Alembic
Docker
pytest
CI/CD
Logging
Monitoring
```

------------------------------------------------------------------------

# 🧭 Learning Roadmap

My FastAPI learning roadmap:

``` text
                    FASTAPI
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      Basics        Pydantic        HTTP
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                    CRUD
                       │
                       ▼
                 Dependencies
                       │
                       ▼
                   APIRouter
                       │
                       ▼
                  PostgreSQL
                       │
                       ▼
                   SQLAlchemy
                       │
                       ▼
                    Alembic
                       │
                       ▼
              Authentication
                       │
                       ▼
                  Async / Await
                       │
                       ▼
                    Testing
                       │
                       ▼
                Docker / Deploy
                       │
                       ▼
             Production Architecture
```

------------------------------------------------------------------------

# 📁 Current Learning Structure

The repository starts simple and will evolve as the concepts become more
advanced.

``` text
fastapi/
│
├── main.py
├── dtos.py
├── mockData.py
├── myenv/
└── README.md
```

As the project grows, it will move toward a modular production-style
structure.

> `myenv/` should normally **not** be committed to GitHub. Add it to
> `.gitignore`.

Example `.gitignore`:

``` gitignore
myenv/
__pycache__/
*.pyc
.env
.pytest_cache/
```

------------------------------------------------------------------------

# ▶️ Running Locally

## 1. Clone the repository

``` bash
git clone <your-repository-url>
cd fastapi
```

## 2. Create a virtual environment

Windows:

``` powershell
python -m venv myenv
```

Activate:

``` powershell
.\myenv\Scripts\Activate.ps1
```

Linux/macOS:

``` bash
python -m venv myenv
source myenv/bin/activate
```

## 3. Install dependencies

``` bash
pip install fastapi uvicorn
```

Or, if a requirements file exists:

``` bash
pip install -r requirements.txt
```

## 4. Start FastAPI

``` bash
fastapi dev main.py
```

------------------------------------------------------------------------

# 🖥️ Development Server

When running:

``` bash
fastapi dev main.py
```

FastAPI's development tooling starts the application and watches the
project for changes.

Typical output:

``` text
Starting FastAPI in development mode

Using import string: main:app

Server started at:
http://127.0.0.1:8000

Documentation:
http://127.0.0.1:8000/docs
```

The basic process is:

``` text
fastapi dev main.py
        ↓
Find main.py
        ↓
Import app
        ↓
Start ASGI server
        ↓
Run application startup
        ↓
Accept HTTP requests
        ↓
Watch source files
        ↓
Reload when code changes
```

------------------------------------------------------------------------

# 🧠 Key Concepts I Want to Master

-   [ ] HTTP fundamentals
-   [ ] REST API design
-   [ ] FastAPI routing
-   [ ] Path parameters
-   [ ] Query parameters
-   [ ] Request bodies
-   [ ] Response models
-   [ ] Pydantic
-   [ ] Data validation
-   [ ] Serialization / deserialization
-   [ ] CRUD
-   [ ] Dependency Injection
-   [ ] APIRouter
-   [ ] Middleware
-   [ ] Exception handling
-   [ ] Lifespan
-   [ ] Async / await
-   [ ] ASGI
-   [ ] Uvicorn
-   [ ] PostgreSQL
-   [ ] SQLAlchemy
-   [ ] Alembic
-   [ ] Authentication
-   [ ] Authorization
-   [ ] JWT
-   [ ] OAuth2
-   [ ] Testing
-   [ ] Docker
-   [ ] Deployment
-   [ ] Logging
-   [ ] Monitoring
-   [ ] Production architecture

------------------------------------------------------------------------

# 🎯 Goal

The goal of this repository is to progress from:

``` text
"How do I create a FastAPI endpoint?"
```

to:

``` text
"How do I design, build, test, secure,
scale and deploy a production-grade
Python backend?"
```

This repository will therefore contain both **learning experiments** and
**practical backend implementations**.

------------------------------------------------------------------------

## 📌 FastAPI Philosophy

> **Build APIs with Python type hints, validate data automatically,
> document APIs automatically, and keep the architecture modular enough
> to grow with the application.**

------------------------------------------------------------------------

## 📖 Useful Resources

-   FastAPI Documentation --- https://fastapi.tiangolo.com/
-   Python Documentation --- https://docs.python.org/
-   Pydantic Documentation --- https://docs.pydantic.dev/
-   Starlette Documentation --- https://www.starlette.io/
-   Uvicorn Documentation --- https://www.uvicorn.org/

------------------------------------------------------------------------

## ⭐ Repository Status

**Currently learning:** FastAPI fundamentals → REST APIs → Pydantic →
CRUD

More advanced topics will be added progressively.

If you're also learning FastAPI, feel free to explore the code and
follow along.
