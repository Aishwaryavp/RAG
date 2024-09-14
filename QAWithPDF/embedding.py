import os
from dotenv import load_dotenv

# Load environment variables from .env file if necessary
load_dotenv()

# Ensure GOOGLE_APPLICATION_CREDENTIALS is set correctly
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
from google.cloud import storage

# Automatically uses the credentials from the environment variable
client = storage.Client()

# Example: List all buckets in the project
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)




from llama_index.core import VectorStoreIndex
from llama_index.core import ServiceContext
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model,documents):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        #service_context = ServiceContext.from_defaults(llm=model,embed_model=gemini_embed_model, chunk_size=800, chunk_overlap=20)
        node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
    
        
        logging.info("")
        index = VectorStoreIndex.from_documents(documents,model=model,embed_model=gemini_embed_model)

        #index = VectorStoreIndex.from_documents(document,service_context=service_context)
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine(llm=model)
        return query_engine
    except Exception as e:
        raise customexception(e,sys)