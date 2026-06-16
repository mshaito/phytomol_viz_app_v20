import streamlit as st
import plotly.express as px
from utils.ui_helpers import banner, get_data, interpretation_box

banner("1. GC-MS Explorer", "Table 1 style module, compound profile and relative abundance.", "🧪")
df = get_data("gcms_compounds.csv", "GC-MS compounds")
st.dataframe(df, use_container_width=True)

fig = px.bar(df.sort_values("Area_Percent", ascending=False), x="Compound", y="Area_Percent", color="Chemical_Class", title="Relative abundance of compounds")
st.plotly_chart(fig, use_container_width=True)
selected = st.selectbox("Select a compound", df["Compound"])
row = df[df["Compound"] == selected].iloc[0]
c1, c2, c3 = st.columns(3)
c1.metric("Area %", f"{row['Area_Percent']}%")
c2.metric("Retention time", f"{row['Retention_Time']} min")
c3.metric("Class", row["Chemical_Class"])
interpretation_box("GC-MS", ["Retention time helps distinguish compounds as they elute from the GC column.", "Area percent is relative signal abundance, not an exact concentration.", "This page can be replaced with real GC-MS peak tables later."])
