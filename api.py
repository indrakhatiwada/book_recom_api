from logging import debug
from pyexpat import model
from turtle import title
import uvicorn

import pickle
from model import recommend_book

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()



class Books(BaseModel):
    title: str

pickle_in = open("model.pkl","rb")
df = pickle.load(pickle_in)

@app.post('/predict')
def predict_book(data:Books):
   recommendations = list(recommend_book(data.title))
   return {'recommendations': recommendations}
#    print(str(recommendations).type)
    # print(data.title)

# @app.post('/predict{title}')
# def predict_book(data:Books):
#     #recommend_book(title)
#     print(data)
@app.get('/')
def index():
    return {'message': "This is the homepage of the api"}

app.get('/apiv1/{name}')

def api1(name: str):

    return {'message': f'Hello! @{name}'}

@app.get('/apiv2/')

def api2(name: str):

    return {'message': f'Hello! @{name}'}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port = 8000, debug= True)