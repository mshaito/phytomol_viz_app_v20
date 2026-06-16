import streamlit as st
import plotly.express as px
from utils.ui_helpers import banner, get_data, interpretation_box

banner("4. Target Prediction", "Table 3 style module, compound-protein relationships.", "🎯")
df = get_data("target_links.csv", "target links")
st.dataframe(df, use_container_width=True)
selected = st.selectbox("Select compound", sorted(df.Compound.unique()))
st.write("### Predicted targets")
st.dataframe(df[df.Compound == selected], use_container_width=True)
counts = df.groupby("Protein").size().reset_index(name="Connections").sort_values("Connections", ascending=False)
fig = px.bar(counts, x="Protein", y="Connections", title="Protein connection counts")
st.plotly_chart(fig, use_container_width=True)
interpretation_box("Target prediction", ["Target links represent predicted or curated compound-protein associations.", "Highly connected proteins may become candidates for docking or pathway analysis.", "Experimental validation is required before mechanistic claims."])
