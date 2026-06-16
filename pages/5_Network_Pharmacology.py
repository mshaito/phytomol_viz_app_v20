import streamlit as st
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
from utils.ui_helpers import banner, get_data, interpretation_box

banner("5. Network Pharmacology", "Figures 4 to 6 style module, compound-target-pathway networks.", "🕸")
links = get_data("target_links.csv", "target links")
pathways = get_data("compound_pathways.csv", "compound pathways")
mode = st.radio("Network type", ["Compound-Target", "Compound-Target-Pathway"], horizontal=True)
G = nx.Graph()
if mode == "Compound-Target":
    for _, r in links.iterrows():
        G.add_node(r.Compound, node_type="Compound"); G.add_node(r.Protein, node_type="Protein"); G.add_edge(r.Compound, r.Protein)
else:
    for _, r in pathways.iterrows():
        for n,t in [(r.Compound,"Compound"),(r.Protein,"Protein"),(r.Pathway,"Pathway"),(r.Disease,"Disease")]: G.add_node(n,node_type=t)
        G.add_edges_from([(r.Compound,r.Protein),(r.Protein,r.Pathway),(r.Pathway,r.Disease)])
pos = nx.spring_layout(G, seed=42)
edge_x=[]; edge_y=[]
for a,b in G.edges():
    x0,y0=pos[a]; x1,y1=pos[b]; edge_x += [x0,x1,None]; edge_y += [y0,y1,None]
node_x=[]; node_y=[]; text=[]; hover=[]
for n,a in G.nodes(data=True):
    x,y=pos[n]; node_x.append(x); node_y.append(y); text.append(n); hover.append(f"{n}<br>{a.get('node_type')}")
fig=go.Figure()
fig.add_trace(go.Scatter(x=edge_x,y=edge_y,mode="lines",line=dict(width=1),hoverinfo="none"))
fig.add_trace(go.Scatter(x=node_x,y=node_y,mode="markers+text",text=text,textposition="top center",hovertext=hover,marker=dict(size=20)))
fig.update_layout(title=mode,showlegend=False,height=650,margin=dict(l=10,r=10,t=50,b=10))
st.plotly_chart(fig,use_container_width=True)
cent = nx.degree_centrality(G)
st.dataframe(pd.DataFrame({"Node":cent.keys(),"Degree_Centrality":cent.values()}).sort_values("Degree_Centrality",ascending=False), use_container_width=True)
interpretation_box("Network pharmacology", ["Nodes can represent compounds, proteins, pathways, or diseases.", "Degree centrality helps identify highly connected hubs.", "Network results should guide hypotheses, not replace laboratory validation."])
