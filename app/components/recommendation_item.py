"""
Recommendation item component for StyleAI.
"""

from __future__ import annotations

from scripts import add_image_path
from pathlib import Path
# pyrefly: ignore [missing-import]
from PIL import Image
# pyrefly: ignore [missing-import]
import streamlit as st


def render_recommendation_item(item) -> None:
    """
    Render a single recommended fashion item.

    Parameters
    ----------
    item : pd.Series or dict-like
        Product metadata containing details like image_path, category, etc.
    """
    project_root = Path(__file__).resolve().parent.parent.parent

    # Try to load and render the image
    image_path_str = item.get("image_path")
    if image_path_str:
        image_path = project_root / image_path_str
        if image_path.exists():
            try:
                img = Image.open(image_path)
                # Replace 'use_container_width=True' with a fixed width:
                st.image(img, width=160)

            except Exception as e:
                st.error(f"Error loading image: {e}")
        else:
            st.warning("Image not found")
    else:
        st.warning("No image path provided")

    # Display fashion group and category
    fashion_group = item.get("fashion_group", "Unknown")
    category = item.get("category", "")
    
    st.markdown(f"**{fashion_group}**")
    if category and category != fashion_group:
        st.caption(category)

    # Display item text
    text = item.get("text", "")
    if text:
        st.markdown(f"<small>{text.title()}</small>", unsafe_allow_html=True)
