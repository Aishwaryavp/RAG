from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging
GOOGLE_API_KEY="AIzaSyCqKQuLyUCytODqyUfiVyG-jJz82gvuFVA"
from google.cloud import storage

# Automatically uses the credentials from the environment variable
client = storage.Client()

# Example: List all buckets in the project
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)


def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("./notebook/Data/")
        documents=loader.load_data()
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    