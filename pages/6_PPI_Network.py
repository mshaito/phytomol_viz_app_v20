import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from utils.ui_helpers import banner, get_data, interpretation_box

banner("6. PPI Network", "Figure 5 style module, protein-protein interaction network and hub ranking.", "🧬")
df = get_data("ppi_network.csv", "PPI network")
st.dataframe(df, use_container_width=True)
G = nx.from_pandas_edgelist(df, source="Protein_A", target="Protein_B", edge_attr="Interaction_Score")
pos = nx.spring_layout(G, seed=7)
edge_x=[]; edge_y=[]
for a,b in G.edges():
    x0,y0=pos[a]; x1,y1=pos[b]; edge_x += [x0,x1,None]; edge_y += [y0,y1,None]
node_x=[]; node_y=[]; text=[]
for n in G.nodes():
    x,y=pos[n]; node_x.append(x); node_y.append(y); text.append(n)
fig=go.Figure([go.Scatter(x=edge_x,y=edge_y,mode="lines"), go.Scatter(x=node_x,y=node_y,mode="markers+text",text=text,textposition="top center",marker=dict(size=24))])
fig.update_layout(height=600, showlegend=False, title="Protein-protein interaction network")
st.plotly_chart(fig,use_container_width=True)
deg = pd.DataFrame({"Protein": list(dict(G.degree()).keys()), "Degree": list(dict(G.degree()).values())}).sort_values("Degree", ascending=False)
st.dataframe(deg, use_container_width=True)
interpretation_box("PPI network", ["PPI analysis explores how predicted targets interact with each other.", "Hub proteins may represent important pathway regulators.", "Interaction scores depend on source database and confidence thresholds."])
