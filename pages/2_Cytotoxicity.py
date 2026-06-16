import streamlit as st
import plotly.express as px
from utils.ui_helpers import banner, get_data, equation_box, interpretation_box

banner("2. Cytotoxicity", "Figure 2 style module, dose-response and IC50 interpretation.", "📈")
df = get_data("cytotoxicity.csv", "cytotoxicity")
st.dataframe(df, use_container_width=True)
fig = px.line(df, x="Concentration_ug_mL", y="Viability_Percent", color="Cell_Line", markers=True, title="Dose-response curves")
st.plotly_chart(fig, use_container_width=True)
equation_box("Four-parameter logistic model", r"Y=Bottom+\frac{Top-Bottom}{1+(X/IC_{50})^{HillSlope}}", "This equation is commonly used to fit dose-response curves and estimate IC50, the concentration associated with 50% inhibition.")
interpretation_box("Cytotoxicity", ["Lower IC50 generally indicates stronger antiproliferative activity.", "Normal-cell viability is needed to discuss selectivity.", "Synthetic data cannot be used as biological evidence."])
