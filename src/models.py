from pydantic import BaseModel
from typing import Optional, Dict, Any

class ExperimentConfig(BaseModel):
    task_type: str
    dataset_hash: str
    model_architecture: str
    hyperparams: Dict[str, Any]
    
    class Config:
        schema_extra = {
            "example": {
                "task_type": "image_classification",
                "dataset_hash": "abc123",
                "model_architecture": "EfficientNet-B0",
                "hyperparams": {
                    "learning_rate": 0.001,
                    "batch_size": 32
                }
            }
        }

class MLSystemProfile(BaseModel):
    gpu_profile: Dict[str, Any]
    framework_profile: Dict[str, Any]
    checkpoint_registry: Dict[str, Any]
    service_status: Dict[str, Any]
    
    class Config:
        schema_extra = {
            "example": {
                "gpu_profile": {"device_count": 1, "devices": []},
                "framework_profile": {},
                "checkpoint_registry": {},
                "service_status": {}
            }
        }