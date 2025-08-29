from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes import coworkspace_endpoints
import config

app = FastAPI(docs_url=config.documentation_url)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",    # VS Code Live Server default
        "http://localhost:3000",    # Frontend development server
        "http://localhost:8000",    # Alternative local development port
        "http://127.0.0.1:5500",    # VS Code Live Server alternative
        "http://127.0.0.1:3000",    # Frontend alternative
        # Add your Azure static web app URL here
        "https://your-azure-static-webapp-name.azurestaticapps.net",
        # Optionally add your custom domain if you set one up
        "https://your-custom-domain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=coworkspace_endpoints.app)

@app.get("/")
def root():
    return {"message": "GOTRE co-workspace API is up and running"}

@app.get("/health")
async def health_check():
    """
    Health check endpoint for Azure Container Apps
    """
    return {"status": "healthy"}
