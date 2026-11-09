from fastapi import FastAPI, APIRouter, HTTPException
from app.api.v1.api import api_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.include_router(api_router, prefix="")

@app.get("/")
async def root():
    return {"message": "Główna strona"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # kto może pytać
    allow_credentials=True,                   # czy wolno wysyłać ciasteczka
    allow_methods=["*"],                      # GET, POST, PUT, DELETE...
    allow_headers=["*"],                      # np. Authorization
)
@app.get("/health")
def health():
    return {"status": "ok"}

"""
# I think it's redundant if endpoint doesn't exist it will send 404 anyway
@app.api_route("/{path:path}", methods=["GET", "POST","PUT","PATCH","DELETE"])
async def catch_all(path : str):
    raise HTTPException(status_code=404, detail=f"Route {path} not found")"""
