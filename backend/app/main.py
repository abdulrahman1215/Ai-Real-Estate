from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Real Estate Platform",
    description="Full-stack AI-powered real estate API",
    version="1.0.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Real Estate API is running 🏠"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}