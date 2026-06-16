import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components
from pathlib import Path
from utils.ui_helpers import banner, get_data, interpretation_box

banner("7. Docking Viewer", "Figures 7 and 8 style module, docking scores and interaction summaries.", "🔗")
df = get_data("docking_scores.csv", "docking scores")
st.dataframe(df, use_container_width=True)
fig = px.bar(df.sort_values("Docking_Score"), x="Compound", y="Docking_Score", color="Protein", hover_data=["Hydrogen_Bonds", "Key_Residues"], title="Docking score ranking")
st.plotly_chart(fig, use_container_width=True)
heat = df.pivot_table(index="Protein", columns="Compound", values="Docking_Score")
st.plotly_chart(px.imshow(heat, text_auto=True, aspect="auto", title="Docking score heatmap"), use_container_width=True)
with st.expander("3D viewer placeholder", expanded=False):
    pdb_path = Path(__file__).resolve().parents[1] / "data" / "structures" / "demo_protein.pdb"
    pdb = pdb_path.read_text().replace('`','') if pdb_path.exists() else ''
    html = f"""
    <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
    <div id="viewer" style="width:100%; height:420px; position:relative;"></div>
    <script>
      let viewer = $3Dmol.createViewer("viewer", {{backgroundColor:"white"}});
      viewer.addModel(`{pdb}`, "pdb");
      viewer.setStyle({{}}, {{cartoon:{{color:"spectrum"}}, stick:{{radius:0.15}}}});
      viewer.zoomTo(); viewer.render();
    </script>
    """
    components.html(html, height=440)
interpretation_box("Docking", ["More negative docking scores usually indicate more favorable predicted binding.", "Docking rankings are useful for prioritization but do not prove activity.", "Future versions can load real PDB, PDBQT, SDF, and interaction files."])
