export default function NodeDetails({ node }) {
  if (!node) return null;

  return (
    <div className="node-details">
      <h3>Node Details</h3>
      <p>ID: {node.id}</p>
    </div>
  );
}