from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import sys

# Add backend directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import engine, Base
from routes import users, tables

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FLUTE CRM API",
    description="Dynamic Form Builder API",
    version="1.0.0"
)

origins = [
    "http://localhost:4200",
    "http://localhost:3000",
    "http://10.10.10.112:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tables.router)

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "message": "FLUTE CRM API is running",
        "version": "1.0.0"
    }

@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "FLUTE CRM API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8001)),
        reload=True,
        log_level="info"
    )
