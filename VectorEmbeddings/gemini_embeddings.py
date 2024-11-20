import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

result = genai.embed_content(
        model="models/text-embedding-004",
        content="The food is delicious")

print(str(result['embedding']))