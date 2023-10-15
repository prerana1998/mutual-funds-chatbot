import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_ENV"] = os.getenv("PINECONE_ENV")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

loader = PyPDFDirectoryLoader("Data/New data")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=30,
)
texts = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings()
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.getenv("PINECONE_ENV"),  # next to api key in console
)

index_name = "documents"

# First, check if our index already exists. If it doesn't, we create it
if index_name not in pinecone.list_indexes():
    # we create a new index
    pinecone.create_index(
        name=index_name,
        metric='cosine',
        dimension=1536
    )
# The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
