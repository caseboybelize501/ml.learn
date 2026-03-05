import React, { useState, useEffect } from 'react';

const EvalCycleView = ({ experimentId }) => {
  const [evalResults, setEvalResults] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch evaluation results for specific experiment
    fetch(`/api/experiment/${experimentId}/eval`)
      .then(response => response.json())
      .then(data => {
        setEvalResults(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching eval results:', error);
        setLoading(false);
      });
  }, [experimentId]);

  if (loading) {
    return <div>Loading evaluation results...</div>;
  }

  return (
    <div className="eval-cycle-view">
      <h1>Evaluation Cycle Results</h1>
      {evalResults && (
        <div>
          <p>Consecutive Passes: {evalResults.consecutive_passes}</p>
          <p>Production Ready: {evalResults.production_ready ? 'Yes' : 'No'}</p>
          
          <h2>Stage Results</h2>
          <ul>
            {Object.entries(evalResults.evaluation_results).map(([stage, result]) => (
              <li key={stage}>
                <strong>{result.stage}:</strong> {result.score} ({result.passed ? 'Passed' : 'Failed'})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default EvalCycleView;