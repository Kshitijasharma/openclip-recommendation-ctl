"""
Home page for the StyleAI application.
"""

from __future__ import annotations

# pyrefly: ignore [missing-import]
import streamlit as st

from backend.pipeline import pipeline
from components.sidebar import render_sidebar
from components.upload_panel import render_upload_panel
from components.uploaded_item import render_uploaded_item
from components.outfit_card import render_outfit_card

def render_home_page() -> None:
    """
    Render the StyleAI home page.
    """

    # Render sidebar information
    render_sidebar()

    # Render upload panel
    image, query_group, analyze = render_upload_panel()

    if not analyze:
        return

    if image is None:
        st.warning("Please upload an image.")
        return

    # Generate recommendations
    with st.spinner("Generating recommendations..."):
        result = pipeline.recommend(
            image=image,
            query_group=query_group,
        )

    if not result.outfits:
        st.info("No outfit recommendations found.")
        return

    # ---------------------------------------------------------
    # Uploaded image + recommendations
    # ---------------------------------------------------------

    left_col, right_col = st.columns([0.8, 2.2])

    with left_col:
        render_uploaded_item(
            image=image,
            fashion_group=query_group,
        )

    with right_col:

        st.subheader("Top Recommendation")

        render_outfit_card(
            outfit=result.outfits[0],
            outfit_number=1,
        )

        if len(result.outfits) > 1:

            st.divider()

            st.subheader("✨ Alternative Recommendation")
            

            render_outfit_card(
                outfit=result.outfits[1],
                outfit_number=2,
            )