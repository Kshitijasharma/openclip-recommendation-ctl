# pyrefly: ignore [missing-import]
# Streamlit entry point

"""
StyleAI Streamlit Application.

Entry point for the Streamlit frontend.
"""

# pyrefly: ignore [missing-import]
import sys
from pathlib import Path

from components.sidebar import render_sidebar

# Add project root and app folder to python path so python can find backend and app components
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(PROJECT_ROOT / "app") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "app"))

# pyrefly: ignore [missing-import]
import streamlit as st

from pages.home import render_home_page


def main() -> None:
    """Launch the StyleAI application."""

    st.set_page_config(
        page_title="StyleAI",
        page_icon="👗",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    render_sidebar()
    render_home_page()


if __name__ == "__main__":
    main()