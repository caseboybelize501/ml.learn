import numpy as np
from typing import Dict, Any

class AdaptiveMutator:
    def __init__(self):
        pass
    
    def mutate_hyperparameters(self, current_params: Dict[str, Any],
                             eval_results: Dict[str, Any]) -> Dict[str, Any]:
        # Mutate hyperparameters based on evaluation weaknesses
        mutated_params = current_params.copy()
        
        # Identify weak stages
        weak_stages = self._identify_weak_stages(eval_results)
        
        if "calibration" in weak_stages:
            # Target calibration weakness
            mutated_params["learning_rate"] = max(1e-6, mutated_params["learning_rate"] * 0.8)
            mutated_params["weight_decay"] = mutated_params.get("weight_decay", 0) + 0.001
        
        if "robustness" in weak_stages:
            # Target robustness weakness
            mutated_params["dropout_rate"] = min(0.8, mutated_params.get("dropout_rate", 0.2) + 0.1)
            
        return mutated_params
    
    def _identify_weak_stages(self, eval_results: Dict[str, Any]) -> List[str]:
        # Identify stages that failed evaluation
        weak_stages = []
        
        for stage_name, result in eval_results.items():
            if not result.get("passed", True):
                weak_stages.append(stage_name)
                
        return weak_stages