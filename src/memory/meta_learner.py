import sklearn
from sklearn.ensemble import RandomForestClassifier
from typing import Dict, List, Any

class MetaLearner:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.is_trained = False
        
    def train(self, training_data: List[Dict[str, Any]]):
        # Train meta-learner on past experiments
        X = []
        y = []
        
        for data in training_data:
            features = [
                data.get("hardware", 0),
                data.get("dataset_size", 0),
                data.get("task_type", 0),
                data.get("cycles_to_production_ready", 0)
            ]
            X.append(features)
            y.append(data.get("best_strategy", "random"))
            
        self.model.fit(X, y)
        self.is_trained = True
        
    def predict_strategy(self, hardware: str, dataset_size: int,
                        task_type: str) -> str:
        # Predict best search strategy for new experiment
        if not self.is_trained:
            return "random"
            
        features = [[hardware, dataset_size, task_type, 0]]
        prediction = self.model.predict(features)[0]
        
        return prediction