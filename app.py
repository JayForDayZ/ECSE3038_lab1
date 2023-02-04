from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello World!"}

@app.get("Pokemon")
async def get_pokemon():
    # variable = await something()
        return{ "name:" "pikachu"}
