import React, { useState, useEffect } from 'react';

const ExperimentTracker = () => {
  const [experiments, setExperiments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch experiments from API
    fetch('/api/registry/experiments')
      .then(response => response.json())
      .then(data => {
        setExperiments(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching experiments:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading experiments...</div>;
  }

  return (
    <div className="experiment-tracker">
      <h1>Experiment Tracker</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Task</th>
            <th>Status</th>
            <th>Cycles</th>
            <th>Production Ready</th>
          </tr>
        </thead>
        <tbody>
          {experiments.map(exp => (
            <tr key={exp.id}>
              <td>{exp.id}</td>
              <td>{exp.task_type}</td>
              <td>{exp.status}</td>
              <td>{exp.cycles}</td>
              <td>{exp.production_ready ? 'Yes' : 'No'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ExperimentTracker;