"""
Reusable component for displaying a recommended outfit.
"""

from __future__ import annotations

from typing import Any, Dict

# pyrefly: ignore [missing-import]
import streamlit as st

from components.recommendation_item import render_recommendation_item


def render_outfit_card(
    outfit: Dict[str, Any],
    outfit_number: int,
) -> None:
    """
    Render a single recommended outfit.

    Parameters
    ----------
    outfit : Dict[str, Any]
        Ranked outfit returned by the recommendation pipeline.

    outfit_number : int
        Outfit number for display.
    """

    with st.container(border=True):

        # ==========================================================
        # Header
        # ==========================================================

        title_col, score_col = st.columns([4, 1])

        with title_col:
            if outfit_number == 1:
                st.markdown("### Best Match")
            else:
                st.markdown(f"### ✨ Outfit {outfit_number}")

        with score_col:
            st.metric(
                label="Match",
                value=f"{outfit['score'] * 100:.0f}%",
            )

        st.divider()

        # ==========================================================
        # Items to Display
        # ==========================================================

        display_items = {
            group: item
            for group, item in outfit["items"].items()
            if group != "Accessories"
        }

        columns = st.columns(len(display_items))

        for column, (_, item) in zip(columns, display_items.items()):

            with column:
                render_recommendation_item(item)