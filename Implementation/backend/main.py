import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI
from graph.graph_service import get_graph_data
from services.query_service import process_query
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Context Graph API Running"}

@app.get("/graph")
def graph():
    return get_graph_data()

@app.post("/query")
def query(req: QueryRequest):
    return process_query(req.query)


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)