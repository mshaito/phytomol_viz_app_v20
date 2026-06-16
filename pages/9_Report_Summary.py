import streamlit as st
from utils.data_loader import load_csv
from utils.ui_helpers import banner

banner("9. Report Summary", "Synthetic workflow summary and export-ready interpretation.", "📄")
gcms = load_csv("gcms_compounds.csv"); admet = load_csv("admet_properties.csv"); docking = load_csv("docking_scores.csv")
st.write("### Dataset overview")
st.write(f"GC-MS compounds: **{len(gcms)}**")
st.write(f"ADMET compounds: **{len(admet)}**")
st.write(f"Docking pairs: **{len(docking)}**")
best = docking.sort_values("Docking_Score").iloc[0]
st.success(f"Best synthetic docking pair: {best.Compound} with {best.Protein}, score {best.Docking_Score} kcal/mol")
st.write("### Suggested manuscript wording")
summary = "This demonstration platform uses synthetic data to illustrate a computational natural product discovery workflow, including chemical profiling, ADMET visualization, target mapping, network pharmacology, docking score comparison, and molecular dynamics metric exploration."
st.write(summary)
st.download_button("Download summary text", summary, file_name="phytomol_viz_summary.txt")
st.write("### Important limitation")
st.warning("The included data are synthetic and should not be interpreted as experimental or validated biological results.")
