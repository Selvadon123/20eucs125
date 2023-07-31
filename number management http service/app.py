from fastapi import FastAPI, Query
from typing import List

from logic import Logic
import uvicorn

app = FastAPI()
logic = Logic()


@app.get("/number/management")
async def root(url: List[str] = Query([])):
    return logic.get_response(url)



if __name__ == '__main__':
    
    uvicorn.run("app:app", host="0.0.0.0", port=8080,reload=True, access_log=False)