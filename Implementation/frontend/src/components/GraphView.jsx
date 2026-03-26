import ReactFlow, { Background, Controls } from "reactflow";
import "reactflow/dist/style.css";

const GraphView = ({ nodes, edges }) => {
  const formattedNodes = nodes.map((n, i) => ({
    id: String(n.id || i),
    data: { label: n.label || n.id || "Node" },
    position: { x: Math.random() * 400, y: Math.random() * 400 }
  }));

  const formattedEdges = edges.map((e, i) => ({
    id: `e-${i}`,
    source: String(e.source),
    target: String(e.target)
  }));

  return (
    <div style={{ height: "100vh" }}>
      <ReactFlow nodes={formattedNodes} edges={formattedEdges}>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

export default GraphView;