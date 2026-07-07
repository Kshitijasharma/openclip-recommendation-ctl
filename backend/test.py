import sys
from pathlib import Path

# Add project root to sys.path to allow running this script directly
if __name__ == "__main__" or __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from PIL import Image
from backend.embedding import embedding_generator
from backend.retrieval import retriever

# Resolve the path to the download.png asset dynamically
image_path = Path(__file__).resolve().parent.parent / "app" / "assests" / "download.png"

# Load image
image = Image.open(image_path)

# Generate the embedding
embedding = embedding_generator.generate_embedding(image)

# Retrieve nearest neighbor matches
results = retriever.retrieve(embedding)

print(results.head())