
import streamlit as st
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding
from google.cloud import storage

# Automatically uses the credentials from the environment variable
client = storage.Client()

# Example: List all buckets in the project
buckets = list(client.list_buckets())
for bucket in buckets:
    print(bucket.name)




    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            documents=load_data(doc)
            model=load_model()
            gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
            query_engine=download_gemini_embedding(model,documents)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    
