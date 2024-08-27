from fastapi import FastAPI
from app.controllers.excel_controller import router as excel_router

app = FastAPI()

# Includi il router
app.include_router(excel_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Excel Upload API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)