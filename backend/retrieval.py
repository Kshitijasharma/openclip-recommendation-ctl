# FAISS retrieval
"""
FAISS retrieval module.

This module searches the precomputed FAISS index using a query embedding
and returns the corresponding product metadata.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from backend.config import TOP_K
from backend.loader import loader


class Retriever:
    """
    Retrieves the nearest fashion items from the FAISS index.
    """

    def __init__(self) -> None:
        self.index = loader.index
        self.metadata = loader.metadata

    def retrieve(
        self,
        embedding: np.ndarray,
        top_k: int = TOP_K,
    ) -> pd.DataFrame:
        """
        Retrieve the top-k nearest fashion items.

        Parameters
        ----------
        embedding : np.ndarray
            Query embedding of shape (1, embedding_dim).

        top_k : int
            Number of nearest neighbours to retrieve.

        Returns
        -------
        pd.DataFrame
            Retrieved items with similarity scores.
        """

        distances, indices = self.index.search(embedding, top_k)

        results = self.metadata.iloc[indices[0]].copy()

        results["similarity"] = distances[0]

        results.reset_index(drop=True, inplace=True)

        return results


# Shared application-wide retriever
retriever = Retriever()