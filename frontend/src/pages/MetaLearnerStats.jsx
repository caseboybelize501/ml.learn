import React, { useState, useEffect } from 'react';

const MetaLearnerStats = () => {
  const [metaData, setMetaData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch meta-learner statistics
    fetch('/api/memory/meta')
      .then(response => response.json())
      .then(data => {
        setMetaData(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching meta data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading meta-learner statistics...</div>;
  }

  return (
    <div className="meta-learner-stats">
      <h1>Meta-Learner Statistics</h1>
      {metaData && (
        <div>
          <p>Strategy Accuracy: {metaData.strategy_accuracy}</p>
          <p>Best Strategies:</p>
          <ul>
            {metaData.best_strategies.map((strategy, index) => (
              <li key={index}>{strategy}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default MetaLearnerStats;