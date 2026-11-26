from fastapi import FastAPI

from app.core.database import Base, engine
from app.api import records, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise Data Operations Platform",
    description="Business record processing and reporting APIs",
    version="1.0.0"
)

app.include_router(records.router)
app.include_router(reports.router)


@app.get("/")
def root():

    return {
        "message": "Enterprise Data Operations Platform",
        "status": "running",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }