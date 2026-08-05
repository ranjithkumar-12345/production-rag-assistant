"""
Production RAG Assistant - Main Application
This is a dummy version to test if everything works!
"""

from fastapi import FastAPI

# Create FastAPI app
app = FastAPI(
    title="Production RAG Assistant",
    description="AI-powered document Q&A system",
    version="0.1.0"
)

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "RAG Assistant is running! (Dummy Version)"
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    """Simple hello endpoint to test parameters"""
    return {"message": f"Hello {name}! Welcome to RAG Assistant!"}

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "ok",
        "services": {
            "api": "running",
            "database": "not_connected_yet",
            "llm": "not_configured_yet"
        }
    }