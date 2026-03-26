import { useEffect, useState } from "react";
import GraphView from "./components/GraphView";
import ChatBox from "./components/ChatBox";
import { fetchGraph } from "./services/api";

function App() {
  const [graph, setGraph] = useState({ nodes: [], edges: [] });
  const [answer, setAnswer] = useState("");

  useEffect(() => {
    fetchGraph().then(setGraph);
  }, []);

  return (
    <div className="app" style={{ display: "flex", gap: "20px" }}>
      <div className="left">
        <h2>Graph View</h2>
        <GraphView nodes={graph.nodes} edges={graph.edges} />
      </div>

      <div className="right">
        <h2>AI Query Interface</h2>
        <ChatBox setGraph={setGraph} setAnswer={setAnswer} />
        <div style={{ marginTop: "20px" }}>
          <strong>Answer:</strong>
          <p>{answer}</p>
        </div>
      </div>
    </div>
  );
}

export default App;