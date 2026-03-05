from typing import Dict, Any
from src.bootstrap.system_profile import MLSystemProfile

class MLPlanner:
    def __init__(self, system_profile: MLSystemProfile):
        self.system_profile = system_profile
        
    def plan_experiment(self, task: str, data_profile: Dict) -> Dict[str, Any]:
        # Determine hardware constraints from system profile
        gpu_count = self.system_profile.gpu_profile.device_count
        vram_total = sum([dev["vram_total"] for dev in self.system_profile.gpu_profile.devices])
        
        # Route to appropriate agents based on task and hardware
        agent_routing = {
            "data": "DataAgent",
            "architecture": "ArchitectureAgent",
            "train": "TrainAgent",
            "eval": "EvalAgent",
            "hyper": "HyperAgent",
            "learn": "LearnAgent"
        }
        
        return {
            "task": task,
            "data_profile": data_profile,
            "hardware_constraints": {
                "gpu_count": gpu_count,
                "total_vram_mb": vram_total
            },
            "agent_routing": agent_routing,
            "temperature": 0.3,
            "max_tokens": 2048
        }

# Global planner instance
ml_planner = None

def plan_experiment(task: str, data_profile: Dict):
    if ml_planner is None:
        raise Exception("MLPlanner not initialized")
    return ml_planner.plan_experiment(task, data_profile)