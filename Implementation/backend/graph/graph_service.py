from graph.build_graph import build_graph

def get_graph_data():
    G = build_graph()

    nodes = [{"id": n} for n in G.nodes()]
    edges = [{"source": u, "target": v} for u, v in G.edges()]

    return {"nodes": nodes, "edges": edges}