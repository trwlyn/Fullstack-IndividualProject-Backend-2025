from fastapi import FastAPI
from routes import coworkspace_endpoints
import config

app = FastAPI(docs_url=config.documentation_url)

app.include_router(router=coworkspace_endpoints.app)


@app.get("/")
def root():
    return {"message": "GOTRE co-workspace API is up and running"}