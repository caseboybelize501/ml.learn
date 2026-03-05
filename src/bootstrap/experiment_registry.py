import hashlib
import json
from typing import Dict, List

class ExperimentRegistry:
    def __init__(self):
        self.experiments = {}
        
    def register_experiment(self, config: Dict) -> str:
        # Create hash of config
        config_json = json.dumps(config, sort_keys=True)
        config_hash = hashlib.sha256(config_json.encode()).hexdigest()
        
        # Store experiment
        self.experiments[config_hash] = {
            "config": config,
            "status": "registered"
        }
        
        return config_hash
    
    def is_duplicate(self, config: Dict) -> bool:
        config_json = json.dumps(config, sort_keys=True)
        config_hash = hashlib.sha256(config_json.encode()).hexdigest()
        return config_hash in self.experiments
    
    def get_experiment(self, config_hash: str) -> Dict:
        return self.experiments.get(config_hash, None)

# Global registry instance
experiment_registry = ExperimentRegistry()