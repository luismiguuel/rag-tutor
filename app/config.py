import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_GENERATION_MODEL = os.getenv(
    "GEMINI_GENERATION_MODEL",
    "gemini-2.5-flash"
)

GEMINI_EMBEDDING_MODEL = os.getenv(
    "GEMINI_EMBEDDING_MODEL",
    "gemini-embedding-001"
)

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "./.chroma"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "ml_documents"
)