from fastapi import FastAPI

app = FastAPI()
print('FastAPI')

@app.get("/")
async def root():
    return {"message": "Hello World"}