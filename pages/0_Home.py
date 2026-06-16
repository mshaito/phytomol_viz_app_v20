import streamlit as st
from pathlib import Path
from utils.ui_helpers import workflow_diagram

st.set_page_config(page_title="PhytoMol-Viz Home", page_icon="🧬", layout="wide")

st.title("🧬 PhytoMol-Viz")
st.subheader("Interactive visualization and education platform for natural product drug discovery workflows")

logo = Path(__file__).resolve().parents[1] / "assets" / "logo.svg"
if logo.exists():
    st.image(str(logo), width=360)

st.markdown("### Platform workflow")
workflow_diagram()

st.info("This version uses synthetic demonstration data and supports CSV upload on key pages. It is intended for app development, teaching, workflow visualization, and future replacement with real experimental or computational outputs.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("App version", "2.0")
c2.metric("Data mode", "Demo + upload")
c3.metric("Core modules", "9")
c4.metric("Main output", "Interactive report")

st.markdown("""
### What changed in v2.0
- Added a visual workflow landing page.
- Added demo-data or upload-data options in analysis pages.
- Added mathematical and biological interpretation panels.
- Added stronger MD, docking, network, and report explanations.
- Added a lightweight 3D molecular placeholder viewer for docking education.

### Design principle
The vetiver study can be used as a first case-study structure, but the app is designed as a reusable framework for other natural product studies.
""")
