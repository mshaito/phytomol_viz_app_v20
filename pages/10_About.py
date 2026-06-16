import streamlit as st
from utils.ui_helpers import banner
banner("About", "Project information, citation placeholder, and development notes.", "ℹ️")
st.markdown("""
**PhytoMol-Viz** is a Streamlit-based prototype for visualizing natural product computational drug discovery workflows.

### Current scope
- Synthetic demo datasets
- CSV upload support in core pages
- GC-MS, cytotoxicity, ADMET, target prediction, network pharmacology, docking, and MD visualization

### Intended use
Teaching, workflow demonstration, software prototyping, and future replacement with real experimental or computational data.

### Citation placeholder
Shaito, M. PhytoMol-Viz: Interactive Natural Product Drug Discovery Visualization Platform. Software prototype.
""")
