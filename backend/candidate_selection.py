# pyrefly: ignore [missing-import]
"""
Candidate selection for outfit generation.

This module organizes retrieved fashion items into candidate pools
based on the outfit template corresponding to the uploaded item's
fashion group.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd

from backend.templates import OUTFIT_TEMPLATES


class CandidateSelector:
    """
    Organizes retrieved products into fashion-group candidate pools.
    """

    def select_candidates(
        self,
        retrieved_items: pd.DataFrame,
        query_group: str,
    ) -> Dict[str, pd.DataFrame]:
        """
        Select candidate pools for outfit generation.

        Parameters
        ----------
        retrieved_items : pd.DataFrame
            DataFrame returned by the retriever.

        query_group : str
            Fashion group of the uploaded image.

        Returns
        -------
        Dict[str, pd.DataFrame]
            Mapping of fashion group -> candidate DataFrame.
        """

        if query_group not in OUTFIT_TEMPLATES:
            raise ValueError(
                f"No outfit template defined for fashion group '{query_group}'."
            )

        template = OUTFIT_TEMPLATES[query_group]

        candidate_pools: Dict[str, pd.DataFrame] = {}

        for group in template.required_groups:

            pool = (
                retrieved_items[
                    retrieved_items["fashion_group"] == group
                ]
                .sort_values("similarity", ascending=False)
                .reset_index(drop=True)
            )

            candidate_pools[group] = pool

        return candidate_pools


# Shared application-wide instance
candidate_selector = CandidateSelector()