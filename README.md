# 🚀 FastAPI Issue Tracker API

## 🌐 Live Demo

-   **Live API:** https://fast-api-issue-tracker-1.onrender.com
-   **Swagger UI:** https://fast-api-issue-tracker-1.onrender.com/docs
-   **ReDoc:** https://fast-api-issue-tracker-1.onrender.com/redoc
-   **GitHub Repository:**
    https://github.com/KaifullaKazim/Fast-API-Issue-Tracker

------------------------------------------------------------------------

## 📖 Overview

A lightweight **Issue Tracking REST API** built with **FastAPI** to
practice backend development concepts including:

-   CRUD Operations
-   Batch Create
-   Batch Update
-   Request Validation
-   Middleware
-   UUID Generation
-   JSON File Persistence
-   Cloud Deployment on Render

------------------------------------------------------------------------

## ✨ Features

-   Complete CRUD Operations
-   Batch Create API
-   Batch Update API
-   UUID-based Issue IDs
-   Pydantic Validation
-   Enum Validation
-   JSON File Storage
-   Custom Middleware
-   Interactive Swagger UI
-   ReDoc Documentation
-   Render Deployment
-   Modular Project Structure

------------------------------------------------------------------------

## 🛠 Tech Stack

  Technology   Purpose
  ------------ -------------
  Python       Backend
  FastAPI      REST API
  Pydantic     Validation
  Uvicorn      ASGI Server
  UUID         Unique IDs
  JSON         Persistence
  Render       Deployment

------------------------------------------------------------------------

## 📂 Project Structure

``` text
Fast-API-Issue-Tracker/
│
├── app/
│   ├── middleware/
│   │   └── timer.py
│   ├── routes/
│   │   └── issues.py
│   ├── schemas.py
│   └── storage.py
│
├── data/
│   └── issues.json
│
├── main.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# 📚 API Endpoints

  Method   Endpoint                      Description
  -------- ----------------------------- -------------------------
  GET      `/api/v1/issues/`             Retrieve all issues
  GET      `/api/v1/issues/{issue_id}`   Retrieve a single issue
  POST     `/api/v1/issues/`             Create a new issue
  PUT      `/api/v1/issues/{issue_id}`   Update an issue
  DELETE   `/api/v1/issues/{issue_id}`   Delete an issue
  POST     `/api/v1/issues/Batch`        Batch Create
  PUT      `/api/v1/issues/Batch`        Batch Update

------------------------------------------------------------------------

# 🔍 Endpoint Details

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

## GET /api/v1/issues/{issue_id}

Returns a single issue matching the UUID.

**Example**

``` http
GET /api/v1/issues/7fa8...
```

------------------------------------------------------------------------

## POST /api/v1/issues/

Creates a new issue.

**Request**

``` json
{
  "title":"Login Bug",
  "description":"OAuth failure",
  "priority":"high"
}
```

A UUID is automatically generated and the status defaults to `open`.

------------------------------------------------------------------------

## PUT /api/v1/issues/{issue_id}

Updates an existing issue.

Example:

``` json
{
  "title":"Updated Login Bug",
  "description":"Fixed OAuth",
  "status":"closed",
  "priority":"medium"
}
```

------------------------------------------------------------------------

## DELETE /api/v1/issues/{issue_id}

Deletes the specified issue from the JSON storage and returns the
deleted object.

------------------------------------------------------------------------

## POST /api/v1/issues/Batch

Creates multiple issues in a single request.

``` json
{
  "issues":[
    {
      "title":"Issue 1",
      "description":"Example",
      "priority":"low"
    },
    {
      "title":"Issue 2",
      "description":"Example",
      "priority":"high"
    }
  ]
}
```

------------------------------------------------------------------------

## PUT /api/v1/issues/Batch

Updates multiple issues using their IDs.

``` json
{
  "issues":[
    {
      "id":"uuid",
      "title":"Updated",
      "description":"Updated description",
      "status":"closed",
      "priority":"high"
    }
  ]
}
```

------------------------------------------------------------------------

# 📦 Issue Model

``` json
{
  "id":"UUID",
  "title":"Issue Title",
  "description":"Issue Description",
  "status":"open",
  "priority":"medium"
}
```

------------------------------------------------------------------------

# 📂 Data Persistence

All data is stored inside:

``` text
data/issues.json
```

The storage layer:

-   Reads JSON
-   Writes JSON
-   Creates the folder automatically
-   Keeps the project database-free for learning purposes

------------------------------------------------------------------------

# ⚡ Middleware

Every request passes through a custom middleware that measures execution
time.

Header added:

``` text
X-Process-Time
```

------------------------------------------------------------------------

# ✔ Validation

Validation is implemented using Pydantic.

-   Required fields
-   Optional fields
-   Min/Max length
-   Enum validation
-   Automatic serialization

------------------------------------------------------------------------

# 📸 Screenshots

Add screenshots here after uploading them to your repository.

``` md
![Swagger UI](images/swagger-ui.png)

![GET Endpoint](images/get-endpoint.png)

![POST Endpoint](images/post-endpoint.png)

![Batch Create](images/batch-create.png)

![Batch Update](images/batch-update.png)
```

------------------------------------------------------------------------

# ▶ Running Locally

``` bash
git clone https://github.com/KaifullaKazim/Fast-API-Issue-Tracker.git
cd Fast-API-Issue-Tracker

python -m venv env

# Windows
env\Scripts\activate

pip install -r requirements.txt

fastapi dev main.py
```

or

``` bash
uvicorn main:app --reload
```

------------------------------------------------------------------------

# ☁ Deployment

Hosted using Render.

Root URL redirects automatically to Swagger UI.

------------------------------------------------------------------------

# 🎯 Learning Outcomes

-   FastAPI
-   CRUD APIs
-   Batch APIs
-   Middleware
-   Routing
-   UUID
-   Pydantic
-   JSON Persistence
-   Error Handling
-   Render Deployment

------------------------------------------------------------------------

# 🚀 Future Improvements

-   SQLite
-   PostgreSQL
-   SQLAlchemy
-   JWT Authentication
-   Docker
-   Pagination
-   Search
-   Filtering
-   CI/CD
-   Pytest

------------------------------------------------------------------------

# 👨‍💻 Author

**Mohammed Kaifulla Kazim**

GitHub: https://github.com/KaifullaKazim

If you found this project useful, consider giving it a ⭐.
