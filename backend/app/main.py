from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import properties

app = FastAPI(
    title="AI Real Estate Platform",
    description="Full-stack AI-powered real estate API",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(properties.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "AI Real Estate API is running "}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}