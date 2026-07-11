


# 🚀 FastAPI Issue Tracker API

A lightweight **Issue Tracking REST API** built with **FastAPI** to practice backend development concepts including CRUD operations, Batch Processing, Request Validation, Middleware, and File-Based Persistence.

This project demonstrates how to build a structured REST API using FastAPI while following clean project organization and Pydantic schema validation.

---

## 📌 Features

* ✅ Complete CRUD Operations
* ✅ Batch Create Issues
* ✅ Batch Update Issues
* ✅ UUID-based Issue IDs
* ✅ Request Validation using Pydantic
* ✅ Custom Middleware for Request Processing Time
* ✅ JSON File Storage (No Database Required)
* ✅ Automatic Interactive API Documentation
* ✅ Clean Modular Project Structure

---

## 🛠️ Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| FastAPI    | REST API Framework |
| Python     | Backend Language   |
| Pydantic   | Data Validation    |
| UUID       | Unique Issue IDs   |
| JSON       | Data Persistence   |
| Uvicorn    | ASGI Server        |

---

# 📂 Project Structure

```text
Fast-API-Issue-Tracker/
│
├── app/
│   ├── middleware/
│   │   └── timer.py
│   │
│   ├── routes/
│   │   └── issues.py
│   │
│   ├── schemas.py
│   ├── storage.py
│   └── main.py
│
├── data/
│   └── issues.json
│
├── requirements.txt
└── README.md
```

---

# 📚 API Endpoints

## Retrieve All Issues

```http
GET /api/v1/issues/
```

Returns every issue stored in the JSON database.

---

## Retrieve Single Issue

```http
GET /api/v1/issues/{issue_id}
```

Returns a specific issue using its UUID.

---

## Create Issue

```http
POST /api/v1/issues/
```

Example Request

```json
{
  "title": "Login Bug",
  "description": "Unable to login using Google",
  "priority": "high"
}
```

---

## Update Issue

```http
PUT /api/v1/issues/{issue_id}
```

Example Request

```json
{
  "title": "Updated Login Bug",
  "description": "OAuth token expired"
}
```

---

## Delete Issue

```http
DELETE /api/v1/issues/{issue_id}
```

Deletes an issue from storage.

---

# 🚀 Batch Operations

## Batch Create

```http
POST /api/v1/issues/Batch_Create
```

Example

```json
{
  "issues": [
    {
      "title": "Issue 1",
      "description": "Description 1",
      "priority": "medium"
    },
    {
      "title": "Issue 2",
      "description": "Description 2",
      "priority": "high"
    }
  ]
}
```

---

## Batch Update

```http
PUT /api/v1/issues/Batch_updation
```

Example

```json
{
  "issues": [
    {
      "id": "issue-id-1",
      "title": "Updated Title",
      "description": "Updated Description",
      "status": "closed",
      "priority": "high"
    },
    {
      "id": "issue-id-2",
      "title": "Another Update",
      "description": "Updated Again",
      "status": "in_progress",
      "priority": "medium"
    }
  ]
}
```

---

# 📋 Issue Model

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

# 📁 Data Persistence

Instead of using a traditional database, this project stores data inside:

```text
data/issues.json
```

The storage layer is responsible for

* Reading existing issues
* Writing updated issues
* Automatically creating the data directory if it does not exist

This makes the project beginner-friendly while demonstrating data persistence concepts before integrating databases like SQLite, PostgreSQL, or MongoDB.

---

# ⚡ Middleware

A custom middleware measures the execution time of every request.

For every API request, the middleware adds the following response header:

```text
X-Process-Time
```

Example:

```text
X-Process-Time: 0.003217
```

This demonstrates how middleware can intercept requests and responses for logging, monitoring, analytics, and performance measurement.

---

# ✔️ Validation

Input validation is handled using **Pydantic**.

Examples include:

* Required fields
* Optional fields
* Minimum and maximum string lengths
* Enum validation
* Automatic request parsing
* Automatic response serialization

---

# ▶️ Getting Started

## Clone the Repository

```bash
git clone https://github.com/KaifullaKazim/Fast-API-Issue-Tracker.git
```

Move into the project directory.

```bash
cd Fast-API-Issue-Tracker
```

---

## Create a Virtual Environment

Windows

```bash
python -m venv env
```

Activate

```bash
env\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv env
source env/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start the Server

```bash
uvicorn app.main:app --reload
```

The server will start at

```text
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```text
http://127.0.0.1:8000/docs
```

ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🎯 Learning Outcomes

This project helped reinforce the following backend development concepts:

* FastAPI fundamentals
* REST API design
* CRUD operations
* Request & response validation
* Path and query parameters
* UUID generation
* Batch API design
* JSON file persistence
* Middleware implementation
* Error handling with HTTP exceptions
* Project structuring using routers and schemas

---

# 🔮 Future Improvements

Some features planned for future versions include:

* SQLite/PostgreSQL integration
* SQLAlchemy ORM
* JWT Authentication
* User Accounts
* Role-Based Access Control (RBAC)
* Pagination
* Filtering and Searching
* Sorting
* Logging
* Docker Support
* Unit Testing with Pytest
* CI/CD using GitHub Actions
* Deployment on Render or Railway

---

# 👨‍💻 Author

**Mohammed Kaifulla Kazim**

GitHub: **https://github.com/KaifullaKazim**

If you found this project useful, consider giving it a ⭐ on GitHub!
