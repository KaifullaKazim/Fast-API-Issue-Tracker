# 🚀 FastAPI Issue Tracker API

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)
![Render](https://img.shields.io/badge/Hosted%20on-Render-46E3B7?style=for-the-badge\&logo=render\&logoColor=white)
![REST API](https://img.shields.io/badge/API-REST-blue?style=for-the-badge)

**A RESTful Issue Tracker built using FastAPI demonstrating CRUD operations, Batch Processing, Middleware, Request Validation, and JSON-based data persistence.**

</div>

---

## 🌐 Live Demo

🚀 **Live API**

https://fast-api-issue-tracker-1.onrender.com

📖 **Swagger Documentation**

https://fast-api-issue-tracker-1.onrender.com/docs

📚 **ReDoc Documentation**

https://fast-api-issue-tracker-1.onrender.com/redoc

💻 **GitHub Repository**

https://github.com/KaifullaKazim/Fast-API-Issue-Tracker

---

# ✨ Features

* ✅ Complete CRUD Operations
* ✅ Batch Create API
* ✅ Batch Update API
* ✅ UUID-based Issue IDs
* ✅ Pydantic Request Validation
* ✅ Enum Validation
* ✅ Automatic OpenAPI Documentation
* ✅ Interactive Swagger UI
* ✅ ReDoc Documentation
* ✅ Custom Middleware
* ✅ JSON File Persistence
* ✅ Modular Project Structure

---

# 🛠 Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Backend Development           |
| FastAPI    | REST API Framework            |
| Pydantic   | Request & Response Validation |
| Uvicorn    | ASGI Server                   |
| JSON       | Lightweight Data Storage      |
| UUID       | Unique Issue Identification   |
| Render     | Cloud Deployment              |

---

# 📁 Project Structure

```text
Fast-API-Issue-Tracker
│
├── app
│   ├── middleware
│   │   └── timer.py
│   │
│   ├── routes
│   │   └── issues.py
│   │
│   ├── schemas.py
│   └── storage.py
│
├── data
│   └── issues.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🚀 API Endpoints

| Method | Endpoint                    | Description              |
| ------ | --------------------------- | ------------------------ |
| GET    | `/api/v1/issues/`           | Retrieve all issues      |
| GET    | `/api/v1/issues/{issue_id}` | Retrieve a single issue  |
| POST   | `/api/v1/issues/`           | Create a new issue       |
| PUT    | `/api/v1/issues/{issue_id}` | Update an existing issue |
| DELETE | `/api/v1/issues/{issue_id}` | Delete an issue          |
| POST   | `/api/v1/issues/Batch`      | Batch Create Issues      |
| PUT    | `/api/v1/issues/Batch`      | Batch Update Issues      |

---

# 📝 Sample Request

------------------------------------------------------------------------

# 🔍 Endpoint Details
------------------------------------------------------------------------
## GET /api/v1/issues/

Returns all stored issues from `data/issues.json`.

**Response**

``` json
[
  {
    "id":"uuid",
    "title":"Bug",
    "description":"Example",
    "status":"open",
    "priority":"high"
  }
]
```

------------------------------------------------------------------------

## Create Issue

```json
{
    "title": "Login Issue",
    "description": "Unable to login using Google",
    "priority": "high"
}
```


------------------------------------------------------------------------

## GET /api/v1/issues/{issue_id}

Returns a single issue matching the UUID.

**Example**

``` http
GET /api/v1/issues/7fa8...
```

------------------------------------------------------------------------

------------------------------------------------------------------------

## DELETE /api/v1/issues/{issue_id}

Deletes the specified issue from the JSON storage and returns the
deleted object.

------------------------------------------------------------------------

## Batch Create

```json
{
    "issues": [
        {
            "title": "Issue 1",
            "description": "Description",
            "priority": "medium"
        },
        {
            "title": "Issue 2",
            "description": "Description",
            "priority": "high"
        }
    ]
}
```

---

## Batch Update

```json
{
    "issues": [
        {
            "id": "UUID",
            "title": "Updated Issue",
            "description": "Updated Description",
            "status": "closed",
            "priority": "high"
        }
    ]
}
```

---

# 📦 Issue Model

```json
{
    "id": "UUID",
    "title": "Issue Title",
    "description": "Issue Description",
    "status": "open",
    "priority": "medium"
}
```

---

# 📂 Data Storage

This project intentionally uses **JSON-based persistence** instead of a relational database to focus on FastAPI fundamentals.

Data is stored in:

```text
data/issues.json
```

The storage layer automatically:

* Loads existing records
* Creates the data directory if missing
* Writes updates back to the JSON file

---

# ⚡ Custom Middleware

A custom middleware measures the processing time of every request.

Each response contains:

```text
X-Process-Time
```

Example:

```text
X-Process-Time: 0.00231
```

---

# 📖 Automatic API Documentation

FastAPI automatically generates OpenAPI documentation.

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

---

# ▶️ Running Locally

Clone the repository

```bash
git clone https://github.com/KaifullaKazim/Fast-API-Issue-Tracker.git
```

Move into the project

```bash
cd Fast-API-Issue-Tracker
```

Create a virtual environment

```bash
python -m venv env
```

Activate

Windows

```bash
env\Scripts\activate
```

Linux/macOS

```bash
source env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
fastapi dev main.py
```

or

```bash
uvicorn main:app --reload
```

Visit

```
http://127.0.0.1:8000
```

You will automatically be redirected to the interactive Swagger documentation.

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* FastAPI
* REST API Design
* CRUD Operations
* Batch API Design
* APIRouter
* Pydantic Models
* Request Validation
* Response Models
* UUID Generation
* Custom Middleware
* JSON Data Persistence
* Error Handling
* Modular Project Structure
* Cloud Deployment using Render

---

# 🚀 Future Improvements

* SQLite Integration
* PostgreSQL
* SQLAlchemy ORM
* JWT Authentication
* User Registration & Login
* Role-Based Access Control
* Pagination
* Filtering
* Search API
* Unit Testing with Pytest
* Docker
* GitHub Actions CI/CD
* Logging
* Rate Limiting

---

# 👨‍💻 Author

**Mohammed Kaifulla Kazim**

🔗 GitHub

https://github.com/KaifullaKazim

If you found this project useful, consider giving it a ⭐ on GitHub.
