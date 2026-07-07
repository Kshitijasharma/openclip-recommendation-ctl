"""
Sidebar component for StyleAI.
"""

from __future__ import annotations

# pyrefly: ignore [missing-import]
import streamlit as st


def render_sidebar() -> None:
    """
    Render the StyleAI sidebar with product description and instructions.
    """

    st.sidebar.divider()
    st.sidebar.markdown("## 👗 StyleAI")
    st.sidebar.markdown("### Complete the Look with AI")
    
    st.sidebar.markdown("**Short description:**")
    st.sidebar.write(
        'Upload any fashion item and receive complete outfit recommendations '
        'powered by OpenCLIP embeddings and FAISS similarity search.'
    )
    
    st.sidebar.divider()
    
    st.sidebar.markdown("### Technology")
    st.sidebar.markdown(
        "• OpenCLIP\n\n"
        "• FAISS\n\n"
        "• Polyvore Dataset\n\n"
        "• Streamlit"
    )
    
    st.sidebar.divider()
    
    st.sidebar.markdown("### How It Works")
    st.sidebar.markdown(
        "1. Upload an image\n\n"
        "2. Select the fashion group\n\n"
        "3. Click Analyze Outfit\n\n"
        "4. View complete outfit recommendations"
    )
    
    st.sidebar.divider()
    
    st.sidebar.markdown("**StyleAI v1.0**")
