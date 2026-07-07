"""
Upload panel component for StyleAI.
"""

from __future__ import annotations

from typing import Optional, Tuple

# pyrefly: ignore [missing-import]
from PIL import Image
# pyrefly: ignore [missing-import]
import streamlit as st


FASHION_GROUPS = [
    "Topwear",
    "Bottomwear",
    "Dress",
    "Footwear",
    "Outerwear",
    "Bag",
    "Jewelry",
    "Accessories",
]


def render_upload_panel() -> Tuple[Optional[Image.Image], Optional[str], bool]:
    """
    Render the upload panel.

    Returns
    -------
    tuple
        (
            uploaded_image,
            selected_fashion_group,
            analyze_clicked
        )
    """

    uploaded_image = None

    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Upload Fashion Item")

            uploaded_file = st.file_uploader(
                "Choose an image",
                type=["jpg", "jpeg", "png"],
            )

            query_group = st.selectbox(
                "Fashion Group",
                FASHION_GROUPS,
            )

            analyze = st.button(
                "Analyze Outfit",
                use_container_width=True,
                type="primary",
            )

        with col2:
            st.subheader("Uploaded Image")
            if uploaded_file is not None:
                uploaded_image = Image.open(uploaded_file).convert("RGB")
                st.image(
                    uploaded_image,
                    width=160,
                    
                )
            else:
                st.markdown(
                    """
                    <div style="
                        border: 2px dashed #4b5563;
                        border-radius: 8px;
                        height: 220px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        color: #9ca3af;
                        text-align: center;
                        padding: 10px;
                        margin-top: 10px;
                    ">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 10px; opacity: 0.5;">
                                <rect width="18" height="18" x="3" y="3" rx="2" ry="2"/>
                                <circle cx="9" cy="9" r="2"/>
                                <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>
                            </svg>
                            <p style="margin: 0; font-size: 14px;">Preview will appear here</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    return uploaded_image, query_group, analyze