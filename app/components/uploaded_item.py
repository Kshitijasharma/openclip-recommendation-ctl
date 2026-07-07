"""
Uploaded item display component.
"""

from __future__ import annotations

# pyrefly: ignore [missing-import]
from PIL import Image

# pyrefly: ignore [missing-import]
import streamlit as st


def render_uploaded_item(
    image: Image.Image,
    fashion_group: str,
) -> None:
    """
    Display the uploaded fashion item.
    """

    with st.container(border=True):

        st.subheader("📸 Uploaded Item")

        # Create a smaller copy for display
        display_image = image.copy()
        display_image.thumbnail((180, 180))

        st.image(display_image)

        st.markdown(
            f"**Fashion Group:** {fashion_group}"
        )