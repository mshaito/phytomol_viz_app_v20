import streamlit as st
from pathlib import Path
from utils.data_loader import list_demo_files
from utils.ui_helpers import workflow_diagram

st.set_page_config(page_title="PhytoMol-Viz", page_icon="🧬", layout="wide")

ROOT = Path(__file__).parent
logo = ROOT / "assets" / "logo.svg"

st.title("🧬 PhytoMol-Viz")
st.subheader("Interactive natural product drug discovery visualization platform")

if logo.exists():
    st.image(str(logo), width=380)

st.markdown("### End-to-end workflow")
workflow_diagram()

st.info("This prototype uses synthetic demonstration data inspired by common workflows in GC-MS, cytotoxicity, ADMET, target prediction, docking, and molecular dynamics analysis.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Data mode", "Demo + upload")
col2.metric("Core modules", "9")
col3.metric("Workflow", "GC-MS to MD")
col4.metric("Status", "Prototype")

st.markdown("""
### Suggested workflow
1. Inspect compounds in **GC-MS Explorer**.
2. Explore dose-response and IC50 concepts in **Cytotoxicity**.
3. Compare descriptors in **ADMET Dashboard**.
4. Explore compound-protein relationships in **Target Prediction** and networks.
5. Review docking and molecular dynamics outputs.
6. Summarize the workflow in **Report Summary**.

### Data status
All included datasets are synthetic and should not be reported as experimental findings.
""")

with st.expander("Included demo datasets"):
    for f in list_demo_files():
        st.write(f"- `{f}`")

st.success("Use the pages in the sidebar to explore each module.")
