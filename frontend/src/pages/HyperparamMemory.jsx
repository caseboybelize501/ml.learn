import React, { useState, useEffect } from 'react';

const HyperparamMemory = () => {
  const [hyperparamData, setHyperparamData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch hyperparameter memory data
    fetch('/api/memory/hyperparams')
      .then(response => response.json())
      .then(data => {
        setHyperparamData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching hyperparam data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading hyperparameter memory...</div>;
  }

  return (
    <div className="hyperparam-memory">
      <h1>Hyperparameter Memory</h1>
      {hyperparamData && (
        <div>
          <p>Memory contains {hyperparamData.length} relationships</p>
          <ul>
            {hyperparamData.map((item, index) => (
              <li key={index}>
                {item.hyperparam} → {item.eval_stage} ({item.relationship_type})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default HyperparamMemory;