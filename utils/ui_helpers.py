from pathlib import Path
import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

WORKFLOW_STEPS = [
    ("🧪", "GC-MS", "Compound profile"),
    ("📈", "Cytotoxicity", "Dose response"),
    ("💊", "ADMET", "Drug-likeness"),
    ("🎯", "Targets", "Compound-protein links"),
    ("🕸", "Networks", "Hub analysis"),
    ("🔗", "Docking", "Binding scores"),
    ("⚛", "MD", "Stability metrics"),
    ("📄", "Report", "Summary")
]

def banner(title: str, subtitle: str = "", icon: str = "🧬"):
    st.markdown(f"# {icon} {title}")
    if subtitle:
        st.caption(subtitle)
    st.info("Demo datasets are synthetic and must not be interpreted as experimental or validated biological findings.")


def workflow_diagram():
    cols = st.columns(len(WORKFLOW_STEPS))
    for col, (icon, title, desc) in zip(cols, WORKFLOW_STEPS):
        with col:
            st.markdown(
                f"""
                <div style='text-align:center; padding:10px; border-radius:12px; background:#f5f7fb; min-height:95px'>
                    <div style='font-size:28px'>{icon}</div>
                    <b>{title}</b><br>
                    <span style='font-size:12px; color:#5f6b7a'>{desc}</span>
                </div>
                """, unsafe_allow_html=True
            )


def get_data(filename: str, label: str, help_text: str = "Upload a CSV with the same columns as the demo file.") -> pd.DataFrame:
    mode = st.radio(f"Data source for {label}", ["Use synthetic demo data", "Upload CSV"], horizontal=True, key=f"mode_{filename}")
    if mode == "Upload CSV":
        uploaded = st.file_uploader(help_text, type=["csv"], key=f"upload_{filename}")
        if uploaded is not None:
            try:
                return pd.read_csv(uploaded)
            except Exception as exc:
                st.error(f"Could not read uploaded CSV: {exc}")
    return pd.read_csv(DATA_DIR / filename)


def interpretation_box(title: str, bullets):
    with st.expander(f"Interpretation guide: {title}", expanded=False):
        for b in bullets:
            st.markdown(f"- {b}")


def equation_box(title: str, latex: str, explanation: str):
    with st.expander(f"Equation: {title}", expanded=False):
        st.latex(latex)
        st.write(explanation)
