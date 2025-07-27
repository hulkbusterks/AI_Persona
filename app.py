from fastapi import FastAPI,Body
from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent
from config.client import model
from tools.my_details import my_info
from tools.tools import tools
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from tools.get_details import get_personality
from models.api_models import VideoId
from database.pinecone_upsert import upsert_video_chunks_to_pinecone
from database.pinecone_retriever import semantic_search_by_creator
from database.charachter_db import store_video_chunks_in_db,create_video_creator_table,insert_video_creator
app=FastAPI()



@app.get("/")
def health():
    return {"message": "Hello, I am alive!"}




@app.post("/my_personality",)
def personality(video_id:VideoId=Body(...)):
    return get_personality(list(video_id.video_id))


@app.get("/my_details")
def my_details():
    return my_info()


if __name__ == "__main__":
    create_video_creator_table()
    store_video_chunks_in_db(video_id="KZeIEiBrT_w")

    upsert_video_chunks_to_pinecone(video_id="KZeIEiBrT_w")
    print(semantic_search_by_creator(creator_id="creator123", search_query="What is the markov chain?"))