import streamlit as st
import plotly.express as px
from utils.ui_helpers import banner, get_data, equation_box, interpretation_box

banner("3. ADMET Dashboard", "Table 2 and Figure 3 style module, descriptors and drug-likeness.", "💊")
df = get_data("admet_properties.csv", "ADMET properties")
st.dataframe(df, use_container_width=True)
compound = st.selectbox("Compound", df["Compound"])
row = df[df.Compound == compound].iloc[0]
cols = st.columns(5)
for col, name in zip(cols, ["MW", "LogP", "TPSA", "HBA", "HBD"]):
    col.metric(name, row[name])
fig = px.scatter(df, x="MW", y="LogP", size="TPSA", color="Drug_Likeness", hover_name="Compound", title="MW, LogP, and TPSA comparison")
st.plotly_chart(fig, use_container_width=True)
equation_box("LogP", r"LogP=\log_{10}\left(\frac{[compound]_{octanol}}{[compound]_{water}}\right)", "LogP estimates lipophilicity, which influences solubility and membrane permeability.")
interpretation_box("ADMET", ["MW, LogP, TPSA, HBA, and HBD are common early-stage screening descriptors.", "These descriptors support prioritization, but do not prove efficacy or safety.", "Future versions can connect to RDKit or external ADMET tools."])
