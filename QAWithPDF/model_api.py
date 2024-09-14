import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from logger import logging
from llama_index.core import Settings
from google.cloud import storage

# Automatically uses the credentials from the environment variable
client = storage.Client()

# Example: List all buckets in the project
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY="AIzaSyCqKQuLyUCytODqyUfiVyG-jJz82gvuFVA"

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        Settings.model=Gemini(models='gemini-pro',api_key=GOOGLE_API_KEY)
        return Settings.model
    except Exception as e:
        raise customexception(e,sys)
        