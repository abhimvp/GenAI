from langchain_community.vectorstores import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from datasets import load_dataset
from getpass import getpass


load_dotenv()
api_key = getpass()
astra_db_scb = os.environ["ASTRA_DB_SECURE_BUNDLE_PATH"]
astra_db_key_space = os.environ["ASTRA_DB_KEYSPACE"]
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)  # type: ignore
# https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/
myEmbedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)  # type: ignore
# https://docs.datastax.com/en/astra-db-serverless/databases/python-driver.html#basic-configuration
# configuration to connect to datastacks astradb and create an astra session
astraSession = Cluster(
    cloud={"secure_connect_bundle": astra_db_scb},
    auth_provider=PlainTextAuthProvider(
        "token", os.environ["ASTRA_DB_APPLICATION_TOKEN"]
    ),
).connect()
# https://docs.datastax.com/en/developer/python-driver/3.25/api/cassandra/cluster/index.html

# create a table
myCassandraVStore = Cassandra(
    embedding=myEmbedding,
    session=astraSession,
    keyspace=astra_db_key_space,
    table_name="qa_mini_demo",
)

print("Loading data from hugging face")
myDataset=load_dataset("Biddls/Onion_News",split="train")
headlines = myDataset["text"][:50]
print("Generating embeddings and storing in AstraDB")
myCassandraVStore.add_texts(headlines)
print("Inserted %i headlines." % len(headlines))