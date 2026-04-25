from fastapi import FastAPI
from app.routers import auth, watch_list

app = FastAPI()

app.include_router(auth.router)
app.include_router(watch_list.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
