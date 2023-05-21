from fastapi import FastAPI
import uvicorn
import requests as req

from db_transactions.crud import create_user as db_create_user, db_update_user

app = FastAPI()


@app.get("/people")
def get_starwars_people(number: int):
    response = req.get(f'https://swapi.dev/api/people/{number}/')
    return {"message": response.json()}


@app.post('/user/')
def create_user(name: str):
    return db_create_user(name)


@app.post('/update_user/')
def update_user(id: int, name: str):
    return db_update_user(id, name)


@app.get("/starships")
def get_starships(number: int):
    response = req.get(f'https://swapi.dev/api/people/{number}/')
    return {"message": response.json()}


if __name__ == '__main__':
    uvicorn.run(app, port=8082)