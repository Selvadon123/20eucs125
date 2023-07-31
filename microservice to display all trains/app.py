from fastapi import FastAPI
from logic import Logic
import uvicorn

app = FastAPI()
logic = Logic()


@app.get("/trains/all")
async def root():
    return logic.get_all_trains()



if __name__ == '__main__':
    
    uvicorn.run("app:app", host="0.0.0.0", port=8080,reload=True, access_log=False)