export default function QueryResult({ data }) {
  if (data.error) {
    return <p className="error">{data.error}</p>;
  }

  return (
    <div className="result">
      <h3>Answer</h3>
      <p>{data.answer}</p>

      <h4>Generated SQL</h4>
      <pre>{data.sql}</pre>

      <h4>Raw Result</h4>
      <pre>{JSON.stringify(data.result, null, 2)}</pre>
    </div>
  );
}