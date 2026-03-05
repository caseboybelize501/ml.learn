from typing import Dict, List

class GPUProfile:
    def __init__(self, device_count: int, devices: List[Dict]):
        self.device_count = device_count
        self.devices = devices


class FrameworkProfile:
    def __init__(self, frameworks: Dict):
        self.frameworks = frameworks


class CheckpointRegistry:
    def __init__(self, checkpoints: List[Dict]):
        self.checkpoints = checkpoints


class ServiceStatus:
    def __init__(self, mlflow: bool, ray: bool, optuna: bool, inference_servers: List[str]):
        self.mlflow = mlflow
        self.ray = ray
        self.optuna = optuna
        self.inference_servers = inference_servers


class MLSystemProfile:
    def __init__(self, gpu_profile: GPUProfile, framework_profile: FrameworkProfile,
                 checkpoint_registry: CheckpointRegistry, service_status: ServiceStatus):
        self.gpu_profile = gpu_profile
        self.framework_profile = framework_profile
        self.checkpoint_registry = checkpoint_registry
        self.service_status = service_status
        
    def to_dict(self):
        return {
            "gpu_profile": self.gpu_profile.__dict__ if hasattr(self.gpu_profile, '__dict__') else self.gpu_profile,
            "framework_profile": self.framework_profile.__dict__ if hasattr(self.framework_profile, '__dict__') else self.framework_profile,
            "checkpoint_registry": self.checkpoint_registry.__dict__ if hasattr(self.checkpoint_registry, '__dict__') else self.checkpoint_registry,
            "service_status": self.service_status.__dict__ if hasattr(self.service_status, '__dict__') else self.service_status
        }

    def __repr__(self):
        return f"MLSystemProfile(gpu={self.gpu_profile.device_count} devices)"