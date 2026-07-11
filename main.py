from fastapi import FastAPI  # pyright: ignore[reportMissingImports]
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware
from fastapi.responses import RedirectResponse # pyright: ignore[reportMissingImports]

app = FastAPI(title="FastAPI Issue Tracker API",
    description="""
A RESTful Issue Tracker built with FastAPI demonstrating:

- CRUD Operations
- Batch Create
- Batch Update
- Request Validation with Pydantic
- Custom Middleware
- JSON File Persistence
""",
    version="1.0.0",
)
app.middleware("http")(timer_middleware)
app.include_router(issues_router)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")