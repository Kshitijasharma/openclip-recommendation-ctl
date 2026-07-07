"""
Hero section for the StyleAI application.
"""

from __future__ import annotations

# pyrefly: ignore [missing-import]
import streamlit as st


def render_hero() -> None:
    """
    Render the application hero section.
    """

    st.markdown(
        """<div style="text-align:center; padding:20px 0 10px 0;">
<h1 style="margin-bottom:0;">
    👗 StyleAI
</h1>
<h3 style="color:#9ca3af; margin-top:5px;">
    Complete the Look with AI
</h3>
<p style="
    max-width:750px;
    margin:auto;
    color:#cfcfcf;
    font-size:18px;
    line-height:1.6;
">
    Upload any fashion item and receive complete outfit
    recommendations powered by OpenCLIP embeddings,
    FAISS similarity search, and intelligent outfit generation.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.divider()