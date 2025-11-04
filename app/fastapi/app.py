# region imports and environment variables
import os
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
# endregion imports and environment variables

# region FastAPI app initialization

app = FastAPI(
    title="Project Orbit API",
    description="API for Project Orbit",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
# endregion FastAPI app initialization

# region root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
# endregion / endpoint

# region GET companies endpoint
@app.get("/companies")
def get_companies():
    return {"message": "Companies"}
# endregion /companies endpoint

# region POST dashboard/rag endpoint (RAG Based Dashboard)
@app.post("/dashboard/rag")
def create_dashboard_rag(payload: dict):
    return {"message": "Dashboard RAG"}
# endregion POST dashboard/rag endpoint (RAG Based Dashboard)

# region POST dashboard/structured endpoint (Structured Dashboard)
@app.post("/dashboard/structured")
def create_dashboard_structured(payload: dict):
    return {"message": "Dashboard Structured"}
# endregion POST dashboard/structured endpoint (Structured Dashboard)