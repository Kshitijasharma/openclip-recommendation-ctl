# pyrefly: ignore [missing-import]

"""
Outfit ranking module.

This module scores generated outfits and returns the
highest-ranked recommendations.
"""

from __future__ import annotations

from typing import Dict, List

import pandas as pd

from backend.config import NUM_OUTFITS


class OutfitRanker:
    """
    Scores and ranks generated outfits.
    """

    def rank(
        self,
        outfits: List[Dict[str, pd.Series]],
        top_n: int = NUM_OUTFITS,
    ) -> List[Dict]:
        """
        Rank outfit combinations.

        Parameters
        ----------
        outfits : List[Dict[str, pd.Series]]
            Generated outfit combinations.

        top_n : int
            Number of outfits to return.

        Returns
        -------
        List[Dict]
            Ranked outfits.
        """

        ranked_outfits = []

        for outfit in outfits:

            similarities = [
                float(item["similarity"])
                for item in outfit.values()
            ]

            score = sum(similarities) / len(similarities)

            ranked_outfits.append(
                {
                    "score": round(score, 4),
                    "items": outfit,
                }
            )

        ranked_outfits.sort(
            key=lambda outfit: outfit["score"],
            reverse=True,
        )

        return ranked_outfits[:top_n]


# Shared application-wide instance
outfit_ranker = OutfitRanker()