# backend/config.py

"""
Global configuration for the backend.

This module contains only application configuration such as:
- Project paths
- Data file locations
- Model configuration
- Retrieval parameters

No business logic or file loading should be implemented here.
"""

from pathlib import Path
import torch

# Project Directories
# =============================================================================


# backend/
BACKEND_DIR = Path(__file__).resolve().parent

# style-ai/
PROJECT_ROOT = BACKEND_DIR.parent

# models/
MODELS_DIR = PROJECT_ROOT / "models"

# backend/models/clip/
CLIP_MODEL_DIR = MODELS_DIR / "clip"

# backend/models/retrieval/
RETRIEVAL_DIR = MODELS_DIR / "retrieval"

# Data Files
# =============================================================================


METADATA_PATH = RETRIEVAL_DIR / "metadata.csv"
EMBEDDINGS_PATH = RETRIEVAL_DIR / "embeddings.npy"
FAISS_INDEX_PATH = RETRIEVAL_DIR / "fashion_index.faiss"

# OpenCLIP Configuration
# =============================================================================

CLIP_MODEL_NAME = "ViT-B-32"
CLIP_PRETRAINED = "laion2b_s34b_b79k"

# Expected embedding dimension
EMBEDDING_DIM = 512

# OpenCLIP default input resolution
IMAGE_SIZE = 224

# Device Configuration
# =============================================================================

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# Retrieval Configuration
# =============================================================================

# Number of nearest neighbours retrieved from FAISS
TOP_K = 50

# Recommendation Configuration
# =============================================================================

# Number of outfits returned to the frontend
NUM_OUTFITS = 2

# Maximum outfit combinations generated before ranking
MAX_OUTFIT_COMBINATIONS = 100


# Randomness
# =============================================================================

RANDOM_SEED = 42

# Candidate Selection Configuration
# =============================================================================

# Maximum candidates retained per fashion group
MAX_CANDIDATES_PER_GROUP = 3