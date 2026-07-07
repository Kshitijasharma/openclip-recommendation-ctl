# pyrefly: ignore [missing-import]
"""
Outfit generation module.

This module generates outfit combinations from candidate pools.
"""

from __future__ import annotations

from itertools import product
from typing import Dict, List

import pandas as pd

from backend.config import MAX_CANDIDATES_PER_GROUP


class LookGenerator:
    """
    Generates outfit combinations from candidate pools.
    """

    def generate(
        self,
        candidate_pools: Dict[str, pd.DataFrame],
    ) -> List[Dict[str, pd.Series]]:
        """
        Generate outfit combinations.

        Parameters
        ----------
        candidate_pools : Dict[str, pd.DataFrame]
            Mapping of fashion group -> candidate DataFrame.

        Returns
        -------
        List[Dict[str, pd.Series]]
            Generated outfit combinations.
        """

        if not candidate_pools:
            return []

        groups = []
        candidate_lists = []

        for group, pool in candidate_pools.items():

            if pool.empty:
                continue

            groups.append(group)

            top_candidates = [
                row
                for _, row in pool.head(MAX_CANDIDATES_PER_GROUP).iterrows()
            ]

            candidate_lists.append(top_candidates)

        outfits = []

        if not candidate_lists:
            return []

        for combination in product(*candidate_lists):

            outfit = {
                group: item
                for group, item in zip(groups, combination)
            }

            outfits.append(outfit)

        return outfits


# Shared application-wide instance
look_generator = LookGenerator()