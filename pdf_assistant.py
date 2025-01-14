import typer
from typing import Optional,List
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import pgvector2


import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
db_url ='postgresql+psycopg://ai:ai@localhost:5532/ai'

knowledge_base = PDFUrlKnowledgeBase(
    urls=['https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf'],
)

knowledge_base.load()

