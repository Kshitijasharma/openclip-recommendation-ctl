# load metadata, embeddings, FAISS

"""
Loads and caches precomputed retrieval assets.

Responsibilities:
- Load metadata.csv
- Load embeddings.npy
- Load FAISS index

Assets are loaded only once and reused for the application's lifetime.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

# pyrefly: ignore [missing-import]
import faiss
import numpy as np
import pandas as pd

from backend.config import (
    METADATA_PATH,
    EMBEDDINGS_PATH,
    FAISS_INDEX_PATH,
)


class DataLoader:
    """
    Singleton-style loader for retrieval assets.

    The assets are lazily loaded and cached to avoid repeated
    disk I/O during inference.
    """

    def __init__(self) -> None:
        self._metadata: Optional[pd.DataFrame] = None
        self._embeddings: Optional[np.ndarray] = None
        self._index: Optional[faiss.Index] = None

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def load(self) -> None:
        """
        Load all assets if they are not already loaded.
        """
        if self.is_loaded:
            return

        self._validate_files()

        self._metadata = pd.read_csv(METADATA_PATH)
        self._embeddings = np.load(EMBEDDINGS_PATH)
        self._index = faiss.read_index(str(FAISS_INDEX_PATH))

    @property
    def metadata(self) -> pd.DataFrame:
        """
        Returns the metadata dataframe.
        """
        self.load()
        return self._metadata

    @property
    def embeddings(self) -> np.ndarray:
        """
        Returns the embedding matrix.
        """
        self.load()
        return self._embeddings

    @property
    def index(self) -> faiss.Index:
        """
        Returns the FAISS index.
        """
        self.load()
        return self._index

    @property
    def is_loaded(self) -> bool:
        """
        Returns True if all assets have been loaded.
        """
        return (
            self._metadata is not None
            and self._embeddings is not None
            and self._index is not None
        )

    # ------------------------------------------------------------------ #
    # Internal Helpers
    # ------------------------------------------------------------------ #

    @staticmethod
    def _validate_file(path: Path) -> None:
        """
        Raise FileNotFoundError if a required file is missing.
        """
        if not path.exists():
            raise FileNotFoundError(f"Required file not found: {path}")

    def _validate_files(self) -> None:
        """
        Validate that all required retrieval assets exist.
        """
        self._validate_file(METADATA_PATH)
        self._validate_file(EMBEDDINGS_PATH)
        self._validate_file(FAISS_INDEX_PATH)


# Shared application-wide loader instance.
loader = DataLoader()