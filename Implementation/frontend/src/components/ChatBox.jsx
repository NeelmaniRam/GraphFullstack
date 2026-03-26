import { useState } from "react";
import { queryAPI } from "../services/api";

export default function ChatBox({ setGraph, setAnswer }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!query) return;

    setLoading(true);
    try {
      const res = await queryAPI(query);

      // Update graph in App
      setGraph({
        nodes: res.nodes || res.data?.nodes || [],
        edges: res.edges || res.data?.edges || []
      });

      // Update AI answer in App
      setAnswer(res.answer || res.data?.answer || "");

    } catch (err) {
      console.error(err);
      setAnswer("Error fetching response");
    }
    setLoading(false);
  };

  return (
    <div className="chat">
      <input
        type="text"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ width: "300px", padding: "8px" }}
      />
      <button onClick={handleSubmit} style={{ marginLeft: "10px" }}>
        {loading ? "Loading..." : "Ask"}
      </button>
    </div>
  );
}