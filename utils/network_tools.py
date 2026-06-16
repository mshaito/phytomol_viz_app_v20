import pandas as pd
import networkx as nx


def degree_table(graph: nx.Graph) -> pd.DataFrame:
    """Return a sorted degree table for a NetworkX graph."""
    return pd.DataFrame(
        {"Node": list(dict(graph.degree()).keys()), "Degree": list(dict(graph.degree()).values())}
    ).sort_values("Degree", ascending=False)


def centrality_table(graph: nx.Graph) -> pd.DataFrame:
    """Return degree, betweenness, and closeness centrality values."""
    if graph.number_of_nodes() == 0:
        return pd.DataFrame(columns=["Node", "Degree_Centrality", "Betweenness", "Closeness"])
    return pd.DataFrame({
        "Node": list(graph.nodes()),
        "Degree_Centrality": pd.Series(nx.degree_centrality(graph)),
        "Betweenness": pd.Series(nx.betweenness_centrality(graph)),
        "Closeness": pd.Series(nx.closeness_centrality(graph)),
    }).reset_index(drop=True).sort_values("Degree_Centrality", ascending=False)
