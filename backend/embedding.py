"""
OpenCLIP embedding generation.

This module converts a user-uploaded image into a normalized
512-dimensional embedding for similarity search.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add project root to sys.path to allow importing backend package when run directly
if __name__ == "__main__" or __package__ is None:
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from typing import Union

import numpy as np
# pyrefly: ignore [missing-import]
import open_clip
import torch
# pyrefly: ignore [missing-import]
from PIL import Image

from backend.config import (
    CLIP_MODEL_NAME,
    CLIP_PRETRAINED,
    DEVICE,
)


class EmbeddingGenerator:
    """
    Generates OpenCLIP embeddings for uploaded images.
    """

    def __init__(self) -> None:
        self.device = torch.device(DEVICE)

        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name=CLIP_MODEL_NAME,
            pretrained=CLIP_PRETRAINED,
        )

        self.model.to(self.device)
        self.model.eval()

    def generate_embedding(
        self,
        image: Union[Image.Image, str],
    ) -> np.ndarray:
        """
        Generate a normalized embedding from an image.

        Parameters
        ----------
        image : PIL.Image.Image or str
            Uploaded PIL image or path to an image.

        Returns
        -------
        np.ndarray
            Normalized embedding of shape (1, embedding_dim).
        """

        if isinstance(image, str):
            image = Image.open(image)

        image = image.convert("RGB")

        image_tensor = self.preprocess(image).unsqueeze(0).to(self.device)

        with torch.inference_mode():
            embedding = self.model.encode_image(image_tensor)

            # L2 normalization for cosine similarity
            embedding = embedding / embedding.norm(dim=-1, keepdim=True)

        return embedding.cpu().numpy().astype(np.float32)


# Shared application-wide embedding generator
embedding_generator = EmbeddingGenerator()