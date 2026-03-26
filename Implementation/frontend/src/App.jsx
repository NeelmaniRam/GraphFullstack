import { useEffect, useState } from "react";
import GraphView from "./components/GraphView";
import ChatBox from "./components/ChatBox";
import { fetchGraph } from "./services/api";

function App() {
  const [graph, setGraph] = useState({ nodes: [], edges: [] });
  const [answer, setAnswer] = useState(""); // store latest AI answer

  // Initial fetch of graph
  useEffect(() => {
    fetchGraph().then(setGraph);
  }, []);

  return (
    <div className="app" style={{ display: "flex", gap: "20px" }}>
      <div className="left" style={{ flex: 1 }}>
        <h2>Graph View</h2>
        <GraphView nodes={graph.nodes} edges={graph.edges} />
      </div>

      <div className="right" style={{ flex: 1 }}>
        <h2>AI Query Interface</h2>
        <ChatBox
          setGraph={setGraph}   // pass setGraph to ChatBox
          setAnswer={setAnswer} // pass setAnswer to ChatBox
        />
        {answer && (
          <div style={{ marginTop: "20px" }}>
            <strong>Answer:</strong>
            <p>{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;