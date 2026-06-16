import streamlit as st
import plotly.express as px
from utils.ui_helpers import banner, get_data, equation_box, interpretation_box

banner("8. MD Simulation Viewer", "Figures 9 and 10 style module, RMSD, RMSF, Rg, H-bonds, and SASA.", "⚛")
md = get_data("md_metrics.csv", "MD metrics")
rmsf = get_data("rmsf.csv", "RMSF")
complexes = sorted(md.Complex.unique())
selected = st.multiselect("Complexes", complexes, default=complexes)
f = md[md.Complex.isin(selected)]
for metric, label in [("RMSD","Structural deviation"),("Rg","Compactness"),("H_Bonds","Hydrogen bonding"),("SASA","Solvent accessibility")]:
    st.plotly_chart(px.line(f, x="Time_ns", y=metric, color="Complex", markers=True, title=f"{metric} over simulation time, {label}"), use_container_width=True)
st.write("### RMSF by residue")
rmsf_long = rmsf.melt(id_vars="Residue", var_name="Complex", value_name="RMSF")
rmsf_long = rmsf_long[rmsf_long.Complex.isin(selected)]
st.plotly_chart(px.line(rmsf_long, x="Residue", y="RMSF", color="Complex", markers=True, title="RMSF profile"), use_container_width=True)
equation_box("RMSD", r"RMSD=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(r_i-r_i^{ref})^2}", "RMSD tracks how much the simulated structure deviates from a reference structure over time.")
equation_box("RMSF", r"RMSF(i)=\sqrt{\langle (r_i-\langle r_i\rangle)^2\rangle}", "RMSF estimates residue-level flexibility across a simulation trajectory.")
interpretation_box("MD simulation", ["Stable RMSD suggests structural equilibration.", "RMSF identifies flexible residues or loops.", "Rg reflects protein compactness, while SASA reflects solvent exposure.", "Hydrogen-bond trends help assess ligand interaction persistence."])
